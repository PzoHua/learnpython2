from sys import argv

script, first ,second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

-----------------------------------------------------------------------------
#####
这句命令中的 ex13.py 部分就是所谓的“参数(argument)”

“import”语句. 这是你将 python 的功能引入你的脚本的方法，
所谓脚本，就是你写的 .py 程序

argv 是所谓的“参数变量(argument variable)”，是一个非常标准的编程术语。
script, first ,second, third = argv -------“把 argv 中的东西解包，将所有的参数依次赋予左边的变量名”。 


把这些我们导入(import)进来的功能称作模组。你将看到类似这样的说法：“你需 要把 sys 模组 import 进来。
”也有人将它们称作“库(libraries)”，不过我们还是叫它们模组吧。
