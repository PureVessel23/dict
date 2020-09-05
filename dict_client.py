"""
dict 客户端
发起请求，展示结果
"""

from socket import *
from getpass import getpass


ADDR = ('0.0.0.0', 8000)

s = socket()
s.connect(ADDR)

# 注册
def do_register():
	while True:
		name = input('User:')
		passwd = getpass()
		passwd_copy = getpass('Please Enter Again:')


		if (' ' in name) or (' ' in passwd):
			print('用户名或密码不能存在空格')
			continue
		
		if passwd != passwd_copy:
			print('两次密码不一致')
			continue

		msg = 'R %s %s' % (name, passwd)
		# 发送请求
		s.send(msg.encode())
		# 接收反馈
		data  = s.recv(128).decode()
		if data == 'OK':
			print('注册成功')
		else:
			print('注册失败')

		return

		

# 创建网络连接
def main():
	
	while True:
		print("""
		------------welcome--------------
		1. 注册      2. 登录      3. 退出
		""")	
		cmd = input('请输入选项:')
		if cmd == '1':
			do_register()
		elif cmd == '2':
			pass
		elif cmd == '3':
			pass
		else:
			print('请输入正确命令')


if __name__ == "__main__":
	main()
