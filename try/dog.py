class Dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def HAHA(self):
        print("My name is {}".format(self.name))

my_dog=Dog("小花",3)
my_dog.HAHA()
print(my_dog.name)
print(my_dog.age)