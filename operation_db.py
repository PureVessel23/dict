"""
数据处理
"""
import pymysql
import hashlib
import time

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

	
	# 处理注册
	def register(self, name, passwd):
		sql = 'select * from user where name = "%s"' % name
		self.cur.execute(sql)
		r = self.cur.fetchone()
		
		# 如果查找到，则说明用户已存在
		if r:
			return False
		
		# 加密处理
		hash = hashlib.md5((name + 'the-salt').encode())
		hash.update(passwd.encode())		

		sql = 'insert into user (name,passwd) values (%s,%s)'
		try:
			self.cur.execute(sql, [name, hash.hexdigest()])
			self.db.commit()
			return True
		except Exception:
			self.db.rollback()
			return False

	# 处理登录
	def login(self, name, passwd):
		
		hash = hashlib.md5((name + 'the-salt').encode())
		hash.update(passwd.encode())

		sql = 'select * from user where name = %s and passwd = %s'
		self.cur.execute(sql, [name, hash.hexdigest()])
		r = self.cur.fetchone()

		if r:
			return True
		else:
			return False


	# 插入历史记录
	def insert_history(self, name, word):
		tm = time.ctime()

		sql = 'insert into hist (name, word, time) values (%s,%s,%s)'
		try:
			self.cur.execute(sql, [name, word, tm])
			self.db.commit()
		except Exception:
			self.db.rollback()

	# 查单词
	def query(self, word):
		sql = 'select mean from words where word = %s'
		self.cur.execute(sql, [word])
		r = self.cur.fetchone()
		if r:
			return r[0]


	# 历史记录
	def history(self, name):
		sql = 'select name, word, time from hist where name=%s order by id desc limit 10'
		self.cur.execute(sql, [name])
		return self.cur.fetchall()		











	
