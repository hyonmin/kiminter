from tkinter import *
from tkinter import ttk
import handle_article_db as dbdb
import gain_xl_date
import math

# font
# LabelFrame
f1 = ("calibre", 14, 'bold')
# Treeview
f2 = ("calibre", 12, "normal")
# label and entry
f3 = ("Lato", 12, "normal")

# keep an id of article you select.
id_article = []

color_bg = "Lavender"

def a(self):
    self.articles = Toplevel(self.master)
    self.articles.geometry('1000x735+455+100')
    self.articles.config(bg=color_bg)
    #======================frames=============
    self.baseFrame = Frame(self.articles, bg=color_bg)
    self.baseFrame.pack()
    self.frame_list = LabelFrame(self.baseFrame, text = "list des articles",\
        font = f1, bg=color_bg, pady=2)
    self.frame_list.pack(padx=8, pady=5)

    self.frame_manager = LabelFrame(self.baseFrame, text = "modification",\
        font = f1, bg=color_bg)
    self.frame_manager.pack(padx=8, expand=True, fill='both')
    self.frame_manager_lbl = Frame(self.frame_manager, bg=color_bg)
    self.frame_manager_lbl.pack(side='left')
    self.frame_manager_btn = Frame(self.frame_manager, bg=color_bg)
    self.frame_manager_btn.pack(side='right', expand=True)

    self.frame_choisir = LabelFrame(self.baseFrame, text = "en fabrication",\
        font = f1, bg=color_bg)
    self.frame_choisir.pack(padx=8,pady=5, expand=True, fill=X)
    self.frame_article_left = Frame(self.frame_choisir, bg=color_bg)
    self.frame_article_left.pack(side='left', padx=(245,0), pady=10)
    self.frame_article_btns = Frame(self.frame_choisir, bg=color_bg, padx=30)
    self.frame_article_btns.pack(side='left', padx=(8,0))
    self.frame_article_right = Frame(self.frame_choisir, bg=color_bg)
    self.frame_article_right.pack(side='right', padx=(0,245), pady=10)

    #=========================================
    self.style_articles = ttk.Style()
    # style for the body of the treeview.
    self.style_articles.configure(style="mystyle2.Treeview", rowheight=23, font=f2)
    self.style_articles.map("mystyle2.Treeview", background=[('selected', 'grey40')])
    self.style_articles.theme_use("default")
    self.style_articles.configure("mystyle2.Treeview.Heading", font=f2)

    # TreeView
    self.tree_list_article = ttk.Treeview(self.frame_list, height=6,\
        style="mystyle2.Treeview", selectmode='browse')

    self.column_list = ("article", "poids 0.5m(g)", "largeur(cm)", "longueur(cm)", 'soufflet(cm)',\
        "poids du produit(kg)", "quantité(pcs)", "poids emballage", "poids sac", "épaisseur", "id")
    
    self.tree_list_article['columns'] = self.column_list

    self.tree_list_article.column('#0', width=0, stretch=NO)
    self.tree_list_article.column('article', anchor=CENTER, width=120)
    self.tree_list_article.column('poids du produit(kg)', anchor=CENTER, width=140)
    self.tree_list_article.column('largeur(cm)', anchor=CENTER, width=120)
    self.tree_list_article.column('longueur(cm)', anchor=CENTER, width=120)
    self.tree_list_article.column('soufflet(cm)', anchor=CENTER, width=120)
    self.tree_list_article.column('quantité(pcs)', anchor=CENTER, width=180)
    self.tree_list_article.column('poids emballage', anchor=CENTER, width=180)
    self.tree_list_article.column('poids sac', anchor=CENTER, width=120)
    self.tree_list_article.column('épaisseur', anchor=CENTER, width=120)
    self.tree_list_article.column('poids 0.5m(g)', anchor=CENTER, width=120)
    self.tree_list_article.column('id', width=0, stretch=NO)

    self.tree_list_article.heading('#0', text='', anchor=CENTER)
    self.tree_list_article.heading('article', text='article', anchor=CENTER)
    self.tree_list_article.heading('poids du produit(kg)', text='poids du produit(kg)', anchor=CENTER)
    self.tree_list_article.heading('largeur(cm)', text='largeur(cm)', anchor=CENTER)
    self.tree_list_article.heading('longueur(cm)', text='longueur(cm)', anchor=CENTER)
    self.tree_list_article.heading('soufflet(cm)', text='soufflet(cm)', anchor=CENTER)
    self.tree_list_article.heading('quantité(pcs)', text='quantité(pcs)', anchor=CENTER)
    self.tree_list_article.heading('poids emballage', text='poids emballage', anchor=CENTER)
    self.tree_list_article.heading('poids sac', text='poids sac', anchor=CENTER)
    self.tree_list_article.heading('épaisseur', text='épaisseur', anchor=CENTER)
    self.tree_list_article.heading('poids 0.5m(g)', text='poids 0.5m(g)', anchor=CENTER)
    self.tree_list_article.heading('id', text='', anchor=CENTER)

    # scollbar
    self.scroll_y_article = Scrollbar(self.frame_list, orient="vertical", width=14,\
        command=self.tree_list_article.yview)
    self.tree_list_article.configure(yscroll = self.scroll_y_article.set)
    self.scroll_y_article.pack(side='right', fill=Y, pady=(3,0))

    self.scroll_x_article = Scrollbar(self.frame_list, orient="horizontal", width=14,\
        command=self.tree_list_article.xview)
    self.tree_list_article.configure(xscroll = self.scroll_x_article.set)
    self.scroll_x_article.pack(side='bottom', fill=X)

    # to put the treeview, 'pack' function should be after all components of the treeview.
    self.tree_list_article.pack(padx=2, pady=2)

    # labels and entries for the modification frame==============
    self.article_name = StringVar()

    self.lbl_article = Label(self.frame_manager_lbl, text="Article", font=f3, bg=color_bg)
    self.lbl_article.grid(row=0, column=0, sticky='w', padx=(70,15), pady=4) 
    self.ent_article = Entry(self.frame_manager_lbl,  width=18, bd=3, justify='center',\
        font=f3, textvariable=self.article_name, disabledbackground="lemon chiffon", disabledforeground="black")
    self.ent_article.grid(row=0, column=1, pady=4)
    self.lbl_weight = Label(self.frame_manager_lbl, text="poids du Produit(kg)", font=f3, bg=color_bg)
    self.lbl_weight.grid(row=0, column=2, sticky='w', padx=(100,0), pady=4) 
    self.ent_weight = Entry(self.frame_manager_lbl, width=18, bd=3, justify='center', font=f3)
    self.ent_weight.grid(row=0, column=3, padx=15, pady=4)

    self.lbl_width = Label(self.frame_manager_lbl, text="Largeur(cm)", font=f3, bg=color_bg)
    self.lbl_width.grid(row=1, column=0, sticky='w', padx=(70,15), pady=4) 
    self.ent_width = Entry(self.frame_manager_lbl, width=18, bd=3, justify='center', font=f3)
    self.ent_width.grid(row=1, column=1, pady=4)
    self.lbl_length = Label(self.frame_manager_lbl, text="Longueur(cm)", font=f3, bg=color_bg)
    self.lbl_length.grid(row=1, column=2, sticky='w', padx=(100,0), pady=4) 
    self.ent_length = Entry(self.frame_manager_lbl, width=18, bd=3, justify='center', font=f3)
    self.ent_length.grid(row=1, column=3, pady=4)

    self.lbl_weight_pack = Label(self.frame_manager_lbl, text="poids Emballage(kg)", font=f3, bg=color_bg)
    self.lbl_weight_pack.grid(row=2, column=0, sticky='w', padx=(70,15), pady=4) 
    self.ent_weight_pack = Entry(self.frame_manager_lbl, width=18, bd=3, justify='center', font=f3)
    self.ent_weight_pack.grid(row=2, column=1, pady=4)
    self.lbl_weight_sac = Label(self.frame_manager_lbl, text="poids Sac(kg)", font=f3, bg=color_bg)
    self.lbl_weight_sac.grid(row=2, column=2, sticky='w', padx=(100,0), pady=4) 
    self.ent_weight_sac = Entry(self.frame_manager_lbl, width=18, bd=3, justify='center', font=f3)
    self.ent_weight_sac.grid(row=2, column=3, pady=4)

    self.lbl_quantity = Label(self.frame_manager_lbl, text="Quantité(pcs)", font=f3, bg=color_bg)
    self.lbl_quantity.grid(row=3, column=0, sticky='w', padx=(70,15), pady=4) 
    self.ent_quantity = Entry(self.frame_manager_lbl, width=18, bd=3, justify='center', font=f3)
    self.ent_quantity.grid(row=3, column=1, pady=4)
    self.lbl_gusset = Label(self.frame_manager_lbl, text="Soufflet(cm)", font=f3, bg=color_bg)
    self.lbl_gusset.grid(row=3, column=2, sticky='w', padx=(100,0), pady=4) 
    self.ent_gusset = Entry(self.frame_manager_lbl, width=18, bd=3, justify='center', font=f3)
    self.ent_gusset.grid(row=3, column=3, pady=4)

    self.lbl_poid_demi = Label(self.frame_manager_lbl, text="poids 0.5 metre(g)", font=f3, bg=color_bg)
    self.lbl_poid_demi.grid(row=4, column=0, sticky='w', padx=(70,15), pady=(4,0)) 
    self.ent_poid_demi = Entry(self.frame_manager_lbl, width=18, bd=3, justify='center',\
        font=f3, state= 'disabled', disabledbackground="lemon chiffon", disabledforeground="black")
    self.ent_poid_demi.grid(row=4, column=1, pady=(4,0))
    self.lbl_thickness = Label(self.frame_manager_lbl, text="épaisseur(μm)", font=f3, bg=color_bg)
    self.lbl_thickness.grid(row=4, column=2, sticky='w', padx=(100,0), pady=(4,0)) 
    self.ent_thickness = Entry(self.frame_manager_lbl, width=18, bd=3, justify='center',\
        font=f3, state= 'disabled', disabledbackground="lemon chiffon", disabledforeground="black")
    self.ent_thickness.grid(row=4, column=3, pady=(4,0))

    # buttons for modificaiton================
    self.btn_add = Button(self.frame_manager_btn, text = "Ajouter", width=7, font=f3, bd=3,\
        command = lambda: add_new(striper(), gain_xl_date.xl_date(None), 0))
    self.btn_add.grid(row=0, column=0, padx=20, pady=(10,0))

    self.btn_modif = Button(self.frame_manager_btn, text = "Modifier", width=7, font=f3, bd=3,\
        state='disabled', command = lambda: mod_old())
    self.btn_modif.grid(row=1, column=0, pady=10)

    self.btn_delete = Button(self.frame_manager_btn, text = "Supprimer", width=7, font=f3, bd=3,\
        state='disabled', command = lambda: del_art())
    self.btn_delete.grid(row=2, column=0, pady=(0,10))

    self.btn_clear = Button(self.frame_manager_btn, text = "Vider", width=7, font=f3, bd=3,\
        command= lambda: clear_ent())
    self.btn_clear.grid(row=3, column=0, pady=(0,10))
    # choosing a element in treeview it will happen================
    def clear_ent():
        self.ent_article.config(state='normal')
        self.ent_poid_demi.config(state='normal')
        self.ent_thickness.config(state='normal')
        self.ent_article.delete(0,'end')
        self.ent_poid_demi.delete(0,'end')
        self.ent_width.delete(0,'end')
        self.ent_length.delete(0,'end')
        self.ent_gusset.delete(0,'end')
        self.ent_weight.delete(0,'end')
        self.ent_quantity.delete(0,'end')
        self.ent_weight_pack.delete(0,'end')
        self.ent_weight_sac.delete(0,'end')
        self.ent_thickness.delete(0,'end')
        self.btn_add.config(state='normal')
        self.btn_modif.config(state='disabled')
        self.btn_delete.config(state='disabled')
        self.ent_poid_demi.config(state='disabled')
        self.ent_thickness.config(state='disabled')

    def select(event):
        clear_ent()
        id_article.clear()
        self.ent_poid_demi.config(state='normal')
        self.ent_thickness.config(state='normal')

        e = self.tree_list_article.selection()
        items = self.tree_list_article.item(e)
        self.ent_article.insert(0, items['values'][0])
        self.ent_poid_demi.insert(0, items['values'][1])
        self.ent_width.insert(0, items['values'][2])
        self.ent_length.insert(0, items['values'][3])
        self.ent_gusset.insert(0, items['values'][4])
        self.ent_weight.insert(0, items['values'][5])
        self.ent_quantity.insert(0, items['values'][6])
        self.ent_weight_pack.insert(0, items['values'][7])
        self.ent_weight_sac.insert(0, items['values'][8])
        self.ent_thickness.insert(0, items['values'][9])
        
        id_article.append(items['values'][5])
        id_article.append(items['values'][2])
        id_article.append(items['values'][3])
        id_article.append(items['values'][7])
        id_article.append(items['values'][8])
        id_article.append(items['values'][6])
        id_article.append(items['values'][4])
        id_article.append(items['values'][1])
        id_article.append(items['values'][9])
        id_article.append(items['values'][10])    # keep id first

        self.ent_poid_demi.config(state='disabled')
        self.ent_thickness.config(state='disabled')
        self.btn_modif.config(state='normal')
        self.btn_delete.config(state='normal')
        self.btn_add.config(state='disabled')
        self.ent_article.config(state='disabled')

    self.tree_list_article.bind('<<TreeviewSelect>>', select)

    # list boxes for making articles activated and inactivated.================
    self.article_inactive = StringVar()
    self.article_active = StringVar()

    self.yscroll_listbox_left = Scrollbar(self.frame_article_left, orient = 'vertical', width=14)
    self.yscroll_listbox_left.pack(side='right', fill=Y, pady=(29,0))
    self.yscroll_listbox_right = Scrollbar(self.frame_article_right, orient = 'vertical', width=14)
    self.yscroll_listbox_right.pack(side='right', fill=Y, pady=(29,0))

    self.lbl_inactive = Label(self.frame_article_left, text="inactif", bg=color_bg, font=f1).pack()

    self.listbox_inactive = Listbox(self.frame_article_left,\
        listvariable=self.article_inactive, yscrollcommand=self.yscroll_listbox_left.set)
    self.listbox_inactive.pack()

    self.lbl_active = Label(self.frame_article_right, text="actif", bg= color_bg, font=f1).pack()
    self.listbox_active = Listbox(self.frame_article_right,\
        listvariable=self.article_active, yscrollcommand=self.yscroll_listbox_right.set)
    self.listbox_active.pack()

    # arrow button to move articles you want to activate or inactivate
    self.btn_arrow_right = Button(self.frame_article_btns, text=">>", font=f1, bd=3,\
        command = lambda: make_actif())
    self.btn_arrow_right.pack(pady=(0,5))
    self.btn_arrow_left = Button(self.frame_article_btns, text="<<", font=f1, bd=3,\
        command = lambda: make_inactif())
    self.btn_arrow_left.pack()
    
    # prohibit from accessing other windows
    self.articles.grab_set()
    # warning messages=============================
    def warn_general(m):
        warn_top = Toplevel()
        warn_top.geometry("250x150+850+450")
        warn_top.title("Attention!")
        msg = Label(warn_top, text = m, font=f1)
        msg.pack(pady=(35,20))
        msg_btn = Button(warn_top, text = "OK", command = warn_top.destroy, font = f1)
        msg_btn.pack()
        warn_top.grab_set()

    # database control=============================
    #create a db if no exists
    def conn():
        connection = dbdb.connect()
        dbdb.create_tables(connection)
        return connection

    # check if the name of article you want to add aleady exists
    # one of the processes to add a new article
    def check_duplicated():
        article = self.article_name.get()
        article = article.strip()
        article = article.upper()
        try:
            articles_from_db = dbdb.get_all_names(conn())
        except:
            warn_general("il s'agit d'article en double.")
            return
        
        art = []
        for A in articles_from_db:
            art.append(A[0])
        try:
            if article in art:
                warn_general("il s'agit d'article en double.")
                return
            else:
                return article
        except:
            warn_general("il s'agit d'article en double.")
            return

    # to refine the text which will be inserted into the table
    # and also get the thickness and reference weight.
    def get_entries():
        a = self.ent_weight.get()
        b = self.ent_width.get()
        c = self.ent_length.get()
        d = self.ent_weight_pack.get()
        e = self.ent_weight_sac.get()
        f = self.ent_quantity.get()
        g = self.ent_gusset.get()
        h=[a,b,c,d,e,f,g]
        return h

    def striper():
        h = get_entries()
        j=0
        for i in h:
            h[j] = i.strip()
            try:
                h[j] = float(i)
            except ValueError:
                warn_general("vérifiez les chiffres.")
                return
            j += 1
        try:
            def fraction(p):
                numerator = (h[1]+h[6]*2)* 0.01 * h[2] *0.01 * h[5] * 948 * 2 * (1-p)
                return numerator
            
            denominator = (h[0] - h[3] - h[4])
            #thickness = (h[0] - h[3] - h[4])*5000 / (h[5] * (h[1]+(h[6]*2))*0.01 * h[2]*0.01 * 948)*10000
            if h[6] != 0:
                numerator = fraction(0.1)
            else:
                numerator = fraction(0)
            thickness = denominator * 100000000 * 0.98 /numerator    # 0.98, get 2% benefit.
            demi = (h[1]+(h[6]*2)) * 0.01 * 0.5 * thickness*2 * 948 / 100
            thickness = math.floor(thickness) / 100
            demi = math.floor(demi) / 1000
            
        except TypeError: return

        h.append(demi)
        h.append(thickness)
        return h

    def add_new(s, c, m):
        try:
            data_articles = s
            data_articles.append(0)    # active:1, inactive:0
            data_articles.append(c)    # create date
            data_articles.append(m)    # modified: date, non-modified:0
            data_articles.append(0)    # deleted: date, non-deleted: 0
            art = check_duplicated()
            data_articles.insert(0, art.upper()) # insert article name into a list(data_article)
            dbdb.add_article(conn(), data_articles)
            warn_general("c'est passé")    # it is to clear all entries and to give a message
            get_treeview()
        except:
            warn_general("ça ne peut pas passer(2)")
            return

    # to modify an old one
    def mod_old():
        h = striper()
        i = 0
        j = 0
        print(id_article)
        ori_id = id_article[9]
        id_article.pop()
        created = dbdb.find_created(conn(), (ori_id,))[0]

        for d in id_article:
            id_article[j]=float(d)
            j += 1

        try:
            for n in range(len(id_article)):
                if n >= 0 and n <= 6:
                    if h[n] != id_article[n]:
                        h.append(gain_xl_date.xl_date(None))
                        h.append(ori_id)
                        dbdb.get_article_modified(conn(), h)
                        add_new(id_article, created, gain_xl_date.xl_date(None))
                        id_article.clear()
                        #j = [str(0), str(ori_id)]
                        dbdb.del_modified(conn(), (0, ori_id))
                        get_treeview()
                        i += 1
                        return
                
        except:
            id_article.clear()
            warn_general("ça ne peut pas passer(0)")
            return

        id_article.clear()
        if i == 0:
            id_article.clear()
            warn_general("pas de modification")
            return


    def del_art():
        try:

            del_var = [str(gain_xl_date.xl_date(None)), str(id_article[9])]
            dbdb.delete_article(conn(), del_var)
            get_treeview()
            warn_general("c'est passé")
        except:
            warn_general("ça ne peut pas passer(1)")
            return

    # insert items in listboxes
    def insert_listbox():
        inactif = dbdb.get_listbox(conn(), 0)
        actif = dbdb.get_listbox(conn(), 1)
        for A in actif:
            self.listbox_active.insert("end", A)
        for I in inactif:
            self.listbox_inactive.insert("end", I)
        #
        #self.listbox_active.insert("end", list_actif)

    def clear_listboxes():
        self.listbox_inactive.delete('0', 'end')
        self.listbox_active.delete('0', 'end')

    def make_actif():
        if self.listbox_inactive.curselection() == ():
            return
        else:
            for i in self.listbox_inactive.curselection():
                actif_soon = self.listbox_inactive.get(i)[0]
            dbdb.make_acf_inacf(conn(), (1, actif_soon))
            clear_listboxes()
            insert_listbox()

    def make_inactif():
        if self.listbox_active.curselection() == ():
            return
        else:
            for i in self.listbox_active.curselection():
                inactif_soon = self.listbox_active.get(i)[0]
            dbdb.make_acf_inacf(conn(), (0, inactif_soon))
            clear_listboxes()
            insert_listbox()

    # insert article information into the treeview ==============================
    def get_treeview():
        self.tree_list_article.delete(*self.tree_list_article.get_children())
        info_articles = dbdb.get_info_treeview(conn())
        for A in info_articles:
            self.tree_list_article.insert('', 'end', values = A)
        id_article.clear()
        clear_listboxes()
        insert_listbox()
        clear_ent()
    get_treeview()
        