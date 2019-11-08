import os
print(' ')

print(os.path.abspath('.'))
print(os.path.abspath('..'))
print(os.path.abspath('./test/test_path.py'))
print(os.path.abspath('./test'))

print(' ')

path_test_file=os.path.abspath('./test/test_path.py')
print(path_test_file)
print(os.path.dirname(path_test_file))
print(os.path.exists(path_test_file +'test'))
print(os.path.isfile(path_test_file))
print(os.path.isdir(path_test_file))

print(' ')

print(__file__)
print(os.path.abspath(__file__))
path=(os.path.dirname(os.path.abspath(__file__)))
print(path)
BASE_PATH=os.path.abspath(./path)
print(BASE_PATH)