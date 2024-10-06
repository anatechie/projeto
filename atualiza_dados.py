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
    
def atualiza_cliente(conn, id_cliente, Nome, Sobrenome, RG, CPF, Telefone,  Endereco, Data_Nasc, Email):
    cursor = conn.cursor()
    sql_atualiza_cliente = """
        UPDATE cliente
        SET Nome = ?, Sobrenome = ?, RG = ? , CPF = ?, Telefone = ?,  Endereco = ?, Data_Nasc = ?, Email = ?
        WHERE id_cliente = ?;
    """
    
    try:
        cursor.execute(sql_atualiza_cliente, (Nome, Sobrenome, id_cliente))
        conn.commit()
        console.print(f"[green]CLIENTE {id_cliente} ATUALIZADO[/green]")
    except sqlite3.DatabaseError as erro:
        console.print(f"[bold dark red]Erro ao atualizar dados do cliente: {erro}[/bold dark red]")

def atualiza_produto(conn, id_produto, Nome_produto, Preco, Tipo_produto, Peso, Quantidade, Descricao):
    cursor = conn.cursor()
    sql_atualiza_produto = """
        UPDATE produto
        SET id_produto = ?, Nome_produto  = ?, Preco = ?, Tipo_Produto = ?, Peso = ?, Quantidade = ?, Descricao = ?
        WHERE id_produto = ?
    """
    
    try:
        cursor.execute(sql_atualiza_produto, (id_produto, Nome_produto, Preco, Tipo_produto, Peso, Quantidade, Descricao))
        conn.commit()
        console.print(f"[green]PRODUTO {id_produto} ATUALIZADO[/green]")
    except sqlite3.DatabaseError as erro:
        console.print(f"[bold dark red]Erro ao atualizar dados do produto: {erro}[/bold dark red]")

def atualiza_funcionario(conn, id_funcionario, Nome, Sobrenome, CPF, Endereco, Telefone, Cargo, Status):
    cursor = conn.cursor()
    sql_atualiza_funcionario = """
        UPDATE funcionario
        SET Nome = ?, Sobrenome = ?, CPF = ?, Endereco = ?, Telefone = ?, Cargo = ?, Status = ?
        WHERE id_funcionario = ?;
    """
    try:
        cursor.execute(sql_atualiza_funcionario, (Nome, Sobrenome, CPF, Endereco, Telefone, Cargo, Status, id_funcionario))
        conn.commit()
        console.print(f"[green]FUNCIONÁRIO {id_funcionario} ATUALIZADO[/green]")
    except sqlite3.DatabaseError as erro:
        console.print(f"[bold dark red]Erro ao atualizar dados do funcionário: {erro}[/bold dark red]")

def atualiza_fornecedor(conn, id_fornecedor, Nome, CNPJ, Telefone, Endereco, Email, Status, id_produto):
    cursor = conn.cursor()
    sql_atualiza_fornecedor = """
        UPDATE fornecedor
        SET Nome = ?, CNPJ = ?, Telefone = ?, Endereco = ?, Email = ?, Status = ?, id_produto = ?
        WHERE id_fornecedor = ?;
    """
    try:
        cursor.execute(sql_atualiza_fornecedor, (Nome, CNPJ, Telefone, Endereco, Email, Status, id_produto, id_fornecedor))
        conn.commit()
        console.print(f"[green]FORNECEDOR {id_fornecedor} ATUALIZADO[/green]")
    except sqlite3.DatabaseError as erro:
        console.print(f"[bold dark red]Erro ao atualizar dados do fornecedor: {erro}[/bold dark red]")

def atualiza_venda(conn, id_venda, Quantidade, Preco, Nota_Fiscal):
    cursor = conn.cursor()
    sql_atualiza_venda = """
        UPDATE venda
        SET Quantidade = ?, Preco = ?, Nota_Fiscal = ?
        WHERE id_venda = ?;
    """
    try:
        cursor.execute(sql_atualiza_venda, (Quantidade, Preco, Nota_Fiscal, id_venda))
        conn.commit()
        console.print(f"[green]VENDA {id_venda} ATUALIZADA[/green]")
    except sqlite3.DatabaseError as erro:
        console.print(f"[bold dark red]Erro ao atualizar dados da venda: {erro}[/bold dark red]")

def atualiza_nfc(conn, id_nfc, Nota_Fiscal, Data_compra):
    cursor = conn.cursor()
    sql_atualiza_nfc = """
        UPDATE nfc
        SET Nota_Fiscal = ?, Data_compra = ?
        WHERE id_nfc = ?;
    """
    try:
        cursor.execute(sql_atualiza_nfc, (Nota_Fiscal, Data_compra, id_nfc))
        conn.commit()
        console.print(f"[green]NFC {id_nfc} ATUALIZADO[/green]")
    except sqlite3.DatabaseError as erro:
        console.print(f"[bold dark red]Erro ao atualizar dados da NFC: {erro}[/bold dark red]")

def atualiza_estoque(conn, id_estoque, Qnt_produto, Preco_compra, Preco_venda, id_cliente, id_produto, id_funcionario):
    cursor = conn.cursor()
    sql_atualiza_estoque = """
        UPDATE estoque
        SET Qnt_produto = ?, Preco_compra = ?, Preco_venda = ?, id_cliente = ?, id_produto = ?, id_funcionario = ?
        WHERE id_estoque = ?;
    """
    try:
        cursor.execute(sql_atualiza_estoque, (Qnt_produto, Preco_compra, Preco_venda, id_cliente, id_produto, id_funcionario, id_estoque))
        conn.commit()
        console.print(f"[green]ESTOQUE {id_estoque} ATUALIZADO[/green]")
    except sqlite3.DatabaseError as erro:
        console.print(f'[bold dark red]Erro ao atualizar dados no Estoque: {erro}[/bold dark red]')

    conn = conexao()
    if conn:
        try:
            atualiza_cliente(conn, 1, "Novo Nome", "Novo Sobrenome", "RG12345", "CPF123456789", "6199999999", "Nova Rua", "2000-01-01", "novoemail@example.com")
            atualiza_produto(conn, 1, "Nova Manga", 5.50, "Fruta", "4g", 10, "Manga Madura")
            atualiza_funcionario(conn, 1, "Novo Nome", "Novo Sobrenome", "CPF123456789", "Nova Rua", "6198888888", "Novo Cargo", "Ativo")
            atualiza_fornecedor(conn, 1, "Novo Fornecedor", "CNPJ123456789", "6197777777", "Nova Rua", "fornecedor@example.com", "Ativo", 1)
            atualiza_venda(conn, 1, 5, 200.00, "Nº38")
            atualiza_nfc(conn, 1, "NFC Atualizada", "2024-10-05 19:57:19")
            atualiza_estoque(conn, 1, 20, 30.00, 50.00, 1, 1, 1)
        except sqlite3.DatabaseError as erro:
            console.print(f"[bold dark red]Erro ao atualizar dados: {erro}[/bold dark red]")
        finally: 
            conn.close()
            console.print("[light green]Conexão fechada.[/light green]")
    else:
        console.print("[light red]Conexão não estabelecida.[/light red]")