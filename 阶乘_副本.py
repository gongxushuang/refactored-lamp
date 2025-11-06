#阶乘的运算
#实际上是一个不断相乘的结果，因此，我们用循环实现
#因为循环次数由输入决定，因此我们用while实现
#为了可循环利用，我们可以定义一个函数

#然后我们就要思考，这个函数怎么定义去计算阶乘
#由于是一个数不断乘小于自己的数，我们可以循环减一，再与上一次的结果相乘
#在最初时，我们应该定义一个变量储存，初始化为1
def get_jiecheng(number):
    result=1
    while number>0:
        result=result * number
        number=number-1
    print(result)

#我们也可以用for实现
def main(number):
    result=1
    for i in range(1,number+1):
        result=result * i
    print(result)
jiecheng_8=main(8)
print(jiecheng_8)




