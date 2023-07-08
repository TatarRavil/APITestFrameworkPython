class BuilderBaseClass:

    def __init__(self):
        self.result = {}

    def build(self):
        return self.result

    def update_inner_value(self, objects, value):
        if not isinstance(objects, list):
            self.result[objects] = value
        else:
            temp = self.result
            for item in objects[:-1]:
                if item not in temp.keys():
                    temp[item] = {}
                temp = temp[item]
            temp[objects[-1]] = value
        return self
