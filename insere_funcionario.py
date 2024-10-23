import sqlite3
from rich.console import  Console
import os

console = Console()


console.print('[magenta]----- CADASTRO DE FUNCIONÁRIO -----[/magenta]')
console.print('[magenta]--------------------------------[/magenta]')
# Exibe a mensagem colorida e depois usa input padrão
console.print('[blue] Informe o nome do funcionário:\t[/blue]', end = ' ')
nome_fun = input() # O input não terá cor, mas a mensagem anterior sim
console.print(f'[blue]Nome inserido:[/blue] {nome_fun}')

def inserir_funcionario(nome):
    cursor.execute('INSERT INTO funcionarios (nome) VALUES (?)', (nome,))
    conn.commit()
    console.print(f'[green]Funcionário "{nome}" inserido com sucesso![/green]')

def listar_funcionarios():
    cursor.execute('SELECT * FROM funcionarios')
    funcionarios = cursor.fetchall()
    if funcionarios:
        console.print('[blue]Lista de Funcionários:[/blue]')
        for funcionario in funcionarios:
            console.print(f'ID: {funcionario[0]}, Nome: {funcionario[1]}')
    else:
        console.print('[yellow]Nenhum funcionário cadastrado.[/yellow]')

def atualizar_funcionario(id, novo_nome):
    cursor.execute('UPDATE funcionarios SET nome = ? WHERE id = ?', (novo_nome, id))
    conn.commit()
    console.print(f'[green]Funcionário com ID {id} atualizado para "{novo_nome}".[/green]')

def excluir_funcionario(id):
    cursor.execute('DELETE FROM funcionarios WHERE id = ?', (id,))
    conn.commit()
    console.print(f'[red]Funcionário com ID {id} excluído.[/red]')

def menu():
    while True:
        console.print('[magenta]----- MENU -----[/magenta]')
        console.print('[cyan]1. Inserir Funcionário[/cyan]')
        console.print('[cyan]2. Listar Funcionários[/cyan]')
        console.print('[cyan]3. Atualizar Funcionário[/cyan]')
        console.print('[cyan]4. Excluir Funcionário[/cyan]')
        console.print('[cyan]5. Sair[/cyan]')
        
        opcao = Prompt.ask('[yellow]Escolha uma opção:[/yellow]')
        
        if opcao == '1':
            nome = Prompt.ask('[blue]Informe o nome do funcionário:[/blue]')
            inserir_funcionario(nome)
        elif opcao == '2':
            listar_funcionarios()
        elif opcao == '3':
            id = Prompt.ask('[blue]Informe o ID do funcionário a ser atualizado:[/blue]')
            novo_nome = Prompt.ask('[blue]Informe o novo nome do funcionário:[/blue]')
            atualizar_funcionario(id, novo_nome)
        elif opcao == '4':
            id = Prompt.ask('[blue]Informe o ID do funcionário a ser excluído:[/blue]')
            excluir_funcionario(id)
        elif opcao == '5':
            console.print('[green]Saindo...[/green]')
            break
        else:
            console.print('[red]Opção inválida! Tente novamente.[/red]')

# Executa o menu
menu()

# Fecha a conexão com o banco de dados
conn.close()