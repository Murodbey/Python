with open ('xmen.txt', 'w+t') as my_file:
    my_file.write('Beast\n')
    my_file.write('Phoenix\n')
    my_file.writelines([
        'Cyclops\n',
        'Bishop\n',
        'Nightcrawler\n',
    ])
my_file.close()

my_file = open('xmen.txt', 'r')
with my_file:
    print(my_file.read())
    print("I`m reading again")
    print(my_file.read())
