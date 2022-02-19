from tkinter import *
from tkinter import ttk
import handle_article_db as dbdb

# font
# LabelFrame
f1 = ("calibre", 14, 'bold')
# Treeview
f2 = ("calibre", 12, "normal")
# label and entry
f3 = ("Lato", 12, "normal")

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
    self.style_articles.configure(style="mystyle2.Treeview", rowheight=10, font=f2)
    self.style_articles.map("mystyle2.Treeview", background=[('selected', 'blue')])
    self.style_articles.theme_use("default")
    self.style_articles.configure("mystyle2.Treeview.Heading", font=f2)

    # TreeView
    self.tree_list_article = ttk.Treeview(self.frame_list, height=15,\
        style="mystyle2.Treeview", selectmode='browse')

    self.tree_list_article['columns']=("article", "poid 0.5m", "largeur", "longueur", "poid du produit",\
        "quantité(pcs)", "poid emballage", "poid sac", "épaisseur")

    self.tree_list_article.column('#0', width=0, stretch=NO)
    self.tree_list_article.column('article', anchor=CENTER, width=120)
    self.tree_list_article.column('poid du produit', anchor=CENTER, width=140)
    self.tree_list_article.column('largeur', anchor=CENTER, width=120)
    self.tree_list_article.column('longueur', anchor=CENTER, width=120)
    self.tree_list_article.column('quantité(pcs)', anchor=CENTER, width=180)
    self.tree_list_article.column('poid emballage', anchor=CENTER, width=180)
    self.tree_list_article.column('poid sac', anchor=CENTER, width=120)
    self.tree_list_article.column('épaisseur', anchor=CENTER, width=120)
    self.tree_list_article.column('poid 0.5m', anchor=CENTER, width=120)

    self.tree_list_article.heading('#0', text='', anchor=CENTER)
    self.tree_list_article.heading('article', text='article', anchor=CENTER)
    self.tree_list_article.heading('poid du produit', text='poid du produit', anchor=CENTER)
    self.tree_list_article.heading('largeur', text='largeur', anchor=CENTER)
    self.tree_list_article.heading('longueur', text='longueur', anchor=CENTER)
    self.tree_list_article.heading('quantité(pcs)', text='quantité(pcs)', anchor=CENTER)
    self.tree_list_article.heading('poid emballage', text='poid emballage', anchor=CENTER)
    self.tree_list_article.heading('poid sac', text='poid sac', anchor=CENTER)
    self.tree_list_article.heading('épaisseur', text='épaisseur', anchor=CENTER)
    self.tree_list_article.heading('poid 0.5m', text='poid 0.5m', anchor=CENTER)

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
    #==============================


    # labels and entries for the modification frame==============
    self.lbl_article = Label(self.frame_manager_lbl, text="Article", font=f3, bg=color_bg)
    self.lbl_article.grid(row=0, column=0, sticky='w', padx=(70,15), pady=4) 
    self.ent_article = Entry(self.frame_manager_lbl,  width=18, bd=3, justify='center', font=f3)
    self.ent_article.grid(row=0, column=1, pady=4)
    self.lbl_weight = Label(self.frame_manager_lbl, text="Poid du Produit(kg)", font=f3, bg=color_bg)
    self.lbl_weight.grid(row=0, column=2, sticky='w', padx=(100,0), pady=4) 
    self.ent_weight = Entry(self.frame_manager_lbl, width=18, bd=3, justify='center', font=f3)
    self.ent_weight.grid(row=0, column=3, padx=15, pady=4)

    self.lbl_width = Label(self.frame_manager_lbl, text="Largeur(mm)", font=f3, bg=color_bg)
    self.lbl_width.grid(row=1, column=0, sticky='w', padx=(70,15), pady=4) 
    self.ent_width = Entry(self.frame_manager_lbl, width=18, bd=3, justify='center', font=f3)
    self.ent_width.grid(row=1, column=1, pady=4)
    self.lbl_length = Label(self.frame_manager_lbl, text="Longueur(mm)", font=f3, bg=color_bg)
    self.lbl_length.grid(row=1, column=2, sticky='w', padx=(100,0), pady=4) 
    self.ent_length = Entry(self.frame_manager_lbl, width=18, bd=3, justify='center', font=f3)
    self.ent_length.grid(row=1, column=3, pady=4)

    self.lbl_weight_pack = Label(self.frame_manager_lbl, text="Poid Emballage(kg)", font=f3, bg=color_bg)
    self.lbl_weight_pack.grid(row=2, column=0, sticky='w', padx=(70,15), pady=4) 
    self.ent_weight_pack = Entry(self.frame_manager_lbl, width=18, bd=3, justify='center', font=f3)
    self.ent_weight_pack.grid(row=2, column=1, pady=4)
    self.lbl_weight_sac = Label(self.frame_manager_lbl, text="Poid Sac(kg)", font=f3, bg=color_bg)
    self.lbl_weight_sac.grid(row=2, column=2, sticky='w', padx=(100,0), pady=4) 
    self.ent_weight_sac = Entry(self.frame_manager_lbl, width=18, bd=3, justify='center', font=f3)
    self.ent_weight_sac.grid(row=2, column=3, pady=4)

    self.lbl_quantity = Label(self.frame_manager_lbl, text="Quantité(pcs)", font=f3, bg=color_bg)
    self.lbl_quantity.grid(row=3, column=0, sticky='w', padx=(70,15), pady=4) 
    self.ent_quantity = Entry(self.frame_manager_lbl, width=18, bd=3, justify='center', font=f3)
    self.ent_quantity.grid(row=3, column=1, pady=4)

    self.lbl_poid_demi = Label(self.frame_manager_lbl, text="Poid 0.5 metre(g)", font=f3, bg=color_bg)
    self.lbl_poid_demi.grid(row=4, column=0, sticky='w', padx=(70,15), pady=(4,0)) 
    self.ent_poid_demi = Entry(self.frame_manager_lbl, width=18, bd=3, justify='center',\
        font=f3, state= 'disabled')
    self.ent_poid_demi.grid(row=4, column=1, pady=(4,0))
    self.lbl_thickness = Label(self.frame_manager_lbl, text="épaisseur(μm)", font=f3, bg=color_bg)
    self.lbl_thickness.grid(row=4, column=2, sticky='w', padx=(100,0), pady=(4,0)) 
    self.ent_thickness = Entry(self.frame_manager_lbl, width=18, bd=3, justify='center',\
        font=f3, state= 'disabled')
    self.ent_thickness.grid(row=4, column=3, pady=(4,0))

    # buttons for modificaiton================
    self.btn_add = Button(self.frame_manager_btn, text = "Ajouter", width=7, font=f3, bd=3)
    self.btn_add.grid(row=0, column=0, padx=20, pady=(10,0))

    self.btn_modif = Button(self.frame_manager_btn, text = "Modifier", width=7, font=f3, bd=3)
    self.btn_modif.grid(row=1, column=0, pady=10)

    self.btn_delete = Button(self.frame_manager_btn, text = "Supplimer", width=7, font=f3, bd=3)
    self.btn_delete.grid(row=2, column=0, pady=(0,60))
    #=========================================




    # Treeviews for making articles activated.================
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
    self.btn_arrow_right = Button(self.frame_article_btns, text=">>", font=f1, bd=3)
    self.btn_arrow_right.pack(pady=(0,5))
    self.btn_arrow_left = Button(self.frame_article_btns, text="<<", font=f1, bd=3)
    self.btn_arrow_left.pack()


    self.articles.grab_set()


    # database control
    def conn():
        connection = dbdb.connect()
        dbdb.create_tables(connection)

    def check_duplicated():
        


    def add_new():
        return





'''
    self.style_article_both = ttk.Style()
    # style for the body of the treeview.
    self.style_article_both.configure(style="mystyle3.Treeview", rowheight=10, font=f2)
    self.style_article_both.map("mystyle3.Treeview", background=[('selected', 'blue')])
    self.style_article_both.theme_use("default")

    self.tree_articles_left = ttk.Treeview(self.frame_article_left, height=15,\
        style="mystyle3.Treeview", selectmode='browse')

    self.tree_articles_right = ttk.Treeview(self.frame_article_right, height=15,\
        style="mystyle3.Treeview", selectmode='browse')

    self.tree_articles_left.pack()
    self.tree_articles_right.pack()

'''