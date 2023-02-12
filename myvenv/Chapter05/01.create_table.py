# 모듈추가 
import sqlite3

# 데이터 베이스 열기
conn = sqlite3.connect('Chapter05/SQL_DDL.db')

#커서 생성
cur= conn.cursor()

# sql 명령 작성
create_sql ="""
    create table if not exists item(
    id integer primary key autoincrement,
    code text not null,
    name text not null,
    price integer not null
    )
"""
# sql 명령 실행
cur.execute(create_sql)

# 데이터베이스 닫기
conn.close()