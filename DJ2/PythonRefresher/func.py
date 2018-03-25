def hello():
    print("Hello from Python!!!")

hello()
hello()
hello()

def hello2(theString):
    print("hello " + theString)

hello2("whatever")

age = 46

name = 'Saldor'

def hello3(name, age):
    print("Hello {}!!! , you are {} years old!!!".format(name, age))

hello3("Aragoth", 56)

def hello4(name="Tharnid", age=72):
    return "Hello {}, you are {} years old".format(name, age)

whatever = hello4()
print(whatever)


def Trippleprint(someString):
    print(someString + someString + someString)

Trippleprint('yeah')