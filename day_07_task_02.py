import math

def get_combinations(num):
    
    combinations = list()
    to = 3**num if num != 1 else 2
    
    for i in range(0,to):
        
        temp_i = int(i)
        operators = ''
            
        for j in range(0,num):
            if temp_i % 3 == 0:
                operators = '+' + operators
            elif temp_i % 3 == 1:
                operators = '*' + operators
            elif temp_i % 3 == 2:
                operators = '&' + operators
                
            temp_i = math.floor(temp_i / 3)
        
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
    results = list()
    comb_index = 0
    
    for index, value in enumerate(elements):

        if not results:
            for i in range(0,len(combinations)):
                results.append(int(elements[0]))
                continue
        else:
            for index, i in enumerate(combinations):
                if i[comb_index] == '+':
                    results[index] += int(value)
                elif i[comb_index] == '*':
                    results[index] *= int(value)
                elif i[comb_index] == '&':
                    results[index] = int(str(results[index]) + value)
            comb_index += 1
            
    if int(splitted_row[0]) in results:
        all_sum += int(splitted_row[0])
        
print(all_sum)
