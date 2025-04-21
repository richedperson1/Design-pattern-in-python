from abc import ABC,abstractmethod

class IPlugin(ABC):
    @abstractmethod
    def execute(self):
        pass
    

class pluginA:
    def run(self):
        return "Running plugin A code"
    
class pluginB:
    def run(self):
        return "Running plugin B code"
    
 
class plugin(IPlugin):
    def __init__(self):
        self.plugins = []
    def add_plug(self,plug):
        self.plugins.append(plug)
    def execute(self):
        totalResult = []
        for plug in self.plugins:
            plugResult = plug.execute()
            totalResult.append(plugResult)    
        return totalResult


class pluginBAdapter:
    def __init__(self,plug):
        self.plugCls = plug()
    def execute(self):
        return self.plugCls.run()

    

class pluginAAdapter:
    def __init__(self,plug):
        self.plugCls = plug()
    def execute(self):
        return self.plugCls.run()



    