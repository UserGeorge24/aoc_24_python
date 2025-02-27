import re

def count_xmas(i_content):
    global summa
    summa += len(re.findall('XMAS',i_content)) + len(re.findall('XMAS',i_content[::-1]))

def rotate_by_45(array, direction):
    rotated_array = []
    row_index = 0
#   Convert first line to first col in new array from n. index 
    for index, i in enumerate(array):
        row_index = index
        for j in i if direction == 'R' else i[::-1]:
            try:
                rotated_array[row_index][0] = j + rotated_array[row_index][0] if direction == 'R' else rotated_array[row_index][0] + j  
            except: 
                rotated_array.append([j]) 
            row_index += 1
    return rotated_array

file_path = "C:\\Users\\szita001\\Desktop\\advent\\2024_12_04.txt"
file = [ line.strip() for line in open(file_path,'r').readlines() ]
summa = 0
position_index = 0

# Vertical
while True:
    try: 
#   Get all columns next to next, and convert to single string 
        col_content = ''.join( [ i[position_index] for i in file ] )
    except: break

#   Count XMAS string in proper string in both way    
    count_xmas(col_content)
    position_index += 1

# Horizontal
# Get all columns next to next, and convert to single string
for i in file:    
#   Count XMAS string in proper string in both way    
    count_xmas(i)
        
# Diagonal
#  Rotate right
rotated_array = rotate_by_45(file,'R')
for i in rotated_array:
    count_xmas(str(i))
    
#  Rotate left
rotated_array = rotate_by_45(file,'L')
for i in rotated_array:
    count_xmas(str(i))
    
print(summa)
