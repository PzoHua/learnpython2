# learn formatstring
my_name = 'Zed A. Shaw'
my_age = 35      # not a  lie
my_height = 74   # inches
my_weight = 180  # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "He's got %s eyes and %s hair." % (my_eyes,my_hair)
print "Actually that's not too heavy."
print "His teeth are usually %s depending on the coffee." % my_teeth
# this line is tricky,try to get it exactly right
print "If I add %d,%d,and %d I get %d."  % (my_age,my_height,my_weight,my_age+my_height+my_weight)

-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------

这次的程序是学习格式化字符串（formatstring）的概念及用法

概念：给真正要输出的值预留位置，根据输出的真实值类型（如数字、字符串等）不同，预留方式（通过%控制）也不一样。就像填空题，根据所填答案长短不一，所留的
横线的长短不一样？？？
也像建筑模板，预留所需的混凝土的容积，不同位置留的空间大小不一样。可以想象自己熟悉的现实生活中的场景。
再比如：一个网站需要收集用户的信息，然后经数据处理后反馈调查结果。#在收集用户信息时，填写个人资料 such as name,weight,height,eyes,hair 等
然后把相应的用户信息导入预先制好的程序，程序需要能识别用户填写的数据类型，最后分析输出结果。

%d   # %表示这里有预留位置，d表示十进制整数。（%d即为整数预留的位置） 
%s   # 字符串 (包括数值)
%r   # 全部输出  包括单引号等
%c   # 单个字符
%b   # 二进制
%i   #也是十进制整数
%x   #十六进制整数
%o   #八进制整数
%e   #指数（基地为e）
%E   #指数（基地为E）
%f   #浮点数（小数）
%F   #浮点数（同上）
%g   #指数g或浮点数
%G   #指数G或浮点数
%%   #字符%

一个问题：如果输入的数据与预留的位置不一致会怎么样？
如：print "Let's talk about %d." %  my_name
  TypeError: %d format: a number is required, not str
