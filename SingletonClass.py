class SingletonClass:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            
        return cls.__instance
    
class State (SingletonClass):
    pass
# class SingletonChild(SingletonClass):
#     pass
   
# singleton = SingletonClass()  
# child = SingletonChild()
# child2 = SingletonChild()
# print(child is singleton)

# singleton.singl_variable = "Singleton Variable"
# print(child.singl_variable)
# print(singleton.singl_variable)