class Conta:
    #Metodo de inicializado da conta
    def __init__(self, num_conta, nome, saldo=0):
        self.num_conta = num_conta
        self.nome = nome
        self.saldo = saldo
        self.historico = []

    #metodo para realizar saque da conta.
    def sacar(self, valor):
        if self.saldo < valor: #verificação para ver se o valor do saque e menor que o saldo.
            raise print('Saldo insuficiente!!')
        else:
            self.saldo -= valor
            self.historico.append(f'-{valor} - saque')
            print('Saque realizado com sucesso!')

    #Metodo verificar o saldo.
    def saldo(self):
        return self.saldo

    #Metodo para ralizar depositos.    
    def despositar(self, valor):
        if valor <= 0: #Verificaçao para ver so valor do deposito e menor ou igual a zero.
            raise print('Valor do deposito não pode ser menor que 0 enm menor que 0')
        else:
            self.saldo += valor
            self.historico.append(f'+{valor} depósito')
            print('Deposito realizado com sucesso!')

    #Metodo para realizar transferencia entre contas.
    def transferir(self, conta_destino, valor):
        if valor <= 0: #validacao do valor para saber se e menor que zero.
            raise f"Valor da transferencia deve ser maior que zero."
        if valor > self.saldo: #Validacao para saber se o saldo nao esta negativo.
            raise print('Saldo insuficiente!!')
        else:
            self.saldo -= valor
            self.historico.append(f'-{valor} -transferencia') #acrescentando no historio a retirada do valor da primeira conta.
            conta_destino.saldo += valor
            print('transferencia realizado com sucesso!')
            conta_destino.historico.append(f'+{valor} - transferencia')

    def extrato(self):
        print('Extrato de operaçoes: ')
        for operacao in self.historico:
            print(operacao)


conta1 = Conta(1001, 'Nilson', 100)
conta2 = Conta(1002, 'Jessica', 80)

print(f'conta: {conta1.num_conta} cliente: {conta1.nome} Saldo: R${conta1.saldo}')
print(f'conta: {conta2.num_conta} cliente: {conta2.nome} Saldo: R${conta2.saldo}')

conta1.transferir(conta2, 30)
conta1.sacar(50)

print(f'conta: {conta1.num_conta} cliente: {conta1.nome} Saldo: R${conta1.saldo}')
print(f'conta: {conta2.num_conta} cliente: {conta2.nome} Saldo: R${conta2.saldo}')

conta1.extrato()