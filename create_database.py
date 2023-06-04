import psycopg2

print('开始')
conn = psycopg2.connect(database="rarbg",
                        host="192.168.2.120",
                        user="rarbg",
                        password="rarbg",
                        port="5432")
cursor = conn.cursor()

s = ("CREATE TABLE IF NOT EXISTS items ("
     "magnet text primary key,"
     "title text,"
     "category integer"
     ");")
print(s)
cursor.execute(s)
conn.commit()
conn.close()

print('结束')
