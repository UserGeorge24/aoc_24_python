file_path = "C:\\Users\\szita001\\Desktop\\advent\\2024_12_01_01.txt"

col_1 = []
col_2 = []
summa = 0

with open(file_path,"r") as obj:
    for line in obj:
        temp = line.split(" ")
        col_1.append(int(temp[0]))
        col_2.append(int(temp[3].strip()))

for value in col_1:
    summa = summa + ( ( col_2.count(value) * value ) if col_2.count(value) != 0 else 0 )
