# 电子词典

## 功能说明

#### 用户可以登录和注册

- 登录凭借用户名和密码登录
- 注册要求用户必须填写用户名，密码，其他内容自定
- 用户名要求不能重复
- 要求用户信息能够长期保存

#### 可以通过基本的图形界面 print 以提示客户端输入

- 程序分为服务端和客户端两部分
- 客户端通过 print 打印简单界面输入命令发起请求
- 服务端主要负责逻辑数据处理

#### 客户端启动后进入一级界面，包含如下功能：登录、注册和退出

- 退出后即退出该软件
- 登录成功进入二级界面，失败返回一级界面
- 注册成功可以返回一级界面继续登录，也可以直接用注册用户进入二级界面

#### 用户登录后进入二级界面，功能如下：查单词、历史记录、注销

- 选择注销则返回一级界面
- 查单词：循环输入单词，得到单词解释，输入特殊符号退出查单词查询状态
- 历史记录：查询当前用户的查词记录，要求记录包含 name，word，time，可以查看所有记录或者前 10 条均可

#### 单词本说明

- 每个单词一定占一行
- 单词按照从小到大顺序排列
- 单词和解释之间一定有空格

#### 查词说明

- 直接使用单词本查询（文本操作）
- 先将单词存入数据库，然后通过数据库查询（数据库操作）

## 分析

#### 确定技术

- 通信：TCP 通信
- 并发：多进程并发
- 数据库：MySQL

#### 确定数据库

- 建表：
  - 用户表：id（int，primary key，auto_increment），name（varchar(32)，not null），passwd（varchar(128)，not null）
  - 历史记录：id，name，word（varchar(32)，not null），time（varchar(64)，not null）
  - 单词表：id，wrod，mean（text，not null）
- 编写程序将单词本存入数据库

#### 结构设计

- 客户端
- 服务端（处理数据）

#### 功能分析

客户端：
- 网络模型
- 登录
  - 客户端
    - 输入登录信息
    - 发送请求
    - 得到回复
  - 服务端
    - 接受请求
    - 判断是否允许登录
    - 反馈结果
- 注册
  - 客户端
    - 输入注册信息
    - 将信息发送给服务端
    - 等待反馈
  - 服务端
    - 接收注册信息
    - 验证用户是否存在
    - 插入数据库
    - 将信息反馈给客户端
- 查词
  - 客户端
    - 输入单词
    - 发送给服务器
    - 获取结果
  - 服务端
    - 接收请求
    - 查找单词
    - 反馈结果
    - 插入历史记录
- 历史记录
  - 客户端
    - 发送请求
    - 循环接收历史记录
  - 服务端
    - 接收请求
    - 查询历史记录
    - 发送历史记录

服务端：

## 协议

注册 R name passwd

登录 L  name passwd 

查词 Q  name word 

历史记录 H name

## cookie

```python
import getpass

getpass.getpass()
功能：隐藏输入内容
返回值：输入的字符串内容
```

```python
import hashlib

# 生成加密对象，参数为盐
hash = hashlib.md5('the salt'.encode())

# 对密码进行算法加密
hash.update(passwd.encode())

# 获取加密后的密码字串
hash.hexdigest()
```


