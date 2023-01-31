word = str(input())
cro_al = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
al_len = 0
for i in cro_al:
    word = word.replace(i, '*')

print(len(word))