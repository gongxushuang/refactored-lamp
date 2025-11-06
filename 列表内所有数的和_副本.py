#sum本身就是下列程序代码，我们平时直接用sum即可
def sum_of_list(para_list):
    sum=0
    for item in para_list:
        sum+=item
    return sum
print(sum_of_list([1,5,6,7,8,345,67]))
list=[1,3,45,67,5]
print(f"sum of {list} is {sum_of_list(list)}")