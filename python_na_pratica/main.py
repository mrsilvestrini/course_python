#Imports Libs
import getpass
import os

accounts_list={
        '0001-01':{
            'password':'123',
            'name':'Marcos Oscorp',
            'value':'10.560',
            'admin':False       
        },
        '0001-02':{
            'password':'987',
            'name':'Roberto Oscorp',
            'value':'10.560',
            'admin':False               
        },
        '1111-11':{
            'password':'123',
            'name':'Admin',
            'value':'1000',
            'admin':True               
    }
}
money_slips={
    '20':5,
    '50':5,
    '100':5
}

while True:        
    print(" ")
    print("***********************************************************")
    print("**********  School of Net - Caixa Eletronico  *************")
    print("***********************************************************")
    print(" ")

    #Dados da Conta
    account_typed=input('Digite o Numero da Conta: ')
    password_typed=getpass.getpass('Digite sua Senha: ')
    
    #Dicionario de Contas
    
    #Validando Conta com Uso de Dicionario    
    if account_typed in accounts_list and password_typed == accounts_list[account_typed]['password']:  
        os.system('cls' if os.name=='nt' else 'clear')             
        print("***********************************************************")
        print("**********  School of Net - Caixa Eletronico  *************")
        print("***********************************************************")   
        print("1 - Saldo") 
        print("2 - Saque") 
        if accounts_list[account_typed]['admin']:            
            print("9 - Mostar Cedulas")        
            print("10 - Incluir Cedulas")        
        option_typed=input("Escolha umas das opções acima: ")
        if(option_typed == '1'):
            print("Seu saldo é %s" % accounts_list[account_typed]['value'])     
        elif option_typed == '9' and accounts_list[account_typed]['admin']:
            print(money_slips)
        elif option_typed == '10' and accounts_list[account_typed]['admin']:
            amount_typed=input("Digite a Quantidade de Cedulas: ")
            money_bill_typed=input("Digite a Cedulas a ser Incluida: ")            
            money_slips[money_bill_typed]+=int(amount_typed)
            print(money_slips)
        elif option_typed == '2':
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
            
        else:
            print("Opção Invalida!")
    else:
        print("Conta Invalida, Tente Novamente!")
    
    input("Pressione <ENTER> para Continuar...")    
    os.system('cls' if os.name=='nt' else 'clear')             