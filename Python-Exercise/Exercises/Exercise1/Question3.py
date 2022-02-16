name = ('Shaun', 'Ron', 'Michael')
seat_numbers = (101, 102, 103)
dct={}
for i in range(len(name)):
    dct.update({name[i]: seat_numbers[i]})
print(dct)