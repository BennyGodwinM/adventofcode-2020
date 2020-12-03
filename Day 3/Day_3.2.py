    #Create a dd list

f = open("Day_3_input_data.txt")
text = f.readlines()

map = [[]]

for line in text:
    for character in line:
        if(character!='\n'):
            map[-1].append(character)
    map.append([])

map.pop()

def is_dot_or_tree(character):
    if character=='.':
        return 0
    return 1

def slope_calc(right,down):
    trees = 0
    pos = 0
    row = 0

    #323,31

    while(row+1<323):
        pos+=right
        row+=down
        if(pos>=31):
            pos = pos%31
        # print ("Visited: {} {}".format(row,pos))
        trees += is_dot_or_tree(map[row][pos])

    return(trees)


print(slope_calc(1,1))
print(slope_calc(3,1))
print(slope_calc(5,1))
print(slope_calc(7,1))
print(slope_calc(1,2))
f.close()
