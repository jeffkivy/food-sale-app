from tkinter import*
from pymongo import MongoClient
import time
global time
global day


from tkinter import ttk
client= MongoClient()
db1=client.stock
db2=client.raw
db3=client.daily_raw_material
db4=client.daily_stock_out
db4=client.daily_stock_back
#db3.daily_raw_material.remove()

db5=client.daily_stock_back
db6=client.sold_stock
db5.daily_stock_back.remove()
db7=client.expence
db8=client.wage
#db8.wage.remove()

day =time.strftime("%a, %d %b %Y")
time=time.strftime("%H:%M:%S")


class login():
    def __init__(self, master):
        self.master=master

        self.frame=Frame(self.master, bg='tan')
        self.frame.grid(row=0, column=0)

        self.frame1 = Frame(self.frame, bg='tan')
        self.frame1.grid(row=0, column=0,padx=5, pady=5)

        self.label = Label(self.frame1, bg='tan', text='hardware login',)
        self.label.grid(row=0, column=0,padx=5, pady=5)

        self.frame2 = Frame(self.frame, bg='tan')
        self.frame2.grid(row=1, column=0,padx=5, pady=5)

        self.password = Label(self.frame2, bg='tan', text='password')
        self.password.grid(row=0, column=0)

        self.password_e = Entry(self.frame2, bg='white', text='password', relief='sunken', show='*')
        self.password_e.grid(row=0, column=1,padx=5, pady=5)

        self.frame3 = Frame(self.frame, bg='tan')
        self.frame3.grid(row=2, column=0,padx=5, pady=5)

        self.button = Button(self.frame3, bg='tan', text='login', command=self.login_main)
        self.button.grid(row=0, columnspan=2,padx=5, pady=5)

        self.master.rowconfigure(0, weight=1,)
        self.master.columnconfigure(0, weight=1)

        self.frame.rowconfigure(0, weight=1, )
        self.frame.rowconfigure(1, weight=1, )
        self.frame.rowconfigure(2, weight=1, )
        self.frame.columnconfigure(0, weight=1)
    def login_main(self):
        if self.password_e.get()=='':
            root.destroy()
            class main_page():
                def __init__(self, master):
                    self.master = master

                    self.frame = Frame(self.master)
                    self.frame.grid(sticky='nsew')

                    self.frame1 = Frame(self.frame, bg='tan', relief='sunken', border=3)
                    self.frame1.grid(sticky='nsew')
                    self.today_home = Label(self.frame1, bg='gold',text=day, relief='ridge', border=1)
                    self.today_home.grid(row=0, column=0)
                    self.finance = Label(self.frame1,text='Finance', bg='gold', relief='ridge', border=1)
                    self.finance.grid(row=0, column=1)
                    self.stock = Button(self.frame1,text='Stock management', bg='dark slate gray',command=self.stock, fg='snow',relief='sunken', border=3, font = ('Helvetica', 10, 'bold'))
                    self.stock.grid(row=0, column=2, padx=3, pady=3)
                    self.reports = Label(self.frame1, text='Reports',bg='gold', relief='ridge', border=1)
                    self.reports.grid(row=0, column=3)

                    self.frame2 = Frame(self.frame, bg='tan', relief='raised', border=3)
                    self.frame2.grid(row=1, column=0,padx=4,pady=4, sticky='nsew')

                    self.frame2a = Frame(self.frame2, bg='snow',)
                    self.frame2a.grid(row=0, column=0, padx=2, pady=2,sticky='nsew')

                    self.frame2al = Label(self.frame2a, bg='tan',text='SCIENTIFIC CALCULATOR' )
                    self.frame2al.grid(row=0, column=0, padx=2, pady=2, sticky='nsew')

                    self.frame2ac = Frame(self.frame2a, bg='tan', )
                    self.frame2ac.grid(row=1, column=0, padx=2, pady=2, sticky='nsew')

                    self.frame2acs = Frame(self.frame2ac, bg='white', )
                    self.frame2acs.grid(row=0, column=0, padx=2, pady=2, sticky='nsew')

                    self.frame2acs.rowconfigure(0, weight=1)
                    self.frame2acs.columnconfigure(0, weight=1)

                    self.frame2acn = Frame(self.frame2ac, bg='white', )
                    self.frame2acn.grid(row=1, column=0, padx=2, pady=2, sticky='nsew')

                    self.frame2acn.rowconfigure(0, weight=1)
                    self.frame2acn.columnconfigure(0, weight=1)


                    num1 = StringVar()
                    txtDisplay = Entry(self.frame2acs, textvariable=num1, relief=RIDGE, bd=10, font=40, bg='snow')
                    txtDisplay.grid(row=0, column=0, sticky='nsew')
                    txtDisplay.focus()

                    self.frame2acs.rowconfigure(0, weight=1)
                    self.frame2acs.columnconfigure(0, weight=1)

                    st=['1','4','7','0']
                    col=0
                    for three in st:
                        col+=1
                        Button(self.frame2acn, text=three, width=7, height=3, bg='LightBlue', fg='red',
                               command=lambda: update_entry(st)).grid(row=col, column=0, sticky='nsew')

                    st = ['2', '5', '8','clear']
                    col = 0
                    for three in st:
                        col += 1
                        Button(self.frame2acn, text=three, width=7, height=3, bg='gray', fg='white',
                               command=lambda: update_entry(st)).grid(row=col, column=1, sticky='nsew')

                    st = ['3', '6', '9', '=']
                    col = 0
                    for three in st:
                        col += 1
                        Button(self.frame2acn, text=three, width=7, height=3, bg='powder blue', fg='red',
                               command=lambda: update_entry(st)).grid(row=col, column=2, sticky='nsew')

                    st = [ '+', '-','*','/']
                    col = 0
                    for three in st:
                        col += 1
                        Button(self.frame2acn, text=three, width=3, height=4, bg='powder blue', fg='red',
                               command=lambda: update_entry(st)).grid(row=col, column=3, sticky='nsew')


                    self.frame2b = Frame(self.frame2, bg='white', )
                    self.frame2b.grid(row=0, column=1, padx=2, pady=2,sticky='nsew')

                    self.frame2ba_juu = Frame(self.frame2b, bg='tan', relief='ridge', border=4)
                    self.frame2ba_juu.grid(row=0, column=0, padx=2, pady=2, sticky='nsew')

                    ###
                    self.frame2ba_juu1 = Frame(self.frame2ba_juu, bg='white',)
                    self.frame2ba_juu1.grid(row=0, column=0, padx=2, pady=2, sticky='nsew')

                    self.frame2ba_juu1_label = Label(self.frame2ba_juu1, bg='white',text='daily raw materials', font = ('Helvetica', 10, 'bold'), )
                    self.frame2ba_juu1_label.grid(row=0, column=0, padx=2, pady=2, sticky='nsew')

                    ####

                    ####
                    self.frame2ba_juu2 = Frame(self.frame2ba_juu, bg='white', relief='ridge', border=4)
                    self.frame2ba_juu2.grid(row=1, column=0, padx=2, pady=2, sticky='nsew')

                    self.frame2ba_juu2a = Frame(self.frame2ba_juu2, bg='tan',)
                    self.frame2ba_juu2a.grid(row=0, column=0, padx=2, pady=2, sticky='nsew')

                    self.frame2ba_juu2b = Frame(self.frame2ba_juu2, bg='tan', )
                    self.frame2ba_juu2b.grid(row=0, column=1, padx=2, pady=2, sticky='nsew')

                    self.frame2ba_juu2b_name = Label(self.frame2ba_juu2b, text ='Name', font = ('Times', 10, 'bold'))
                    self.frame2ba_juu2b_name.grid(row=0, column=0, padx=2, pady=2, sticky='nsew')

                    self.select_raw_name ="-------ooo-"

                    self.select_raw_label()



                    self.frame2ba_juu2b_name = Label(self.frame2ba_juu2b, text='Quantity' ,
                                                     font=('Times', 10, 'bold'))
                    self.frame2ba_juu2b_name.grid(row=1, column=0, padx=2, pady=2, sticky='nsew')



                    self.frame2ba_juu2b_price = Label(self.frame2ba_juu2b, text='Price',
                                                     font=('Times', 10, 'bold'))
                    self.frame2ba_juu2b_price.grid(row=2, column=0, padx=2, pady=2, sticky='nsew')



                    self.frame2ba_juu2b_b = Button(self.frame2ba_juu2b,text='save',
                                                     font=('Times', 10, 'bold'),command=self.selected_now_raw)
                    self.frame2ba_juu2b_b.grid(row=3, columnspan=1, padx=2, pady=2, sticky='nsew')



                    ####

                    self.frame2ba_juu.rowconfigure(0, weight=0)
                    self.frame2ba_juu.rowconfigure(1, weight=0)
                    self.frame2ba_juu.columnconfigure(0, weight=1)

                    self.frame2ba_juu2.rowconfigure(0, weight=1)
                    self.frame2ba_juu2.columnconfigure(0, weight=1)
                    self.frame2ba_juu2.columnconfigure(1, weight=1)

                    self.frame2ba_juu2a.rowconfigure(0, weight=1)
                    self.frame2ba_juu2a.columnconfigure(0, weight=1)

                    self.frame2ba_juu2b.rowconfigure(0, weight=1)
                    self.frame2ba_juu2b.columnconfigure(0, weight=1)


                    self.frame2ba_juu1.rowconfigure(0, weight=1)
                    self.frame2ba_juu1.columnconfigure(0, weight=1)

                    self.frame2ba_juu2.rowconfigure(0, weight=1)
                    self.frame2ba_juu2.rowconfigure(1, weight=1)
                    self.frame2ba_juu2.rowconfigure(2, weight=1)
                    self.frame2ba_juu2.rowconfigure(3, weight=1)
                    self.frame2ba_juu2.columnconfigure(0, weight=1)
                    self.frame2ba_juu2.columnconfigure(1, weight=1)




                    self.frame2ba = Frame(self.frame2b, bg='tan',relief='raised', border=4 )
                    self.frame2ba.grid(row=1, column=0, padx=2, pady=2, sticky='nsew')


                    self.frame2ba1 = Frame(self.frame2ba, bg='white', )
                    self.frame2ba1.grid(row=0, column=0, padx=2, pady=2, sticky='nsew')

                    self.frame2bll = Label(self.frame2ba1, text='today\'s stock flow ',bg='white', )
                    self.frame2bll.grid(row=0, column=0, padx=2, pady=2, sticky='nsew')

                    self.frame2ba2 = Frame(self.frame2ba, bg='white', )
                    self.frame2ba2.grid(row=1, column=0, padx=2, pady=2, sticky='nsew')

                    self.sold_stock()


                    stock_display =[]
                    f = db1.stock.find()
                    for index, n in enumerate(f):
                        today_stock = n['stock name']
                        stock_display.append(today_stock)
                    self.r=0
                    for i in stock_display:
                        self.r += 1
                        self.mark = Label(self.frame2ba2, text=i, font=('Helvetica',10,'bold'), bg='white')
                        self.mark.grid(row=self.r, column=0)

                        self.imark = Label(self.frame2ba2,  text='------', font=('Helvetica',10,'bold'), bg='white', width=10)
                        self.imark.grid(row=self.r, column=5,padx=1,pady=1)

                    column=['stock out', 'stock back','quantity sold','cash in','compare to yesterday']
                    co=0
                    for c in column:
                        co+=1
                        self.i = Label(self.frame2ba2, text=c, font=('Helvetica',9,'bold'), bg='white')
                        self.i.grid(row=0, column=co)


                    self.check_buttons()



                    ####### second right frame, expenses and wages
                    self.main_expence_wage = Frame(self.frame2b, bg='tan',relief='sunken', bd=3)
                    self.main_expence_wage.grid(row=2, column=0, padx=2, pady=2, sticky='nsew')

                    self.main_expence = Frame(self.main_expence_wage, bg='tan', )
                    self.main_expence.grid(row=0, column=0, padx=2, pady=2, sticky='nsew')
                    self.main_expence_title = Frame(self.main_expence, bg='tan', )
                    self.main_expence_title.grid(row=0, column=0, padx=2, pady=2, sticky='nsew')

                    self.expence_entry()

                    self.main_expence_label = Label(self.main_expence_title, bg='tan',text='Expenses' ,font=('Helvetica',20,'bold'),width=15 )
                    self.main_expence_label.grid(row=0, column=0, padx=2, pady=2, sticky='nsew')

                    self.main_expence_tt = Label(self.main_expence, text='Title', font=('Times',9,'bold'))
                    self.main_expence_tt.grid(row=1, column=0, padx=2, pady=2, sticky='nsew')

                    self.main_expence_tt = Label(self.main_expence, text='Amount', font=('Times',9,'bold'),)
                    self.main_expence_tt.grid(row=3, column=0, padx=2, pady=2, sticky='nsew')

                    self.main_expence_ea = Entry(self.main_expence, )
                    self.main_expence_ea.grid(row=4, column=0, padx=2, pady=2, sticky='nsew')

                    self.main_expence_tt = Button(self.main_expence, text='saves', command=self.save_expence )
                    self.main_expence_tt.grid(row=5, column=0, padx=2, pady=2, sticky='nsew')

                    self.main_wage = Frame(self.main_expence_wage, bg='tan', )
                    self.main_wage.grid(row=0, column=1, padx=2, pady=2, sticky='nsew')

                    self.main_wage_title = Frame(self.main_wage, bg='tan', )
                    self.main_wage_title.grid(row=0, column=0, padx=2, pady=2, sticky='nsew')

                    self.main_wage_label = Label(self.main_wage_title, bg='tan', text='Wages',font=('Helvetica',20,'bold'),width=15)
                    self.main_wage_label.grid(row=0, column=0, padx=2, pady=2, sticky='nsew')

                    self.main_wage_tt = Label(self.main_wage, text='Name',font=('Times',9,'bold') )
                    self.main_wage_tt.grid(row=1, column=0, padx=2, pady=2, sticky='nsew')



                    self.main_wage_tt = Label(self.main_wage, text='Amount', font=('Times',9,'bold',))
                    self.main_wage_tt.grid(row=3, column=0, padx=2, pady=2, sticky='nsew')



                    self.wage_entry()

                    self.main_wage_tt = Button(self.main_wage, text='save', command=self.save_wage)
                    self.main_wage_tt.grid(row=5, column=0, padx=2, pady=2, sticky='nsew')

                    self.main_profit = Frame(self.frame2b, bg='white', relief='ridge', border=4 )
                    self.main_profit.grid(row=3, column=0, padx=2, pady=2, sticky='nsew')

                    self.display_profit = Frame(self.main_profit, bg='snow',relief='raised', bd=5 )
                    self.display_profit.grid(row=0, column=0, padx=2, pady=2, sticky='nsew')

                    self.display_profitl = Label(self.display_profit,text='closing day turn over', bg='white', font=('Times',12,))
                    self.display_profitl.grid(row=0, column=0, padx=2, pady=2, sticky='nsew')






                    self.total_expense = Frame(self.main_profit, bg='white',relief='raised', bd=5 )
                    self.total_expense.grid(row=0, column=1, padx=2, pady=2, sticky='nsew')

                    self.total_expensel = Label(self.total_expense,text='expense+wages+raw materials', bg='white', font=('Times',12,))
                    self.total_expensel.grid(row=0, column=0, padx=2, pady=2, sticky='nsew')



                    self.net_profit = Frame(self.main_profit, bg='white', relief='raised', bd=5)
                    self.net_profit.grid(row=0, column=2, padx=2, pady=2, sticky='nsew')

                    self.net_profitl = Label(self.net_profit, text='net profit',bg='white',font=('Times',12,) )
                    self.net_profitl.grid(row=0, column=0, padx=2, pady=2, sticky='nsew')

                    self.net_profitl = Label(self.net_profit, text='0.00', bg='white',font=('Times',10,) )
                    self.net_profitl.grid(row=1, column=0, padx=2, pady=2, sticky='nsew')



                    self.compare = Frame(self.main_profit, bg='white', relief='raised', bd=5)
                    self.compare.grid(row=0, column=3, padx=2, pady=2, sticky='nsew')

                    self.comparel = Label(self.compare, bg='white', text='gain(compared to yesterday)',font=('Times',12,))
                    self.comparel.grid(row=0, column=0, padx=2, pady=2, sticky='nsew')

                    self.comparel = Label(self.compare, bg='white', text='0.00',font=('Times',10,))
                    self.comparel.grid(row=1, column=0, padx=2, pady=2, sticky='nsew')

                    self.turn_over()

                    self.master.rowconfigure(0, weight=1, )
                    self.master.columnconfigure(0, weight=1)

                    self.frame.rowconfigure(0, weight=0, )
                    self.frame.rowconfigure(1, weight=1, )
                    self.frame.columnconfigure(0, weight=1)

                    self.frame1.rowconfigure(0, weight=1, )
                    self.frame1.columnconfigure(0, weight=1)
                    self.frame1.columnconfigure(1, weight=1)
                    self.frame1.columnconfigure(2, weight=1)
                    self.frame1.columnconfigure(3, weight=1)

                    self.frame2.rowconfigure(0, weight=1, )
                    self.frame2.columnconfigure(0, weight=1)
                    self.frame2.columnconfigure(1, weight=1)

                    self.frame2a.rowconfigure(0, weight=0, )
                    self.frame2a.rowconfigure(1, weight=1, )
                    self.frame2a.columnconfigure(0, weight=1)

                    self.frame2ac.rowconfigure(0, weight=1, )
                    self.frame2ac.rowconfigure(1, weight=1, )
                    self.frame2ac.rowconfigure(2, weight=1, )
                    self.frame2ac.rowconfigure(3, weight=1, )
                    self.frame2ac.rowconfigure(4, weight=1, )

                    self.frame2ac.columnconfigure(0, weight=1)
                    self.frame2ac.columnconfigure(1, weight=1)
                    self.frame2ac.columnconfigure(2, weight=1)
                    self.frame2ac.columnconfigure(3, weight=1)

                    self.frame2b.rowconfigure(0, weight=1, )
                    self.frame2b.rowconfigure(1, weight=1, )
                    self.frame2b.rowconfigure(2, weight=1, )
                    self.frame2b.columnconfigure(0, weight=1)

                    self.frame2ba.rowconfigure(0, weight=0, )
                    self.frame2ba.rowconfigure(1, weight=1, )
                    self.frame2ba.rowconfigure(2, weight=1, )
                    self.frame2ba.columnconfigure(0, weight=1)

                    self.frame2ba1.rowconfigure(0, weight=1, )
                    self.frame2ba1.columnconfigure(0, weight=1)

                    self.main_expence_wage.rowconfigure(0, weight=1, )
                    self.main_expence_wage.columnconfigure(0, weight=1)
                    self.main_expence_wage.columnconfigure(1, weight=1)


                    self.main_profit.rowconfigure(0, weight=1, )
                    self.main_profit.columnconfigure(0, weight=1)
                    self.main_profit.columnconfigure(1, weight=1)
                    self.main_profit.columnconfigure(2, weight=1)
                    self.main_profit.columnconfigure(3, weight=1)

                    self.samosa_nyama_out = Entry(self.frame2ba2, font=('Times', 8, 'bold'), fg='red',
                                                   )
                    self.samosa_nyama_out.grid(row=1, column=1, padx=3, pady=1, )


                    self.samosa_waru_out = Entry(self.frame2ba2, font=('Times', 8, 'bold'), fg='red')
                    self.samosa_waru_out.grid(row=2, column=1, padx=3, pady=1)

                    self.samosa_ndengu_out = Entry(self.frame2ba2, font=('Times', 8, 'bold'), fg='red')
                    self.samosa_ndengu_out.grid(row=3, column=1, padx=3, pady=1)

                    self.samosa_mayai_out = Entry(self.frame2ba2, font=('Times', 8, 'bold'), fg='red')
                    self.samosa_mayai_out.grid(row=4, column=1, padx=3, pady=1)

                    self.samosa_smoki_out = Entry(self.frame2ba2, font=('Times', 8, 'bold'), fg='red')
                    self.samosa_smoki_out.grid(row=5, column=1, padx=3, pady=1)

                    self.samosa_nyama_back = Entry(self.frame2ba2, font=('Times', 8, 'bold'), fg='red',
                                                  )
                    self.samosa_nyama_back.grid(row=1, column=1, padx=3, pady=1, )

                    self.samosa_waru_back = Entry(self.frame2ba2, font=('Times', 8, 'bold'), fg='red')
                    self.samosa_waru_back.grid(row=2, column=1, padx=3, pady=1)

                    self.samosa_ndengu_back = Entry(self.frame2ba2, font=('Times', 8, 'bold'), fg='red')
                    self.samosa_ndengu_back.grid(row=3, column=1, padx=3, pady=1)

                    self.samosa_mayai_back = Entry(self.frame2ba2, font=('Times', 8, 'bold'), fg='red')
                    self.samosa_mayai_back.grid(row=4, column=1, padx=3, pady=1)

                    self.samosa_smoki_back = Entry(self.frame2ba2, font=('Times', 8, 'bold'), fg='red')
                    self.samosa_smoki_back.grid(row=5, column=1, padx=3, pady=1)

                    self.drop_downn()

                    self.raw_entries()
                    #self.popup_raw()
                    self.tot=[]
                    self.check_nyama = ''
                    self.check_waru = ''
                    self.check_smoki=''
                    self.check_ndengu=''
                    self.check_mayai=''
                    self.stock_out_entry()



                    self.popup_raw()

                    self.stock_back_entry()



                def turn_over(self):
                    try:
                        x = sum(self.turn_over_list)
                    except:
                        x='0.00'
                    el=[]
                    f= db7.expence.find({'date' : day})
                    for index, g in enumerate(f):
                        d=int(g['amount'])
                        print(d)
                        el.append(d)
                    try:
                        e = sum(el)
                        print(e)
                    except:
                        e='0.00'
                    c = db8.wage.find({'date': day})
                    for index, f in enumerate(c):

                        w=int(f['amount'])
                        el.append(w)



                    f = db3.daily_raw_material.find({'date': day})
                    for index, g in enumerate(f):
                        r = int(g['price'])
                        print(r)
                        el.append(r)




                    self.display_profitl = Label(self.display_profit, text=x, bg='white', font=('Times',10,))
                    self.display_profitl.grid(row=1, column=0, padx=2, pady=2, sticky='nsew')

                    self.total_expensel = Label(self.total_expense, text=sum(el), bg='white', font=('Times', 10,))
                    self.total_expensel.grid(row=1, column=0, padx=2, pady=2, sticky='nsew')

                def wage_entry(self):
                    self.main_wage_e = Entry(self.main_wage, )
                    self.main_wage_e.grid(row=2, column=0, padx=2, pady=2, sticky='nsew')

                    self.main_wage_ea = Entry(self.main_wage, )
                    self.main_wage_ea.grid(row=4, column=0, padx=2, pady=2, sticky='nsew')





                    ###########
                def expence_entry(self):

                    self.main_expence_e = Entry(self.main_expence, )
                    self.main_expence_e.grid(row=2, column=0, padx=2, pady=2, sticky='nsew')


                    self.main_expence_ea = Entry(self.main_expence, )
                    self.main_expence_ea.grid(row=4, column=0, padx=2, pady=2, sticky='nsew')

                def save_wage(self):

                    if len(self.main_wage_e.get()) == 0 or len(self.main_wage_ea.get()) == 0:
                        print('empty ')
                    elif db8.wage.find({'date': day, 'title': self.main_wage_e.get()}).count() > 0:
                        print('ikooooo')

                    else:
                        wage = {'date': day, 'title': self.main_wage_e.get(),
                                   'amount': self.main_wage_ea.get()}
                        db8.wage.insert(wage)
                        self.wage_entry()
                        print('saved')
                        self.turn_over()
                        print('oooooooooooooppoooooooooooooooooppppppppppoooppppppppppppppppooooooooooopp')
                def save_expence(self):
                     if len(self.main_expence_e.get())==0 or len(self.main_expence_ea.get())==0:
                         print('empty ')

                     elif db7.expence.find({'date': day,'title': self.main_expence_e.get()}).count()>0:
                         print('ikooooo')


                     else:
                         expence = {'date': day, 'title': self.main_expence_e.get(),
                                       'amount': self.main_expence_ea.get()}
                         db7.expence.insert(expence)
                         self.expence_entry()
                         print('saved')
                         self.turn_over()

                def sold_stock(self):
                    ########################################################################
                    if db5.daily_stock_back.find({'date' : day}).count()==0:
                        self.imark = Label(self.frame2ba2, text='------', font=('Helvetica', 10, 'bold'), bg='white', width=10)

                        self.imark.grid(row=1, column=3)



                        self.imark = Label(self.frame2ba2,  text='------', font=('Helvetica',10,'bold'), bg='white', width=10)
                        self.imark.grid(row=1, column=4)
                    else:

                        g=db5.daily_stock_back.find({'date' : day})
                        for index, k in enumerate(g):
                            nyamab=int(k['samosa nyama'])
                            warub=int(k['samosa waru'])
                            ndengub=int(k['samosa ndengu'])
                            mayaib=int(k['mayai'])
                            smokib=int(k['smoki'])

                        q = db4.daily_stock_out.find({'date': day})
                        for index, a in enumerate(q):
                            nyama = int(a['samosa nyama'])
                            waru = int(a['samosa waru'])
                            ndengu = int(a['samosa ndengu'])
                            mayai = int(a['mayai'])
                            smoki = int(a['smoki'])




                        nyama_sold=''
                        waru_sold=''
                        ndengu_sold=''
                        mayai_sold=''
                        smoki_sold=''
                        print('')

                        u = db1.stock.find({'stock name': 'samosa nyama'})
                        for index, k in enumerate(u):
                            price = int(k['price'])
                        self.nyama_price = price * nyama_sold

                        v = db1.stock.find({'stock name': 'samosa waru'})
                        for index, e in enumerate(v):
                            pricew = int(e['price'])
                            self.waru_price=int(pricew * waru_sold)
                        print(waru_sold)



                        u = db1.stock.find({'stock name': 'samosa ndengu'})
                        for index, k in enumerate(u):
                            price = int(k['price'])
                        self.ndengu_price =price * ndengu_sold


                        u = db1.stock.find({'stock name': 'mayai'})
                        for index, k in enumerate(u):
                            price = int(k['price'])
                        self.mayai_price = price * mayai_sold

                        u = db1.stock.find({'stock name': 'smoki'})
                        for index, k in enumerate(u):
                            price = int(k['price'])
                        self.smoki_price = price * smoki_sold

                        self.turn_over_list=[self.nyama_price, self.waru_price, self.ndengu_price,self.mayai_price,self.smoki_price]


                        self.imark = Label(self.frame2ba2, text=nyama_sold, font=('Helvetica', 10, 'bold'),
                                               bg='white',
                                               width=10)
                        self.imark.grid(row=1, column=3)

                        self.imark = Label(self.frame2ba2, text=waru_sold, font=('Helvetica', 10, 'bold'),
                                           bg='white',
                                           width=10)
                        self.imark.grid(row=2, column=3)

                        self.imark = Label(self.frame2ba2, text=ndengu_sold, font=('Helvetica', 10, 'bold'),
                                           bg='white',
                                           width=10)
                        self.imark.grid(row=3, column=3)

                        self.imark = Label(self.frame2ba2, text=mayai_sold, font=('Helvetica', 10, 'bold'),
                                           bg='white',
                                           width=10)
                        self.imark.grid(row=4, column=3)

                        self.imark = Label(self.frame2ba2, text=smoki_sold, font=('Helvetica', 10, 'bold'),
                                           bg='white',
                                           width=10)
                        self.imark.grid(row=5, column=3)

                        ######**************************#############*************************************##############

                        self.imark = Label(self.frame2ba2, text=self.nyama_price, font=('Helvetica', 10, 'bold'),
                                               bg='white',
                                               width=10)
                        self.imark.grid(row=1, column=4)

                        self.imark = Label(self.frame2ba2, text=self.waru_price, font=('Helvetica', 10, 'bold'),
                                           bg='white',
                                           width=10)
                        self.imark.grid(row=2, column=4)

                        self.imark = Label(self.frame2ba2, text=self.ndengu_price, font=('Helvetica', 10, 'bold'),
                                           bg='white',
                                           width=10)
                        self.imark.grid(row=3, column=4)

                        self.imark = Label(self.frame2ba2, text=self.mayai_price, font=('Helvetica', 10, 'bold'),
                                           bg='white',
                                           width=10)
                        self.imark.grid(row=4, column=4)

                        self.imark = Label(self.frame2ba2, text=self.smoki_price, font=('Helvetica', 10, 'bold'),
                                           bg='white',
                                           width=10)
                        self.imark.grid(row=5, column=4)


                def check_buttons(self):
                    check_sam = ''
                    g = db4.daily_stock_out.find({'date': day})
                    for index, h in enumerate(g):
                        check_sam = h['samosa nyama']
                    if len(check_sam) == 0:
                        self.i = Button(self.frame2ba2, text='save1', font=('Helvetica', 9, 'bold'), bg='white',
                                        command=self.save_stock_out)
                        self.i.grid(row=self.r + 1, column=1, padx=3, pady=3, )

                        self.i = Button(self.frame2ba2, text='save2', font=('Helvetica', 9, 'bold'), bg='white',
                                        command=self.save_stock_back
                                        )
                        self.i.grid(row=self.r + 1, column=2, padx=3, pady=3)
                    else:
                        self.i = Label(self.frame2ba2, text='save1', font=('Helvetica', 9, 'bold'), bg='white',
                                       )
                        self.i.grid(row=self.r + 1, column=1, padx=3, pady=3, )

                        self.i = Button(self.frame2ba2, text='save2', font=('Helvetica', 9, 'bold'), bg='white',
                                        command=self.save_stock_back
                                        )
                        self.i.grid(row=self.r + 1, column=2, padx=3, pady=3)

                def stock_back_entry(self):

                    self.check_nyamab  =self.samosa_nyama_back.get()
                    self.check_warub=self.samosa_waru_back.get()
                    self.check_ndengub=self.samosa_ndengu_back.get()
                    self.check_mayaib = self.samosa_mayai_back.get()
                    self.check_mayaib = self.samosa_smoki_back.get()

                    d=db5.daily_stock_back.find({'date' :day,})
                    for index, j in enumerate(d):
                        self.check_nyamab=j['samosa nyama']
                        self.check_warub = j['samosa waru']
                        self.check_ndengub = j['samosa waru']
                        self.check_mayaib = j['mayai']
                        self.check_smokib = j['smoki']

                    if len(self.check_nyamab)==0:
                        pass
                    else:

                        self.samosa_nyamab_outl = Label(self.frame2ba2, font=('Times', 8, 'bold'), fg='red',relief='sunken', bd=3, text=self.check_nyamab )
                        self.samosa_nyamab_outl.grid(row=1, column=2, padx=3, pady=1, sticky='nsew')

                    if len(self.check_warub)==0:
                       pass

                    else:

                        self.samosa_warub_outl = Label(self.frame2ba2, font=('Times', 8, 'bold'), fg='red',text=self.check_warub,relief='sunken', bd=3)
                        self.samosa_warub_outl.grid(row=2, column=2, padx=3, pady=1, sticky='nsew')

                    if len(self.check_ndengub) == 0:
                        pass

                    else:

                        self.samosa_ndengu_outl = Label(self.frame2ba2, font=('Times', 8, 'bold'), fg='red',
                                                      text=self.check_ndengub, relief='sunken', bd=3)
                        self.samosa_ndengu_outl.grid(row=3, column=2, padx=3, pady=1, sticky='nsew')


                    if len(self.check_mayaib) == 0:
                        pass

                    else:

                        self.samosa_mayai_outl = Label(self.frame2ba2, font=('Times', 8, 'bold'), fg='red',
                                                        text=self.check_mayaib, relief='sunken', bd=3)
                        self.samosa_mayai_outl.grid(row=4, column=2, padx=3, pady=1, sticky='nsew')

                    if len( self.check_smokib) == 0:
                        pass

                    else:

                        self.samosa_smoki_outl = Label(self.frame2ba2, font=('Times', 8, 'bold'), fg='red',
                                                       text=self.check_smokib, relief='sunken', bd=3)
                        self.samosa_smoki_outl.grid(row=5, column=2, padx=3, pady=1, sticky='nsew')

                def stock_out_entry(self):


                    self.nyama_check=self.samosa_nyama_out.get()
                    self.check_waru=self.samosa_waru_out.get()
                    self.check_ndengu=self.samosa_ndengu_out.get()
                    self.check_mayai = self.samosa_mayai_out.get()
                    self.check_mayai = self.samosa_smoki_out.get()

                    d=db4.daily_stock_out.find({'date' :day,})
                    for index, j in enumerate(d):
                        self.check_nyama=j['samosa nyama']
                        self.check_waru = j['samosa waru']
                        self.check_ndengu = j['samosa ndengu']
                        self.check_mayai = j['mayai']
                        self.check_smoki = j['smoki']

                    if len(self.check_nyama)==0:

                        self.samosa_nyama_backl = Label(self.frame2ba2, font=('Times', 8, 'bold'), fg='red',
                                                       relief='sunken', bd=3)
                        self.samosa_nyama_backl.grid(row=1, column=2, padx=3, pady=1, sticky='nsew')

                        self.samosa_nyama_out = Entry(self.frame2ba2, font=('Times', 8, 'bold'), fg='red', )
                        self.samosa_nyama_out.grid(row=1, column=1, padx=3, pady=1, sticky='nsew')

                    else:
                        self.samosa_nyama_back = Entry(self.frame2ba2, font=('Times', 8, 'bold'), fg='red',
                                                       )
                        self.samosa_nyama_back.grid(row=1, column=2, padx=3, pady=1, sticky='nsew')

                        self.samosa_nyama_outl = Label(self.frame2ba2, font=('Times', 8, 'bold'), fg='red',relief='sunken', bd=3, text=self.check_nyama )
                        self.samosa_nyama_outl.grid(row=1, column=1, padx=3, pady=1, sticky='nsew')

                    if len(self.check_waru)==0:
                        self.samosa_waru_backl = Label(self.frame2ba2, font=('Times', 8, 'bold'), fg='red',
                                                       relief='sunken', bd=3,)
                        self.samosa_waru_backl.grid(row=2, column=2, padx=3, pady=1, sticky='nsew')

                        self.samosa_waru_out = Entry(self.frame2ba2, font=('Times', 8, 'bold'), fg='red')
                        self.samosa_waru_out.grid(row=2, column=1, padx=3, pady=1)

                    else:
                        self.samosa_waru_back = Entry(self.frame2ba2, font=('Times', 8, 'bold'), fg='red',
                                                      )
                        self.samosa_waru_back.grid(row=2, column=2, padx=3, pady=1, sticky='nsew')

                        self.samosa_waru_outl = Label(self.frame2ba2, font=('Times', 8, 'bold'), fg='red',text=self.check_waru,relief='sunken', bd=3)
                        self.samosa_waru_outl.grid(row=2, column=1, padx=3, pady=1, sticky='nsew')

                    if len(self.check_ndengu) == 0:
                        self.samosa_ndengu_backl = Label(self.frame2ba2, font=('Times', 8, 'bold'), fg='red',
                                                       relief='sunken', bd=3, )
                        self.samosa_ndengu_backl.grid(row=3, column=2, padx=3, pady=1, sticky='nsew')

                        self.samosa_ndengu_out = Entry(self.frame2ba2, font=('Times', 8, 'bold'), fg='red')
                        self.samosa_ndengu_out.grid(row=3,column=1, padx=3, pady=1,sticky='nsew')

                    else:
                        self.samosa_ndengu_back = Entry(self.frame2ba2, font=('Times', 8, 'bold'), fg='red',
                                                      )
                        self.samosa_ndengu_back.grid(row=3, column=2, padx=3, pady=1, sticky='nsew')

                        self.samosa_ndengu_outl = Label(self.frame2ba2, font=('Times', 8, 'bold'), fg='red',
                                                      text=self.check_ndengu, relief='sunken', bd=3)
                        self.samosa_ndengu_outl.grid(row=3, column=1, padx=3, pady=1, sticky='nsew')


                    if len(self.check_mayai) == 0:
                        self.samosa_mayai_backl = Label(self.frame2ba2, font=('Times', 8, 'bold'), fg='red',
                                                         relief='sunken', bd=3, )
                        self.samosa_mayai_backl.grid(row=4, column=2, padx=3, pady=1, sticky='nsew')

                        self.samosa_mayai_out = Entry(self.frame2ba2, font=('Times', 8, 'bold'), fg='red')
                        self.samosa_mayai_out.grid(row=4, column=1, padx=3, pady=1,sticky='nsew')

                    else:
                        self.samosa_mayai_back = Entry(self.frame2ba2, font=('Times', 8, 'bold'), fg='red',
                                                        )
                        self.samosa_mayai_back.grid(row=4, column=2, padx=3, pady=1, sticky='nsew')

                        self.samosa_mayai_outl = Label(self.frame2ba2, font=('Times', 8, 'bold'), fg='red',
                                                        text=self.check_mayai, relief='sunken', bd=3)
                        self.samosa_mayai_outl.grid(row=4, column=1, padx=3, pady=1, sticky='nsew')

                    if len(self.check_smoki) == 0:
                        self.samosa_smoki_backl = Label(self.frame2ba2, font=('Times', 8, 'bold'), fg='red',
                                                        relief='sunken', bd=3,)
                        self.samosa_smoki_backl.grid(row=5, column=2, padx=3, pady=1, sticky='nsew')

                        self.samosa_smoki_out = Entry(self.frame2ba2, font=('Times', 8, 'bold'), fg='red')
                        self.samosa_smoki_out.grid(row=5, column=1, padx=3, pady=1,sticky='nsew')

                    else:
                        self.samosa_smoki_back = Entry(self.frame2ba2, font=('Times', 8, 'bold'), fg='red',
                                                       )
                        self.samosa_smoki_back.grid(row=5, column=2, padx=3, pady=1, sticky='nsew')

                        self.samosa_smoki_outl = Label(self.frame2ba2, font=('Times', 8, 'bold'), fg='red',
                                                       text=self.check_smoki, relief='sunken', bd=3)
                        self.samosa_smoki_outl.grid(row=5, column=1, padx=3, pady=1, sticky='nsew')

                def save_stock_back(self):

                    if len(self.samosa_nyama_back.get())==0 or len(self.samosa_waru_back.get())==0 or len(self.samosa_ndengu_back.get())==0 or len(self.samosa_mayai_back.get())==0 or len(self.samosa_smoki_back.get()) ==0:
                        print('no no no no no no no no no')
                    else:
                        stock_back = {'date': day, 'samosa nyama': self.samosa_nyama_back.get(),
                                     'samosa waru': self.samosa_waru_back.get(),
                                     'samosa ndengu': self.samosa_ndengu_back.get()
                            , 'mayai': self.samosa_mayai_back.get(), 'smoki': self.samosa_smoki_back.get()}
                        db5.daily_stock_back.insert(stock_back)
                        self.check_buttons()
                        self.stock_back_entry()

                        f = db4.daily_stock_out.find({'date': day})
                        for index, u in enumerate(f):
                            samosa_nyama = int(u['samosa nyama'])
                            samosa_waru = int(u['samosa waru'])
                            samosa_ndengu = int(u['samosa ndengu'])
                            mayai = int(u['mayai'])
                            smoki = int(u['smoki'])

                        nyamab=int(self.samosa_nyama_back.get())
                        warub = int(self.samosa_waru_back.get())
                        ndengub = int(self.samosa_ndengu_back.get())
                        mayaib = int(self.samosa_mayai_back.get())

                        smokib = int(self.samosa_smoki_back.get())

                        stock_sold={'date' : day, 'samosa nyama' : samosa_nyama-nyamab,'samosa waru':samosa_waru-warub
                        , 'samosa ndengu':samosa_ndengu - ndengub,'mayai':mayai-mayaib,'smoki': smoki-smokib,}

                        db6.sold_stock.insert(stock_sold)
                        self.sold_stock()




                def save_stock_out(self):

                    if len(self.samosa_nyama_out.get())==0 or len(self.samosa_waru_out.get())==0 or len(self.samosa_ndengu_out.get())==0 or len(self.samosa_mayai_out.get())==0 or len(self.samosa_smoki_out.get()) ==0:
                        print('no no no no no no no no no')
                    else:
                        stock_out = {'date': day, 'samosa nyama': self.samosa_nyama_out.get(),
                                     'samosa waru': self.samosa_waru_out.get(),
                                     'samosa ndengu': self.samosa_ndengu_out.get()
                            , 'mayai': self.samosa_mayai_out.get(), 'smoki': self.samosa_smoki_out.get()}
                        db4.daily_stock_out.insert(stock_out)
                        self.check_buttons()
                        self.stock_out_entry()

                def selected_now_raw(self,):

                    if  len(self.frame2ba_juu2b_price_e.get()) ==0:
                        print('nothing')
                    elif len(self.frame2ba_juu2b_q.get()) ==0:
                        print('nothing')
                    else:
                        s=db3.daily_raw_material.find({'name' : self.selected_raw,'date' : day}).count()
                        if s ==1:
                           print('ikooo')
                        else:
                            print('saved')

                            self.tot.append(int( self.frame2ba_juu2b_price_e.get()))

                            self.total =sum(self.tot)



                            rr = {'name': self.selected_raw, 'quantity': self.frame2ba_juu2b_q.get(),
                                  'price': self.frame2ba_juu2b_price_e.get(), 'date': day,'total': self.total }

                            db3.daily_raw_material.insert(rr)

                            self.frame2ba_juu2b_q = Entry(self.frame2ba_juu2b,
                                                          font=('Times', 10, 'bold'))
                            self.frame2ba_juu2b_q.grid(row=1, column=1, padx=2, pady=2, sticky='nsew')

                            self.frame2ba_juu2b_price_e = Entry(self.frame2ba_juu2b,
                                                                font=('Times', 10, 'bold'))
                            self.frame2ba_juu2b_price_e.grid(row=2, column=1, padx=2, pady=2, sticky='nsew')

                            self.frame2ba_juu2b_name = Label(self.frame2ba_juu2b, text='------oo-',
                                                             font=('Times', 10, 'bold'), fg='red')
                            self.frame2ba_juu2b_name.grid(row=0, column=1, padx=2, pady=2, sticky='nsew')



                            self.popup_raw()


                def popup_raw(self):


                    try:
                        self.pop.destroy()
                    except:
                        pass
                    self.pop = Tk()



                    self.pop.title('selected list')
                    self.w = 200
                    self.h = 200

                    self.hs = self.pop.winfo_screenheight()
                    self.ws = self.pop.winfo_screenwidth()

                    self.x = (self.ws / 1) - (self.w / 2)
                    self.y = (self.hs / 3.7) - (self.h / 2)
                    self.pop.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))
                    self.pop.attributes('-topmost', 'true')

                    f = Frame(self.pop, bg='tan')
                    f.grid(sticky='nsew', padx=3, pady=3)

                    tree = ttk.Treeview(f)
                    tree.grid(sticky='nsew')

                    self.pop.rowconfigure(0, weight=1)
                    self.pop.rowconfigure(1, weight=0)
                    self.pop.columnconfigure(0, weight=1)

                    vsb = ttk.Scrollbar(self.pop, orient='vertical', command=tree.yview)
                    vsb.grid(row=0, column=3, sticky='ns')

                    tree.configure(yscrollcommand=vsb.set)

                    tree['columns'] = ('1', '2')
                    tree['show'] = 'headings'

                    tree.column('1', width=100, anchor='c')
                    tree.column('2', width=100, anchor='c')

                    tree.heading('1', text='NAME')
                    tree.heading('2', text='PRICE')
                    h = db3.daily_raw_material.find({'date': day})
                    for index, n in enumerate(h):
                        tree.insert("", 'end', values=(n['name'], n['price']))
                    self.total = sum(self.tot)
                    h = Label(self.pop, text='Total: ' + str(self.total))
                    h.grid(row=1, columnspan=3)
                    self.pop.after(20, self.pop2)

                    self.pop.mainloop()
                def pop2(self):

                    try:
                        self.pop.destroy()
                    except:
                        pass
                    self.pop = Tk()

                    self.pop.title('selected list')
                    self.w = 200
                    self.h = 200

                    self.hs = self.pop.winfo_screenheight()
                    self.ws = self.pop.winfo_screenwidth()

                    self.x = (self.ws / 1.1) - (self.w / 2)
                    self.y = (self.hs / 3.7) - (self.h / 2)
                    self.pop.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))
                    self.pop.attributes('-topmost', 'true')

                    f = Frame(self.pop, bg='tan')
                    f.grid(sticky='nsew', padx=3, pady=3)

                    tree = ttk.Treeview(f)
                    tree.grid(sticky='nsew')

                    self.pop.rowconfigure(0, weight=1)
                    self.pop.rowconfigure(1, weight=0)
                    self.pop.columnconfigure(0, weight=1)

                    vsb = ttk.Scrollbar(self.pop, orient='vertical', command=tree.yview)
                    vsb.grid(row=0, column=3, sticky='ns')

                    tree.configure(yscrollcommand=vsb.set)

                    tree['columns'] = ('1', '2')
                    tree['show'] = 'headings'

                    tree.column('1', width=100, anchor='c')
                    tree.column('2', width=100, anchor='c')

                    tree.heading('1', text='NAME')
                    tree.heading('2', text='PRICE')
                    h = db3.daily_raw_material.find({'date': day})
                    for index, n in enumerate(h):
                        tree.insert("", 'end', values=(n['name'], n['price']))
                    h = Label(self.pop, text='Total: ' + str(self.total))
                    h.grid(row=1, columnspan=3)
                    self.pop.after(20, self.pop3)
                    self.pop.mainloop()
                def pop3(self):

                    try:
                        self.pop.destroy()
                    except:
                        pass
                    self.pop = Tk()

                    self.pop.title('selected list')
                    self.w = 200
                    self.h = 200

                    self.hs = self.pop.winfo_screenheight()
                    self.ws = self.pop.winfo_screenwidth()

                    self.x = (self.ws / 1.2) - (self.w / 2)
                    self.y = (self.hs / 3.7) - (self.h / 2)
                    self.pop.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))
                    self.pop.attributes('-topmost', 'true')

                    f = Frame(self.pop, bg='tan')
                    f.grid(sticky='nsew', padx=3, pady=3)

                    tree = ttk.Treeview(f)
                    tree.grid(sticky='nsew')

                    self.pop.rowconfigure(0, weight=1)
                    self.pop.rowconfigure(1, weight=0)
                    self.pop.columnconfigure(0, weight=1)

                    vsb = ttk.Scrollbar(self.pop, orient='vertical', command=tree.yview)
                    vsb.grid(row=0, column=3, sticky='ns')

                    tree.configure(yscrollcommand=vsb.set)

                    tree['columns'] = ('1', '2')
                    tree['show'] = 'headings'

                    tree.column('1', width=100, anchor='c')
                    tree.column('2', width=100, anchor='c')
                    tree.heading('1', text='NAME')
                    tree.heading('2', text='PRICE')
                    h = db3.daily_raw_material.find()
                    for index, n in enumerate(h):
                        tree.insert("", 'end', values=(n['name'], n['price']))
                    h = Label(self.pop, text='Total: ' + str(self.total))
                    h.grid(row=1, columnspan=3)
                    self.pop.after(20, self.pop3)
                    self.pop.mainloop()

                def pop3(self):
                    try:
                        self.pop.destroy()
                    except:
                        pass
                    self.pop = Tk()
                    self.pop.title('selected list')
                    self.w = 200
                    self.h = 200
                    self.hs = self.pop.winfo_screenheight()
                    self.ws = self.pop.winfo_screenwidth()
                    self.x = (self.ws / 1.3) - (self.w / 2)
                    self.y = (self.hs / 3.7) - (self.h / 2)
                    self.pop.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))
                    self.pop.attributes('-topmost', 'true')
                    f = Frame(self.pop, bg='tan')
                    f.grid(sticky='nsew', padx=3, pady=3)
                    tree = ttk.Treeview(f)
                    tree.grid(sticky='nsew')
                    self.pop.rowconfigure(0, weight=1)
                    self.pop.rowconfigure(1, weight=0)
                    self.pop.columnconfigure(0, weight=1)

                    vsb = ttk.Scrollbar(self.pop, orient='vertical', command=tree.yview)
                    vsb.grid(row=0, column=3, sticky='ns')

                    tree.configure(yscrollcommand=vsb.set)

                    tree['columns'] = ('1', '2')
                    tree['show'] = 'headings'

                    tree.column('1', width=100, anchor='c')
                    tree.column('2', width=100, anchor='c')

                    tree.heading('1', text='NAME')
                    tree.heading('2', text='PRICE')
                    h = db3.daily_raw_material.find()
                    for index, n in enumerate(h):
                        tree.insert("", 'end', values=(n['name'], n['price']))
                    h = Label(self.pop, text='Total: ' + str(self.total))
                    h.grid(row=1, columnspan=3)
                    self.pop.after(20, self.pop4)
                    self.pop.mainloop()

                def pop4(self):

                    try:
                        self.pop.destroy()
                    except:
                        pass
                    self.pop = Tk()

                    self.pop.title('selected list')
                    self.w = 200
                    self.h = 200

                    self.hs = self.pop.winfo_screenheight()
                    self.ws = self.pop.winfo_screenwidth()

                    self.x = (self.ws / 1.4) - (self.w / 2)
                    self.y = (self.hs / 3.7) - (self.h / 2)
                    self.pop.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))
                    self.pop.attributes('-topmost', 'true')

                    f = Frame(self.pop, bg='tan')
                    f.grid(sticky='nsew', padx=3, pady=3)

                    tree = ttk.Treeview(f)
                    tree.grid(sticky='nsew')

                    self.pop.rowconfigure(0, weight=1)
                    self.pop.rowconfigure(1, weight=0)
                    self.pop.columnconfigure(0, weight=1)

                    vsb = ttk.Scrollbar(self.pop, orient='vertical', command=tree.yview)
                    vsb.grid(row=0, column=3, sticky='ns')

                    tree.configure(yscrollcommand=vsb.set)

                    tree['columns'] = ('1', '2')
                    tree['show'] = 'headings'

                    tree.column('1', width=100, anchor='c')
                    tree.column('2', width=100, anchor='c')

                    tree.heading('1', text='NAME')
                    tree.heading('2', text='PRICE')
                    h = db3.daily_raw_material.find()
                    for index, n in enumerate(h):
                        tree.insert("", 'end', values=(n['name'], n['price']))
                    h = Label(self.pop, text='Total: ' + str(self.total))
                    h.grid(row=1, columnspan=3)
                    self.pop.after(20, self.pop5)
                    self.pop.mainloop()

                def pop5(self):

                    try:
                        self.pop.destroy()
                    except:
                        pass
                    self.pop = Tk()

                    self.pop.title('selected list')
                    self.w = 200
                    self.h = 200

                    self.hs = self.pop.winfo_screenheight()
                    self.ws = self.pop.winfo_screenwidth()

                    self.x = (self.ws / 1.5) - (self.w / 2)
                    self.y = (self.hs / 3.7) - (self.h / 2)
                    self.pop.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))
                    self.pop.attributes('-topmost', 'true')

                    f = Frame(self.pop, bg='tan')
                    f.grid(sticky='nsew', padx=3, pady=3)

                    tree = ttk.Treeview(f)
                    tree.grid(sticky='nsew')

                    self.pop.rowconfigure(0, weight=1)
                    self.pop.rowconfigure(1, weight=0)
                    self.pop.columnconfigure(0, weight=1)

                    vsb = ttk.Scrollbar(self.pop, orient='vertical', command=tree.yview)
                    vsb.grid(row=0, column=3, sticky='ns')

                    tree.configure(yscrollcommand=vsb.set)

                    tree['columns'] = ('1', '2')
                    tree['show'] = 'headings'

                    tree.column('1', width=100, anchor='c')
                    tree.column('2', width=100, anchor='c')

                    tree.heading('1', text='NAME')
                    tree.heading('2', text='PRICE')
                    h = db3.daily_raw_material.find()
                    for index, n in enumerate(h):
                        tree.insert("", 'end', values=(n['name'], n['price']))
                    h = Label(self.pop, text='Total: ' + str(self.total))
                    h.grid(row=1, columnspan=3)
                    self.pop.after(20, self.pop6)
                    self.pop.mainloop()
                def pop6(self):

                    try:
                        self.pop.destroy()
                    except:
                        pass
                    self.pop = Tk()

                    self.pop.title('selected list')
                    self.w = 200
                    self.h = 200

                    self.hs = self.pop.winfo_screenheight()
                    self.ws = self.pop.winfo_screenwidth()

                    self.x = (self.ws / 1.6) - (self.w / 2)
                    self.y = (self.hs / 3.7) - (self.h / 2)
                    self.pop.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))
                    self.pop.attributes('-topmost', 'true')

                    f = Frame(self.pop, bg='tan')
                    f.grid(sticky='nsew', padx=3, pady=3)

                    tree = ttk.Treeview(f)
                    tree.grid(sticky='nsew')

                    self.pop.rowconfigure(0, weight=1)
                    self.pop.rowconfigure(1, weight=0)
                    self.pop.columnconfigure(0, weight=1)

                    vsb = ttk.Scrollbar(self.pop, orient='vertical', command=tree.yview)
                    vsb.grid(row=0, column=3, sticky='ns')

                    tree.configure(yscrollcommand=vsb.set)

                    tree['columns'] = ('1', '2')
                    tree['show'] = 'headings'

                    tree.column('1', width=100, anchor='c')
                    tree.column('2', width=100, anchor='c')

                    tree.heading('1', text='NAME')
                    tree.heading('2', text='PRICE')
                    h = db3.daily_raw_material.find()
                    for index, n in enumerate(h):
                        tree.insert("", 'end', values=(n['name'], n['price']))
                    h = Label(self.pop, text='Total: ' + str(self.total))
                    h.grid(row=1, columnspan=3)
                    self.pop.after(20, self.pop7)
                    self.pop.mainloop()
                def pop7(self):

                    try:
                        self.pop.destroy()
                    except:
                        pass
                    self.pop = Tk()

                    self.pop.title('selected list')
                    self.w = 200
                    self.h = 200

                    self.hs = self.pop.winfo_screenheight()
                    self.ws = self.pop.winfo_screenwidth()

                    self.x = (self.ws / 1.7) - (self.w / 2)
                    self.y = (self.hs / 3.7) - (self.h / 2)
                    self.pop.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))
                    self.pop.attributes('-topmost', 'true')

                    f = Frame(self.pop, bg='tan')
                    f.grid(sticky='nsew', padx=3, pady=3)

                    tree = ttk.Treeview(f)
                    tree.grid(sticky='nsew')

                    self.pop.rowconfigure(0, weight=1)
                    self.pop.rowconfigure(1, weight=0)
                    self.pop.columnconfigure(0, weight=1)

                    vsb = ttk.Scrollbar(self.pop, orient='vertical', command=tree.yview)
                    vsb.grid(row=0, column=3, sticky='ns')

                    tree.configure(yscrollcommand=vsb.set)

                    tree['columns'] = ('1', '2')
                    tree['show'] = 'headings'

                    tree.column('1', width=100, anchor='c')
                    tree.column('2', width=100, anchor='c')

                    tree.heading('1', text='NAME')
                    tree.heading('2', text='PRICE')
                    h = db3.daily_raw_material.find()
                    for index, n in enumerate(h):
                        tree.insert("", 'end', values=(n['name'], n['price']))
                    h = Label(self.pop, text='Total: ' + str(self.total))
                    h.grid(row=1, columnspan=3)
                    self.pop.after(20, self.pop8)
                    self.pop.mainloop()
                def pop8(self):

                    try:
                        self.pop.destroy()
                    except:
                        pass
                    self.pop = Tk()

                    self.pop.title('selected list')
                    self.w = 200
                    self.h = 200

                    self.hs = self.pop.winfo_screenheight()
                    self.ws = self.pop.winfo_screenwidth()

                    self.x = (self.ws / 1.8) - (self.w / 2)
                    self.y = (self.hs / 3.7) - (self.h / 2)
                    self.pop.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))
                    self.pop.attributes('-topmost', 'true')

                    f = Frame(self.pop, bg='tan')
                    f.grid(sticky='nsew', padx=3, pady=3)

                    tree = ttk.Treeview(f)
                    tree.grid(sticky='nsew')

                    self.pop.rowconfigure(0, weight=1)
                    self.pop.rowconfigure(1, weight=0)
                    self.pop.columnconfigure(0, weight=1)

                    vsb = ttk.Scrollbar(self.pop, orient='vertical', command=tree.yview)
                    vsb.grid(row=0, column=3, sticky='ns')

                    tree.configure(yscrollcommand=vsb.set)

                    tree['columns'] = ('1', '2')
                    tree['show'] = 'headings'

                    tree.column('1', width=100, anchor='c')
                    tree.column('2', width=100, anchor='c')

                    tree.heading('1', text='NAME')
                    tree.heading('2', text='PRICE')
                    h = db3.daily_raw_material.find()
                    for index, n in enumerate(h):
                        tree.insert("", 'end', values=(n['name'], n['price']))
                    h = Label(self.pop, text='Total: ' + str(self.total))
                    h.grid(row=1, columnspan=3)
                    self.pop.after(20, self.pop9)
                    self.pop.mainloop()
                def pop9(self):

                    try:
                        self.pop.destroy()
                    except:
                        pass
                    self.pop = Tk()

                    self.pop.title('selected list')
                    self.w = 200
                    self.h = 200

                    self.hs = self.pop.winfo_screenheight()
                    self.ws = self.pop.winfo_screenwidth()

                    self.x = (self.ws / 1.9) - (self.w / 2)
                    self.y = (self.hs / 3.7) - (self.h / 2)
                    self.pop.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))
                    self.pop.attributes('-topmost', 'true')

                    f = Frame(self.pop, bg='tan')
                    f.grid(sticky='nsew', padx=3, pady=3)

                    tree = ttk.Treeview(f)
                    tree.grid(sticky='nsew')

                    self.pop.rowconfigure(0, weight=1)
                    self.pop.rowconfigure(1, weight=0)
                    self.pop.columnconfigure(0, weight=1)

                    vsb = ttk.Scrollbar(self.pop, orient='vertical', command=tree.yview)
                    vsb.grid(row=0, column=3, sticky='ns')

                    tree.configure(yscrollcommand=vsb.set)

                    tree['columns'] = ('1', '2')
                    tree['show'] = 'headings'

                    tree.column('1', width=100, anchor='c')
                    tree.column('2', width=100, anchor='c')

                    tree.heading('1', text='NAME')
                    tree.heading('2', text='PRICE')
                    h = db3.daily_raw_material.find()
                    for index, n in enumerate(h):
                        tree.insert("", 'end', values=(n['name'], n['price']))
                    h = Label(self.pop, text='Total: ' + str(self.total))
                    h.grid(row=1, columnspan=3)
                    self.pop.after(20, self.pop10)
                    self.pop.mainloop()

                def pop10(self):

                    try:
                        self.pop.destroy()
                    except:
                        pass
                    self.pop = Tk()

                    self.pop.title('selected list')
                    self.w = 200
                    self.h = 200

                    self.hs = self.pop.winfo_screenheight()
                    self.ws = self.pop.winfo_screenwidth()

                    self.x = (self.ws / 2) - (self.w / 2)
                    self.y = (self.hs / 3.7) - (self.h / 2)
                    self.pop.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))
                    self.pop.attributes('-topmost', 'true')

                    f = Frame(self.pop, bg='tan')
                    f.grid(sticky='nsew', padx=3, pady=3)

                    tree = ttk.Treeview(f)
                    tree.grid(sticky='nsew')

                    self.pop.rowconfigure(0, weight=1)
                    self.pop.rowconfigure(1, weight=0)
                    self.pop.columnconfigure(0, weight=1)

                    vsb = ttk.Scrollbar(self.pop, orient='vertical', command=tree.yview)
                    vsb.grid(row=0, column=3, sticky='ns')

                    tree.configure(yscrollcommand=vsb.set)

                    tree['columns'] = ('1', '2')
                    tree['show'] = 'headings'

                    tree.column('1', width=100, anchor='c')
                    tree.column('2', width=100, anchor='c')

                    tree.heading('1', text='NAME')
                    tree.heading('2', text='PRICE')
                    h = db3.daily_raw_material.find()
                    for index, n in enumerate(h):
                        tree.insert("", 'end', values=(n['name'], n['price']))
                    h = Label(self.pop, text='Total: ' + str(self.total))
                    h.grid(row=1, columnspan=3)
                    self.pop.after(20, self.pop11)
                    self.pop.mainloop()

                def pop11(self):

                    try:
                        self.pop.destroy()
                    except:
                        pass
                    self.pop = Tk()

                    self.pop.title('selected list')
                    self.w = 200
                    self.h = 200

                    self.hs = self.pop.winfo_screenheight()
                    self.ws = self.pop.winfo_screenwidth()

                    self.x = (self.ws / 2.1) - (self.w / 2)
                    self.y = (self.hs / 3.7) - (self.h / 2)
                    self.pop.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))
                    self.pop.attributes('-topmost', 'true')

                    f = Frame(self.pop, bg='tan')
                    f.grid(sticky='nsew', padx=3, pady=3)

                    tree = ttk.Treeview(f)
                    tree.grid(sticky='nsew')

                    self.pop.rowconfigure(0, weight=1)
                    self.pop.rowconfigure(1, weight=0)
                    self.pop.columnconfigure(0, weight=1)

                    vsb = ttk.Scrollbar(self.pop, orient='vertical', command=tree.yview)
                    vsb.grid(row=0, column=3, sticky='ns')

                    tree.configure(yscrollcommand=vsb.set)

                    tree['columns'] = ('1', '2')
                    tree['show'] = 'headings'

                    tree.column('1', width=100, anchor='c')
                    tree.column('2', width=100, anchor='c')

                    tree.heading('1', text='NAME')
                    tree.heading('2', text='PRICE')
                    h = db3.daily_raw_material.find()
                    for index, n in enumerate(h):
                        tree.insert("", 'end', values=(n['name'], n['price']))
                    h = Label(self.pop, text='Total: ' + str(self.total))
                    h.grid(row=1, columnspan=3)
                    self.pop.after(20, self.pop12)
                    self.pop.mainloop()
                def pop12(self):

                    try:
                        self.pop.destroy()
                    except:
                        pass
                    self.pop = Tk()

                    self.pop.title('selected list')
                    self.w = 200
                    self.h = 200

                    self.hs = self.pop.winfo_screenheight()
                    self.ws = self.pop.winfo_screenwidth()

                    self.x = (self.ws / 2.2) - (self.w / 2)
                    self.y = (self.hs / 3.7) - (self.h / 2)
                    self.pop.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))
                    self.pop.attributes('-topmost', 'true')

                    f = Frame(self.pop, bg='tan')
                    f.grid(sticky='nsew', padx=3, pady=3)

                    tree = ttk.Treeview(f)
                    tree.grid(sticky='nsew')

                    self.pop.rowconfigure(0, weight=1)
                    self.pop.rowconfigure(1, weight=0)
                    self.pop.columnconfigure(0, weight=1)

                    vsb = ttk.Scrollbar(self.pop, orient='vertical', command=tree.yview)
                    vsb.grid(row=0, column=3, sticky='ns')

                    tree.configure(yscrollcommand=vsb.set)

                    tree['columns'] = ('1', '2')
                    tree['show'] = 'headings'

                    tree.column('1', width=100, anchor='c')
                    tree.column('2', width=100, anchor='c')

                    tree.heading('1', text='NAME')
                    tree.heading('2', text='PRICE')
                    h = db3.daily_raw_material.find()
                    for index, n in enumerate(h):
                        tree.insert("", 'end', values=(n['name'], n['price']))
                    h = Label(self.pop, text='Total: ' + str(self.total))
                    h.grid(row=1, columnspan=3)
                    self.pop.after(20, self.pop_final)
                    self.pop.mainloop()


                def pop_final(self):

                    try:
                        self.pop.destroy()
                    except:
                        pass

                    self.pop=Tk()

                    self.pop.title('selected listoooooooooo')
                    self.w=200
                    self.h=200
                    self.ws=self.pop.winfo_screenwidth()
                    self.hs = self.pop.winfo_screenheight()
                    self.x=(self.ws/3.8)-(self.w/2)
                    self.y = (self.hs / 3.7) - (self.h / 2)
                    self.pop.geometry('%dx%d+%d+%d' %(self.w,self.h,self.x,self.y))
                    self.pop.attributes('-topmost','true')

                    f =Frame(self.pop, bg='tan')
                    f.grid(sticky='nsew', padx=3, pady=3)

                    tree = ttk.Treeview(f)
                    tree.grid(sticky='nsew')

                    self.pop.rowconfigure(0, weight=1)
                    self.pop.rowconfigure(1, weight=0)
                    self.pop.columnconfigure(0, weight=1)

                    vsb = ttk.Scrollbar(self.pop, orient='vertical', command=tree.yview)
                    vsb.grid(row=0, column=3, sticky='ns')

                    tree.configure(yscrollcommand=vsb.set)

                    tree['columns'] = ('1', '2')
                    tree['show'] = 'headings'

                    tree.column('1', width=100, anchor='c')
                    tree.column('2', width=100, anchor='c')

                    tree.heading('1', text='NAME')
                    tree.heading('2', text='PRICE')
                    h = db3.daily_raw_material.find({'date': day})
                    for index, n in enumerate(h):
                        tree.insert("", 'end', values=(n['name'],n['price']))
                    h=Label(self.pop, text='Total: ' + str(self.total))
                    h.grid(row=1, columnspan=3)
                    self.pop.resizable(0,0)
                    self.pop.mainloop()
                def raw_entries(self):

                    self.frame2ba_juu2b_q = Entry(self.frame2ba_juu2b,
                                                     font=('Times', 10, 'bold'))
                    self.frame2ba_juu2b_q.grid(row=1, column=1, padx=2, pady=2, sticky='nsew')

                    self.frame2ba_juu2b_price_e = Entry(self.frame2ba_juu2b,
                                                  font=('Times', 10, 'bold'))
                    self.frame2ba_juu2b_price_e.grid(row=2, column=1, padx=2, pady=2, sticky='nsew')

 
                def select_raw_label(self):

                    try:
                        self.select_raw_name = self.selected_raw

                        self.frame2ba_juu2b_name = Label(self.frame2ba_juu2b, text=self.select_raw_name,
                                                         font=('Times', 10, 'bold'),fg='red')
                        self.frame2ba_juu2b_name.grid(row=0, column=1, padx=2, pady=2, sticky='nsew')
                    except:
                        pass

                    self.frame2ba_juu2b_name = Label(self.frame2ba_juu2b, text=self.select_raw_name,
                                                         font=('Times', 10, 'bold'),fg='red')
                    self.frame2ba_juu2b_name.grid(row=0, column=1, padx=2, pady=2, sticky='nsew')

                def drop(self,event):
                    self.drop_down.destroy()
                    self.drop_downn()

                    self.selected_raw=event

                    self.select_raw_label()

                def drop_downn(self):
                    k = db2.raw.find()
                    raw_material = []

                    for index, j in enumerate(k):
                        raw_mat = j['name']
                        raw_material.append(raw_mat)

                    self.variable = StringVar()
                    self.variable.set('select raw material')

                    self.drop_down = OptionMenu(self.frame2ba_juu2a, self.variable, *raw_material, command=self.drop)
                    self.drop_down.grid(sticky='new', padx=2, pady=2)

                    self.drop_down.configure(width=20)

                def stock(self):
                    class stock:

                        def __init__(self, master):
                            self.master=master

                            self.frame=Frame(self.master, bg='tan')
                            self.frame.grid(padx=2, pady=2,sticky='nsew')

                            ####
                            self.frame1 = Frame(self.frame, bg='tan')
                            self.frame1.grid(row=0,column=0,padx=2, pady=2, sticky='nsew',)

                            self.frame1_1 = Frame(self.frame1, bg='white')
                            self.frame1_1.grid(row=0, column=0, padx=2, pady=2, sticky='nsew')

                            self.frame1_1.rowconfigure(0, weight=1)
                            self.frame1_1.columnconfigure(0, weight=1)


                            self.frame1a1_label = Label(self.frame1_1,bg='white',  text='Add Stock/Stock table', font=('Times', 15, 'bold'))
                            self.frame1a1_label.grid(row=0, column=0, padx=2, pady=2, sticky='nsew', )

                            #####
                            self.frame1_2 = Frame(self.frame1, bg='dark slate gray', relief='raised', bd=10,)
                            self.frame1_2.grid(row=1, column=0, padx=7, pady=7, )


                            stock_add=['Stock name', 'Price']
                            row=0
                            for i in stock_add:

                                self.ik =Label(self.frame1_2, text=i,font=('Times',12, 'bold'))
                                self.ik.grid(row=row, column=0, padx=5,pady=5)
                                row += 1



                            self.ib = Button(self.frame1_2, text='save', command=self.save_stock,font=('Times', 12, 'bold'),)
                            self.ib.grid(row=2, columnspan=3, padx=5, pady=5)




                            ######

                            #####
                            ####

                            self.frame2 = Frame(self.frame, bg='tan')
                            self.frame2.grid(row=0, column=1, padx=2, pady=2, sticky='nsew', )



                            self.frame2_2 = Frame(self.frame2, bg='white')
                            self.frame2_2.grid(row=0, column=0, padx=2, pady=2, sticky='nsew')

                            self.frame2_2.rowconfigure(0, weight=1)
                            self.frame2_2.columnconfigure(0, weight=1)


                            self.frame2a2_label = Label(self.frame2_2,bg='white',  text='Add Raw material/Table', font=('Times', 15, 'bold'))
                            self.frame2a2_label.grid(row=0, column=0, padx=2, pady=2, sticky='nsew', )

                            #####
                            self.frame2_2 = Frame(self.frame2, bg='dark slate gray', relief='raised', bd=10,)
                            self.frame2_2.grid(row=1, column=0, padx=7, pady=7, )


                            stock_add=['name', ]

                            row=0
                            for i in stock_add:
                                row+=1
                                self.ik =Label(self.frame2_2, text=i,font=('Times',12, 'bold'))
                                self.ik.grid(row=row, column=0, padx=5,pady=5)

                            self.ib = Button(self.frame2_2, text='save', command=self.raw_save,font=('Times', 12, 'bold'),)
                            self.ib.grid(row=2, columnspan=3, padx=5, pady=5)




                            ######

                            #####
                            ####


                            ####

                            ### raw materials


                            self.master.rowconfigure(0, weight=1)
                            self.master.columnconfigure(0, weight=1)

                            self.frame.rowconfigure(0, weight=1)
                            self.frame.columnconfigure(0, weight=1)
                            self.frame.columnconfigure(1, weight=1)

                            self.frame1.rowconfigure(0, weight=0)
                            self.frame1.rowconfigure(1, weight=0)
                            self.frame1.rowconfigure(2, weight=1)
                            self.frame1.columnconfigure(0, weight=1)

                            self.frame2.rowconfigure(0, weight=0)
                            self.frame2.rowconfigure(1, weight=0)
                            self.frame2.rowconfigure(2, weight=1)
                            self.frame2.columnconfigure(0, weight=1)

                            self.frame2.columnconfigure(0, weight=1)

                            self.raw_entries()
                            self.stock_entries()
                            self.stock_table()
                            self.raw_table()


                        def raw_entries(self):
                            self.r = Entry(self.frame2_2, font=('Times', 12, 'bold'))
                            self.r.grid(row=1, column=1, padx=5, pady=5)

                        def stock_entries(self):
                            self.s = Entry(self.frame1_2, font=('Times', 12, 'bold'))
                            self.s.grid(row=0, column=1, padx=5, pady=5)

                            self.p = Entry(self.frame1_2, font=('Times', 12, 'bold'))
                            self.p.grid(row=1, column=1, padx=5, pady=5)

                        def raw_table(self):
                            #######
                            self.frame2_2_d = Frame(self.frame2, bg='tan', relief='sunken', bd=10, )
                            self.frame2_2_d.grid(row=2, column=0, padx=2, pady=2, sticky='nsew')
                            self.frame2_2_d.rowconfigure(0, weight=1)
                            self.frame2_2_d.columnconfigure(0, weight=1)

                            tree = ttk.Treeview(self.frame2_2_d, )
                            tree.grid(sticky='nsew')

                            self.frame2_2_d.rowconfigure(0, weight=1)
                            self.frame2_2_d.columnconfigure(0, weight=1)

                            vsb = ttk.Scrollbar(self.frame2_2_d, orient='vertical', command=tree.yview)
                            vsb.grid(row=0, column=3, sticky='ns')

                            tree.configure(yscrollcommand=vsb.set)

                            tree['columns'] = ('1',)
                            tree['show'] = 'headings'

                            tree.column('1', width=200, anchor='c')


                            tree.heading('1', text='NAME')

                            h = db2.raw.find()
                            for index, n in enumerate(h):
                                tree.insert("", 'end', values=(n['name'], ))

                        def raw_save(self):
                            if len(self.r.get()) == 0:
                                print('nothing')
                            else:
                                h = db2.raw.find({'name': self.r.get()}).count()
                                print(h)
                                if h == 1:
                                    pass
                                else:
                                    print('pass')
                                    raw = {'name': self.r.get()}

                                    db2.raw.insert(raw)
                                    self.raw_table()
                                    self.raw_entries()

                        def stock_table(self):
                            #######
                            self.frame1_2_d = Frame(self.frame1, bg='tan', relief='sunken', bd=10, )
                            self.frame1_2_d.grid(row=2, column=0, padx=2, pady=2, sticky='nsew')
                            self.frame1_2_d.rowconfigure(0, weight=1)
                            self.frame1_2_d.columnconfigure(0, weight=1)




                            tree = ttk.Treeview(self.frame1_2_d, )
                            tree.grid(sticky='nsew')

                            self.frame1_2_d.rowconfigure(0, weight=1)
                            self.frame1_2_d.columnconfigure(0, weight=1)

                            vsb = ttk.Scrollbar(self.frame1_2_d, orient='vertical', command=tree.yview)
                            vsb.grid(row=0, column=3, sticky='ns')

                            tree.configure(yscrollcommand=vsb.set)

                            tree['columns'] = ('1', '2')
                            tree['show'] = 'headings'

                            tree.column('1', width=100, anchor='c')
                            tree.column('2', width=100, anchor='c')

                            tree.heading('1', text='STOCK NAME')
                            tree.heading('2', text='PRICE')
                            h = db1.stock.find()
                            for index, n in enumerate(h):
                                tree.insert("", 'end', values=(n['stock name'], n['price']))



                        def save_stock(self):

                            if len(self.s.get()) ==0:
                                print('nothing')
                            elif len(self.p.get()) ==0:
                                print('nothing')

                            else:
                                if self.p.get() is  int ==False:
                                    print('no')
                                else:
                                    h =db1.stock.find({'stock name' : self.s.get()}).count()
                                    print(h)
                                    if h ==1:
                                        pass
                                    else:
                                        print('pass')
                                        stock = {'stock name': self.s.get(), 'price': self.p.get()}
                                        db1.stock.insert(stock)
                                        self.stock_table()
                                        self.stock_entries()
                    roots=Tk()
                    roots.title('')
                    c= stock(roots)
                    roots.mainloop()
                def update_entry(v):
                    current_value = num1.get()
                    num1.set(current_value + v)
                def clear(self):
                    txtDisplay.delete(0, END)
                    return
            root1 = Tk()
            root1.title('sambuu app')
            l = main_page(root1)
            root1.mainloop()

root=Tk()
l=login(root)
root.mainloop()
