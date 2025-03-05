import re

def count_xmas(i_content):
    if len(re.findall('MAS',i_content)) != 0 or len(re.findall('MAS',i_content[::-1])) != 0:
        return True

file_path = "C:\\Users\\szita001\\Desktop\\advent\\2024_12_04.txt"
file = [ line.strip() for line in open(file_path,'r').readlines() ]
summa = 0

for index, value in enumerate(file):
    
    if index == 0: continue
    all_occ = re.finditer('A',value)
    
    for match in all_occ:
        if match.start() == 0: continue
        try:
            prev_row = file[index - 1]
            next_row = file[index + 1]
    #       Left up + middle + right bottom
            string_leftup = prev_row[match.start() - 1] + file[index][match.start()] + next_row[match.start() + 1]
    #       Left down + middle + right up
            string_rightup = next_row[match.start() - 1] + file[index][match.start()] + prev_row[match.start() + 1]

            summa = summa + 1 if count_xmas(string_leftup) == True and count_xmas(string_rightup) == True else summa
        except: continue
print(summa)
