import pymysql


# 打开数据库连接
class MysqlDb:
    def __init__(self):
        self.host = '127.0.0.1'
        self.user = 'root'
        self.passwd = 'admin_root'
        self.database = 'cloud_talk'
        self.db = None
        self.connect()

    def connect(self):
        self.db = pymysql.connect(self.host, self.user, self.passwd, self.database)

    def select(self, sql):
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = self.db.cursor()
        try:
            # 使用 execute()  方法执行 SQL 查询
            cursor.execute(sql)
            # 使用 fetchone() 方法获取全部数据.
            data = cursor.fetchall()

            return data
        except:
            return 0

    def insert(self):
        # 使用cursor()方法获取操作游标
        cursor = self.db.cursor()
        # SQL 插入语句
        sql = ''
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
        except:
            # 如果发生错误则回滚
            self.db.rollback()

    def delete(self):
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = self.db.cursor()
        # SQL删除记录语句
        sql = ""
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 向数据库提交
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()

    def update(self,sql):
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = self.db.cursor()
        # SQL更新记录语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 向数据库提交
            self.db.commit()
            return 1
        except:
            # 发生错误时回滚
            self.db.rollback()
            return 0

    def close(self):
        # 关闭数据库连接
        self.db.close()

# if __name__ == '__main__':
#     db = MysqlDb()
#     data = db.select()
#     print(data)
#     db.close()


# fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
# fetchall(): 接收全部的返回结果行.
# rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。
