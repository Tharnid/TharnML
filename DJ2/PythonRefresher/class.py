class Dog:
    
    dogInfo = "yeah...dogs are cool"
    
    def __init__(self, name, age, furcolor):
        self.name = name
        self.age = age 
        self.furcolor = furcolor

    def bark(self):
        print("Bark!!!")

    def bark2(self, str):
        print("BARK!!!" + str)

mydog = Dog("Duke", 9, "Brown")
mydog.bark()
mydog.bark2("asdfasdfasdfasdf")

mydog.name = 'Duke'
mydog.age = 11
print(mydog.name)
print(mydog.age)

print(Dog.dogInfo)

nextDog = Dog("Rufus", 10, "Gray")

print(nextDog.name)
print(mydog.name)