from chef import Chef

class ChineseChef(Chef):# how you inherit from the chef class # using inheritance the chinese chef can also do the same things as the normal chef
    def make_fried_rice(self):
        print("Making fried rice")
    def make_special_dish(self): # overriding a specific function 
        print("the chef makes orange chicken")
