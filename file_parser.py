import functools
class ParserFinder:
    parser_types = []
    def __init__(self,f):
        super().__init__()
        self.f = f

    def predict_parser(self):
        sample_lines = [self.f.readline() for i in range(10)]
        results = []
        for parser_type in self.parser_types:
            score,options = parser_type.predict_type(sample_lines)
            results.append({
                "score":score,
                "parser":parser_type(self.f,options)
            })
        self.f.seek(0)
        return sorted(results, key = lambda i: i['score'],reverse=True)
    @staticmethod
    def register_parser(cls):
        ParserFinder.parser_types.append(cls)

class ParserOptions:
    pass

class TSVParserOptions(ParserOptions):
    pass
class CSVParserOptions(ParserOptions):
    pass

class Parser:
    def __init__(self,f,options):
        self.f = f
        self.options = options
    @staticmethod
    def predict_type(sample_lines):
        raise NotImplementedError()

@ParserFinder.register_parser
class TSVParser(Parser):
    name="TSV"
    __options__ = TSVParserOptions
    def __init__(self,f,options):
        super().__init__(f,options)

    def __iter__(self):
        self.f.seek(0)
        return self

    def __next__(self):
        return self.f.readline().strip().split(",")

    @staticmethod
    def predict_type(sample_lines):
        if sample_lines[0].count("\t") >= 4:
            return 1, TSVParserOptions()
        return 0, TSVParserOptions()

@ParserFinder.register_parser
class CSVParser(Parser):
    name="CSV"
    __options__ = CSVParserOptions
    def __init__(self,f,options):
        super().__init__(f,options)

    def __iter__(self):
        self.f.seek(0)
        return self

    def __next__(self):
        return self.f.readline().strip().split(",")

    @staticmethod
    def predict_type(sample_lines):
        if sample_lines[0].count(",") >= 4:
            return 1, CSVParserOptions()
        return 0, CSVParserOptions()

class SSVParserOptions(ParserOptions):
    def __init__(self,split_locations):
        super().__init__()
        self.split_locations = split_locations

@ParserFinder.register_parser
class SSVParser(Parser):
    __options__ = SSVParserOptions
    name="SSV"
    def __init__(self,f,options):
        super().__init__(f,options)
    def __iter__(self):
        self.f.seek(0)
        return self.itr()
    def itr(self):
        for line in self.f:
            output = []
            last = 0
            if len(line) < self.options.split_locations[-1]:
                continue
            for split_index in self.options.split_locations:
                output.append(line[:(split_index-last)].strip())
                line = line[(split_index-last):]
                last = split_index
            output.append(line.strip())
            yield output

    @staticmethod
    def predict_type(sample_lines):
        total_gaps = {}
        for l in sample_lines:
            clean_line = l.rstrip()
            if clean_line == "":
                continue
            for i in range(1,len(clean_line)):
                if clean_line[i] == " ":
                    if i not in total_gaps:
                        total_gaps[i] = 0
                    total_gaps[i] +=1
        splits = []
        for i in total_gaps.keys():
            if total_gaps[i] > 8:
                splits.append(i)
        sorted_splits = sorted(splits)
        def red_f(acu,value):
            if acu[-1]+1 == value:
                return acu[:-1]+[value]
            return acu+[value]
        if len(sorted_splits) < 5:
            return 0, SSVParserOptions([])
        split_locations = functools.reduce(red_f,sorted_splits[1:],[sorted_splits[0]])
        if len(split_locations) > 4:
            return 0.9, SSVParserOptions(split_locations)
        return 0, SSVParserOptions([])

# with open('Pick Place for Movis_ApS_iMX6_PCB(Movis_ApS_iMX6 Rev. 4).csv') as f:
#     ParserFinder(f).predict_parser()
# with open('tsv.tsv') as f:
#     ParserFinder(f).predict_parser()
