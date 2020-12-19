#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang

'''
可变对象，传参
'''
def test_1(data):

    if isinstance(data, list):

        data.append("abc")


if __name__ == '__main__':
    test_data = [1 ,2 ,3]

    test_1(test_data)

    print(test_data)
    pass




