class ContaBanco:
    #Metodo de inicializado da conta
    def __init__(self, num_conta, nome, saldo=0):
        self.num_conta = num_conta
        self.nome = nome
        self.__saldo = saldo
        self.historico = []

    #metodo para realizar saque da conta.
    def sacar(self, valor):
        if self.__saldo < valor: #verificação para ver se o valor do saque e menor que o saldo.
            raise ValueError('Saldo insuficiente!!')
        else:
            self.__saldo -= valor
            self.historico.append(f'Saque -{valor}')
            print('Saque realizado com sucesso!')

    #Metodo verificar o saldo.
    def get_saldo(self):
        return self.__saldo

    #Metodo para ralizar depositos.    
    def despositar(self, valor):
        if valor <= 0: #Verificaçao para ver so valor do deposito e menor ou igual a zero.
            raise print('Valor do deposito não pode ser menor ou igual a 0')
        else:
            self.__saldo += valor
            self.historico.append(f'Deposito  +{valor}')
            print('Deposito realizado com sucesso!')

    #Metodo para realizar transferencia entre contas.
    def transferir(self, conta_destino, valor):
        if valor <= 0: #validacao do valor para saber se e menor que zero.
            raise f"Valor da transferencia deve ser maior que zero."
        if valor > self.__saldo: #Validacao para saber se o saldo nao esta negativo.
            raise ValueError('Saldo insuficiente!!')
        else:
            self.__saldo -= valor
            self.historico.append(f'Transferecncia  -{valor}') #acrescentando no historio a retirada do valor da primeira conta.
            conta_destino.receber_transferencia(valor)
            print('transferencia realizado com sucesso!')

    def receber_transferencia(self, valor):
        self.__saldo += valor
        self.historico.append(f'Transferencia recebida de {self.num_conta}: +{valor:.2f}')
    
    #Metodo para exibir o historico de transacoes e movimentaçoes da conta.
    def extrato(self):
        print('Extrato da Conta: ')
        for operacao in self.historico:
            print(operacao)
        print(f'Saldo atual: {self.__saldo}')
        print('....'*20)


from cliente import Cliente

cliente1 = Cliente(1001, 'Nilson')
cliente2 = Cliente(1002, 'Jessica')

conta1 = Conta( 1001, cliente1, 100)
conta2 = Conta( 1002, cliente2, 80)

print(f'conta: {conta1.num_conta} cliente: {cliente1.nome} Saldo: R${conta1.get_saldo()}')
print(f'conta: {conta2.num_conta} cliente: {cliente2.nome} Saldo: R${conta2.get_saldo()}')

print('Fazendo uma transferencia da conta1 para conta 2 no valor de 30,00')
conta1.transferir(conta2, 30)
print('Fazendo um saque da conta1 no valor de 50,00')
conta1.sacar(50)
print(f'Fazendo uma deposito na conta 1 no valor de 200')
conta1.despositar(200)

conta1.extrato()
print('verificando o extrado da conta 2')
conta2.extrato()