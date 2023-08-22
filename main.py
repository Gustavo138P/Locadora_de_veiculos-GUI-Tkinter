from tkinter import *
from tkinter.font import Font
from funcoes import *

janela = Tk()
class interface():
    def __init__(self):
        self.janela = janela
        self.pagina_Inicial()
        self.frames_PgI()
        self.widgets_PgI()
        janela.mainloop()
    def pagina_Inicial(self):
        self.janela.title('PÁGINA INICIAL')
        self.janela.minsize(width=300, height=300)
        self.janela.config(background='#008B8B')
        self.janela.maxsize(width=400, height=400)
    def pagina_Login(self):
        self.pg2 = Toplevel()
        self.pg2.title('LOGIN')
        self.pg2.resizable(True, True)
        self.pg2.minsize(width=300, height=300)
        self.pg2.config(background='#008B8B')
        self.pg2.maxsize(width=400, height=400)
        self.pg2.transient(self.janela)
        self.pg2.focus_force()
        self.pg2.grab_set()
        self.frames_Login()
        self.widgets_Login()
    def pagina_Cadastrar(self):
        self.pg3 = Toplevel()
        self.pg3.title('CADASTRAR')
        self.pg3.minsize(width=300, height=300)
        self.pg3.config(background='#008B8B')
        self.pg3.maxsize(width=400, height=400)
        self.pg3.transient(self.janela)
        self.pg3.focus_force()
        self.pg3.grab_set()
        self.frames_Cadastrar()
        self.widgets_Cadastrar()
    def pagina_Home(self):
        self.pg4 = Toplevel()
        self.pg4.title('HOME')
        self.pg4.minsize(width=300, height=300)
        self.pg4.config(background='#008B8B')
        self.pg4.maxsize(width=400, height=400)
        self.pg4.transient(self.pg2)
        self.pg4.focus_force()
        self.pg4.grab_set()
        self.frames_Home()
        self.widgets_Home()
    def cadastrar_User(self):
        self.user_name = self.entradaUsuario.get()
        self.complet_name = self.entrada_cNome.get()
        self.senha_user = self.entrada_cSenha.get()
        cadastro(self.user_name, self.complet_name, self.senha_user, 'usuarios.txt')
    def logar(self):
        self.tentativa = 0
        self.nome_usuario = self.entradaNome.get()
        self.senha_usuario = self.entradaSenha.get()
        usuarios = verificar_arquivo('usuarios.txt')
        if usuarios:
            self.arquivo = open('usuarios.txt', 'r')
            for linha in self.arquivo:
                atual_linha = linha.split(sep="#")
                if atual_linha[0] == self.nome_usuario:
                    if atual_linha[1] == self.senha_usuario:
                        self.pagina_Home()
                        self.tentativa+=1
                        break
            if self.tentativa == 0:
                self.senha_errada = Label(self.frame2Login, background='#008B8B', text='Usuario ou senha incorretos')
                self.senha_errada.place(relx=0.001, rely=0.8, relheight=0.2, relwidth=0.9)
    def frames_PgI(self):
        self.frame1 = Frame(self.janela, background='#008B8B')
        self.frame1.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.4)

        self.frame2 = Frame(self.janela, background='#008B8B')
        self.frame2.place(relx=0.05, rely=0.5, relwidth=0.9, relheight=0.4)
    def widgets_PgI(self):
        self.fonte = Font(family="Arial Black", size=20)
        self.logo = Label(self.frame1, text='GUSTAVO\nLOCADORA', background='#008B8B', font=self.fonte)
        self.logo.place(relx=0.15, rely=0.15, relheight=0.7, relwidth=0.7)

        self.fonte = Font(family="Arial Black", size=10)
        self.login = Button(self.frame2, text='LOGIN', bd=4, background='#FF4500', font=self.fonte, command=self.pagina_Login)
        self.login.place(relx=0.25, rely=0.2, relheight=0.2, relwidth=0.5)

        self.cadastrar = Button(self.frame2, text='CADASTRAR', bd=4, background='#FF4500', font=self.fonte, command=self.pagina_Cadastrar)
        self.cadastrar.place(relx=0.25, rely=0.4, relheight=0.2, relwidth=0.5)
    def frames_Login(self):
        self.frame1Login = Frame(self.pg2, background='#008B8B')
        self.frame1Login.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.15)

        self.frame2Login = Frame(self.pg2, background='#008B8B')
        self.frame2Login.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.49)

        self.frame3Login = Frame(self.pg2, background='#008B8B')
        self.frame3Login.place(relx=0.05, rely=0.7, relwidth=0.9, relheight=0.15)
    def widgets_Login(self):
        self.fonte = Font(family="Arial Black", size=15)
        self.fonte2 = Font(family="Arial Black", size=25)
        self.fonte3 = Font(family="Arial Black", size=9)

        self.loginTitulo = Label(self.frame1Login, text='LOGIN', background='#008B8B', font=self.fonte2)
        self.loginTitulo.place(relx=0.15, rely=0.001, relheight=0.9, relwidth=0.7)

        self.loginNome = Label(self.frame2Login, text='NOME:', background='#008B8B', font=self.fonte3)
        self.loginNome.place(relx=0.001, rely=0.03, relheight=0.2, relwidth=0.2)

        self.entradaNome = Entry(self.frame2Login, background='white')
        self.entradaNome.place(relx=0.001, rely=0.2, relheight=0.2, relwidth=0.9)

        self.loginSenha = Label(self.frame2Login, text='SENHA:', background='#008B8B', font=self.fonte3)
        self.loginSenha.place(relx=0.001, rely=0.4, relheight=0.2, relwidth=0.2)

        self.entradaSenha = Entry(self.frame2Login, background='white', show="*")
        self.entradaSenha.place(relx=0.001, rely=0.6, relheight=0.2, relwidth=0.9)

        self.confirmarLogin = Button(self.frame3Login, text='CONFIRMAR', bd=4, background='#FF4500', font=self.fonte, command=self.logar)
        self.confirmarLogin.place(relx=0.4, rely=0.001, relheight=0.7, relwidth=0.55)
    def frames_Cadastrar(self):
        self.frame1Cadastrar = Frame(self.pg3, background='#008B8B')
        self.frame1Cadastrar.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.15)

        self.frame2Cadastrar = Frame(self.pg3, background='#008B8B')
        self.frame2Cadastrar.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.6)

        self.frame3Cadastrar = Frame(self.pg3, background='#008B8B')
        self.frame3Cadastrar.place(relx=0.05, rely=0.8, relwidth=0.9, relheight=0.15)
    def widgets_Cadastrar(self):
        self.fonte = Font(family="Arial Black", size=15)
        self.fonte2 = Font(family="Arial Black", size=20)
        self.fonte3 = Font(family="Arial Black", size=9)

        self.cadastrarTitulo = Label(self.frame1Cadastrar, text='CADASTRAR', background='#008B8B', font=self.fonte2)
        self.cadastrarTitulo.place(relx=0.15, rely=0.001, relheight=0.9, relwidth=0.7)

        self.cadastrarUsuario = Label(self.frame2Cadastrar, text='NOME DE USUÁRIO:', background='#008B8B', font=self.fonte3)
        self.cadastrarUsuario.place(relx=0.001, rely=0.001, relheight=0.1, relwidth=0.5)

        self.entradaUsuario = Entry(self.frame2Cadastrar, background='white')
        self.entradaUsuario.place(relx=0.001, rely=0.08, relheight=0.14, relwidth=0.9)

        self.cadastrarNome = Label(self.frame2Cadastrar, text='NOME COMPLETO:', background='#008B8B', font=self.fonte3)
        self.cadastrarNome.place(relx=0.001, rely=0.22, relheight=0.1, relwidth=0.5)

        self.entrada_cNome = Entry(self.frame2Cadastrar, background='white')
        self.entrada_cNome.place(relx=0.001, rely=0.31, relheight=0.14, relwidth=0.9)

        self.cadastrarSenha = Label(self.frame2Cadastrar, text='SENHA:', background='#008B8B', font=self.fonte3)
        self.cadastrarSenha.place(relx=0.001, rely=0.45, relheight=0.1, relwidth=0.2)

        self.entrada_cSenha = Entry(self.frame2Cadastrar, background='white')
        self.entrada_cSenha.place(relx=0.001, rely=0.54, relheight=0.14, relwidth=0.9)

        self.cadastrar_crSenha = Label(self.frame2Cadastrar, text='REPETIR SENHA:', background='#008B8B', font=self.fonte3)
        self.cadastrar_crSenha.place(relx=0.001, rely=0.68, relheight=0.1, relwidth=0.5)

        self.entrada_crSenha = Entry(self.frame2Cadastrar, background='white')
        self.entrada_crSenha.place(relx=0.001, rely=0.77, relheight=0.14, relwidth=0.9)

        self.c_Confirmar = Button(self.frame3Cadastrar, text='CONFIRMAR', bd=4, background='#FF4500', font=self.fonte, command=self.cadastrar_User)
        self.c_Confirmar.place(relx=0.4, rely=0.001, relheight=0.7, relwidth=0.55)
    def frames_Home(self):
        self.frame1Home = Frame(self.pg4, background='#008B8B')
        self.frame1Home.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.15)

        self.frame2Home = Frame(self.pg4, background='white')
        self.frame2Home.place(relx=0.05, rely=0.25, relwidth=0.9, relheight=0.6)
    def widgets_Home(self):
        self.fonte = Font(family="Arial Black", size=15)
        self.fonte2 = Font(family="Arial Black", size=20)
        self.fonte3 = Font(family="Arial Black", size=9)

        self.HomeTitulo = Label(self.frame1Home, text='HOME', background='#008B8B', font=self.fonte2)
        self.HomeTitulo.place(relx=0.15, rely=0.001, relheight=0.9, relwidth=0.7)

        self.HomeCadastrar = Button(self.frame2Home, text='CADASTRAR NOVO VEÍCULO', bd=4, background='#FF4500', font=self.fonte3)
        self.HomeCadastrar.place(relx=0.001, rely=0.001, relheight=0.2, relwidth=1)

        self.HomeListar = Button(self.frame2Home, text='LISTAR VEÍCULOS CADASTRADOS', bd=4, background='#FF4500', font=self.fonte3)
        self.HomeListar.place(relx=0.001, rely=0.2, relheight=0.2, relwidth=1)

        self.HomeAtualizar = Button(self.frame2Home, text='ATUALIZAR VEÍCULO CADASTRADO', bd=4, background='#FF4500', font=self.fonte3)
        self.HomeAtualizar.place(relx=0.001, rely=0.4, relheight=0.2, relwidth=1)

        self.HomeExcluir = Button(self.frame2Home, text='EXCLUIR VEÍCULO', bd=4, background='#FF4500', font=self.fonte3)
        self.HomeExcluir.place(relx=0.001, rely=0.6, relheight=0.2, relwidth=1)

        self.HomeRegistrar = Button(self.frame2Home, text='REGISTRAR ALUGUEL', bd=4, background='#FF4500', font=self.fonte3)
        self.HomeRegistrar.place(relx=0.001, rely=0.8, relheight=0.2, relwidth=1)



interface()