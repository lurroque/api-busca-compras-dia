import MySQLdb
import hug
import os

# Incluir o endpoint da url que será acessada
# Ex: /tratador_de_compras/compras_por_dia
@hug.get("Endpoint")
def busca_compras_do_dia():
    """API simples que busca as compras feitas
         em um dia."""
    
    # Criando conexão com o Banco
    db = MySQLdb.connect(host = "IP_do_banco",
                    user = "admin",
                    passwd = "senha",
                    db = "banco")
    cur = db.cursor()
    query = cur.execute("""SELECT * FROM compras
                        WHERE data >= curdate()
                        limit 10;""")
    linhas = cur.fetchall()

    # Criando lista que armazenará um json com as informações
    compras = []

    for linha in linhas:
        compras.append(linha[2], linha[3])

    db.close()

    # Retornando lista com json das compras
    return compras