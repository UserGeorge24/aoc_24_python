def make_pairs(updates): 
    pairs_temp = []
    for index,update in enumerate(updates):
        try:    
            for value in updates[index+1:]:
                pairs_temp.append([update])
                pairs_temp[len(pairs_temp)-1].append(value)
        except: continue        
    return pairs_temp

file_path = "C:\\Users\\szita001\\Desktop\\advent\\2024_12_05.txt"
file = [ line.strip() for line in open(file_path,'r').readlines() ]
summa = 0

page_ordering_rules = []
forward_pairs = []

for index,value in enumerate(file):
    if value == '': break
    page_ordering_rules.append([int(value[0:2])])
    page_ordering_rules[index].append(int(value[3:5]))

for value in file[::-1]:
    if value == '': break
    
    updates = value.split(',')
    updates = [int(i) for i in updates]
    
    try_to_fix_flag = False
        
    while True:

        forward_pairs  = make_pairs(updates)
       
        intersect_values_of_forward = list(filter(lambda x: x in page_ordering_rules, forward_pairs))
        
        if len(forward_pairs) == len(intersect_values_of_forward):
            if try_to_fix_flag == True:
               summa += int(updates[int((len(updates)-1)/2)])
            break
        else:
            try_to_fix_flag = True 
            
            diff = list(filter(lambda x: x not in intersect_values_of_forward, forward_pairs))
            
            for i in diff:
                to_be_replaced_01 = int(i[0])
                to_be_replaced_02 = int(i[1])
                index_of_first  = updates.index(to_be_replaced_01)
                index_of_second = updates.index(to_be_replaced_02)
                updates[index_of_first]  = to_be_replaced_02
                updates[index_of_second] = to_be_replaced_01
       
print(summa)
