import re

summa = 0
file = open(file_path,"r").read()
all_matched_pattern = re.findall('mul\([0-9]{1,3},[0-9]{1,3}\)', file)

for value in all_matched_pattern:
    numbers = re.findall('[0-9]{1,3}',value)
    summa += int(numbers[0]) * int(numbers[1])
        
print(summa)
