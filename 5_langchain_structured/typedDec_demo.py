from typing import TypedDict

class student(TypedDict):
    name:str
    age:int
    marks:float

student1: student={
    "name":'jonny',
    "age":21,
    "marks":90.20
}

print(student1)