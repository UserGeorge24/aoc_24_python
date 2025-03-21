import operator

summa = 0

def get_operator(curr_line):
    for index, value in enumerate(curr_line):        
        if curr_line[index] > curr_line[index+1] and curr_line[index+1] > curr_line[index+2]:
            return operator.gt
        elif curr_line[index] < curr_line[index+1] and curr_line[index+1] < curr_line[index+2]:
            return operator.lt

with open(file_path,"r") as obj:
    for line in obj:
        
        curr_line = line.strip().split(' ')
        curr_line = [int(i) for i in curr_line]
        
        try:
            o_operator = get_operator(curr_line)
        except: continue

        if o_operator == '': continue
        
        elements_of_apply = int()
        v_cond = True
        len_of_curr_line = len(curr_line)
        counter = int()

        copy_curr_line = curr_line[:]
        
        while v_cond == True:
            counter += 1
            for index,value in enumerate(copy_curr_line[:-1]):
                if o_operator(value, copy_curr_line[index + 1]) and operator.le(abs( value - copy_curr_line[index + 1]), 3):
                    elements_of_apply += 1
                    v_cond = False if index == len(copy_curr_line) - 2 else True
                else:      
                    match counter:
                        case 1:
                            del copy_curr_line[index]
                            temp_index = index
                            elements_of_apply = 0
                            break
                        case 2:
                            copy_curr_line = curr_line[:]
                            elements_of_apply = 0
                            del copy_curr_line[temp_index + 1]
                            break
                        case 3:
                            v_cond = False
                            elements_of_apply = 0
                            break                            
        
        if elements_of_apply == len(copy_curr_line) - 1:
            summa += 1
        
print(summa)
