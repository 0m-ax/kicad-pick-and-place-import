from enum import Enum

class AttriuteParser:
    name = "parser"
    def __init__(self,options):
        super().__init__()
        self.options = options
    def parse_value(self,value):
        raise NotImplementedError

class ParserPredictor:
    def __init__(self,extractor,context):
        super().__init__()
        self.extractor = extractor
        self.context = context
    def get_values(self,key):
        itr = iter(self.extractor)
        return [next(itr)[key] for i in range(10)]

class RotationParserPredictor(ParserPredictor):
    def predict_parser(self):
        float_values = map(lambda value:float(value),self.get_values("rotation"))
        max_value = max(float_values)
        return [
            {
                "parser":DegreeRotationParser(RotationParserOptions()),
                "score":1 if max_value > 1 else 0.5
            },
            {
                "parser":PercentageRotationParser(RotationParserOptions()),
                "score":0.5 if max_value > 1 else 1
            }
        ]


class RotationParserOptions:
    pass

class DegreeRotationParser(AttriuteParser):
    name = "Degree"
    def parse_value(self,value):
        return float(value)

class PercentageRotationParser(AttriuteParser):
    name = "Percentage"
    def parse_value(self,value):
        return float(value)*350

class PositionParserPredictor(ParserPredictor):
    def __init__(self, extractor, context, axis):
        super().__init__(extractor, context)
        self.axis = axis
    def predict_parser(self):
        values = self.get_values(self.axis)
        ends_with_mil = map(lambda value: value.lower().endswith("mil"),values)
        ends_with_mm = map(lambda value: value.lower().endswith("mm"),values)

        output = []
        output.append({
            "score":0.9 if sum(ends_with_mil) > 8 else 0.4,
            "parser":InchPositionParser(InchParserOptions(scale=1/1000)),
        })
        output.append({
            "score":0.9 if sum(ends_with_mm) > 8 else 0.4,
            "parser":MMPositionPasrer(PositionParserOptions()),
        })
        return sorted(output, key = lambda i: i['score'],reverse=True)

class PositionParser(AttriuteParser):
    def parse_value(self,value):
        return float(value.lower().rstrip('mil').rstrip('mm'))*self.options.scale

class PositionParserOptions:
    def __init__(self,scale=1,has_suffix=False):
        super().__init__()
        self.scale = scale
        self.has_suffix = has_suffix

class InchParserOptions(PositionParserOptions):
    pass

class InchPositionParser(PositionParser):
    name="Inch"
    def parse_value(self,value):
        return super().parse_value(value)*25.4

class MMPositionPasrer(PositionParser):
    name="MM"
    pass

class SideParserPredictor(ParserPredictor):
    def predict_parser(self):
        values = map(lambda value: value.lower(), self.get_values("side"))
        values_t_b = map(lambda value: value == "t" or value == "b",values)
        values_1_0 = map(lambda value: value == "1" or value == "0",values)
        values_top_bottom = map(lambda value: value == "1" or value == "0",values)
        return sorted([
            {
                "score":0.9 if sum(values_t_b) > 8 else 0.4,
                "parser":SideParser(SideParserOptions("t","b"))
            },
            {
                "score":0.9 if sum(values_1_0) > 8 else 0.4,
                "parser":SideParser(SideParserOptions("1","0"))
            },
            {
                "score":0.9 if sum(values_1_0) > 8 else 0.4,
                "parser":SideParser(SideParserOptions("top","bottom"))
            }
        ], key = lambda i: i['score'],reverse=True)

class SideParserOptions:
    def __init__(self,top_string,bottom_string):
        super().__init__()
        self.top_string = top_string
        self.bottom_string = bottom_string

class SideParser(AttriuteParser):
    @property
    def name(self):
        return "Side top:"+self.options.top_string+" bottom:"+self.options.bottom_string
    def parse_value(self,value):
        if value.lower() == self.options.top_string:
            return Side.TOP
        if value.lower() == self.options.bottom_string:
            return Side.TOP


class RefParserPredictor(ParserPredictor):
    def predict_parser(self):
        return [
            {
                "score":1,
                "parser":RefParser(RefParserOptions())
            },
        ]
        
class RefParserOptions:
    pass

class RefParser(AttriuteParser):
    name="Default"
    def parse_value(self,value):
        return value

class Side(Enum):
    TOP = 1
    BOTTOM = 2

class DummyExtractor:
    def parse_value(self,value):
        return ""

class AttriuteParser:
    def __init__(self,extractor,parsers):
        super().__init__()
        self.extractor = extractor
        self.parsers = parsers
    def __iter__(self):
        def iter_f():
            for row in self.extractor:
                yield dict([(key,self.parsers[key].parse_value(value)) for key,value in row.items()])
        return iter_f()
