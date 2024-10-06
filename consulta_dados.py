from rich.console import Console
#from rich.table import Table
import sqlite3

console = Console()

def conexao():
    conn = None
    try:
        conn = sqlite3.connect('hortifruti.db')
        console.print(f"[green]Conexão bem sucedida![/green]")
        return conn
    except sqlite3.DatabaseError as erro:
        console.print(f"[bold dark red]Erro ao conectar ao banco de dados: {erro}[/bold dark red]")
        return None

def consulta_dado(conn,tabela):
    cursor= conn.cursor()
    sql_consulta = f"""
    SELECT * FROM {tabela};
    """
    try:
        cursor.execute(sql_consulta)
        res = cursor.fetchall()
        return res
    except sqlite3.Error as erro:
        return f"[bold dark red]Erro ao consultar dados: {erro}[/bold dark red]"

try:
    conn = conexao()
    if conn: 
        tabela_ = ["cliente", "produto", "funcionario", "fornecedor", "venda", "nfc", "estoque"]
        for tabela in tabela_:
            res = consulta_dado(conn, tabela)
            console.print(f'Resultados: {tabela}')
            for resu in res:
                console.print(resu)
                console.print('------------------------')
finally:
    if conn:
        conn.close()
        console.print(f'[green]CONEXAO FINALIZADA[/green]')

