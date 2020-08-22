import sqlite3
class myconnect:
      
      def __init__(self):
            self.con = sqlite3.connect("emp.db")
            self.con.execute(''' create table if not exists emp(
                              id integer primary  key AUTOINCREMENT,
                              name text,
                              email text,
                              mobile_no text,
                              type text,
                              experience integer,
                              salary text
                        ) ''')
            #5      
                  
      def savetodb(self,ename,eemail,emob,etype,eexp,esalary):
            #6

      def display(self):
            #7
      
