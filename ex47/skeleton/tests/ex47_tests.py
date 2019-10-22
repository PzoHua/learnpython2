#_*_coding=utf-8_*_

# 测试专用的骨架文件
from nose.tools import *
from ex47.game import Room


# 由断言函数assert_equal(a, b)测试，即核实a==b

# 测试类Room初始化内容
def test_room():

    # 在类Room中创建一个实例gold, 通过三个参数（gold、"GoldRoom"和"""This...."""）
    # 初始化该实例
    gold = Room("GoldRoom",
            """This room has gold in it you can grab. There's a
            door to the north.""")
    # 断言方法assert_equal， 用来核实gold.name == "GoldRoom"       
    assert_equal(gold.name, "GoldRoom") 
    assert_equal(gold.paths, {})


# 测试类Room中的go函数
def test_room_paths():

    # 调用类创建实例，三个参数初始化实例内容
    center = Room("Center", "Test room in the center.")
    north = Room("North", "Test room in the north.")
    south = Room("South", "Test room in the south.")
    
    # From center get the add_paths attributr, and set it 字典
    center.add_paths({'north': north, 'south': south})
    assert_equal(center.go('north'), north) # 断言判断两个值，值一：center.go('north')为None;值二：north为<__main__.Room object at 0x02F79950>
    assert_equal(center.go('south'), south) 

# 测试类Room中的go函数
def test_map():
    start = Room("Start", "You can go west and down a hole.")
    west = Room("Trees", "There are trees here, you can go east.")
    down = Room("Dungeon", "It's dark down here, you can go up.")
    
    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})
    
    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)
    
