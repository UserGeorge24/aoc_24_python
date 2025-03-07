
def make_pairs(updates): 
    forward_pairs_temp = []
    for index,update in enumerate(updates):
        try:    
            for value in updates[index+1:len(updates)]:
                forward_pairs_temp.append([int(update)])
                forward_pairs_temp[len(forward_pairs_temp)-1].append(int(value))
        except: continue        
    return forward_pairs_temp

def is_fit_to_rule(pairs):
    global page_ordering_rules
    for row in pairs:
        try:
            if page_ordering_rules.count(row) == 0:
                return False
        except: continue
    return True

file_path = "C:\\Users\\szita001\\Desktop\\advent\\2024_12_05.txt"
file = [ line.strip() for line in open(file_path,'r').readlines() ]
summa = 0

page_ordering_rules = []
forward_pairs = []
backward_pairs = []

for index,value in enumerate(file):
    if value == '': break
    page_ordering_rules.append([int(value[0:2])])
    page_ordering_rules[index].append(int(value[3:5]))
    
for value in file[::-1]:
    if value == '': break
    
    updates = value.split(',')
    
    forward_pairs  = make_pairs(updates)
    updates.reverse()
    backward_pairs = make_pairs(updates)
    
    if is_fit_to_rule(forward_pairs) == True and is_fit_to_rule(forward_pairs) == True:
        summa += int(updates[int((len(updates)-1)/2)])
    else: continue

print(summa)
