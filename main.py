from tkinter import *
from tkinter.font import Font
from funcoes import *
from tkinter import ttk

janela = Tk()


class interface():
    def __init__(self):
        self.valor_locacao = 0
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

    def pagina_Cadastrar_veiculos(self):
        self.pg5 = Toplevel()
        self.pg5.title('CADASTRAR VEÍCULO')
        self.pg5.minsize(width=300, height=300)
        self.pg5.config(background='#008B8B')
        self.pg5.maxsize(width=400, height=400)
        self.pg5.transient(self.pg4)
        self.pg5.focus_force()
        self.pg5.grab_set()
        self.frames_Cadastrar_veiculos()
        self.widgets_Cadastrar_veiculos()

    def pagina_Listar_Veiculos(self):
        self.pg6 = Toplevel()
        self.pg6.title('LISTAR VEÍCULOS')
        self.pg6.minsize(width=500, height=500)
        self.pg6.config(background='#008B8B')
        self.pg6.resizable(False, False)
        self.pg6.transient(self.pg4)
        self.pg6.focus_force()
        self.pg6.grab_set()
        self.frames_Listar_veiculos()
        self.widgets_Listar_veiculos()

    def pagina_Atualizar_Veiculos(self):
        self.pg7 = Toplevel()
        self.pg7.title('ATUALIZAR VEÍCULO')
        self.pg7.minsize(width=300, height=300)
        self.pg7.config(background='#008B8B')
        self.pg7.maxsize(width=400, height=400)
        self.pg7.transient(self.pg4)
        self.pg7.focus_force()
        self.pg7.grab_set()
        self.frames_Atualizar_veiculos()
        self.widgets_Atualizar_veiculos()

    def pagina_excluir_veiculos(self):
        self.pg8 = Toplevel()
        self.pg8.title('EXCLUIR VEÍCULO')
        self.pg8.minsize(width=300, height=100)
        self.pg8.config(background='#008B8B')
        self.pg8.maxsize(width=400, height=400)
        self.pg8.transient(self.pg4)
        self.pg8.focus_force()
        self.pg8.grab_set()
        self.frames_Excluir_veiculos()
        self.widgets_Excluir_veiculos()

    def pagina_locacao(self):
        self.pg9 = Toplevel()
        self.pg9.title('REGISTRAR LOCAÇÃO')
        self.pg9.minsize(width=500, height=400)
        self.pg9.resizable(False, False)
        self.pg9.config(background='#008B8B')
        self.pg9.transient(self.pg4)
        self.pg9.focus_force()
        self.pg9.grab_set()
        self.frames_Registrar_locacao()
        self.widgets_Registrar_locacao()

    def cadastrar_User(self):
        self.user_name = self.entradaUsuario.get()
        self.complet_name = self.entrada_cNome.get()
        self.senha_user = self.entrada_cSenha.get()
        cadastro_usuarios(self.user_name, self.complet_name, self.senha_user, 'usuarios.txt')
        limpar_texto(self.entradaUsuario)
        limpar_texto(self.entrada_cNome)
        limpar_texto(self.entrada_cSenha)
        limpar_texto(self.entrada_crSenha)

    def logar(self):
        self.tentativa = 0
        self.nome_usuario = self.entradaNome.get()
        self.senha_usuario = self.entradaSenha.get()
        limpar_texto(self.entradaNome)
        limpar_texto(self.entradaSenha)
        usuarios = verificar_usuarios('usuarios.txt')
        if usuarios:
            self.arquivo = open('usuarios.txt', 'r')
            for linha in self.arquivo:
                atual_linha = linha.split(sep="#")
                if atual_linha[0] == self.nome_usuario:
                    if atual_linha[1] == self.senha_usuario:
                        self.pagina_Home()
                        self.tentativa += 1
                        break
            if self.tentativa == 0:
                self.senha_errada = Label(self.frame2Login, background='#008B8B', text='Usuario ou senha incorretos')
                self.senha_errada.place(relx=0.001, rely=0.8, relheight=0.2, relwidth=0.9)

    def cadastrar_Veiculo(self):
        self.Modelo= self.entradaModelo.get()
        self.Montadora = self.entradaMontadora.get()
        self.Tipo = self.entradaClassificacao.get()
        self.valor = self.entradaValor.get()
        self.Modelo = self.Modelo.upper()
        self.Montadora = self.Montadora.upper()
        self.Tipo = self.Tipo.upper()
        self.valor = self.valor.upper()
        self.nome_arquivo = 'veiculos.txt'
        cadastrar_veiculos(self.Modelo, self.Montadora, self.Tipo, self.valor, self.nome_arquivo)
        limpar_texto(self.entradaModelo)
        limpar_texto(self.entradaMontadora)
        limpar_texto(self.entradaClassificacao)
        limpar_texto(self.entradaValor)

    def listar_veiculos(self):
        opcao = self.selecao.get()
        lista = []
        listar(opcao, "veiculos.txt", lista)

        self.planilha.delete(*self.planilha.get_children())
        for (modelo, montadora, tipo, valor) in lista:
            self.planilha.insert("", "end", values=(modelo, montadora, tipo, valor))

    def atualizar_veiculo(self):
        opcao = self.selecao_veiculo.get()
        opcao2 = self.selecao_veiculo2.get()
        novo = self.novo_valor.get()
        novo = novo.upper()
        atualizar_v('veiculos.txt', opcao, opcao2, novo)
        limpar_texto(self.novo_valor)
        limpar_texto(self.selecao_veiculo)
        limpar_texto(self.selecao_veiculo2)

    def Excluir_veiculos(self):
        opcao = self.Excluir_veiculo.get()
        exclusao = Excluir_v('veiculos.txt', opcao)

        if exclusao == 1:
            self.pg8.destroy()

    def calculo_valor(self):

        diarias_str = self.diarias_cliente.get()

        if diarias_str.isdigit():
            diarias = int(diarias_str)
            valor_base = obter_valor_base('veiculos.txt', self.selecionar_veiculo_locacao.get())
            self.valor_locacao = diarias * valor_base
            self.imprimir.set(str(self.valor_locacao))
        else:
            self.imprimir.set("Valor diárias inválido")

    def locar_veiculo(self):
        diarias_str = self.diarias_cliente.get()

        if diarias_str.isdigit():
            diarias = int(diarias_str)
            g_diarias = diarias_str
            opcao = self.selecionar_veiculo_locacao.get()
            valor_base = obter_valor_base('veiculos.txt', self.selecionar_veiculo_locacao.get())
            valor = diarias * valor_base
            g_valor = str(valor)
            registrar_Locacao('locacao.txt', opcao, self.nome_cliente.get(), self.cpf_cliente.get(), self.rg_cliente.get(), self.telefone_cliente.get(), self.email_cliente.get(), g_valor, g_diarias, self.selecionar_pagamento.get())
            self.pg9.destroy()
        else:
            self.imprimir.set("Valor diárias inválido")

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
        self.cadastrarNome.place(relx=0.001, rely=0.22, relheight=0.1, relwidth=0.45)

        self.entrada_cNome = Entry(self.frame2Cadastrar, background='white')
        self.entrada_cNome.place(relx=0.001, rely=0.31, relheight=0.14, relwidth=0.9)

        self.cadastrarSenha = Label(self.frame2Cadastrar, text='SENHA:', background='#008B8B', font=self.fonte3)
        self.cadastrarSenha.place(relx=0.001, rely=0.45, relheight=0.1, relwidth=0.2)

        self.entrada_cSenha = Entry(self.frame2Cadastrar, background='white')
        self.entrada_cSenha.place(relx=0.001, rely=0.54, relheight=0.14, relwidth=0.9)

        self.cadastrar_crSenha = Label(self.frame2Cadastrar, text='REPETIR SENHA:', background='#008B8B', font=self.fonte3)
        self.cadastrar_crSenha.place(relx=0.001, rely=0.68, relheight=0.1, relwidth=0.4)

        self.entrada_crSenha = Entry(self.frame2Cadastrar, background='white')
        self.entrada_crSenha.place(relx=0.001, rely=0.77, relheight=0.14, relwidth=0.9)

        self.c_Confirmar = Button(self.frame3Cadastrar, text='CONFIRMAR', bd=4, background='#FF4500', font=self.fonte, command=self.cadastrar_User)
        self.c_Confirmar.place(relx=0.4, rely=0.001, relheight=0.7, relwidth=0.55)

    def frames_Home(self):
        self.frame1Home = Frame(self.pg4, background='#008B8B')
        self.frame1Home.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.15)

        self.frame2Home = Frame(self.pg4, background='#008B8B')
        self.frame2Home.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.9)

    def widgets_Home(self):
        self.fonte = Font(family="Arial Black", size=15)
        self.fonte2 = Font(family="Arial Black", size=20)
        self.fonte3 = Font(family="Arial Black", size=9)

        self.HomeTitulo = Label(self.frame1Home, text='HOME', background='#008B8B', font=self.fonte2)
        self.HomeTitulo.place(relx=0.15, rely=0.001, relheight=0.9, relwidth=0.7)

        self.HomeCadastrar = Button(self.frame2Home, text='CADASTRAR NOVO VEÍCULO', bd=4, background='#FF4500', font=self.fonte3, command=self.pagina_Cadastrar_veiculos)
        self.HomeCadastrar.place(relx=0.001, rely=0.001, relheight=0.12, relwidth=1)

        self.HomeListar = Button(self.frame2Home, text='LISTAR VEÍCULOS CADASTRADOS', bd=4, background='#FF4500', font=self.fonte3, command=self.pagina_Listar_Veiculos)
        self.HomeListar.place(relx=0.001, rely=0.121, relheight=0.12, relwidth=1)

        self.HomeAtualizar = Button(self.frame2Home, text='ATUALIZAR VEÍCULO CADASTRADO', bd=4, background='#FF4500', font=self.fonte3, command=self.pagina_Atualizar_Veiculos)
        self.HomeAtualizar.place(relx=0.001, rely=0.241, relheight=0.12, relwidth=1)

        self.HomeExcluir = Button(self.frame2Home, text='EXCLUIR VEÍCULO', bd=4, background='#FF4500', font=self.fonte3, command=self.pagina_excluir_veiculos)
        self.HomeExcluir.place(relx=0.001, rely=0.361, relheight=0.12, relwidth=1)

        self.HomeRegistrar = Button(self.frame2Home, text='REGISTRAR LOCAÇÃO', bd=4, background='#FF4500', font=self.fonte3, command=self.pagina_locacao)
        self.HomeRegistrar.place(relx=0.001, rely=0.481, relheight=0.12, relwidth=1)

        self.HomeListarLocacoes= Button(self.frame2Home, text='LISTAR LOCAÇÕES', bd=4, background='#FF4500', font=self.fonte3)
        self.HomeListarLocacoes.place(relx=0.001, rely=0.601, relheight=0.12, relwidth=1)

    def frames_Cadastrar_veiculos(self):
        self.frame1Cadastrar_veiculos = Frame(self.pg5, background='#008B8B')
        self.frame1Cadastrar_veiculos.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.75)

        self.frame2Cadastrar_veiculos = Frame(self.pg5, background='#008B8B')
        self.frame2Cadastrar_veiculos.place(relx=0.05, rely=0.8, relwidth=0.9, relheight=0.15)

    def widgets_Cadastrar_veiculos(self):
        self.fonte = Font(family="Arial Black", size=9)
        self.cadastrarVeiculo1 = Label(self.frame1Cadastrar_veiculos, text='MODELO:', background='#008B8B', font=self.fonte)
        self.cadastrarVeiculo1.place(relx=0.001, rely=0.001, relheight=0.1, relwidth=0.28)

        self.entradaModelo = Entry(self.frame1Cadastrar_veiculos, background='white')
        self.entradaModelo.place(relx=0.001, rely=0.08, relheight=0.14, relwidth=0.9)

        self.cadastrarVeiculo2 = Label(self.frame1Cadastrar_veiculos, text='MONTADORA:', background='#008B8B', font=self.fonte)
        self.cadastrarVeiculo2.place(relx=0.001, rely=0.22, relheight=0.1, relwidth=0.35)

        self.entradaMontadora = Entry(self.frame1Cadastrar_veiculos, background='white')
        self.entradaMontadora.place(relx=0.001, rely=0.31, relheight=0.14, relwidth=0.9)

        self.cadastrarVeiculo3 = Label(self.frame1Cadastrar_veiculos, text='TIPO:', background='#008B8B', font=self.fonte)
        self.cadastrarVeiculo3.place(relx=0.001, rely=0.45, relheight=0.1, relwidth=0.2)

        self.entradaClassificacao = Entry(self.frame1Cadastrar_veiculos, background='white')
        self.entradaClassificacao.place(relx=0.001, rely=0.54, relheight=0.14, relwidth=0.9)

        self.cadastrarVeiculo4 = Label(self.frame1Cadastrar_veiculos, text='VALOR:', background='#008B8B', font=self.fonte)
        self.cadastrarVeiculo4.place(relx=0.001, rely=0.68, relheight=0.1, relwidth=0.26)

        self.entradaValor = Entry(self.frame1Cadastrar_veiculos, background='white')
        self.entradaValor.place(relx=0.001, rely=0.77, relheight=0.14, relwidth=0.9)

        self.c_Confirmar = Button(self.frame2Cadastrar_veiculos, text='CADASTRAR', bd=4, background='#FF4500', font=self.fonte, command=self.cadastrar_Veiculo)
        self.c_Confirmar.place(relx=0.4, rely=0.001, relheight=0.7, relwidth=0.55)

    def frames_Listar_veiculos(self):
        self.frame1Listar_veiculos= Frame(self.pg6, background='#008B8B')
        self.frame1Listar_veiculos.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.2)

        self.frame2Listar_veiculos= Frame(self.pg6, background='#008B8B')
        self.frame2Listar_veiculos.place(relx=0.05, rely=0.25, relwidth=0.9, relheight=0.7)

    def widgets_Listar_veiculos(self):
        self.fonte = Font(family='Arial Black')
        self.fonte2 = Font(family="Arial Black", size=9)
        self.fonte3 = Font(family="Arial Black", size=15)

        self.selecionar_opcao = Label(self.frame1Listar_veiculos, background='#008B8B', font=self.fonte, text='Selecione a categoria do veículo:')
        self.selecionar_opcao.place(relx=0.001, rely=0.01, relheight=0.4, relwidth=0.6)

        opcoes = ['TODOS', 'HATCH', 'SEDÃ', 'ESPORTIVO', 'SUV', 'FAMILIAR']
        self.selecao = ttk.Combobox(self.frame1Listar_veiculos, values=opcoes)
        self.selecao.place(relx=0.002, rely=0.38, relheight=0.3, relwidth=0.5)

        self.confirmar_opcao = Button(self.frame1Listar_veiculos, text='CONFIRMAR', bd=4, background='#FF4500', font=self.fonte2, command=self.listar_veiculos)
        self.confirmar_opcao.place(relx=0.502, rely=0.38, relheight=0.3, relwidth=0.25)

        self.titulo_lista = Label(self.frame1Listar_veiculos, text='LISTA DE VEÍCULOS', background='#008B8B', font=self.fonte3)
        self.titulo_lista.place(relx=0.202, rely=0.68, relheight=0.3, relwidth=0.6)

        self.planilha = ttk.Treeview(self.frame2Listar_veiculos, columns=('MODELO', 'MONTADORA', 'TIPO', 'VALOR'), show='headings')
        self.planilha.column('MODELO', minwidth=0, width=50)
        self.planilha.column('MONTADORA', minwidth=0, width=50)
        self.planilha.column('TIPO', minwidth=0, width=50)
        self.planilha.column('VALOR', minwidth=0, width=50)
        self.planilha.heading('MODELO', text='MODELO')
        self.planilha.heading('MONTADORA', text='MONTADORA')
        self.planilha.heading('TIPO', text='TIPO')
        self.planilha.heading('VALOR', text='VALOR')
        self.planilha.place(relx=0.0001, rely=0.001, relheight=1, relwidth=0.95)

        self.Scroll_lista = Scrollbar(self.frame2Listar_veiculos, orient='vertical')
        self.planilha.configure(yscrollcommand=self.Scroll_lista.set)
        self.Scroll_lista.place(relx=0.9501, rely=0.001, relheight=1, relwidth=0.05)

    def frames_Atualizar_veiculos(self):
        self.frame1Atualizar_veiculos = Frame(self.pg7, background='#008B8B')
        self.frame1Atualizar_veiculos.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.4)

        self.frame2Atualizar_veiculos = Frame(self.pg7, background='#008B8B')
        self.frame2Atualizar_veiculos.place(relx=0.05, rely=0.45, relwidth=0.9, relheight=0.5)

    def widgets_Atualizar_veiculos(self):

        self.fonte = Font(family='Arial Black')

        self.texto_Atualiza_veiculo = Label(self.frame1Atualizar_veiculos, background='#008B8B', font=self.fonte, text='SELECIONE O VEÍCULO')
        self.texto_Atualiza_veiculo.place(relx=0, rely=0, relheight=0.3, relwidth=1)

        lista = []
        listar('TODOS', "veiculos.txt", lista)
        veiculos = [sublista[0] for sublista in lista]
        self.selecao_veiculo = ttk.Combobox(self.frame1Atualizar_veiculos, values=veiculos)
        self.selecao_veiculo.place(relx=0, rely=0.3, relheight=0.2, relwidth=1)

        self.texto2_Atualiza_veiculo = Label(self.frame1Atualizar_veiculos, background='#008B8B', font=self.fonte, text='SELECIONE O VALOR A ALTERAR')
        self.texto2_Atualiza_veiculo.place(relx=0, rely=0.5, relheight=0.3, relwidth=1)

        lista = ['MODELO', 'MONTADORA', 'TIPO', 'VALOR']
        self.selecao_veiculo2 = ttk.Combobox(self.frame1Atualizar_veiculos, values=lista)
        self.selecao_veiculo2.place(relx=0, rely=0.8, relheight=0.2, relwidth=1)

        self.texto3_Atualiza_veiculo = Label(self.frame2Atualizar_veiculos, background='#008B8B', font=self.fonte, text='DIGITE O NOVO VALOR')
        self.texto3_Atualiza_veiculo.place(relx=0, rely=0, relheight=0.3, relwidth=1)

        self.novo_valor = Entry(self.frame2Atualizar_veiculos)
        self.novo_valor.place(relx=0, rely=0.3, relheight=0.3, relwidth=1)

        self.botao_seleciona_veiculo = Button(self.frame2Atualizar_veiculos, text='ATUALIZAR VEÍCULO', bd=4, background='#FF4500', font=self.fonte, command=self.atualizar_veiculo)
        self.botao_seleciona_veiculo.place(relx=0.15, rely=0.6, relheight=0.3, relwidth=0.7)

    def frames_Excluir_veiculos(self):

        self.frame1Excluir_veiculos = Frame(self.pg8, background='#008B8B')
        self.frame1Excluir_veiculos.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.7)

        self.frame2EXcluir_veiculos = Frame(self.pg8, background='#008B8B')
        self.frame2EXcluir_veiculos.place(relx=0.05, rely=0.75, relwidth=0.9, relheight=0.2)


    def widgets_Excluir_veiculos(self):

        self.fonte = Font(family='Arial Black', size=15)

        self.texto_Excluir_veiculo = Label(self.frame1Excluir_veiculos, background='#008B8B', font=self.fonte, text='SELECIONE O VEÍCULO')
        self.texto_Excluir_veiculo.place(relx=0, rely=0.1, relheight=0.4, relwidth=1)

        lista = []
        listar('TODOS', "veiculos.txt", lista)
        veiculos = [sublista[0] for sublista in lista]
        self.Excluir_veiculo = ttk.Combobox(self.frame1Excluir_veiculos, values=veiculos)
        self.Excluir_veiculo.place(relx=0, rely=0.5, relheight=0.3, relwidth=1)

        self.botao_Excluir_veiculo = Button(self.frame2EXcluir_veiculos, text='EXCLUIR VEÍCULO', bd=4, background='#FF4500', font=self.fonte, command=self.Excluir_veiculos)
        self.botao_Excluir_veiculo.place(relx=0, rely=0, relheight=1, relwidth=1)

    def frames_Registrar_locacao(self):
        self.frame1Registrar_locacao = Frame(self.pg9, background='#008B8B')
        self.frame1Registrar_locacao.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.2)

        self.frame2Registrar_locacao = Frame(self.pg9, background='#008B8B')
        self.frame2Registrar_locacao.place(relx=0.05, rely=0.25, relwidth=0.9, relheight=0.5)

        self.frame3Registrar_locacao = Frame(self.pg9, background='#008B8B')
        self.frame3Registrar_locacao.place(relx=0.05, rely=0.75, relwidth=0.9, relheight=0.2)

    def widgets_Registrar_locacao(self):
        self.fonte = Font(family="Arial Black", size=15)
        self.fonte2 = Font(family="Arial Black", size=12)

        self.texto_Locacao = Label(self.frame1Registrar_locacao, text='SELECIONE O VEÍCULO', font=self.fonte, background='#008B8B')
        self.texto_Locacao.place(relx=0.2, rely=0, relwidth=0.6, relheight=0.3)

        lista = []
        listar('TODOS', "veiculos.txt", lista)
        veiculos = [sublista[0] for sublista in lista]
        self.selecionar_veiculo_locacao = ttk.Combobox(self.frame1Registrar_locacao, values=veiculos)
        self.selecionar_veiculo_locacao.place(relx=0.2, rely=0.3, relwidth=0.6, relheight=0.3)

        self.texto_cliente = Label(self.frame1Registrar_locacao, text='DADOS DO CLIENTE', font=self.fonte, background='#008B8B')
        self.texto_cliente.place(relx=0.2, rely=0.7, relwidth=0.6, relheight=0.3)

        self.texto_nome = Label(self.frame2Registrar_locacao, text='NOME', font=self.fonte2, background='#008B8B')
        self.texto_nome.place(relx=0, rely=0, relwidth=0.15, relheight=0.1)

        self.nome_cliente = Entry(self.frame2Registrar_locacao)
        self.nome_cliente.place(relx=0, rely=0.1, relwidth=0.5, relheight=0.1)

        self.texto_cpf = Label(self.frame2Registrar_locacao, text='CPF', font=self.fonte2, background='#008B8B')
        self.texto_cpf.place(relx=0.6, rely=0, relwidth=0.15, relheight=0.1)

        self.cpf_cliente = Entry(self.frame2Registrar_locacao)
        self.cpf_cliente.place(relx=0.63, rely=0.1, relwidth=0.3, relheight=0.1)

        self.texto_telefone = Label(self.frame2Registrar_locacao, text='TELEFONE', font=self.fonte2, background='#008B8B')
        self.texto_telefone.place(relx=0, rely=0.25, relwidth=0.2, relheight=0.1)

        self.telefone_cliente = Entry(self.frame2Registrar_locacao)
        self.telefone_cliente.place(relx=0, rely=0.35, relwidth=0.5, relheight=0.1)

        self.texto_rg = Label(self.frame2Registrar_locacao, text='RG', font=self.fonte2, background='#008B8B')
        self.texto_rg.place(relx=0.6, rely=0.25, relwidth=0.15, relheight=0.1)

        self.rg_cliente = Entry(self.frame2Registrar_locacao)
        self.rg_cliente.place(relx=0.63, rely=0.35, relwidth=0.3, relheight=0.1)

        self.texto_email = Label(self.frame2Registrar_locacao, text='EMAIL', font=self.fonte2, background='#008B8B')
        self.texto_email.place(relx=0, rely=0.5, relwidth=0.15, relheight=0.1)

        self.email_cliente = Entry(self.frame2Registrar_locacao)
        self.email_cliente.place(relx=0, rely=0.6, relwidth=0.5, relheight=0.1)

        self.texto_diarias = Label(self.frame2Registrar_locacao, text='DIARIAS', font=self.fonte2, background='#008B8B')
        self.texto_diarias.place(relx=0.63, rely=0.5, relwidth=0.15, relheight=0.1)

        self.diarias_cliente = Entry(self.frame2Registrar_locacao)
        self.diarias_cliente.place(relx=0.63, rely=0.6, relwidth=0.3, relheight=0.1)

        self.texto_pagamento = Label(self.frame2Registrar_locacao, text='FORMA DE PAGAMENTO', font=self.fonte2, background='#008B8B')
        self.texto_pagamento.place(relx=0, rely=0.75, relwidth=0.45, relheight=0.1)

        lista2 = ['DINHEIRO', 'CARTÃO DE CRÉDITO', 'CARTÃO DE DÉBITO', 'PIX']
        self.selecionar_pagamento = ttk.Combobox(self.frame2Registrar_locacao, values=lista2)
        self.selecionar_pagamento.place(relx=0, rely=0.85, relwidth=0.6, relheight=0.1)

        self.valor_final = Label(self.frame3Registrar_locacao, text='VALOR TOTAL:', background='#008B8B', font=self.fonte2)
        self.valor_final.place(relx=0, rely=0, relwidth=0.3, relheight=0.5)

        self.imprimir = StringVar()
        self.imprimir.set("")
        self.mostrar_valor = Label(self.frame3Registrar_locacao, textvariable=self.imprimir, background='#008B8B', font=self.fonte2)
        self.mostrar_valor.place(relx=0.3, rely=0, relwidth=0.4, relheight=0.5)

        self.calcular_valor = Button(self.frame2Registrar_locacao, text='CALCULAR VALOR', bd=4, background='#FF4500', command=self.calculo_valor)
        self.calcular_valor.place(relx=0.63, rely=0.75, relwidth=0.3, relheight=0.2)

        self.confirmar_locacao = Button(self.frame3Registrar_locacao, text='CONFIRMAR', bd=4, background='#FF4500', command=self.locar_veiculo)
        self.confirmar_locacao.place(relx=0.2, rely=0.6, relwidth=0.6, relheight=0.4)

interface()
