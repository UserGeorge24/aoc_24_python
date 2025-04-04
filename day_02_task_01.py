import operator

file_path = "C:\\Users\\szita001\\Desktop\\advent\\2024_12_02.txt"

summa = 0

with open(file_path,"r") as obj:
    for line in obj:
        curr_line = line.strip().split(' ')
        
        curr_line = [int(i) for i in curr_line]

        o_operator = operator.gt if curr_line[0] > curr_line[1] else ( operator.lt if curr_line[0] < curr_line[1] else '' )
        
        if o_operator == '':
            continue
        
        elements_of_apply = int()
        
        for index,value in enumerate(curr_line[:-1]):    
            if o_operator(value, curr_line[index + 1]) and operator.le(abs( value - curr_line[index + 1]), 3):
                elements_of_apply += 1
            else:
                break
        
        summa = summa + 1 if elements_of_apply == len(curr_line) - 1 else summa 
