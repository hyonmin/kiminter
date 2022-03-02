from tkinter import *
from tkinter import ttk
import handle_ext_stacker as bdbd

# font
# LabelFrame
f1 = ("calibre", 14, 'bold')
# Treeview
f2 = ("calibre", 12, "normal")
# label and entry
f3 = ("Lato", 12, "normal")

f4 = ("calibre", 18, 'bold')
color_bg = "Lavender"

def reports(self, equipe_id, production_date):
    self.reports = Toplevel(self.master)
    self.reports.title('Report')
    self.reports.geometry('1000x600+455+150')
    self.reports.config(bg=color_bg)

    self.frame_main = Frame(self.reports, bg=color_bg)
    self.frame_main.pack()

    self.frame_tree = Frame(self.frame_main, bg=color_bg)
    self.frame_tree.pack(side='top')
    self.frame_article = Frame(self.frame_main, bg=color_bg)
    self.frame_article.pack(side='left', anchor='w')
    self.frame_total = Frame(self.frame_main, bg=color_bg)
    self.frame_total.pack(side = 'left', anchor='e', padx=(120,0))


    # style for column names
    self.style_report1 = ttk.Style()
    # style for the body of the treeview.
    self.style_report1.configure("report.Treeview", rowheight=31, font=f1)
    self.style_report1.map("report.Treeview", background=[('selected', 'blue')])
    self.style_report1.theme_use("default")
    self.style_report1.configure("report.Treeview.Heading", font=f1)

    self.tree_report1 = ttk.Treeview(self.frame_tree, height=10, style="report.Treeview", selectmode='browse')
    self.tree_report1['columns']=("MACHINE", "ROULEAUX", "POIDS", "DECHET")
    self.tree_report1.column('#0', width=0, stretch=NO)
    self.tree_report1.column("MACHINE", anchor=CENTER, width=223)
    self.tree_report1.column("ROULEAUX", anchor=CENTER, width=223)
    self.tree_report1.column("POIDS", anchor=CENTER, width=223)
    self.tree_report1.column("DECHET", anchor=CENTER, width=223)

    self.tree_report1.heading('#0', text='', anchor=CENTER)
    self.tree_report1.heading('MACHINE', text='MACHINE', anchor=CENTER)
    self.tree_report1.heading('ROULEAUX', text='ROULEAUX', anchor=CENTER)
    self.tree_report1.heading('POIDS', text='POIDS(kg)', anchor=CENTER)
    self.tree_report1.heading('DECHET', text='DECHET(kg)', anchor=CENTER)
    # scollbar
    self.scroll_y_report = Scrollbar(self.frame_tree, width=18, command=self.tree_report1.yview)
    self.tree_report1.configure(yscroll = self.scroll_y_report.set)
    self.scroll_y_report.pack(side=RIGHT, fill=Y, pady=9)
    self.tree_report1.tag_configure('odd', background="Silver")
    self.tree_report1.tag_configure('even', background="White")

    self.tree_report1.pack(padx=2, pady=10)
    

    connection = bdbd.connect()
    bdbd.create_dechet_table(connection)
    bdbd.create_tables(connection)
    info_report = bdbd.release_report_per_machine(connection, equipe_id, production_date)

    for A in info_report:
        if info_report.index(A) % 2 == 0:
            self.tree_report1.insert('', 'end', values=A, tags = ('odd',))
        else:
            self.tree_report1.insert('', 'end', values=A, tags = ('even',))


    # style for column names
    self.style_report2 = ttk.Style()
    # style for the body of the treeview.
    self.style_report2.configure("report2.Treeview", rowheight=31, font=f1)
    self.style_report2.map("report2.Treeview", background=[('selected', 'blue')])
    self.style_report2.theme_use("default")
    self.style_report2.configure("report2.Treeview.Heading", font=f1)

    self.tree_report2 = ttk.Treeview(self.frame_article, height=6, style="report2.Treeview", selectmode='browse')
    self.tree_report2['columns']=("ARTICLE", "POIDS")
    self.tree_report2.column('#0', width=0, stretch=NO)
    self.tree_report2.column("ARTICLE", anchor=CENTER, width=223)
    self.tree_report2.column("POIDS", anchor=CENTER, width=223)

    self.tree_report2.heading('#0', text='', anchor=CENTER)
    self.tree_report2.heading('ARTICLE', text='ARTICLE', anchor=CENTER)
    self.tree_report2.heading('POIDS', text='POIDS(kg)', anchor=CENTER)
    # scollbar
    self.scroll_y_report2 = Scrollbar(self.frame_article, width=18, command=self.tree_report2.yview)
    self.tree_report2.configure(yscroll = self.scroll_y_report2.set)
    self.scroll_y_report2.pack(side=RIGHT, fill=Y, pady=9)
    self.tree_report2.tag_configure('odd', background="Silver")
    self.tree_report2.tag_configure('even', background="White")

    self.tree_report2.pack(padx=2, pady=10)


    article_report = bdbd.report_article(connection, equipe_id, production_date)

    for A in article_report:
        if article_report.index(A) % 2 == 0:
            self.tree_report2.insert('', 'end', values=A, tags = ('odd',))
        else:
            self.tree_report2.insert('', 'end', values=A, tags = ('even',))

    

    total = bdbd.report_total(connection, equipe_id, production_date)
    total = total[0]

    self.lbl_rolls = Label(self.frame_total, text = 'Rouleaux: ' + str(total[0]), font = f4, bg=color_bg)
    self.lbl_rolls.grid(row=0,column=0, pady=10, sticky='w')

    self.lbl_prod = Label(self.frame_total, text = 'Production: ' + total[1], font = f4, bg=color_bg)
    self.lbl_prod.grid(row=1,column=0, pady=10, sticky='w')

    self.lbl_blanc = Label(self.frame_total, text = 'Dechet blanc: ' + total[2], font = f4, bg=color_bg)
    self.lbl_blanc.grid(row=2,column=0, pady=10, sticky='w')

    self.lbl_noir = Label(self.frame_total, text = 'Dechet noir: ' + total[3], font = f4, bg=color_bg)
    self.lbl_noir.grid(row=3,column=0, pady=10, sticky='w')




    self.reports.grab_set()

    
