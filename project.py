

import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Sushmitha1@')
cur=mydb.cursor()



#CREATION OF THE DATABASE
cur.execute('create database INVENTORY_MANAGEMENT1')
cur.execute('use INVENTORY_MANAGEMENT1')
#import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Sushmitha1@',database='INVENTORY_MANAGEMENT1')
cur=mydb.cursor()


#CREATION OF THE MANUFACTURE TABLE
a='create table MANUFACTURE1(manufacture_id1 integer primary key,product_id1 integer(4),product_name1 varchar(30),number_of_items1 integer(10),manufacture_date1 date,defective_items1 integer(4),company1 varchar(30),store varchar(40),color1 varchar(30))'

#CREATION OF THE GOODS TABLE
b='create table GOODS1(goods_id1 integer(4),manufacture_date1 date,product_name varchar(30),manufacture_id1 integer(4),store1 varchar(30),FOREIGN KEY(manufacture_id1) REFERENCES manufacture1(manufacture_id1))'

#CREATION OF THE PURCHASE TABLE
c='create table PURCHASE1(purchase_id1 integer(4),goods_id1 integer(4),amount1 integer(6),store1 varchar(40),p_date date,p_name1 varchar(40))'

#CREATION OF SALE TABLE
d='create table SALE1(sale_id1 integer(4),goods_id1 integer(4),sale_date1 date,profit_margin1 integer(4),store1 varchar(40),company1 varchar(4))'
cur.execute(a)
cur.execute(b)
cur.execute(c)
cur.execute(d)
#cur.execute('create table SALE1(sale_id1 integer(4),goods_id1 integer(4),sale_date1 date,profit_margin1 integer(4),store1 varchar(40),company1 varchar(4))')

#INSERTION OF THE VALUES IN MANUFACTURE TABLE
t1='insert into MANUFACTURE1(manufacture_id1,product_id1,product_name1,number_of_items1,manufacture_date1,defective_items1,company1,store,color1) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
a1=(100,200,'shirt',90,'2023-04-01',2,'abc','ORay','blue'),(101,201,'red_toys',90,'2023-04-01',2,'abc','MyKids','red'),(102,202,'wooden_chair',90,'2023-05-01',2,'SS_Export','ajio','black'),(103,203,'shirt',50,'2023-04-07',2,'SS_Export','MyCare','blue')
cur.executemany(t1,a1)
mydb.commit()

#INSERTION OF THE VALUES IN GOODS TABLE
t2='insert into GOODS1(goods_id1,manufacture_date1,product_name,manufacture_id1,store1) values(%s,%s,%s,%s,%s)'
a2=(300,'2023-04-02','shirt',100,'ORay'),(301,'2023-04-03','red_toys',101,'MyKids')
cur.executemany(t2,a2)
mydb.commit()

#INSERTION OF THE VALUES IN PURCHASE TABLE
t3='insert into PURCHASE1(purchase_id1,goods_id1,amount1,store1,p_date,p_name1) values (%s,%s,%s,%s,%s,%s)'
a3=(401,300,700,'ORay','2023-04-21','shirt'),(402,302,2000,'MyKids','2023-04-22','toy'),(403,302,800,'Filpkart','2023-04-23','bag')
cur.executemany(t3,a3)
mydb.commit()

#INSERTION OF THE VALUES IN SALE TABLE
t4='insert into SALE1(sale_id1,goods_id1,sale_date1,profit_margin1,store1,company1) values(%s,%s,%s,%s,%s,%s)'
a4=(501,300,'2023-04-03',456,'ORay','a'),(502,301,'2023-04-04',354,'MyKids','d'),(503,302,'2023-04-02',564,'MyCare','s')
cur.executemany(t4,a4)
mydb.commit()

#s='drop table goods1'
#cur.execute(s)
#mydb.commit()

#s='drop table purchase1'
#cur.execute(s)
#mydb.commit()


#DELETE THE DEFECTIVE ITEM ,EG: THE SHIRT WHICH WAS ACCIDENTALLY PURCHASED BY THE "ORay"STORE,MANUFACTURE ON THE DATE '01-04-2023'
q='DELETE FROM purchase1 WHERE p_name1 = "shirt" AND p_date = "2023-04-21" AND store1 = "ORay"'
cur.execute(q)
mydb.commit()



#UPDATE THE MANUFACTURE DETAILS OF ALL THE RED COLORED TOYS WHICH ARE PURCHASED BY THE "MyKids" STORE
q1='UPDATE manufacture SET purchase_id1 = "MyKids" WHERE color1 = "red" AND manufacture_id1 IN (SELECT manufacture_id1 FROM goods1 WHERE goods_id1 IN (SELECT goods_id1 FROM sale1 WHERE store = "ORay")'
cur.execute(q1)
mydb.commit()




#DISPLAY ALL THE "WOODEN_CHAIR" ITEMS THAT WERE MANUFACTURED BEFORE THE 1ST MAY 2023
q3='SELECT * FROM  goods1 JOIN manufacture1 ON goods1.manufacture_id1 = manufacture1.manufacture_id1 WHERE product_name1 = "wooden chair" AND manufacture_date1 = "2023-05-01"'
cur.execute(q3)
rows=cur.fetchall()
for i in rows:
    print(i)
mydb.commit()



#DISPLAY THE PROFIT_MARGIN AMOUNT OF THE "WOODEN_TABLE" THAT WAS SOLD BY THE "MyCare" STORE ,MANUFACTURED BY THE "SS_Export" COMPANY
q4='SELECT sale1.profit_margin FROM sale1 JOIN goods1 ON sale1.goods_id1 = goods1.goods_id1 JOIN manufacture1 ON goods1.manufacture_id1 = manufacture1.manufacture_id1 JOIN purchase ON goods1.purchase_id1 = purchase1.purchase_id1 WHERE prouduct_name = "wooden table" AND store = "MyCare",company = "SS Export"'
cur.execute(q4)
row = cur.fetchone()
print(row[0])
mydb.commit()