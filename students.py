class Student:

    def __init__(self, name, cohort):
        self.name = name 
        self.cohort = cohort
    
    def talk(self):
        return "I can talk!"
    
    def what_cohort(self):
        return "I am in cohort " + self.cohort
    
    def say_favourite_language(self, language):
        return "I love " + language





