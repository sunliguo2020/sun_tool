# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/5/30 12:14
"""
import pymysql
from dbutils.pooled_db import PooledDB

POOL = PooledDB(
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
    db='crawl',
    charset='utf8'
)


class Connect(object):
    def __init__(self):
        self.conn = conn = POOL.connection()
        self.cur = conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cur.close()
        self.conn.close()

    def exec(self, sql, **kwargs):
        self.cur.execute(sql, kwargs)
        self.conn.commit()

    def fetch_one(self, sql, **kwargs):
        self.cur.execute(sql, kwargs)
        result = self.cur.fetchone()
        return result

    def fetch_all(self, sql, **kwargs):
        self.cur.execute(sql, kwargs)
        result = self.cur.fetchall()
        return result
