import sqlite3
from rich.console import Console
from rich.table import Table

console = Console(

)
def conexao():
    conn = None
    try:
        conn = sqlite3.connect('hortifruti.db')
        console.print(f"[green]Conexão bem sucedida![/green]")
        return conn
    except sqlite3.DatabaseError as erro:
        console.print(f"[bold dark red]Erro ao conectar ao banco de dados: {erro}[/bold dark red]")
        return None
       

def cria_tabela(conn):
    console.print(f"[green]Criando tabelas...[/green]")
    tabelas = [
        '''
         CREATE TABLE IF NOT EXISTS CLIENTE(
         id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
         Nome VARCHAR(50) NOT NULL,
         Sobrenome VARCHAR(40) NOT NULL,
         RG VARCHAR(12),
         CPF VARCHAR(11) NOT NULL,
         Telefone VARCHAR(14),
         Endereco VARCHAR(60),
         Data_Nasc DATE NOT NULL,
         Email VARCHAR(50)
        );
        ''',
        
        '''
        CREATE TABLE IF NOT EXISTS produto(
        id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome_produto VARCHAR(50) NOT NULL,
        Preco DECIMAL(10,2) NOT NULL,
        Tipo_Produto VARCHAR(20),
        Peso VARCHAR(10),
        Quantidade INTEGER NOT NULL,
        Descricao VARCHAR(100)
        );
        ''',
        
        '''
        CREATE TABLE IF NOT EXISTS funcionario(
        id_funcionario INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome VARCHAR(50) NOT NULL,
        Sobrenome VARCHAR(40) NOT NULL,
        CPF VARCHAR(12) NOT NULL,
        Endereco VARCHAR(40),
        Telefone VARCHAR(14),
        Cargo VARCHAR(20),
        Status VARCHAR(10)
        );
        ''',
        '''
        CREATE TABLE IF NOT EXISTS fornecedor(
        id_fornecedor INTEGER PRIMARY KEY NOT NULL,
        Nome VARCHAR(50) NOT NULL,
        CNPJ VARCHAR(20) NOT NULL,
        Telefone VARCHAR(14),
        Endereco VARCHAR(60),
        Email VARCHAR(50),
        Status VARCHAR(10),
        id_produto INTERGER,
        FOREIGN KEY (id_produto) REFERENCES produto(id_produto)
        );
        '''
        ,
        '''
        CREATE TABLE IF NOT EXISTS venda(
        id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
        Quantidade INTEGER NOT NULL,
        Preco DECIMAL(10,2) NOT NULL,
        Nota_Fiscal INTEGER NOT NULL,
        id_cliente INTEGER NOT NULL,
        id_produto INTEGER NOT NULL,
        id_funcionario INTEGER NOT NULL,
        FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente),
        FOREIGN KEY (id_produto) REFERENCES produto(id_produto),
        FOREIGN KEY (id_funcionario) REFERENCES funcionario(id_funcionario)
        );
        ''',
        
        '''
        CREATE TABLE IF NOT EXISTS nfc(
        id_NFC INTEGER PRIMARY KEY AUTOINCREMENT,
        Nota_Fiscal INT(30) NOT NULL,
        Data_compra DATETIME,
        id_cliente INTEGER NOT NULL,
        id_produto INTEGER NOT NULL,
        id_funcionario INTEGER NOT NULL,
        FOREIGN KEY (id_cliente) REFERENCES CLIENTE(id_cliente),
        FOREIGN KEY (id_produto) REFERENCES produto(id_produto),
        FOREIGN KEY (id_funcionario) REFERENCES funcionario(id_funcionario)
        );
        ''',
        
        '''
        CREATE TABLE IF NOT EXISTS estoque(
        id_estoque INTEGER PRIMARY KEY AUTOINCREMENT,
        Qnt_produto INT(100) NOT NULL,
        Preco_compra DECIMAL(10,2),
        Preco_venda DECIMAL(10,2),
        Tipo_produto VARCHAR(15),
        id_produto INTEGER NOT NULL,
        id_funcionario INTEGER NOT NULL,
        FOREIGN KEY (id_produto) REFERENCES produto(id_produto),
        FOREIGN KEY (id_funcionario) REFERENCES funcionario(id_funcionario)
        );
        '''
    ]
    for tabela in tabelas:
        try: 
            cursor = conn.cursor()
            cursor.execute(tabela)
            conn.commit()
            console.print(f'[green]Tabela criada com sucesso![/green]')
        except sqlite3.DatabaseError as erro: 
            console.print(f'[bold dark red]Erro ao criar tabela. Descrição do erro: {erro}[/bold dark red]')


conn = conexao()
if conn:
    try:
        cria_tabela(conn)
    finally:
        if conn:
            conn.close()
            console.print(f'[light green]Conexão fechada.[/light green]')
else:
    console.print(f'[light red]Conexão não estabelecida.[/light red]')