# pymysql的使用
import pymysql


# 增删改查

def main():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456',
                           db='hrs', charset='utf8')
    print(conn)
    try:
        with conn.cursor() as cursor:
            res2 = cursor.execute('delete from tb_dept where dno=50')
            if res2 == 1:
                print('删除成功！！！')

            res = cursor.execute('insert into tb_dept values(50, "研发二部", "驻马店")')
            if res == 1:
                print('插入成功！！！')

            res3 = cursor.execute('update tb_dept set dloc="南京" where dno=50')
            if res3 == 1:
                print('修改成功！！！')
            # 查询
            res1 = cursor.execute('select dno, dname, dloc from tb_dept')
            print('行数：', res1)
            print(cursor.fetchmany(2))

            # for row in cursor.fetchall():
            #     print(f'部门编号：{row[0]}')
            #     print(f'部门名称：{row[1]}')
            #     print(f'部门地址：{row[2]}')
            #     print('-------------')

            conn.commit()
    except pymysql.MySQLError as error:
        print(error)
        print('插入失败！！！')
        conn.rollback()
    finally:
        conn.close()


if __name__ == '__main__':
    main()
