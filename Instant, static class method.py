#Instant method
class MyClass:
    def instance_method(self):
        # Accessing instance variables
        self.instance_variable = 10
        
        # Accessing class variable
        MyClass.class_variable = 20
        
        # Perform operations specific to an instance
        # ...
        
obj = MyClass()  # Creating an instance of the class
obj.instance_method()  # Calling the instance method on the instance

#Static method
class MyClass:
    @staticmethod
    def static_method():
        # Perform operations independent of instance or class state
        # ...
        
MyClass.static_method()  # Calling the static method on the class

#Class method
class MyClass:
    class_variable = 0
    
    @classmethod
    def class_method(cls):
        # Accessing/modifying class variables
        cls.class_variable = 10
        
        # Perform operations related to the class
        # ...
        
MyClass.class_method()  # Calling the class method on the class

