from utils import header
from open_file_bank import open_file_bank,write_money_slips

def main():
    header()
    make_money_slips()
    

def make_money_slips():
    file=open_file_bank('w')
    write_money_slips(file)
    file.close()    

main()    
