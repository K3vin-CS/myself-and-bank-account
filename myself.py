class Human:
    def __init__(self, name, age, hobby, school):
        self.name = name
        self.age = age
        self.hobby = hobby
        self.school = school
    
    def introduce(self):
        return f"Hi my name is {self.name}. I am {self.age} years old and I study at {self.school}"

    def do_hobby(self):
        return "My hobby is {self.hobby}"

    def goal(self, dream_job):
        return f"My name is {self.name} and my biggest dream is to be a {dream_job} "

bro = Human("Kevin", 18, "playing games", "binus university")

print(bro.introduce())
print(bro.do_hobby)
print(bro.goal("Software Engineer"))

