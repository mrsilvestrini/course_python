#Imports Libs
import getpass

print(" ")
print("***********************************************************")
print("**********  School of Net - Caixa Eletronico  *************")
print("***********************************************************")
print(" ")

#Dados da Conta
account_typed=input('Digite o Numero da Conta: ')
password_typed=getpass.getpass('Digite sua Senha: ')

#Output
print(account_typed)
print(password_typed)

#Dicionario de Contas
accounts_list={
    '0001-01':{
        'password':'123456789',
        'name':'Marcos Oscorp',
        'value':'10.560'        
    },
    '0001-02':{
        'password':'987654321',
        'name':'Roberto Oscorp',
        'value':'10.560'        
    }
}
#Validando Conta com Uso de Dicionario
if account_typed in accounts_list and password_typed == accounts_list[account_typed]['password']:
    print('Conta Validada com Sucesso')
else:
    print('Conta Inválida')
