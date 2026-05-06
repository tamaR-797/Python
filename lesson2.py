def reverse_list(list1):
    list1.reverse()
    return list1


print(reverse_list([51, 63, 3, 6, 5564]))


def cal_avg(list2):
    sum=0
    for i in list2:
        sum += i
    return sum / len(list2)


print(cal_avg([51, 63, 3, 6, 55]))


def fib(n):
    arr=[]
    temp1=0
    temp2=1
    for i in range(n):
        arr.append(temp1+temp2)
        temp1 = temp2
        temp2 = arr[i]
    return arr

print(fib(15))