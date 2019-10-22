#_*_coding=utf-8_*_

# 定义一个类叫Room是一个对象
class Room(object):
	
    # 初始化定义（如果调用这个初始化则需要三个参数）
	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.paths = {}
	
    # 定义一个函数go， 需要两个参数（self、direction）
	def go(self, direction):
		return self.paths.get(direction, None) # 返回一个路径给go
	
    # 定义一个函数add_paths, 需要两参数（self、paths）
	def add_paths(self, paths):
		self.paths.update(paths)   # 更新路径
        
center = Room("Center", "Test room in the center.")
north = Room("North", "Test room in the north.")

print north
print center.go('north')
