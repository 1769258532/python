# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang

import pymysql.cursors


# Connect to the database

# 获得数据库连接


class Context:
    def __init__(self) -> None:
        print("------------init-----------------------------------")
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          port=3307,
                                          password='123456',
                                          db='student',
                                          charset='utf8',
                                          cursorclass=pymysql.cursors.DictCursor)

        self.cursor = self.connection.cursor()

    def __enter__(self):
        print("----enter--------")
        return self.cursor, self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("-----------exit")
        self.cursor.close()
        self.connection.close()


if __name__ == '__main__':
    with Context() as c:
        sql = "INSERT INTO `subject` (`subject_no`, `subject_name`, `ks`, `term_no`) VALUES (%s, %s, %s, %s)"
        c[0].execute(sql, (4, 'oop', 100, 1))
        c[1].commit()

    pass
