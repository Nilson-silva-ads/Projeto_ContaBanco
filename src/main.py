from core.entities.conta import ContaBanco

def menu_principal():        
    print('--'*30)
    print('Simulador de Conta'.center(60))
    print('--'*30)
    print('1 - Abrir nova conta')
    print('2 - Listar Contas')
    print('3 - Acessar conta')
    print('4 - Excluir conta')
    print('5 - Sair')
    print('--'*30)

def menu():
    print('--'*20)
    print('operaçoes da conta'.center(40))
    print('--'*20)
    print('1 - Saldo.')
    print('2 - Depositar.')
    print('3 - Extrato.')
    print('4 - Sacar.')
    print('5 - Transferir')
    print('6 - voltar ao menu principal.')
    print('--'*20)

def abir_conta(conta: list) -> ContaBanco:
    print('Ciando Nova Conta')
    num_conta = int(input('Numero da Conta'))