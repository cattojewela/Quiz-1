print('-----------------[4]------------------')

with open("t8.shakespeare.txt", 'r') as f_var:
    Str = f_var.read()

linecount = len(Str.splitlines())
Str = Str.lower()

def replaceSymbol(myStr):
    myStr = myStr.replace('\n', ' ')
    myStr = myStr.replace('\r', ' ')
    myStr = myStr.replace('\t', ' ')
    myStr = myStr.replace(',', ' ')
    myStr = myStr.replace(':', ' ')
    myStr = myStr.replace(';', ' ')
    myStr = myStr.replace('.', ' ')
    myStr = myStr.replace('?', ' ')
    myStr = myStr.replace('!', ' ')
    myStr = myStr.replace('"', ' ')
    myStr = myStr.replace('&', ' ')
    return myStr

def strToList(myStr):
    new_list = myStr.split(' ')
    return new_list

myStr = replaceSymbol(Str)
new_list = strToList(myStr)
new_dictionary = {}

for mem in new_list:
    new_dictionary.setdefault(mem, 0)

for mem in new_list:
    new_dictionary[mem] = new_dictionary[mem] + 1


print('--------sort alphabetically--------')
alphabetically_sorted_list = sorted(new_dictionary)

with open("wordcount.txt", 'w') as output:  
    for mem in alphabetically_sorted_list:
        output.write(f'{mem} : {new_dictionary[mem]}\n')


print('--------sort based on VALUE--------')

list_of_tuple_pair = []
for mem in new_dictionary:
    # appending a tuple pair in a list
    list_of_tuple_pair.append((mem, new_dictionary[mem]))


def take_second(elem):
    return elem[1]

sorted_list_of_tuple_pair = sorted(list_of_tuple_pair, key = take_second, reverse = True)

for (key,value) in sorted_list_of_tuple_pair:
    print(f'{key} : {value} ')
