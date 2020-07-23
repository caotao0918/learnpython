# pymysql的使用
import pymysql


def main():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456',
                           db='hrs', charset='utf8')
    print(conn)
    try:
        with conn.cursor() as cursor:
            cursor.execute('delete from tb_dept where dno=50')
            res = cursor.execute('insert into tb_dept values(50, "研发二部", "驻马店")')
            cursor.execute('update tb_dept set dloc="南京" where dno=50')
            res1 = cursor.execute('select * from tb_dept')
            print(res1)
            if res == 1:
                print('成功！')
            conn.commit()
    except pymysql.MySQLError as error:
        print(error)
        print('插入失败！！！')
        conn.rollback()
    finally:
        conn.close()


if __name__ == '__main__':
    main()
