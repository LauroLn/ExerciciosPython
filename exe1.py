from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import ttk
import tkinter as tk
import sys
import os
import pymongo
from tkinter import messagebox


sld7 = pymongo.MongoClient("mongodb://localhost:27017/")
db=sld7["sld7"]
collection = db["cadastro"]


Tela = Tk()

Tela.title("Exercicio-1")

Tela.geometry("800x400")

Tela.resizable(False, False)

Tela.configure(bg="#E0FFFF")

pasta_imgs = "Documentos"

fonte = 12

def imagem():
    caminho = filedialog.askopenfilename(initialdir=pasta_imgs, title="Escolher a Imagem", filetypes=(("Arquivos de Imagem","*.jpg; *.jpeg; *.png; *.jfif;"),("Todos os arquivos","*.*")))
    img_pil = Image.open(caminho)
    largura, altura = img_pil.size
    if largura > 85:
        proporcao = largura / 155
        nova_altura = int(altura/proporcao)
        img_pil = img_pil.resize((152, nova_altura))
    img_tk = ImageTk.PhotoImage(img_pil)
    lbl_img = Label(Tela, image=img_tk)
    lbl_img.image = img_tk
    lbl_img.place(x=20, y=20)


def sair():
    sys.exit()

def salvar():
    cod = txt_cod.get()
    nome = txt_nome.get()
    idade= txt_idade.get()
    peso = txt_peso.get()
    cid = cidade.get()
    nasc = txt_nasc.get()
    altura = txt_altura.get()
    sexo = var.get()
    cadastro = txt_cad.get()

    txt_cod.delete(0, tk.END)
    txt_nome.delete(0, tk.END)
    txt_idade.delete(0, tk.END)
    txt_peso.delete(0, tk.END)
    txt_nasc.delete(0, tk.END)
    txt_altura.delete(0, tk.END)
    txt_cad.delete(0, tk.END)

    cadastro = {"codigo": cod, "nome": nome, "idade": idade, "peso": peso, "cidade": cid, "nascimento": nasc, "altura": altura, "sexo":sexo, "cadastro": cadastro}
    collection.insert_one(cadastro)

    messagebox.showinfo("Menssagem", "Cadastrado com Sucesso")

def att():
    cod = txt_cod.get()
    nome = txt_nome.get()
    idade= txt_idade.get()
    peso = txt_peso.get()
    cid = cidade.get()
    nasc = txt_nasc.get()
    altura = txt_altura.get()
    sexo = var.get()
    cadastro = txt_cad.get()

    collection.update_one({"codigo": cod }, {"$set":{"nome": nome, "idade": idade, "peso": peso, "cidade": cid, "nascimento": nasc, "altura": altura, "sexo":sexo, "cadastro": cadastro}})

    txt_cod.delete(0, tk.END)
    txt_nome.delete(0, tk.END)
    txt_idade.delete(0, tk.END)
    txt_peso.delete(0, tk.END)
    txt_nasc.delete(0, tk.END)
    txt_altura.delete(0, tk.END)
    txt_cad.delete(0, tk.END)

    messagebox.showinfo("Menssagem", "Cadastrado Atualizado com sucesso")

def excluir():
    cod = txt_cod.get()
    
    collection.delete_one({"codigo": cod})
    messagebox.showinfo("Menssagem", "Cadastrado excluido com sucesso")

    txt_cod.delete(0, tk.END)
    txt_nome.delete(0, tk.END)
    txt_idade.delete(0, tk.END)
    txt_peso.delete(0, tk.END)
    txt_nasc.delete(0, tk.END)
    txt_altura.delete(0, tk.END)
    txt_cad.delete(0, tk.END)

def consulta():
    cod = txt_cod.get()
    resultado = collection.find_one({"codigo": cod})

    if resultado:
     txt_cod.insert(END, f"{resultado["codigo"]}\n")
     txt_nome.insert(END, f"{resultado["nome"]}\n")
     txt_idade.insert(END, f"{resultado["idade"]}\n")
     txt_peso.insert(END, f"{resultado["peso"]}\n")
     txt_nasc.insert(END, f"{resultado["nascimento"]}\n")
     txt_altura.insert(END, f"{resultado["altura"]}\n")
     txt_cad.insert(END, f"{resultado["cadastro"]}\n")
    else:
        messagebox.showinfo("Menssagem", "Cadastrado consultado com sucesso")






