# coding: utf-8

# print("--------------------------------")
def print_multiple_chart(n):
    '打印乘法口角表的函数'
    for i in range(n):
        for j in range(i + 1):
            print('%d * %d = %2d' % ((j + 1) , (i + 1) , (j + 1)* (i + 1)), end='  ')
        print('')

if __name__ == '__main__':


    print_multiple_chart(3)
    print_multiple_chart(4)
    print_multiple_chart(5)