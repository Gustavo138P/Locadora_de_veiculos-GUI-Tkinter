def verificar_arquivo(nome_arquivo):
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

def cadastro(usuario, nome, senha, nome_arquivo):
    try:
        arquivo = open(nome_arquivo, 'a')
    except:
        print('Erro ao abrir o arquivo')
    else:
        arquivo.write(nome + "#" + usuario + "#" + senha + "\n")
    finally:
        arquivo.close()