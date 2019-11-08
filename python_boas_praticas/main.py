from modules import utils
from modules import operations

def main():    
    utils.header()    
    account_auth=operations.auth_account()
    if account_auth:
        utils.clear()
        utils.header()
        option_typed=operations.get_menu_options_typed(account_auth)
        operations.do_operation(option_typed,account_auth)                    
    else:
        print("Conta Invalida, Tente Novamente!")
            
    
while True:
    main()  
    utils.pause()
    utils.clear()          