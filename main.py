class Person:
    def __init__(self, a_name, a_age, a_hp):
        self.name = a_name
        self.age = a_age
        self.hp = a_hp


person1 = Person("민수", 23, "010-0000-0000")
person2 = Person("영희", 21, "010-0000-0001")

print(f"안녕하세요 저는 {person1.name}입니다.")
print(f"안녕하세요 저는 {person2.name}입니다.")