# /usr/bin/python
# 总体来说，交换操作的处理时间大约是移动操作的3倍，因为后者只需进行一次赋值。在基准测试中，插入排序算法的性能很不错。

def quicksort(alist):
    for index in range(1,len(alist)):
