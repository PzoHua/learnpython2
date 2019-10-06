#_*_coding=utf-8_*_
import os


# 创建一个叫新文件的类，这是一个测试文件目录
def new_file(test_dir):
    # 列举测试文件目录下的所有文件（名），结果以列表的形式返回。
    lists = os.listdir(test_dir)
    # sort按key的关键字进行升序排序，lambda的参数fn为列表lists的元素，获取文件
    # 的最后修改时间，所以最终以文件时间从小到大排序，
    # 最后对文件lists元素，按文件修改时间大小，从小到大排序
    lists.sort(key = lambda fn:os.path.getmtime(test_dir + '\\' + fn))
    # 获取最新文件的绝对路径，列表中的最后一个值，文件夹+文件名
    file_path = os.path.join(test_dir, lists[-1])
    # 返回值
    return file_path
    
print new_file('c:\\work\\student_img')

# 总结：获取一个文件夹下的所有文件，对所有文件按照修改时间排序，获取最新的文件
