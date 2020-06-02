# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version May 27 2020)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv
import wx.grid

###########################################################################
## Class PickPlaceWizard
###########################################################################

class PickPlaceWizard ( wx.adv.Wizard ):

    def __init__( self, parent ):
        wx.adv.Wizard.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, bitmap = wx.NullBitmap, pos = wx.DefaultPosition, style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.m_pages = []

        self.file_select_Page = wx.adv.WizardPageSimple( self  )
        self.add_page( self.file_select_Page )

        bSizer4 = wx.BoxSizer( wx.VERTICAL )

        self.filePicker = wx.FilePickerCtrl( self.file_select_Page, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
        bSizer4.Add( self.filePicker, 0, wx.ALL, 5 )


        self.file_select_Page.SetSizer( bSizer4 )
        self.file_select_Page.Layout()
        bSizer4.Fit( self.file_select_Page )
        self.file_parser_Page = wx.adv.WizardPageSimple( self  )
        self.add_page( self.file_parser_Page )

        file_parser_BSizer = wx.BoxSizer( wx.VERTICAL )

        parser_predictions_choiceChoices = []
        self.parser_predictions_choice = wx.Choice( self.file_parser_Page, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, parser_predictions_choiceChoices, 0 )
        self.parser_predictions_choice.SetSelection( 0 )
        file_parser_BSizer.Add( self.parser_predictions_choice, 0, wx.ALL, 5 )

        self.m_staticline1 = wx.StaticLine( self.file_parser_Page, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        file_parser_BSizer.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

        self.file_parser_options_Panel = wx.Panel( self.file_parser_Page, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        file_parser_BSizer.Add( self.file_parser_options_Panel, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_staticline2 = wx.StaticLine( self.file_parser_Page, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        file_parser_BSizer.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

        self.file_parser_Grid = wx.grid.Grid( self.file_parser_Page, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.file_parser_Grid.CreateGrid( 1, 1 )
        self.file_parser_Grid.EnableEditing( False )
        self.file_parser_Grid.EnableGridLines( True )
        self.file_parser_Grid.EnableDragGridSize( False )
        self.file_parser_Grid.SetMargins( 0, 0 )

        # Columns
        self.file_parser_Grid.EnableDragColMove( False )
        self.file_parser_Grid.EnableDragColSize( True )
        self.file_parser_Grid.SetColLabelSize( 30 )
        self.file_parser_Grid.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.file_parser_Grid.EnableDragRowSize( True )
        self.file_parser_Grid.SetRowLabelSize( 80 )
        self.file_parser_Grid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.file_parser_Grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        file_parser_BSizer.Add( self.file_parser_Grid, 0, wx.ALL, 5 )


        self.file_parser_Page.SetSizer( file_parser_BSizer )
        self.file_parser_Page.Layout()
        file_parser_BSizer.Fit( self.file_parser_Page )
        self.extractor_Page = wx.adv.WizardPageSimple( self  )
        self.add_page( self.extractor_Page )

        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        extractor_predictions_choiceChoices = []
        self.extractor_predictions_choice = wx.Choice( self.extractor_Page, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, extractor_predictions_choiceChoices, 0 )
        self.extractor_predictions_choice.SetSelection( 0 )
        bSizer3.Add( self.extractor_predictions_choice, 0, wx.ALL, 5 )

        self.m_staticline3 = wx.StaticLine( self.extractor_Page, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer3.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )

        self.extractor_options_Panel = wx.Panel( self.extractor_Page, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer3.Add( self.extractor_options_Panel, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_staticline4 = wx.StaticLine( self.extractor_Page, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer3.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )

        self.extractor_Grid = wx.grid.Grid( self.extractor_Page, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.extractor_Grid.CreateGrid( 1, 5 )
        self.extractor_Grid.EnableEditing( False )
        self.extractor_Grid.EnableGridLines( True )
        self.extractor_Grid.EnableDragGridSize( False )
        self.extractor_Grid.SetMargins( 0, 0 )

        # Columns
        self.extractor_Grid.EnableDragColMove( False )
        self.extractor_Grid.EnableDragColSize( True )
        self.extractor_Grid.SetColLabelSize( 30 )
        self.extractor_Grid.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.extractor_Grid.EnableDragRowSize( True )
        self.extractor_Grid.SetRowLabelSize( 80 )
        self.extractor_Grid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.extractor_Grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        bSizer3.Add( self.extractor_Grid, 0, wx.ALL, 5 )


        self.extractor_Page.SetSizer( bSizer3 )
        self.extractor_Page.Layout()
        bSizer3.Fit( self.extractor_Page )
        self.attribute_parser_Page = wx.adv.WizardPageSimple( self  )
        self.add_page( self.attribute_parser_Page )

        bSizer8 = wx.BoxSizer( wx.VERTICAL )

        self.m_notebook1 = wx.Notebook( self.attribute_parser_Page, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_panel81 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer9 = wx.BoxSizer( wx.VERTICAL )

        ref_parser_choiceChoices = []
        self.ref_parser_choice = wx.Choice( self.m_panel81, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ref_parser_choiceChoices, 0 )
        self.ref_parser_choice.SetSelection( 0 )
        bSizer9.Add( self.ref_parser_choice, 0, wx.ALL, 5 )

        self.m_staticline9 = wx.StaticLine( self.m_panel81, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer9.Add( self.m_staticline9, 0, wx.EXPAND |wx.ALL, 5 )

        self.m_panel5 = wx.Panel( self.m_panel81, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer9.Add( self.m_panel5, 1, wx.EXPAND |wx.ALL, 5 )


        self.m_panel81.SetSizer( bSizer9 )
        self.m_panel81.Layout()
        bSizer9.Fit( self.m_panel81 )
        self.m_notebook1.AddPage( self.m_panel81, u"Ref", True )
        self.m_panel91 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer91 = wx.BoxSizer( wx.VERTICAL )

        x_parser_choiceChoices = []
        self.x_parser_choice = wx.Choice( self.m_panel91, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, x_parser_choiceChoices, 0 )
        self.x_parser_choice.SetSelection( 0 )
        bSizer91.Add( self.x_parser_choice, 0, wx.ALL, 5 )

        self.m_staticline10 = wx.StaticLine( self.m_panel91, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer91.Add( self.m_staticline10, 0, wx.EXPAND |wx.ALL, 5 )

        self.m_panel6 = wx.Panel( self.m_panel91, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer91.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )


        self.m_panel91.SetSizer( bSizer91 )
        self.m_panel91.Layout()
        bSizer91.Fit( self.m_panel91 )
        self.m_notebook1.AddPage( self.m_panel91, u"X", False )
        self.m_panel10 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer92 = wx.BoxSizer( wx.VERTICAL )

        y_parser_choiceChoices = []
        self.y_parser_choice = wx.Choice( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, y_parser_choiceChoices, 0 )
        self.y_parser_choice.SetSelection( 0 )
        bSizer92.Add( self.y_parser_choice, 0, wx.ALL, 5 )

        self.m_staticline11 = wx.StaticLine( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer92.Add( self.m_staticline11, 0, wx.EXPAND |wx.ALL, 5 )

        self.m_panel7 = wx.Panel( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer92.Add( self.m_panel7, 1, wx.EXPAND |wx.ALL, 5 )


        self.m_panel10.SetSizer( bSizer92 )
        self.m_panel10.Layout()
        bSizer92.Fit( self.m_panel10 )
        self.m_notebook1.AddPage( self.m_panel10, u"Y", False )
        self.m_panel11 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer93 = wx.BoxSizer( wx.VERTICAL )

        side_parser_choiceChoices = []
        self.side_parser_choice = wx.Choice( self.m_panel11, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, side_parser_choiceChoices, 0 )
        self.side_parser_choice.SetSelection( 0 )
        bSizer93.Add( self.side_parser_choice, 0, wx.ALL, 5 )

        self.m_staticline12 = wx.StaticLine( self.m_panel11, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer93.Add( self.m_staticline12, 0, wx.EXPAND |wx.ALL, 5 )

        self.m_panel8 = wx.Panel( self.m_panel11, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer93.Add( self.m_panel8, 1, wx.EXPAND |wx.ALL, 5 )


        self.m_panel11.SetSizer( bSizer93 )
        self.m_panel11.Layout()
        bSizer93.Fit( self.m_panel11 )
        self.m_notebook1.AddPage( self.m_panel11, u"Side", False )
        self.m_panel12 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer94 = wx.BoxSizer( wx.VERTICAL )

        rotation_parser_choiceChoices = []
        self.rotation_parser_choice = wx.Choice( self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, rotation_parser_choiceChoices, 0 )
        self.rotation_parser_choice.SetSelection( 0 )
        bSizer94.Add( self.rotation_parser_choice, 0, wx.ALL, 5 )

        self.m_staticline13 = wx.StaticLine( self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer94.Add( self.m_staticline13, 0, wx.EXPAND |wx.ALL, 5 )

        self.m_panel9 = wx.Panel( self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer94.Add( self.m_panel9, 1, wx.EXPAND |wx.ALL, 5 )


        self.m_panel12.SetSizer( bSizer94 )
        self.m_panel12.Layout()
        bSizer94.Fit( self.m_panel12 )
        self.m_notebook1.AddPage( self.m_panel12, u"Rotation", False )

        bSizer8.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )

        self.attribute_parser_grid = wx.grid.Grid( self.attribute_parser_Page, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.attribute_parser_grid.CreateGrid( 5, 5 )
        self.attribute_parser_grid.EnableEditing( True )
        self.attribute_parser_grid.EnableGridLines( True )
        self.attribute_parser_grid.EnableDragGridSize( False )
        self.attribute_parser_grid.SetMargins( 0, 0 )

        # Columns
        self.attribute_parser_grid.EnableDragColMove( False )
        self.attribute_parser_grid.EnableDragColSize( True )
        self.attribute_parser_grid.SetColLabelSize( 30 )
        self.attribute_parser_grid.SetColLabelValue( 0, u"Ref" )
        self.attribute_parser_grid.SetColLabelValue( 1, u"X" )
        self.attribute_parser_grid.SetColLabelValue( 2, u"Y" )
        self.attribute_parser_grid.SetColLabelValue( 3, u"Side" )
        self.attribute_parser_grid.SetColLabelValue( 4, u"Rotation" )
        self.attribute_parser_grid.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.attribute_parser_grid.EnableDragRowSize( True )
        self.attribute_parser_grid.SetRowLabelSize( 80 )
        self.attribute_parser_grid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.attribute_parser_grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        bSizer8.Add( self.attribute_parser_grid, 0, wx.ALL, 5 )


        self.attribute_parser_Page.SetSizer( bSizer8 )
        self.attribute_parser_Page.Layout()
        bSizer8.Fit( self.attribute_parser_Page )
        self.Centre( wx.BOTH )


        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.OnExit )
        self.Bind( wx.EVT_INIT_DIALOG, self.OnWizardInit )
        self.Bind( wx.adv.EVT_WIZARD_CANCEL, self.OnExit )
        self.Bind( wx.adv.EVT_WIZARD_FINISHED, self.OnFnished )
        self.Bind( wx.adv.EVT_WIZARD_PAGE_CHANGED, self.OnWizardPageChange )
        self.Bind( wx.adv.EVT_WIZARD_PAGE_CHANGING, self.OnWizardPageChanging )
        self.parser_predictions_choice.Bind( wx.EVT_CHOICE, self.OnParserPredictionsChoice )
        self.extractor_predictions_choice.Bind( wx.EVT_CHOICE, self.OnExtractorPredictionsChoice )
        self.ref_parser_choice.Bind( wx.EVT_CHOICE, self.OnRefParseChoice )
        self.x_parser_choice.Bind( wx.EVT_CHOICE, self.OnXParseChoice )
        self.y_parser_choice.Bind( wx.EVT_CHOICE, self.OnYParseChoice )
        self.side_parser_choice.Bind( wx.EVT_CHOICE, self.OnSideParseChoice )
        self.rotation_parser_choice.Bind( wx.EVT_CHOICE, self.OnRotationParseChoice )
    def add_page(self, page):
        if self.m_pages:
            previous_page = self.m_pages[-1]
            page.SetPrev(previous_page)
            previous_page.SetNext(page)
        self.m_pages.append(page)

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def OnExit( self, event ):
        event.Skip()

    def OnWizardInit( self, event ):
        event.Skip()


    def OnFnished( self, event ):
        event.Skip()

    def OnWizardPageChange( self, event ):
        event.Skip()

    def OnWizardPageChanging( self, event ):
        event.Skip()

    def OnParserPredictionsChoice( self, event ):
        event.Skip()

    def OnExtractorPredictionsChoice( self, event ):
        event.Skip()

    def OnRefParseChoice( self, event ):
        event.Skip()

    def OnXParseChoice( self, event ):
        event.Skip()

    def OnYParseChoice( self, event ):
        event.Skip()

    def OnSideParseChoice( self, event ):
        event.Skip()

    def OnRotationParseChoice( self, event ):
        event.Skip()


