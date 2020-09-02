import pymysql
import re

f = open('word_book.txt')
db = pymysql.connect(host='localhost', port=3306, user='root', password='@Jiraiya2323', database='dict', charset='utf8')
cur = db.cursor()

sql = 'insert into words (word,mean) values (%s,%s)'

for line in f:
    tup = re.findall(r'(\w+)\s+(.+)', line)[0]

    try:
        cur.execute(sql, tup)
        db.commit()
    except Exception:
        db.rollback()

f.close()
cur.close()
db.close()
