# /usr/bin/env python
# -*- coding: utf-8 -*-
#reduce的工作过程是 ：在迭代序列的过程中，首先把 前两个元素（只能两个）传给 函数，函数加工后，然后把 得到的结果和第三个元素 作为两个参数传给函数参数， 函数加工后得到的结果又和第四个元素 作为两个参数传给函数参数，依次类推。
#map()方法会将 一个函数 映射到序列的每一个元素上，生成新序列，包含所有函数返回值。
#filter(function, sequence)：对sequence中的item依次执行function(item)，将执行结果为True的item组成一个List/String/Tuple（取决于sequence的类型）filter(function or None, sequence) -> list, tuple, or string：入参为函数和列表/元组/字符串，返回值为item列表/元组/字符串。

def test(x,y):
    return x+y
print reduce(test,[i for i in range(10)])
print map(lambda x:x+1,[i for i in range(10)])
print filter(lambda x:x-5,[i for i in range(10)])

