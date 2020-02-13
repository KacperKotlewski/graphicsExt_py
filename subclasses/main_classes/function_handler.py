import inspect


class FunctionHolder:
    def __init__(self, function, arguments = None):
        self.setFunction(function)
        self.arguments = dict()
        self.setArguments(arguments)

    def setFunction(self, function): self.function = function

    def setArguments(self, arguments:dict): self.arguments = arguments
    def addArguments(self, arguments: dict):
        for key, val in arguments.items():
            if(type(self.arguments) != dict): self.arguments = dict()
            self.arguments[key] = val

    def getFunctionAttribs(self):
        sig = inspect.signature(self.function)
        print(str(self.getName()),sig)

    def getName(self): return self.function.__name__

    def run(self):
        self.function(**self.arguments)

    def clone(self):
        return FunctionHolder(self.function, self.arguments)



class FunctionList:
    def __init__(self):
        self.functions = []

    def add(self, function_holder:FunctionHolder):
        self.functions.append(function_holder)

    def remove(self, function_holder:FunctionHolder):
        self.functions.remove(function_holder)

    def runAll(self):
        for func in self.functions:
            func.run()

    def clone(self):
        return FunctionList(self.functions)
