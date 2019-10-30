import pymysql.cursors
class DBB:
    def __init__(self):
        self.conn=pymysql.connect(host='localhost',user='root',password='root',db='dbbank')
        self.cursor=self.conn.cursor()
    
    def accno(self):
        qry="select ifnull(max(accno),0)max from tbuser";
        self.cursor.execute(qry)
        row=self.cursor.fetchone()
        self.conn.commit()
        self.conn.close()
        #print(type(row[0]))
        print(row[0]+1)
        return row[0]+1
    
    def transid(self):  
        qry="select ifnull(max(transid),0)max from tbtransaction";
        self.cursor.execute(qry)
        row=self.cursor.fetchone()
        self.conn.commit()
        self.conn.close()
        return row[0]+1
    
    def insert(self,c):
        self.cursor.execute(c)
        self.conn.commit()
        self.conn.close()
    
    def execute(self,qry):
        self.cursor.execute(qry)
        row=self.cursor.fetchone()
        self.conn.commit()
        self.conn.close()
        return row,self.cursor.rowcount
        