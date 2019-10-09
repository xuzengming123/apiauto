import MySQLdb

# 创建一个connection对象，代表了一个数据库的连接
connection =  MySQLdb.connect(
                    host='192.168.80.21',     #数据库IP地址
                    user='qa_test01',             #mysql用户名
                    passwd='xvjQ073Q9RTI1CcVwZ4C',           #mysql用户登录密码
                    db='test',               #数据库名
                    #如果数据库里面的文本是utf-8编码的，
                    #charset指定是utf-8
                    charset = 'utf8'
)

# 返回一个cursor对象
c = connection.cursor()


c.execute("""SELECT * FROM sq_course """)
rows = c.fetchall()
print(rows)

# 插入一条数据

c.execute("INSERT INTO sq_course (name,`desc`,display_idx) VALUES ('c++','c++课程',2)")
# 提交
connection.commit()

c.execute("""SELECT * FROM sq_course """)
rows = c.fetchall()
print(rows)

connection.close()