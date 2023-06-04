import psycopg2
from psycopg2.extras import execute_values

conn = psycopg2.connect(database="rarbg",
                        host="192.168.2.120",
                        user="rarbg",
                        password="rarbg",
                        port="5432")
cursor = conn.cursor()


def insert(cur, batch):
    execute_values(cur, "INSERT INTO items2 (magnet, title, category) VALUES %s", batch)
    batch.clear()


with open('data/moviesrarbg.txt') as f:
    i = 0
    batch = []
    for line in f.readlines():
        i += 1
        l = line.strip().split('&dn=')
        magnet, name = l[0], l[1]
        magnet = magnet.replace('magnet:?xt=urn:btih:', '')
        if len(magnet) != 40:
            print('error')
        else:
            batch.append((magnet, name, 1))
        if i % 1000 == 0:
            insert(cursor, batch)
            print('处理了' + str(i) + '条数据')
    insert(cursor, batch)
conn.commit()
count = cursor.rowcount
print(count, "Record inserted successfully into table")
conn.close()
print('结束')
