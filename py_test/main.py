
def hello(name) :
    '''函数说明'''
    return "hello, " + str(name)


l = [1, 2, 3, 4, 5]
new_list = map(hello, l) # 结果: [2， 4， 6， 8， 10]
for i in new_list:
    print(i)