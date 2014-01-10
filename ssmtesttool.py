#coding=utf-8
from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
#from PyQt4 import QtCore
#import ui_10_1,ui_10_2,ui_10_3  
import ssmtestui
import sys  
import datarule 
import os
import pywinauto

try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

  
class TestDialog(QMainWindow,QDialog):
    def __init__(self,parent=None):  
        super(TestDialog,self).__init__(parent) 
        reload(sys)
        sys.setdefaultencoding('utf-8')
        self.startid = 0
        self.datanum = 200

        self.mainUi=ssmtestui.Ui_MainWindow()
        self.mainUi.setupUi(self) 
        self.db = datarule.datarule()
        self.casecount = self.db.casecount()
        self.loadtable()
        self.mainUi.predatabu.clicked.connect(self.predata)
        self.mainUi.prenextdatabu.clicked.connect(self.prenextdata)
        self.mainUi.prepredatabu.clicked.connect(self.prepredata)
        self.mainUi.initdatabu.clicked.connect(self.initdata)
        self.mainUi.selectdatabu.clicked.connect(self.selectdata)
#            self.pageid = 0
#            self.query = False#是否点击查询按钮
#            self.queryid = 0
#            self.mainUi=myrssmain.Ui_MainWindow()
#            self.mainUi.setupUi(self) 
#            self.db = model.myrss()
#            self.themecount = self.db.selectthemecount()[0]-1
#            #初始化时间空间数据
#            self.initaddtime = self.db.selectinittime()
#            self.starttime = datetime.datetime.strptime(self.initaddtime[0][:10],'%Y-%m-%d')
#            self.endtime = datetime.datetime.strptime(self.initaddtime[1][:10],'%Y-%m-%d')
#    #        print type(self.starttime)
#            self.mainUi.starttime.setDate(self.starttime)
#            self.mainUi.endtime.setDate(self.endtime)
#            #加载数据
#            self.loadtable()
#            #界面操作
#            self.mainUi.prepagebut.clicked.connect(self.prepage)
#            self.mainUi.nextpagebut.clicked.connect(self.nextpage)
#            self.mainUi.startpagebut.clicked.connect(self.startpage)
#            self.mainUi.endpagebut.clicked.connect(self.endpage)
#            self.mainUi.clearbut.clicked.connect(self.resetcont)
#            self.mainUi.selectbut.clicked.connect(self.querycont)
#    #        print self.mainUi.parttitle.text() is ''
#            
    
    def loadtable(self):
        db = self.db
        self.alldata =  db.uidata(self.startid,self.datanum)
#        print db.uidata(0,1)[0][0]
        for i in xrange(len(self.alldata)):

            for x in xrange(len(self.alldata[i])):
                        
                #解决中文乱码问题，待学习具体原因
                item = u'%s'%self.alldata[i][x]
                newItem = QTableWidgetItem(item) 
                self.mainUi.tableWidget.setItem(i, x, newItem)
        if self.casecount>2:
            self.mainUi.nextcasetext.setText(u'%s'%db.uidata(self.startid+1,1)[0][0])
        if self.casecount>1:
            self.mainUi.casetext.setText(u'%s'%db.uidata(self.startid,1)[0][0])

    def predata(self):
        #当前用例
        db = self.db
        casename = self.mainUi.casetext.text()
        db.insertdata(str(casename))
        self.Clickdemotest()
#        self.mainUi.precasetext.setText(u'%s'%db.uidata(self.startid,1)[0][0])
#        self.mainUi.casetext.setText(u'%s'%db.uidata(self.startid+1,1)[0][0])
#        self.mainUi.nextcasetext.setText(u'%s'%db.uidata(self.startid+2,1)[0][0])
#        self.startid += 1

    def prenextdata(self):
        #下一个用例
        db = self.db
        casename = self.mainUi.nextcasetext.text()
        db.insertdata(str(casename))
#        self.Clickdemotest()
        if self.startid + 2 >= self.casecount:
            self.mainUi.nextcasetext.setText('no next case')
            self.mainUi.precasetext.setText(u'%s'%db.uidata(self.startid,1)[0][0])
            self.mainUi.casetext.setText(u'%s'%db.uidata(self.startid+1,1)[0][0])
#            self.mainUi.nextcasetext.setText(u'%s'%db.uidata(self.startid+2,1)[0][0])
            
        else:
            self.mainUi.precasetext.setText(u'%s'%db.uidata(self.startid,1)[0][0])
            self.mainUi.casetext.setText(u'%s'%db.uidata(self.startid+1,1)[0][0])
            self.mainUi.nextcasetext.setText(u'%s'%db.uidata(self.startid+2,1)[0][0])
            self.startid += 1
            self.Clickdemotest()
    
    def prepredata(self):
        #上一个用例
        db = self.db
        casename = self.mainUi.nextcasetext.text()
        db.insertdata(str(casename))
#        self.Clickdemotest()
        if self.startid <=1:
            self.mainUi.precasetext.setText('no last case') 
            self.mainUi.casetext.setText(u'%s'%db.uidata(self.startid-1,1)[0][0])
            self.mainUi.nextcasetext.setText(u'%s'%db.uidata(self.startid,1)[0][0])

        else:

            self.mainUi.precasetext.setText(u'%s'%db.uidata(self.startid-2,1)[0][0])
            self.mainUi.casetext.setText(u'%s'%db.uidata(self.startid-1,1)[0][0])
            self.mainUi.nextcasetext.setText(u'%s'%db.uidata(self.startid,1)[0][0])
            self.startid -= 1
            self.Clickdemotest()


    def initdata(self):
        #bug1 执行数据后，再初始化数据；部分数据界面不显示
        self.startid = 0
        db = self.db
        db.initdata()
        self.casecount = db.casecount()
        self.mainUi.tableWidget.clearContents()
        self.loadtable()
        self.mainUi.precasetext.setText('no next case')
        
        
    def selectdata(self):

        currentrow = self.mainUi.tableWidget.selectedItems()
#        print currentrow
        if currentrow==[]:
            self.mainUi.selectcasetext.setText('no select case')
            return False
        else:
            db = self.db
#            print currentrow[0].text()
            insertdata1 =  db.insertdata(str(currentrow[0].text()))
            self.Clickdemotest()
            self.mainUi.selectcasetext.setText('success update case data')
            return True
    
    
    def Clickdemotest(self):
        #调用demo工具的上传
        try:
            app = pywinauto.application.Application()
            app[ur"EMR_社保监控信息上传接口测试"].TypeKeys('{ENTER}')
        except  Exception,msg:
            print msg
        

    

        
        



if __name__ == "__main__":          
    app=QApplication(sys.argv)  
    myapp=TestDialog()  
    myapp.show()  
    sys.exit(app.exec_())

