import pcbnew
import os
import wx
import wx.grid
import pick_place.pick_place_wizard
import pick_place.file_parser
import pick_place.extractor
import pick_place.attribute_parser

class PickAndPacePlugin(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Pick and Place Import"
        self.category = "Tools"
        self.description = "Reads a Pick and Place file and places compoents on a PCB"

    def Run(self):
        app = wx.App(False)
        wizard = PickPlaceWizardImpl(None)
        wizard.RunWizard(wizard.file_select_Page)
        app.MainLoop()
        pass


class PickPlaceWizardImpl(pick_place.pick_place_wizard.PickPlaceWizard):
    def OnExit(self,event):
        self.Destroy()

    def OnWizardPageChanging(self, event):
        if event.GetPage() == self.file_select_Page:
            if self.filePicker.GetPath() == "":
                event.Veto()
        if event.GetPage() == self.file_parser_Page:
            if self.selected_parser == None:
                event.Veto()
        if event.GetPage() == self.extractor_Page:
            if self.selected_extractor == None:
                event.Veto()
        if event.GetPage() == self.attribute_parser_Page:
            if self.selected_ref_parser == None or self.selected_x_parser == None or self.selected_y_parser == None or self.selected_side_parser == None or self.selected_rotation_parser == None:
                event.Veto()

    def OnWizardPageChange( self, event):
        if event.GetPage() == self.file_parser_Page:
            self.OnFileParserPageEnter(event)
        if event.GetPage() == self.extractor_Page:
            self.OnExtractorPageEnter(event)
        if event.GetPage() == self.attribute_parser_Page:
            self.OnAttributeParserPageEnter(event)

    def OnExtractorPageEnter( self, event):
        self.predicted_extractors = pick_place.extractor.ExtractorFinder(self.selected_parser).predirect_parser()
        self.extractor_predictions_choice.SetItems(list(map(lambda parser_prediction:parser_prediction["extractor"].name,self.predicted_extractors)))
  
    def OnExtractorPredictionsChoice(self, event):
        self.selected_extractor = self.predicted_extractors[self.extractor_predictions_choice.GetSelection()]["extractor"]
        it = iter(self.selected_extractor)
        sample_rows = [next(it) for i in range(5)]
        self.extractor_Grid.ClearGrid()
        self.extractor_Grid.DeleteRows(0,self.extractor_Grid.GetNumberRows())
        self.extractor_Grid.AppendRows(len(sample_rows))

        for c in range(len(sample_rows[0].keys())):
            self.extractor_Grid.SetColLabelValue(c,list(sample_rows[0].keys())[c])
        for r in range(len(sample_rows)):
            for c in range(len(sample_rows[0].keys())):
                self.extractor_Grid.SetCellValue(r,c,sample_rows[r][list(sample_rows[0].keys())[c]])
        self.Layout()

    def OnFileParserPageEnter(self,event):
        self.selected_parser = None
        self.file_parser_Grid.ClearGrid()
        self.f = open(self.filePicker.GetPath())
        self.predicted_parsers = pick_place.file_parser.ParserFinder(self.f).predict_parser()
        self.parser_predictions_choice.SetItems(list(map(lambda parser_prediction:parser_prediction["parser"].name,self.predicted_parsers)))
    
    def OnParserPredictionsChoice( self, event ):
        self.selected_parser = self.predicted_parsers[self.parser_predictions_choice.GetSelection()]["parser"]
        it = iter(self.selected_parser)
        sample_rows = [next(it) for i in range(5)]
        max_col = max(map(lambda row:len(row),sample_rows))
        self.file_parser_Grid.ClearGrid()
        self.file_parser_Grid.DeleteRows(0,self.file_parser_Grid.GetNumberRows())
        self.file_parser_Grid.DeleteCols(0,self.file_parser_Grid.GetNumberCols())
        self.file_parser_Grid.AppendCols(max_col)
        self.file_parser_Grid.AppendRows(len(sample_rows))
        for r in range(len(sample_rows)):
            for c in range(len(sample_rows[r])):
                self.file_parser_Grid.SetCellValue(r,c,sample_rows[r][c])
        self.Layout()

    def OnAttributeParserPageEnter(self, event):
        self.predicted_rotation_parsers = pick_place.attribute_parser.RotationParserPredictor(self.selected_extractor,{}).predict_parser()
        self.rotation_parser_choice.SetItems(list(map(lambda parser_prediction:parser_prediction["parser"].name,self.predicted_rotation_parsers)))

        self.predicted_side_parsers = pick_place.attribute_parser.SideParserPredictor(self.selected_extractor,{}).predict_parser()
        self.side_parser_choice.SetItems(list(map(lambda parser_prediction:parser_prediction["parser"].name,self.predicted_side_parsers)))

        self.predicted_ref_parsers = pick_place.attribute_parser.RefParserPredictor(self.selected_extractor,{}).predict_parser()
        self.ref_parser_choice.SetItems(list(map(lambda parser_prediction:parser_prediction["parser"].name,self.predicted_ref_parsers)))

        self.predicted_x_parsers =  pick_place.attribute_parser.PositionParserPredictor(self.selected_extractor,{},"x").predict_parser()
        self.x_parser_choice.SetItems(list(map(lambda parser_prediction:parser_prediction["parser"].name,self.predicted_x_parsers)))

        self.predicted_y_parsers =  pick_place.attribute_parser.PositionParserPredictor(self.selected_extractor,{},"y").predict_parser()
        self.y_parser_choice.SetItems(list(map(lambda parser_prediction:parser_prediction["parser"].name,self.predicted_y_parsers)))
    
    selected_ref_parser = None
    def OnRefParseChoice(self,event):
        self.selected_ref_parser = self.predicted_ref_parsers[self.ref_parser_choice.GetSelection()]["parser"]
        self.OnAttributeParserChoice(event)

    selected_x_parser = None
    def OnXParseChoice(self,event):
        self.selected_x_parser = self.predicted_x_parsers[self.x_parser_choice.GetSelection()]["parser"]
        self.OnAttributeParserChoice(event)

    selected_y_parser = None
    def OnYParseChoice(self,event):
        self.selected_y_parser = self.predicted_y_parsers[self.y_parser_choice.GetSelection()]["parser"]
        self.OnAttributeParserChoice(event)

    selected_side_parser = None
    def OnSideParseChoice(self,event):
        self.selected_side_parser = self.predicted_side_parsers[self.side_parser_choice.GetSelection()]["parser"]
        self.OnAttributeParserChoice(event)

    selected_rotation_parser = None
    def OnRotationParseChoice(self,event):
        self.selected_rotation_parser = self.predicted_rotation_parsers[self.rotation_parser_choice.GetSelection()]["parser"]
        self.OnAttributeParserChoice(event)

    def OnAttributeParserChoice(self,event):
        self.selected_attribute_parser = pick_place.attribute_parser.AttriuteParser(self.selected_extractor,{
            "ref":pick_place.attribute_parser.DummyExtractor() if self.selected_ref_parser is None else self.selected_ref_parser,
            "x":pick_place.attribute_parser.DummyExtractor() if self.selected_x_parser is None else self.selected_x_parser,
            "y":pick_place.attribute_parser.DummyExtractor() if self.selected_y_parser is None else self.selected_y_parser,
            "side":pick_place.attribute_parser.DummyExtractor() if self.selected_side_parser is None else  self.selected_side_parser,
            "rotation":pick_place.attribute_parser.DummyExtractor() if self.selected_rotation_parser is None else self.selected_rotation_parser
        })
        it = iter(self.selected_attribute_parser)
        sample_rows = [next(it) for i in range(5)]
        self.attribute_parser_grid.ClearGrid()
        self.attribute_parser_grid.DeleteRows(0,self.attribute_parser_grid.GetNumberRows())
        self.attribute_parser_grid.AppendRows(len(sample_rows))
        cols = ["ref","x","y","side","rotation"]
        for r in range(len(sample_rows)):
            for c in range(len(cols)):
                self.attribute_parser_grid.SetCellValue(r,c,str(sample_rows[r][cols[c]]))
    
    def OnFnished(self,event):
        board = pcbnew.GetBoard()
        ox,oy = board.GetAuxOrigin()
        for row in self.selected_attribute_parser:
            mod = board.FindModuleByReference(row["ref"])
            if mod is not None:
                mod.SetPosition(pcbnew.wxPoint(int(ox+(1000000*row["x"])),int(oy+(-1000000*row["y"]))))
                mod.SetOrientationDegrees(row["rotation"])
                if mod.IsFlipped():
                    if row["side"] == pick_place.attribute_parser.Side.TOP:
                        mod.Flip(mod.GetPosition())
                else:
                    if row["side"] == pick_place.attribute_parser.Side.BOTTOM:
                        mod.Flip(mod.GetPosition())
        pcbnew.Refresh()

PickAndPacePlugin().register()