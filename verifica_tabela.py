from rich.console import Console 
from rich.table import Table
from rich import print
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
    
try:
    #verifica se as tabelas foram criadas
    conn = conexao()
    cursor= conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tabela_ex = cursor.fetchall()
    
    # verica se as tabelas estão no bd
    #tabelas_ define chamada de lista que contém os nomes das tabelas
    #que  devem estar no banco de dados
    table = Table()

    table = Table(title = '[purple]Tabelas do Banco Hortifruti[/purple]')
    table.add_column('[green]Tabela[/green]', style='cyan')
    table.add_column(f'[magenta]Status[/magenta]')

    tabela_es = ['cliente', 'funcionario', 'fornecedor', 'produto', 'estoque', 'venda', 'nfc']
    for tabela in tabela_es:
        if tabela not in [t[0] for t in tabela_ex]:
         #inicia loop de iteração para cada tabela na lista tabelas_
            ## verifica se a table atual(tabela) não está presente na lista de tabelas que foram encontradas no banco de dados(tables)
           #a expressão  [t[0] for t in tables]:  é uma lista de tuplas que contém os nomes das tabelas
            # a condição not in verifica se a tabela atual não está presente na lista de tabelas do bd
              table.add_row(tabela, '[brown]Criada com sucesso![/brown]')
              console.print(f'Tabela {tabela} criada com sucesso!')
        else:
            table.add_row(tabela, '[green]Já existe![/green]')
            console.print(f'Tabela {tabela} já existe!')

    
    console.print(table)
    
except sqlite3.Error as erro:
    console.print(f"Erro no banco de dados", {erro})

  


finally:
    if conn:
        conn.close()

#Sqlite_master é uma tabela mestra do sqlite contendo informações das tabelas dos bancos de dados

