my_file = open ('xmen.txt', 'w+t')
my_file.write('Beast\n')
my_file.write('Phoenix\n')
my_file.writelines([
    'Cyclops',
    'Bishop',
    'Nightcrawler',
])