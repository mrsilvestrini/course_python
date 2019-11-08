import os

def header ():
    print(" ")
    print("***********************************************************")
    print("**********  School of Net - Caixa Eletronico  *************")
    print("***********************************************************")   
    print(" ")

def clear():    
    clear= 'cls' if os.name=='nt' else 'clear'
    os.system(clear)

def pause():
    input("Pressione <ENTER> para Continuar...") 
