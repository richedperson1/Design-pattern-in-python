
from abc import ABC,abstractmethod

class NotificationAbstract(ABC):
    @abstractmethod
    def send(self):
        pass
    

# class NotificationFactory:
#     _register = {}
#     @classmethod
#     def add_notification(self,notify_name):
#         def decorator(notify_cls):
#             self._register[notify_name] = notify_cls
#             return "Register sucessful"
#         return decorator
    
#     def get_notification(self)
    
    
    
def fun(func):
    def decorator(name):
        hi = func(name)
        return f"this is decorator  {hi}"
    
    return decorator
@fun
def helper(name):
    return f"hi : {name}"

print(helper("Rutvik"))