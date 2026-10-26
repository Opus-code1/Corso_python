import mysql.connector as msc

def connect(h="localhost",u="root",p="", db=None):
    return msc.connect(host=h,user=u,password=p,database=db,)
