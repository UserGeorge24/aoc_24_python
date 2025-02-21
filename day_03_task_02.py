import re

file_path = "C:\\Users\\szita001\\Desktop\\advent\\2024_12_03.txt"

summa = 0
file = open(file_path,"r").read()
all_matched_pattern_for_dont = re.split('don\'t\(\)', file)

for index_dont,matched_dont in enumerate(all_matched_pattern_for_dont):
    matched_pattern_for_do = re.split('do\(\)',matched_dont)
    if len(matched_pattern_for_do) == 1 and index_dont != 0: continue
    
    for index_do, matched_do in enumerate(matched_pattern_for_do):
        if len(matched_pattern_for_do) != 1 and index_do == 0: continue
        matched_pattern_to_mull =re.findall('mul\([0-9]{1,3},[0-9]{1,3}\)',matched_do) 
        
        for matched_mull in matched_pattern_to_mull:        
            numbers = re.findall('[0-9]{1,3}',matched_mull)
            summa += int(numbers[0]) * int(numbers[1])
        
print(summa)