btn_img = Button(Tela, text="Escolha uma imagem", command=imagem)
btn_img.place(x=40, y=140)

lbl_cod = Label(Tela, text="Codigo: ",bg="#E0FFFF", font=("Arial",fonte)).place(x=180,y=10)
txt_cod = Entry(Tela, width=7)
txt_cod.place(x=245,y=12)

lbl_nome = Label(Tela, text="Nome: ",bg="#E0FFFF", font=("Arial",fonte)).place(x=180,y=38)
txt_nome = Entry(Tela,width=46)
txt_nome.place(x=245,y=40)

lbl_idade = Label(Tela, text="Idade: ",bg="#E0FFFF", font=("Arial",fonte)).place(x=545,y=38)
txt_idade = Entry(Tela,width=7)
txt_idade.place(x=605,y=40)

lbl_sexo = Label(Tela, text="Sexo: ", bg="#e0ffff", font=("Arial",fonte)).place(x=180,y=78)

var = StringVar()
var.set("M")

radio_m = Radiobutton(Tela, text="M", variable=var, value="M", bg="#e0ffff").place(x=240,y=80)
radio_m = Radiobutton(Tela, text="F", variable=var, value="F", bg="#e0ffff").place(x=290,y=80)

lbl_altura = Label(Tela, text="Altura: ", bg="#e0ffff", font=("Arial",fonte)).place(x=330,y=80)
txt_altura = Entry(Tela,width=7)
txt_altura.place(x=380,y=82)

lbl_peso = Label(Tela, text="Peso: ", bg="#e0ffff", font=("Arial",fonte)).place(x=430,y=80)
txt_peso = Entry(Tela,width=7)
txt_peso.place(x=480,y=82)

lbl_cidade = Label(Tela, text="Cidade: ", bg="#e0ffff", font=("Arial",fonte)).place(x=535,y=82)

cidade = ttk.Combobox(Tela)
cidade['values']=("Jacupiranga","Registro","Iguape","Pariquera","Cananeia","Cajati")
cidade.current(1)
cidade.place(x=605,y=82)

lbl_nasc = Label(Tela, text="Data nascimento: ", bg="#e0ffff", font=("Arial",fonte)).place(x=180,y=110)
txt_nasc = Entry(Tela,width=16)
txt_nasc.place(x=310,y=112)

lbl_cad = Label(Tela, text="Data cadastro: ", bg="#e0ffff", font=("Arial",fonte)).place(x=180,y=140)
txt_cad = Entry(Tela,width=16)
txt_cad.place(x=310,y=142)

lbl_att = Label(Tela, text="Data atualização: ", bg="#e0ffff", font=("Arial",fonte)).place(x=420,y=110)
txt_att = Entry(Tela,width=16)
txt_att.place(x=550,y=112)

lbl_desc = Label(Tela, text="Descrição: ", bg="#e0ffff", font=("Arial",fonte)).place(x=180,y=170)
txt_desc = Entry(Tela,width=16)
txt_desc.place(x=310,y=172)

foto_salvar = PhotoImage(file = r"C:\Users\fatec-dsm3\Desktop\Aula\Python-tec-prog\slide 6\imgs\salvar.png")
foto_excluir = PhotoImage(file = r"C:\Users\fatec-dsm3\Desktop\Aula\Python-tec-prog\slide 6\imgs\excluir.png")
foto_editar = PhotoImage(file = r"C:\Users\fatec-dsm3\Desktop\Aula\Python-tec-prog\slide 6\imgs\alterar.png")
foto_consultar = PhotoImage(file = r"C:\Users\fatec-dsm3\Desktop\Aula\Python-tec-prog\slide 6\imgs\consultar.png")



btn_salvar = Button(Tela, text="Salvar", image= foto_salvar, compound=TOP, command=salvar).place(x=150,y=200)
btn_excluir = Button(Tela, text="excluir", image= foto_excluir, compound=TOP, command=excluir).place(x=200,y=200)
btn_editar = Button(Tela, text="Editar", image= foto_editar, compound=TOP,command=att).place(x=250,y=200)
btn_consultar = Button(Tela, text="Consultar", image= foto_consultar, compound=TOP, command=consulta).place(x=300,y=200)






Tela.mainloop()