import math
    
def get_combinations(num):
    
    combinations = list()
    to = 2**num if num != 1 else 2    
    for i in range(0,to):
        
        temp_i = int(i)
        operators = ''
            
        for j in range(0,num):
            if temp_i % 2 == 0:
                operators = '+' + operators
            else:
                operators = '*' + operators
            temp_i = math.floor(temp_i / 2)
        
        combinations.append(operators)
    return combinations        
    
file_path = "C:\\Users\\szita001\\Desktop\\advent\\2024_12_07.txt"
file = [ line.strip() for line in open(file_path,'r').readlines() ]
all_sum = int() 

for row in file:
    splitted_row = row.split(':')
    elements = splitted_row[1].split(' ')
    elements.pop(0)
    
    combinations = get_combinations(len(elements)-1)
    
    summa = int()

    for i in combinations:
        for index, value in enumerate(elements):    
            
            if index == 0:
                summa = int(value)
                continue

            if i[index-1] == '+':
                summa += int(value)
            elif i[index-1] == '*':
                summa *= int(value)            
            
        if int(splitted_row[0]) == summa:
            all_sum += summa
            break
        
        summa = 0

print(all_sum)
