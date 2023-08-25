import tkinter as tk


def verificar_usuarios(nome_arquivo):
    try:
        arquivo = open(nome_arquivo, 'r')
    except FileNotFoundError:
        return False
    else:
        conteudo = arquivo.read()
        if conteudo:
            return True
        else:
            return False
    finally:
        arquivo.close()


def cadastro_usuarios(usuario, nome, senha, nome_arquivo):
    try:
        arquivo = open(nome_arquivo, 'a')
    except:
        print('Erro ao abrir o arquivo')
    else:
        arquivo.write(nome + "#" + usuario + "#" + senha + "\n")
    finally:
        arquivo.close()


def verificar_veiculos(nome_arquivo):
    try:
        arquivo2 = open(nome_arquivo, 'r')
    except FileNotFoundError:
        return False
    else:
        conteudo2 = arquivo2.read()
        if conteudo2:
            return True
        else:
            return False
    finally:
        arquivo2.close()


def cadastrar_veiculos(modelo, montadora, classificacao, valor, nome_arquivo):
    try:
        arquivo2 = open(nome_arquivo, 'a')
    except:
        print('Erro ao abrir o arquivo')
    else:
        arquivo2.write(modelo + "#" + montadora + "#" + classificacao + "#" + valor + "\n")
    finally:
        arquivo2.close()


def percorrer_lista(opcao, nome_arquivo, lista):
    arquivo = open(nome_arquivo, 'r')

    if opcao == 'TODOS':
        for line in arquivo:
            atual_line = line.split(sep='#')
            lista.append(atual_line)
    else:
        for line in arquivo:
            atual_line = line.split(sep='#')
            if atual_line[2] == opcao:
                lista.append(atual_line)

    arquivo.close()


def listar(opcao, nome_arquivo, lista):
    match opcao:
        case 'TODOS':
            percorrer_lista(opcao, nome_arquivo, lista)
        case 'HATCH':
            percorrer_lista(opcao, nome_arquivo, lista)
        case 'SEDÃ':
            percorrer_lista(opcao, nome_arquivo, lista)
        case 'ESPORTIVO':
            percorrer_lista(opcao, nome_arquivo, lista)
        case 'SUV':
            percorrer_lista(opcao, nome_arquivo, lista)
        case 'FAMILIAR':
            percorrer_lista(opcao, nome_arquivo, lista)


def limpar_texto(entrada):
    entrada.delete(0, tk.END)
