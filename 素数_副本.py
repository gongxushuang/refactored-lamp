#从解决问题的角度写代码，需要什么函数就定义什么
#def print_primes(begin, end):
#    for i in range(begin, end+1):
#       for j in range(2, i):
#           if i % j ==0
#判断完是否整出之后，我们现在的问题是如何呈现，这里有几种方法
#1.在函数里定义print，使得判断后打印，然后在循环的过程中我们就可以不断打印出结果
#2.我们可以定义一个列表，使得每一个结果添加到列表中，最后打印列表
#3.注意到这个定义函数过长，我们可以拆分
#4.历遍和打印素数是一个函数，然后判断是一个函数，在历遍和打印里面执行判断函数

def print_primes1(begin, end):
    for i in range(begin, end+1):
        for j in range(2, i):
            if i % j ==0:
                break
        else:
            print(i)
#这里用了一个for else循环，相当于执行完每一个判断后，只要没有不符合的break就可以对
#通过的结果进行else的控制处理
"""for item in sequence:
    # 循环体
    if condition:
        break  # 提前退出循环
else:
    # 如果循环正常结束（没有break），执行这里"""
list=[]
def print_primes2(begin, end):
    for i in range(begin, end+1):
        for j in range(2, i):
            if i % j ==0:
                break
        else:
            list.append(i)
    print(list)



def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    for i in range(2,num):
        if num % i == 0:
            return False
    return True
#一旦有整除就false，下面的if is_primes（i）就是错的，不会打印
def print_primes3(begin, end):
    for i in range(begin, end+1):
        if is_prime(i):
            print(i)

#这是一个标志变量的标准模式
""""
# 1. 初始化标志
flag = True  # 或 False，表示初始状态

# 2. 在程序运行中可能改变标志
if 某个条件成立:    #在运行过程中验证假设是否成立，发现了反例，改变状态
    flag = False  

# 3. 根据最终标志值执行操作
if flag:
    # 初始假设成立，条件满足时执行
else:
    # 初始假设不成立，条件不满足时执行
"""

# 1. 假设是素数
for i in range(11,25):
    is_prime = True#每一个i都重置is_prime，使得初始都是true
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False  # 2. 找到矛盾（因子）
            break
            # 3. 得出结论
    if is_prime:
        print(i)
#因为写代码还有一个复杂度的问题，他不是由你的代码写的多少和长度决定
#而是由你的执行过程中输入规模和算法逻辑决定，本质上是执行次数的增长趋势
#这里如果你输入1亿长度的区间去判断，可能执行会很慢
#这时我们就需要优化代码，这就是为什么我们只判断到i**（1/2）
#因为以后的都是重复，比如4*9和9*4之于36，只需要判断到4，我就知道36可以整除4和9了
#我们的运行次数就少了



#现在我就要历遍range，对每一个进行判断
#标准是这个数能否被自己以外的数整除，那我们可以对每一个都做一下判断
#这里注意我们不需要判断比本身大的数，肯定不是该数的因子
#因此我们还需要对小于本身的数进行历遍


begin=11
end=25




