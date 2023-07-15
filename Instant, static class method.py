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
