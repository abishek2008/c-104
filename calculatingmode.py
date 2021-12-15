import csv
from collections import Counter

with open("SOCR-HeightWeight.csv",newline="") as f :
    reader=csv.reader(f)
    file_data=list(reader)
    file_data.pop(0)

new_data=[]
for i in range(len(file_data)) :
    num = file_data[i][2]
    new_data.append(float(num))

data = Counter(new_data)
#print(data)
mode_data_for_range = {
                        "75-85": 0,
                        "85-95": 0,
                        "95-105": 0
                    }

#print(data.items())
for height, occurence in data.items():
    if 50 < float(height) < 60:
        mode_data_for_range["75-85"] += occurence
    elif 60 < float(height) < 70:
        mode_data_for_range["85-95"] += occurence
    elif 70 < float(height) < 80:
        mode_data_for_range["95-105"] += occurence


#print (mode_data_for_range.items())

mode_range, mode_occurence = 0, 0
for range, occurence in mode_data_for_range.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode = float((mode_range[0] + mode_range[1]) / 2)
print(f"Mode is -> {mode:2f}")