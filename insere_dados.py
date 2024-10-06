from rich.console import Console
from rich.table import Table
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
    
def insere_cliente(conn):
    cursor = conn.cursor()
    sql_cliente =  """
        INSERT INTO cliente(
        id_cliente,
        Nome, 
        Sobrenome, 
        RG, CPF, 
        Telefone, 
        Endereco,
        Data_Nasc,
        Email) VALUES(1, 'Ana', 'Silva', 
        123456, 12345678910,
        6199999999, 'Rua7 ', 
        '2002-12-08', 'ana@hotmail.com');
        """

    
    try: 
        cursor.execute(sql_cliente)
        conn.commit()
        return "[green]CLIENTE INSERIDO[/green]"
    except sqlite3.DatabaseError as erro:
        return f"[bold dark red]Erro ao inserir CLIENTE: {erro}[/bold dark red]"

    

def insere_produto(conn):
    cursor = conn.cursor()
    sql_produto = """
        INSERT INTO produto(
        id_produto,
        Nome_produto,
        Preco,
        Tipo_Produto,
        Peso,
        Quantidade,
        Descricao) VALUES(1, 'Manga', 5.37, 'fruta', '3g', 1, 'Manga Verde');
        """
    
    try: 
        
        cursor.execute(sql_produto)
        conn.commit()
        return "[green]PRODUTO INSERIDO[/green]"
    except sqlite3.DatabaseError as erro:
        return f"[bold dark red]Erro ao inserir PRODUTO: {erro}[/bold dark red]"

def insere_funcionario(conn):
    cursor = conn.cursor()
    sql_funcionario = """
        INSERT INTO funcionario(
        id_funcionario,
        Nome,
        Sobrenome,
        CPF,
        Endereco,
        Telefone,
        Cargo,
        Status) VALUES(1, 'Breno', 'Silva', 33333333333, 'Qd 314', 6198842384, 'Caixa', 'Ativo');
        """
    
    try: 
        
        cursor.execute(sql_funcionario)
        conn.commit()
        return "[green]FUNCIONÁRIO INSERIDO[/green]"
    except sqlite3.DatabaseError as erro:
        return f"[bold dark red]Erro ao inserir FUNCIONÁRIO: {erro}[/bold dark red]"

def insere_fornecedor(conn):
    cursor = conn.cursor()
    sql_fornecedor = """
        INSERT INTO fornecedor(
        id_fornecedor,
        Nome,
        CNPJ,
        Telefone,
        Endereco,
        Email,
        Status,
        id_produto) VALUES(1, 'Hortifruti', 231236544000130, 5561000000000, 'Rua 0', 'hortifruti@gmail.com', 'Ativo', 1);
        """
    
    try: 
       
        cursor.execute(sql_fornecedor)
        conn.commit()
        return "[green]FORNECEDOR INSERIDO[/green]"
    except sqlite3.DatabaseError as erro:
        return f"[bold dark red]Erro ao inserir FORNECEDOR: {erro}[/bold dark red]"

def insere_venda(conn):
    cursor = conn.cursor()
    sql_venda = """
       INSERT INTO venda(
       id_venda,
       id_cliente, 
       id_produto,
       Quantidade,
       Preco,
       Nota_Fiscal) VALUES(1, 1, 1, 100, 5.37, 'Nº37');
       """
    
    try: 
        
        cursor.execute(sql_venda)
        conn.commit()
        return "[green]VENDA INSERIDA[/green]"
    except sqlite3.DatabaseError as erro:
        return f"[bold dark red]Erro ao inserir VENDA: {erro}[/bold dark red]"

def insere_NFC(conn):
    cursor = conn.cursor()
    sql_nfc = """
        INSERT INTO nfc(id_nfc, Nota_Fiscal, Data_compra, id_cliente,
        id_produto, id_funcionario) VALUES(
        1, 1, 'Nº37', '2024-10-05 19:57:19');
       """
    
    try: 
        
        cursor.execute(sql_nfc)
        conn.commit()
        return "[green]NFC INSERIDO[/green]"
    except sqlite3.DatabaseError as erro:
        return f"[bold dark red]Erro ao inserir NFC: {erro}[/bold dark red]"


def insere_estoque(conn):
    cursor = conn.cursor()
    sql_estoque =  """
        INSERT INTO estoque(
        id_estoque,
        Qnt_produto,
        Preco_compra,
        Preco_venda,
        id_produto,
        id_funcionario) VALUES(1, 26, 80.0, 45.90, 1, 1, 1);
       """
    
    try: 
        
        cursor.execute(sql_estoque)
        conn.commit()
        return "[green]PRODUTO INSERIDO NO ESTOQUE[/green]"
    except sqlite3.DatabaseError as erro:
        return f"[bold dark red]Erro ao inserir PRODUTO NO ESTOQUE: {erro}[/bold dark red]"

   # conexão e inserções
try:
    conn = conexao()
    
    if conn:
        table = Table(title="Resultados das Inserções")
        table.add_column("Tabela", justify="left", style="cyan")
        table.add_column("Status", justify="left", style="green")
        
        # Adiciona as inserções à tabela
        table.add_row("Cliente", insere_cliente(conn))
        table.add_row("Produto", insere_produto(conn))
        table.add_row("Funcionário", insere_funcionario(conn))
        table.add_row("Fornecedor", insere_fornecedor(conn))
        table.add_row("Venda", insere_venda(conn))
        table.add_row("NFC", insere_NFC(conn))
        table.add_row("Estoque", insere_estoque(conn))
        
        # Imprime  tabela com os resultados
        console.print(table)

except sqlite3.DatabaseError as erro:
    console.print(f"[bold dark red]Erro durante a inserção: {erro}[/bold dark red]")
    
finally:
    if conn:
        conn.close()
        console.print('[green]CONEXÃO FINALIZADA[/green]')
