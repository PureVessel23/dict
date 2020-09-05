"""
数据处理
"""
import pymysql

# 编写功能类，提供给服务端使用
class Database:
	def __init__(self, database='dict', host='localhost', user='root', password='@Jiraiya2323', port=3306, charset='utf8'):
		self.database = database
		self.host = host
		self.user = user
		self.password = password
		self.port = port
		self.charset = charset
        	# 链接数据库
		self.__connect_db()

	def __connect_db(self):
		self.db = pymysql.connect(database=self.database, host=self.host, user=self.user, password=self.password, port=self.port, charset=self.charset)

	# 单独创建游标
	def create_cursor(self):
		self.cur = self.db.cursor()

	# 关闭数据库
	def close(self):
		self.cur.close()
		self.db.close()
