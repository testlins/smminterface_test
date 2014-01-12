#coding=gbk

import pyodbc
import threading
import random
import time

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.29.202;DATABASE=ebm_ssm;UID=sa;PWD=ebm123')

class ssmloadtest(object):
    """预置压力测试数据"""
    def __init__(self,ebm_y3=10000,enm_y4=448):
        self.ebm_y3 =  ebm_y3
        self.enm_y4 = enm_y4
        self.icd10 = ['','Z60.951','C30.003','V09.251','Q75.801','H49.153','B97.151','A18.819+','L27.002','K22.401']
        self.icd9 = ['','01.25004','02.2 005','02.34001','03.1 003','03.97001','04.07005','06.01001','05.29002','07.12002']
        self.deplist = ['1101','1108','1204','1207','1401','15','16']
#        self.intime = ['20130101','20130102','20130103','20130104','20130105']
#        self.outtime = ['','20130201','20130202','20130203','20130204','20130205']
#        self.dotime = ['20130101111213','20130102111213','20130103111213','20130104111213','20130105111213']
        self.startid = 100
        

    def preebm_y3(self):
        #预置就诊头表
        ebm_y3num = self.ebm_y3    
        icd10 = self.icd10
        idc9 = self.icd9
        deplist = self.deplist
#        intime = self.intime
#        outtime = self.outtime
#        dotime = self.dotime
        cursor = cnxn.cursor()
        cursor.execute('delete from ebm_y3')
        cursor.execute('delete from ebm_y4')
        cnxn.commit()
        for i in xrange(ebm_y3num):
            timetuple = self.randomtime(0)
            ebm_y3list = [i,'15010401','loadtest%s'%i,'压力测试%s'%i,random.choice(['',random.randint(1,999)]),random.randint(1,2),timetuple[2],random.choice(deplist),random.randint(1000,10000),random.choice(icd10),random.choice(icd10),random.choice(icd10),random.choice(icd10),timetuple[0],timetuple[1],'',random.choice(idc9)]
#            print ebm_y3list
            if i%10 == 0:
            #预置出院状态
#                ebm_y3list[0] = i
#                ebm_y3list[2] += i
#                ebm_y3list[3] += i 
                ebm_y3list[-2] = 30
#                ebm_y3list[-3] = random.choice(outtime[1:])
                ebm_y3list[-6] = random.choice(icd10[1:])
            elif i%10 == 1:
            #预置入院状态
                ebm_y3list[-2] = 10
                ebm_y3list[-3] = ''
            else:
                ebm_y3list[-2] = 20
                ebm_y3list[-3] = random.choice(['',ebm_y3list[-3]])
            ebm_y3tuple = tuple(ebm_y3list)
            cursor.execute('insert into ebm_y3 values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',ebm_y3tuple)
        cnxn.commit()
        cursor.close()

    def loady3(self,startid):
        #分次加载
        cursor = cnxn.cursor()
#        cursor.execute('select Y0006 from ebm_y3 group by id desc limit ?,100',(startid,))
        dosql = 'select  top  100 Y0006,Y0017,Y0018 from  (select  top  %d  Y0006,Y0017,Y0018,id  from  ebm_y3  order  by  id )  T1 order  by  id  desc  '%startid
        cursor.execute(dosql)
        datalist = cursor.fetchall()
        cursor.close()
        return datalist

    def preebm_y4(self):
        ebm_y3num = self.ebm_y3 
        Y0006list = self.loady3(self.startid)
#        print Y0006list
        cursor = cnxn.cursor()
#        cursor.execute('delete from ebm_y4')
#        cnxn.commit()
        while len(Y0006list)>0:
            print Y0006list
            for i in Y0006list:
#            ebm_y4list
                if i[2]=='':
                    i[2] = '20140110'
                for x in xrange(448):
                    id = i[0]+'id'+str(x)
                    Y0006 = i[0]
                    dotime = self.randomtime(1,i[1],i[2])
                    ebm_y4list =[
            [id,'15010401',Y0006,x,x,'检查%s'%x,dotime,random.randint(1000,10000),random.randint(1,20),random.randint(1,1000),'','','','','','3'],
            [id,'15010401',Y0006,x,x,'其他%s'%x,dotime,random.randint(1000,10000),random.randint(1,20),random.randint(1,1000),'','','','','','4'],
            [id,'15010401',Y0006,x,x,'治疗%s'%x,dotime,random.randint(1000,10000),random.randint(1,20),random.randint(1,1000),'','','','','','2'],
            [id,'15010401',Y0006,x,x,'药品%s'%x,dotime,random.randint(1000,10000),random.randint(1,20),random.randint(1,1000),random.randint(1,70) ,random.randint(1,40),random.randint(1,2),random.randint(1,21),random.randint(1,9999),'1']
            ]
                    ebm_y4tuple = tuple(ebm_y4list[random.randint(0,3)])
                    try:
                        cursor.execute('insert into ebm_y4 values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',ebm_y4tuple)
                    except Exception,msg:
                        print msg
                cnxn.commit()
#            cursor.close()
            self.startid += 100
            Y0006list = self.loady3(self.startid)
        cursor.close()

    


        
    def randomtime(self,flag=1,starttime = '20120101',endtime= '20140110'):
        #计算随机时间
        starttime +='000001'
        endtime += '235959'
        starttime  = time.mktime(time.strptime(starttime,'%Y%m%d%H%M%S'))
        endtime = time.mktime(time.strptime(endtime,'%Y%m%d%H%M%S'))
        if flag==0:
            newstarttime = random.randint(starttime,endtime)
            newendtime = random.randint(newstarttime,endtime)
            dotime = random.randint(newstarttime,newendtime)
            return (time.strftime('%Y%m%d',time.localtime(newstarttime)),
                    time.strftime('%Y%m%d',time.localtime(newendtime)),
                    time.strftime('%Y%m%d%H%M%S',time.localtime(dotime)))
        elif flag==1:
            dotime = random.randint(starttime,endtime)
            return time.strftime('%Y%m%d%H%M%S',time.localtime(dotime))


class MyThread(threading.Thread):  
    def __init__(self,Y0006):  
        threading.Thread.__init__(self)  
        self.Y0006 = Y0006
        
        def run(self):
        
            try:
                site = self.site[0]
            except Exception,msg:
                print msg
                return


        
        
if __name__ == '__main__':
    d = ssmloadtest()
    d.preebm_y4()
#    print d.randomtime()
#    print d.casecount()

            
#['','15010401',i[0],'','','检查',self.randomtime(1,i[1],i[2]),random.randint(1000,10000),random.randint(1,20),random.randint(1,1000),'','','','','','3']
#['','15010401',i[0],'','','其他',self.randomtime(1,i[1],i[2]),random.randint(1000,10000),random.randint(1,20),random.randint(1,1000),'','','','','','4']
#['','15010401',i[0],'','','治疗',self.randomtime(1,i[1],i[2]),random.randint(1000,10000),random.randint(1,20),random.randint(1,1000),'','','','','','2']
#['','15010401',i[0],'','','药品',self.randomtime(1,i[1],i[2]),random.randint(1000,10000),random.randint(1,20),random.randint(1,1000),random.randint(1,70) ,random.randint(1,40),random.randint(1,2),random.randint(1,21),random.randint(1,9999),'1']
#