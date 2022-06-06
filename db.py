# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/5/30 7:41
"""
import pymysql
from dbutils.pooled_db import PooledDB


class DBHelper(object):
    def __init__(self,table= '',database='crawl'):
        self.pool = PooledDB(
            creator=pymysql,
            maxconnections=50,
            mincached=2,
            maxcached=3,
            blocking=True,
            setsession=[],
            ping=0,
            host='192.168.1.207',
            port=3306,
            user='root',
            passwd='admin',
            db=database,
            charset='utf8'
        )

    def get_conn_cur(self):
        conn = self.pool.connection()
        cur = conn.cursor()
        return conn, cur

    @staticmethod
    def close_conn_cur(*args):
        for item in args:
            item.close()

    def exec(self, sql, kwargs):
        """

        防止sql注入的形式，执行sql语句
        :param sql: sql语句: insert into table_name (id, name) value (%(id)s, %(name)s)
        :param kwargs: **{id:1, name: "hxc"}
        :return:
        """
        conn, cur = self.get_conn_cur()
        result = cur.execute(sql, kwargs)
        if result == 0:
            print("Number of affected rows is 0")
        elif result >0:
            print("执行完成，Number  of affected rows is ",result)

        conn.commit()
        self.close_conn_cur(conn, cur)

        return result

    def fetch_one(self, sql, **kwargs):
        # print('kwargs:',kwargs)
        conn, cur = self.get_conn_cur()
        cur.execute(sql, kwargs)
        result = cur.fetchone()
        self.close_conn_cur(cur, conn)
        return result

    def fetch_all(self, sql, **kwargs):
        conn, cur = self.get_conn_cur()
        cur.execute(sql, kwargs)
        result = cur.fetchall()
        self.close_conn_cur(cur, conn)
        return result


db = DBHelper()
