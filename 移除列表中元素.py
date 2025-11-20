# def remove_elements_form_list(lista,listb):
#     for item in lista:
#         if item in listb:
#             lista.remove(item)
#     return lista
# list1=[1,5,67,9]
# list2=[1,5]
# print(remove_elements_form_list(list1,list2) )

#这个代码不是很对，因为你对列表进行了一些修改，这些修改使得列表数发生改变，列表项发生移动
#对for循环很不友好，因为当你对列表第0个1做出判断删除后，循环来到列表第2个67，也就是5被略过了，无法进行判断

#那我们就不进行判断了，直接对listb进行历遍，listb中的每一个项，都在lista中删除，没有该项就操作为零
def remove_elements_form_list(lista, listb):
    for item in listb:
        lista.remove(item)
    return lista

#还有一种更简洁的，叫列表推导式，是python中一种简洁的创建列表的方法
#基本语法是[expression for item in iterable if condition]
#expression是指的最终会放进新列表的内容，可以对item进行一些操作
#for item in iterable是循环部分，这里的iterable是指任何可迭代对象
# 如字符串string，元组tuple，范围range，集合set，字典dictionary（可以遍历键值对或键或值）
# 文件对象file，生成器generator
#不管迭代对象是什么，列表推导式的结果是中是一个列表，也就是它可以从各种数据源中创建列表
#if condition是指可选部分，用于过滤元素，只有满足条件的元素才可以被收录
def remove_elements_from_list(lista, listb):
    return[item for item in lista if item not in listb]
#item/for item in lista/if item not in listb
list1=[1,3,56,7,8]
list2=[1,3]
print(remove_elements_from_list(list1, list2))

