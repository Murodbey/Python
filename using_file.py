my_file = open ('xmen.txt', 'w+t')
my_file.write('Beast\n')
my_file.write('Phoenix\n')
my_file.writelines([
    'Cyclops\n',
    'Bishop\n',
    'Nightcrawler\n',
])
my_file.close()

m_file = open('xmen.txt', 'r')
print(my_file.read())
print("I`m reading again")
print(my_file.read())
my_file.close()