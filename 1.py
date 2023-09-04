import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog
import datetime
from datetime import date

x = "hallo"
subwin = 0
day_list = []
for i in range(1,15):
    x = str(i) + "日間"
    day_list.append(x)

class window:
    def __init__(self):
        #saveで保存したself.friend_listの復元
        self.friend_list=[]
        self.last_day = 0
        with open(r"C:\Users\Akasa\restorings\programming_folder\action_maneger\a.txt", mode="r") as f:
            self.txts = f.readlines()
            print(self.txts)
            for self.txt in self.txts:
                print(type(self.txt))
                f_list = self.txt.splitlines()[0]
                print(f_list)
                f_list = f_list.split(' ')
                print(f_list)
            #    f_list[2] = int(f_list[2])
            #    print(f_list)
                if len(f_list) == 3:
                    self.friend_list.append(f_list)
                else:
                    self.last_day = int(f_list)
               # self.friend_list[2] = int(self.friend_list[2])
        print(self.friend_list)
        #表示する人の選定
        self.today = datetime.datetime.now().timetuple()[7]
        self.display_l = []
        self.x = ""
        for i in self.friend_list:
            if int(i[2]) <= self.today:
                self.display_l.append(i[0])
                self.x = self.x + " " + i[0]
        # rootメインウィンドウの設定
        self.root = tk.Tk()
        self.root.title("tkinter:Toplevel")
        self.root.geometry("300x150")   
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill = tk.BOTH, padx=5, pady=10)
        self.label = tk.Label(self.frame,text=self.x) #str(self.display_l)
        self.label.pack()
        self.button = ttk.Button(self.frame, text="サブウィンドウ生成", command=self.sub_window)
        self.button2 = ttk.Button(self.frame, text="終わる", command=self.save)
        self.button.pack()
        self.button2.pack()
        self.renew()
        self.root.mainloop()

    def sub_window(self):
        global subwin
        if subwin == 0 or self.sub_win.winfo_exists() != 1:
            subwin = 1
            self.sub_win = tk.Toplevel()
            self.sub_win.geometry("300x300")
            self.sub_win.title("サブウィンドウ")
            self.label_sub = tk.Label(self.sub_win, text="サブウィンドウ")
            self.label_sub.pack()
            #名前等入力
            self.e = tk.Entry(self.sub_win,width = 20)
            self.e.pack()
            #表示日数の間隔
            day_list_v = tk.StringVar(self.sub_win,value=day_list)
            self.listbox = tk.Listbox(self.sub_win,listvariable=day_list_v)
            self.listbox.pack()
            self.button_sub = ttk.Button(self.sub_win, text="決定", command=self.decide)
            self.button_sub.pack()
            print(self.sub_win.winfo_exists(),self.e)

    def decide(self):
        self.a = self.e.get()
        self.b = self.listbox.curselection()
        if self.a == "" or self.b == ():
            return
        
        if self.today + self.b[0] + 1 > 365:
            self.next_day = self.today + self.b[0] + 1 - 365
        else:
            self.next_day = self.today + self.b[0] + 1
        
        self.friend_list.append([self.a,day_list[self.b[0]],str(self.next_day)])
        self.save()
        self.sub_win.destroy()

    #self.friend_listの保存
    def save(self):
        ret = tkinter.filedialog.asksaveasfile(defaultextension=".txt",initialdir=r"C:\Users\Akasa\restorings\programming_folder\action_maneger",initialfile="a.txt")
        with open(r"C:\Users\Akasa\restorings\programming_folder\action_maneger\a.txt", mode="w") as f :
            for i in self.friend_list:
                f.write(" ".join(i) + '\n')
            f.write(str(self.last_day))

    def renew(self):
        #self.last_day
        #if self.last_day < self.today:
        #    #kousinn
        #    for i in self.friend_list:
        #        if int(i[2]) < self.today:
        #            i[2] = str(int(i[2])+int(i[1]))
        #for i in self.friend_list:
        #    self.andls = set(i) & set(self.x)
        #    if self.andls != {}:
        #        pass
        #    else:
        #        i[2] = str(self.today + int(i[1]) - 1)
        if self.last_day != self.today:
            for i in self.friend_list:
                self.day_interval = sorted(i[1])[0]
                print(self.day_interval)
                self.andls = set(i) & set(self.x)
                if self.andls != {}:
                    i[2] = str(self.today + int(self.day_interval) - 1)
        self.last_day = self.today
        self.root.after(300000,self.renew)


app = window()