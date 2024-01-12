
class StringVar:
    def __init__(self, initial_value=""):
        self._value = initial_value

    def set(self, new_value):
        self._value = new_value

    def get(self):
        return self._value

my_string_var = StringVar()

print("Initial value:", my_string_var.get())  

my_string_var.set("New String")  
print("Updated value:", my_string_var.get())  
