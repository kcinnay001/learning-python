class Student: 
    def __init__(self, name, major, gpa, is_on_probation): # acts as the constructor
        self.name = name # the name of the object is the same as the name that is passed in 
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation 
    
    def on_honor_roll(self): # adding operation for the object
        if self.gpa >= 3.5:
            return True
        else: 
            return False