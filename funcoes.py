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