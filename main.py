from itertools import product
import string

min_len = int(input("Enter minimum length of password: "))
max_len = int(input("Enter maximum length of password: "))
data_list = string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation
cont =0
file_open = open('Wordlist.txt', 'w')
for i in range(min_len, max_len+1):
    for j in product(data_list, repeat=i):
        word = ''.join(j)
        file_open.write(word)
        file_open.write('\n')
        cont+=1

print("Wordliist of {} passwords created".format(cont))