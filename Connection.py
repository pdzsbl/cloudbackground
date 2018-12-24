from impala.dbapi import connect
from multiprocessing import Process
import time

conn = connect(host='192.168.38.129', port=10000, auth_mechanism='PLAIN',
               user='root', password='Tmy15954031572?', database='shop')
cur = conn.cursor()
print('successfully connected')


def login(id, password):
    global cur
    try:
        sql = 'select password from usersheet where id="%s"' % id
        cur.execute(sql)
        results = cur.fetchall()
        # doesn't exists
        if len(results) == 0:
            return False

        pw = results[0][0]
        # check the given password
        return password == pw
    except:
        return False


def registry(id, password):
    global cur
    #try:
    sql = 'select id from usersheet where id="%s"' % id
    cur.execute(sql)
    results = cur.fetchall()
    #         # already exists
    if len(results) != 0:
        return False

    sql = 'insert into table usersheet values("%s", "%s")' % (id, password)
    cur.execute(sql)
    return True
    #except:
     #   return False


def getinfo():
    global cur
    try:
        cur.execute('select * from movie limit 15')
        results = cur.fetchall()
        item_info = list()
        for item in results:
            iteml = list(item)
            iteml.append('./img/images/' + item[0] + '.jpg')
            item_info.append(iteml)

        return item_info

    except:
        return None


def orderinfo(customerid):
    global cur
    try:
        sql = 'select * from bill where customerid="%s"' % customerid
        cur.execute(sql)
        results = cur.fetchall()
        return results

    except:
        return None


def buy(customerid, itemid, quantity):
    global cur
    print("buying")

    try:
        sql = 'select remain from movie where id="%s"' % itemid
        print(sql)
        cur.execute(sql)
        results = cur.fetchall()

        remain = results[0][0]
        print(remain)
        # not enough
        if remain < quantity:
            return False

        # timestamp + itemid
        id = str(int(time.time())) + itemid
        new_remain = remain - quantity
        # create order
        print("creating order")
        sql = 'insert into table bill values("%s", "%s", "%s", %s)' % (id, customerid, itemid, quantity)
        cur.execute(sql)
        p = Process(target=update, args=(new_remain,itemid,))
        p.start()
        return True
    except:
        return False

def update(new_remain, itemid):
    global cur
    print("changing remain")
    sql = 'update movie set remain=%s where id=%s' % (new_remain, itemid)
    try:
        cur.execute(sql)
    except:
        print("update err")

def search(minprice,maxprice,keyword):
    """首先判断各个参数是否为空，不为空加入到sql语句中"""
    sql = 'select * from item where '
    if keyword!="":
        sql+=" name like '%"+keyword+"%' and"
    if minprice!="":
        sql+=" price >= "+ minprice +" and"
    if maxprice!="":
        sql+=" price <= "+ maxprice +" and"
    sql+=" remain > -1;"
    try:

        cur.execute(sql)
        results = cur.fetchall()
        item_info = list()
        for item in results:
            iteml = list(item)
            iteml.append('./img/images/' + item[0] + '.jpg')
            item_info.append(iteml)
        return item_info

    except:
        return False
#registry("test_user", "pass")
'''
registry("test_user3", "pass")

login("test_user", "password")
login("test_user", "pass")
login("test", "pass")

getinfo()
orderinfo("test_user")

buy("test_user", "11181", 1)
'''
'''
cur.close()
conn.close()
'''