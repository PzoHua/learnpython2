
	def __init__(self, name):
		## 调用该类后，优先执行下行代码，需要两参数
		self.name = name
		
		## Person has-a pet of some kind
		self.pet = None
		
## Employee is-a Person
class Employee(Person):

	def __init__(self, name, salary):  # 该初始化函数需要三个参数调用
	## 
	    super(Employee, self).__init__(name)
	## ??
	    self.salary = salary
	
## 创建一个类Fish，内容待定
class Fish(object):
	pass
	

## 创建一个类Salmon, 参数为另一个类
class Salmon(Fish):
	pass
	

## rover is-a Dog
rover = Dog("Rover")
print rover.name

## satan is-a Cat
satan = Cat("Satan")
print satan.name

## mary is-a Person
mary = Person("Mary")
print mary.name
print mary.pet

## puzhonghua is-a Employee
puzhonghua = Employee("puzhonghua", "100")
print puzhonghua.salary

## xiaoka is-a Fish
xiaoka = Fish()

## najah is-a Salmon
najah = Salmon(
