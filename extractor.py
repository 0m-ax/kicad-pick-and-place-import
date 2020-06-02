class ExtractorFinder:
    def __init__(self,parser):
        super().__init__()
        self.parser = parser
    def predirect_parser(self):
        itr = iter(self.parser)
        sample_rows = [next(itr) for i in range(4)]
        return [{
                "extractor":Extractor(self.parser,ExtractorOptions()),
                "score":0.5,
        }]

class ExtractorOptions:
    has_header = True
    ref_col = 0
    x_col = 4
    y_col = 5
    rotation_col = 9
    side_col = 8

class Extractor:
    @property
    def name(self):
        return f'Ref:{self.options.ref_col} X:{self.options.x_col} Y:{self.options.y_col} Side:{self.options.side_col} Rotation:{self.options.rotation_col}'
    def __init__(self,parser,options):
        super().__init__()
        self.parser = parser
        self.options = options

    def __iter__(self):
        def iter_f():
            itr = iter(self.parser)
            i = 0
            for row in itr:
                if self.options.has_header and i == 0:
                    i = 1
                    continue
                if max([self.options.ref_col,self.options.x_col,self.options.y_col,self.options.side_col,self.options.rotation_col]) >= len(row):
                    continue
                yield {
                    "ref":row[self.options.ref_col],
                    "x":row[self.options.x_col],
                    "y":row[self.options.y_col],
                    "side":row[self.options.side_col],
                    "rotation":row[self.options.rotation_col]
                }
        return iter_f()

