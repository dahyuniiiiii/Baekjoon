class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Address: {self.address}"

# 두 개의 인스턴스 생성
dahyun = Person(name="Dahyun", age=23, address="Incheon")
mingyu = Person(name="Mingyu", age=25, address="Asan")

# 정보 출력
print(dahyun)
print(mingyu)