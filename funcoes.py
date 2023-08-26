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


def atualizar_v(nome_arquivo, opcao, opcao2, novo):
    linhas_modificadas = []

    arquivo = open(nome_arquivo, 'r')
    for line in arquivo:
        atual_line = line.split('#')
        if atual_line[0] == opcao:
            match opcao2:
                case 'MODELO':
                    linhas_modificadas.append(novo + "#" + atual_line[1] + "#" + atual_line[2] + "#" + atual_line[3] + '\n')
                case 'MONTADORA':
                    linhas_modificadas.append(atual_line[0] + "#" + novo + "#" + atual_line[2] + "#" + atual_line[3] + '\n')
                case 'TIPO':
                    linhas_modificadas.append(atual_line[0] + "#" + atual_line[1] + "#" + novo + "#" + atual_line[3] + '\n')
                case 'VALOR':
                    linhas_modificadas.append(atual_line[0] + "#" + atual_line[1] + "#" + atual_line[2] + "#" + novo + '\n')
        else:
            linhas_modificadas.append(atual_line[0] + "#" + atual_line[1] + "#" + atual_line[2] + "#" + atual_line[3])
    arquivo.close()

    arquivo2 = open(nome_arquivo, 'w')
    for line in linhas_modificadas:
        atual_line = line.split(sep="\n")
        del atual_line[1]
        arquivo2.write("#".join(atual_line) + "\n")
    arquivo2.close()


def Excluir_v(nome_arquivo, opcao):
    linhas_modificadas = []

    arquivo = open(nome_arquivo, 'r')
    for line in arquivo:
        atual_line = line.split('#')
        if atual_line[0] == opcao:
            continue
        else:
            linhas_modificadas.append(atual_line[0] + "#" + atual_line[1] + "#" + atual_line[2] + "#" + atual_line[3])
    arquivo.close()

    arquivo2 = open(nome_arquivo, 'w')
    for line in linhas_modificadas:
        atual_line = line.split(sep="\n")
        del atual_line[1]
        arquivo2.write("#".join(atual_line) + "\n")
    arquivo2.close()
    return 1
