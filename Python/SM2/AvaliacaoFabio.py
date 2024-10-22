from tkinter import *
import os

c = os.path.dirname(__file__)
nomeArquivo = c+"\\nomes.txt"

def vazio():
    for widget in interface.winfo_children():
        if widget.winfo_rootx() > 0 and widget.winfo_rooty() > BarraDeMenus.winfo_rooty():
            widget.destroy()
    
    vazio = Label(interface, text="EM ANDAMENTO", font=("Arial", 16, "bold"), background="#dde")
    vazio.place(x=150, y=100)

def SalvarDados():
    arquivo = open(nomeArquivo, "a")
    arquivo.write("Nome....:%s" % VNome.get())
    arquivo.write("\nTelefone:%s" % VFone.get())
    arquivo.write("\nE-mail..:%s" % VEmail.get())
    arquivo.write("\nOBS.....:%s" % Vobs.get("1.0",END))
    arquivo.write("\n\n")
    arquivo.close()

def InterfaceNovo():
    for widget in interface.winfo_children():
        if widget.winfo_rootx() > 0 and widget.winfo_rooty() > BarraDeMenus.winfo_rooty():
            widget.destroy()

    global VNome, VFone, VEmail, Vobs

    Label(interface, text="Nome", background="#dde", foreground="#009", anchor=W).place(x=10,y=10, width=100, height=20)
    VNome = Entry(interface)
    VNome.place(x=10, y=30, width=200, height=20)

    Label(interface, text="Telefone", background="#dde", foreground="#009", anchor=W).place(x=10,y=60, width=100, height=20)
    VFone = Entry(interface)
    VFone.place(x=10, y=80, width=100, height=20)

    Label(interface, text="E-mail", background="#dde", foreground="#009", anchor=W).place(x=10,y=110, width=100, height=20)
    VEmail = Entry(interface)
    VEmail.place(x=10, y=130, width=300, height=20)

    Label(interface, text="OBS", background="#dde", foreground="#009", anchor=W).place(x=10,y=160, width=100, height=20)
    Vobs = Text(interface)
    Vobs.place(x=10, y=180, width=300, height=80)

    Button(interface, text="Salvar", command=SalvarDados).place(x=10, y=270, width=100, height=20)
        
def DadosProgramador():
    for widget in interface.winfo_children():
        if widget.winfo_rootx() > 0 and widget.winfo_rooty() > BarraDeMenus.winfo_rooty():
            widget.destroy()

    titulo = Label(interface, text="DADOS DO PROGRAMADOR", font=("Arial", 16, "bold"), background="#dde")
    titulo.place(x=100, y=10)

    label_nome = Label(interface, text="Nome: Raimundo", anchor=W, font=("Arial", 12), background="#dde")
    label_nome.place(x=10, y=100)

    label_idade = Label(interface, text="Idade: 20", font=("Arial", 12), background="#dde")
    label_idade.place(x=10, y=120)


    label_assinatura = Label(interface, text="By Resg", font=("Arial", 10), background="#dde")
    label_assinatura.place(x=440, y=270)
    

interface = Tk()
interface.title("Avaliação do Prof.Fabio")
interface.geometry("500x300")
interface.configure(background="#dde")

BarraDeMenus = Menu(interface)
MenuContatos = Menu(BarraDeMenus, tearoff=0)
MenuContatos.add_command(label="Novo", command=InterfaceNovo)
MenuContatos.add_command(label="Pesquisar", command=vazio)
MenuContatos.add_command(label="Deletar", command=vazio)
MenuContatos.add_separator()
MenuContatos.add_command(label="Fechar", command=interface.quit)
BarraDeMenus.add_cascade(label="Contatos",menu=MenuContatos)

MenuManutencao = Menu(BarraDeMenus, tearoff=0)
MenuManutencao.add_command(label="Banco de Dados", command=vazio)
BarraDeMenus.add_cascade(label="Manuntenção",menu=MenuManutencao)

MenuSobre = Menu(BarraDeMenus, tearoff=0)
MenuSobre.add_command(label="Avaliação do Prof.Fabio", command=vazio)
BarraDeMenus.add_cascade(label="Sobre",menu=MenuSobre)

MenuRelatorio = Menu(BarraDeMenus, tearoff=0)
MenuRelatorio.add_command(label="Relatório 1", command=vazio)
MenuRelatorio.add_command(label="Relatório 2", command=vazio)
MenuRelatorio.add_command(label="Relatório 3", command=vazio)
BarraDeMenus.add_cascade(label="Relatórios",menu=MenuRelatorio)

MenuInfo = Menu(BarraDeMenus, tearoff=0)
MenuInfo.add_command(label="Programa", command=vazio)
MenuInfo.add_command(label="Programador", command=DadosProgramador)
MenuInfo.add_command(label="Sair", command=interface.quit)
BarraDeMenus.add_cascade(label="Relatórios",menu=MenuInfo)


interface.config(menu=BarraDeMenus)

interface.mainloop()
