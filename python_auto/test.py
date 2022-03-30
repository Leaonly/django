# 冒泡排序

'''
def bubble(bad_list):
    length = len(bad_list) - 1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(length):
            if bad_list[i] > bad_list[i+1]:
                sorted = False
                bad_list[i], bad_list[i+1] = bad_list[i+1], bad_list[i]
bubble(my_list)
print(my_list)
'''
my_list = [23,12,93,291,32,566,3,29,1]

def bubble(bad_list):
    length = len(bad_list) - 1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(length):    
            if bad_list[i] > bad_list[i+1]:
                sorted = False
                bad_list[i], bad_list[i+1] = bad_list[i+1], bad_list[i]

bubble(my_list)
print(my_list)

