#_*_coding=utf-8_*_*_coding

print "\n\t复习Python各种符号及其功能\n"
print """
1.Keywords(关键字)

符号            功能
and             与（逻辑运算符）
del             删除
from            用来导入文件或函数（导入包）
not             非（逻辑运算符）
while           当...为真则循环（循环语句）
as              作为（指定到每个变量）
elif            条件语句（需要二次以上的选择时使用，插在if...else中使用）
global          全局变量声明
or              或者（逻辑运算符）
with            try/finally语句的替代
assert          assert语句用来声明某个条件是真的
yield           带有yield的函数在Python中被称为generator（生成器）
break           跳出循环
continue        跳出当前循环执行下次循环
print           打印
exec            exec语句用来执行存储在代码对象、字符串、文件中的Python语句
raise           抛出异常
return          返回
lambda          匿名函数
"""

print """
2.String Formats(字符串格式化）
%d              十进制整数
%i              十进制整数
%o              八进制整数
%u              无符号十进制数
%x              无符号十六整数
%e              指数（基底写为e）
%E              指数（基底写为E）
%f              浮点数
%F              浮点数
%g              指数（基底写为e）或浮点数
%G              指数（基底写为E）或浮点数
%c              单个字符
%r              字符串（represent（））
%s              字符串（str（））
%%              字符'%'
"""

print """
3.Escape Sequences(字符串转义序列）
\\               （在行尾时）续航符
\\                反斜杠
\'                单引号
\"                双引号
\\a               响铃（bell）
\\b               退格(backspace)
\\f               换页
\\r               将当前位置提到所在行的第一位，依次覆盖原来的数据
\\t               横向制表符
\\v               纵向制表符
\\000             空
\\e               转义
\\oyy             八进制数yy代表的字符，如\o12代表换行
\\xyy             十进制数yy代表的字符，如\x0a代表换行
\other            其他的字符以普通格式输出
"""

print """
4.操作符
+                 加
-                 减
*                 乘
/                 除
%                 取余数
//                取整数
**                幂运算 (4**5，表示4的5次方)
<                 小于
>                 大于
<=                小于等于
>=                大于等于
==                等于
!=                不等于
<>                不等于
()                元组
[]                列表
{}                字典
@                 Decorator,修饰器
,                 不换还
：                用于函数或块的标识符
.                 层级调用
=                 赋值
；
+=                递增(x = x + 1 等价于 x+=1)
-=                递减
*=                
/=
//=                
%=
**=
"""

print """
5.特殊操作符
and               逻辑与运算
or                逻辑或运算
not               逻辑非运算
is                比较对象
is not            比较对象
in                序列类型成员判断        
not in            序列类型成员判断
"""

