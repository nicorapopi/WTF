class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def show_name(self):
        print(f"{self.name}")

    def show_score(self):
        print(f"{self.score}")

    def check_status(self):
        if self.score >= 80:
            print("pass")
        else:
            print("fail")

p1 = Student("Thanakrit", 80)
p1.show_name()
p1.show_score()
p1.check_status()
