#from modules import bank_account_variables
import getpass
from modules.bank_account_variables import accounts_list,money_slips

def do_operation(option_typed,account_auth):
    if(option_typed == '1'):
        show_balance(account_auth)
    elif option_typed == '9' and accounts_list[account_auth]['admin']:
        show_money_slips()
    elif option_typed == '10' and accounts_list[account_auth]['admin']:
        insert_money_slips()
    elif option_typed == '2':
        withdraw()
    else:
        print("Opção Invalida!")


def show_balance(account_auth):
    print("Seu saldo é %s" % accounts_list[account_auth]['value'])     


def show_money_slips():
    print("Celulas Disponiveis no Caixa")
    print(money_slips)


def insert_money_slips():
    amount_typed=input("Digite a Quantidade de Cedulas: ")
    money_bill_typed=input("Digite a Cedulas a ser Incluida: ")            
    money_slips[money_bill_typed]+=int(amount_typed)
    print(money_slips)

  
def withdraw():
    value_typed=input("Digite o Valor a ser Sacado: ")            
    money_slips_user={}
    value_int=int(value_typed)
    if value_int // 100 > 0 and value_int // 100 <= money_slips['100']:
        money_slips_user['100']=value_int // 100
        value_int=value_int - value_int // 100 * 100
    if value_int // 50 > 0 and value_int // 50 <= money_slips['50']:
        money_slips_user['50']=value_int // 50
        value_int=value_int - value_int // 50 * 50
    if value_int // 20 > 0 and value_int // 20 <= money_slips['20']:
        money_slips_user['20']=value_int // 20
        value_int=value_int - value_int // 20 * 20
            
    if value_int != 0:
        print("Cedulas indisponiveis para este Valor.")               
        print("Cedulas Disponiveis: 100,50,20")
    else:
        for money_bill in money_slips_user:
            money_slips[money_bill]-=money_slips_user[money_bill]
        print("Pegue as notas")               
        print(money_slips_user)
        
    
def auth_account():    
    account_typed=input('Digite o Numero da Conta: ')
    password_typed=getpass.getpass('Digite sua Senha: ')               
    if account_typed in accounts_list and password_typed == accounts_list[account_typed]['password']:  
        return account_typed
    else:
        return False


def get_menu_options_typed(account_auth):
    print("1 - Saldo") 
    print("2 - Saque") 
    if accounts_list[account_auth]['admin']:            
        print("9 - Mostar Cedulas")        
        print("10 - Incluir Cedulas")   
             
    return input("Escolha umas das opções acima: ")