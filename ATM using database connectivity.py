#Atm using OOPs 
import mysql.connector
class bank:
    def __init__(self):
        self.conn=mysql.connector.connect(host='localhost',user='root',password='abc@123',database='student')
        self.cur=self.conn.cursor()


    def chebal(self):
        accno=int(input('Enter your accountnumber:'))
        epin=int(input('Enter your pin:'))
        query='select *from bank where accountnumber=%s and pid=%s'
        values=(accno,epin)
        self.cur.execute(query,values)
        if self.cur.fetchone():
            print('Successfull')
            query_balance='select *from bank where accountnumber= %s'
            values=(accno,)
            self.cur.execute(query_balance,values)
            balance=self.cur.fetchone()[2]
            print('your balance is:',balance)
        else:
            print('Invallid pin or account number')
        
    



    def depositamt(self):
        enterpid=int(input('Enter your pin:'))
        enteraccountno=int(input('enter enteraccountno:'))
        query='select *from bank where pid=%s and accountnumber=%s'
        values=(enterpid,enteraccountno)
        self.cur.execute(query,values)
        data=self.cur.fetchone()
        if data:
            deposit_amt=int(input('Enter amount you want to deposit:'))
            if deposit_amt>0:
                nbalance=data[2]+deposit_amt
                query='update bank set balance=%s where pid=%s and accountnumber=%s'
                values=(nbalance,enterpid,enteraccountno)
                self.cur.execute(query,values)
                print('record updated successfully')
                choice=input('you want to check balance amount yes /no:')
                if choice=='yes':
                    print('your current balance is:',nbalance,'\n')
                else:
                    print('Thank you \n')
            else:
                print('you dont have enough funds')
        else:
            print('Invallid pin or account number')                                        
        self.conn.commit()
        



    def withdrawamt(self):
        enterpid=int(input('Enter your pin:'))
        enteraccountno=int(input('enter enteraccountno:'))
        query='select *from bank where pid=%s and accountnumber=%s '
        values=(enterpid,enteraccountno)
        self.cur.execute(query,values)
        data=self.cur.fetchone()
        if data:
            withdrawamt=int(input('Enter withdraw amount:'))
            if withdrawamt<=data[2]:
                nbal=data[2]-withdrawamt
                query='update bank set balance=%s where pid=%s and accountnumber=%s '
                values=(nbal,enterpid,enteraccountno)
                self.cur.execute(query,values)
                choice=input('you want to check balance amount yes /no:')
                if choice=='yes':
                    print('your new balance is:',nbal)
                else:
                    print('Thank you \n')
                
                self.conn.commit()
            else:
                print('you dont have enough amount')
        else:
            print('Invallid pin or account number')
        




    def cpin(self):
        enteroldpin=int(input('Enter old pin'))
        query='select *from bank where pid=%s'
        values=(enteroldpin,)
        self.cur.execute(query,values)
        data=self.cur.fetchone()
        if data:
            if data[0]==enteroldpin:
                print(' Id match')
                enternewpin=int(input('Enter new pin'))
                query='update bank set pid=%s where pid=%s'
                values=(enternewpin,enteroldpin)
                self.cur.execute(query,values)
                print('pin set successfully',enternewpin)
            else:
                print('Id not match')
        else:
            print('Invallid pin or account number')
        self.conn.commit()
        
    def conn_close(self):
        self.cur.close()
        self.conn.close()

a=bank()
while True:
    print('*****************WELCOME TO SBI ATM*******************')
    print('1.Check Balance')
    print('2.Debit(Withdraw)')
    print('3.Credit(Deposit)')
    print('4.Change Pin')
    print('5.Exit')
    choice=int(input('Enter your choice:'))      

    if choice==1:
        a.chebal()
    elif choice==2:
        a.depositamt()
    elif choice==3:
        a.withdrawamt()
    elif choice==4:
        a.cpin()
    elif choice==5:
        print('Exit')
        a.conn_close()
        break        
    else:
        print('Wrong Choice')
