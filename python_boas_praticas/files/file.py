import os

#GET BASE PATH OF PROJECT
BASE_PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_PATH)

#file=open(BASE_PATH+'/_file_test.dat','w') #write
#file.write('Marcos\tRoberto\n')
#file.write('Silvestrini')
#file.close()

# file=open(BASE_PATH+'/_file_test.dat','a') #append
# file.write('Marcos\tRoberto\n')
# file.write('Silvestrini\n')
# file.writelines(('test1','test2','test2','test2\n'))
# file.writelines(['test1','test2','test2','test2\n'])
# file.close()

file=open(BASE_PATH+'/_file_test.dat','r') #read
# print(file.read())
# print('\n')
# print(file.read(10))
# print(file.readline())
# print(file.readline(6))
# print(file.readline(2))
# print(file.readline())
#lines=file.readlines()
#for line in lines:
#    print(line)
line=file.readline()
while line:
    line=file.readline()
    print(line)
file.close()