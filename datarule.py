#coding=utf-8
import pyodbc
import sqlite3
import time
iddb1 = sqlite3.connect("db/ssm.db")#,check_same_thread = False)
iddb1.text_factory = str
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.29.202;DATABASE=ebm_ssm;UID=sa;PWD=ebm123')

class datarule(object):
    """处理数据"""   
    def __init__(self):
        self.filename = 'ssmtest.txt'
    
    def initdata(self):
        """初始化测试数据"""
        filename = self.filename
        cu = iddb1.cursor()
        cu.execute('delete from ssmtestdata')
        iddb1.commit()
#        time.sleep(0.1)
        f= open(filename)
        line = f.readline()
        while line:
#            print line
            try:
                line = line.decode('gbk').encode('utf-8')
                line = line.replace('\n','')
            except  Exception,msg:
                print msg
            try:
                line = line.split('	')
            except  Exception,msg:
                print msg
            try:
                line = tuple(line)
#                print line
                cu.execute('insert into ssmtestdata values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',line)
#                iddb1.commit()
            except  Exception,msg:
                print msg

            line = f.readline()
        iddb1.commit()
        cu.close()
        f.close()

    def insertdata(self,casename):
        """插入数据到202的表中"""
        
        cu = iddb1.cursor()
#        cu.execute('select * from ssmtestdata where groupid =(select groupid from ssmtestdata where casename = ?)',(casename,))
        cu.execute('select * from ssmtestdata where groupid =(select groupid from ssmtestdata where casename = ?)',(casename,))

        datalist = cu.fetchall()
        cu.close()
        
        cursor = cnxn.cursor()
        #插入前清除无关数据
        for item in datalist:
            cursor.execute('delete from %s'%item[1])
        cnxn.commit()
        #插入测试数据
        for item1 in datalist:
            #sqlserver格式为gbk 转码数据
            item = []
            for i in item1:
                if isinstance(i,str):
                    i=i.decode('utf-8').encode('gbk')
                item.append(i)
            item = tuple(item)
            print item
            if item[1]=='ebm_y1':
                cursor.execute(('insert into %s values(?,?,?,?,?,?,?)'%item[1]),item[3:10])
            elif item[1]=='ebm_y2':
                cursor.execute(('insert into %s values(?,?,?,?,?,?,?,?,?,?,?,?)'%item[1]),item[3:15])
            elif item[1]=='ebm_y3':
                cursor.execute(('insert into %s values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'%item[1]),item[3:])
            elif item[1]=='ebm_y4':
                cursor.execute(('insert into %s values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'%item[1]),item[3:19])
            else:
                print 'data error'
        cnxn.commit()
        cursor.close()

    def uidata(self,startid,datanum):
        cu = iddb1.cursor()
        cu.execute('select casename from ssmtestdata where casename !=? limit ?,?',('',startid,datanum))
        uidatalist = cu.fetchall()
        cu.close()
        return uidatalist
    
    def casecount(self):
        cu = iddb1.cursor()
        cu.execute('select count(*) from ssmtestdata where casename !=""')
        uidatalist = cu.fetchone()[0]
        cu.close()
        return uidatalist#[0][0]

        
        
        

            
if __name__ == '__main__':
    d = datarule()
#    d.uidata(0,100)
    d.initdata()
    
        