import csv

with open("SOCR-HeightWeight.csv",newline="") as f :
    reader=csv.reader(f)
    file_data=list(reader)
    file_data.pop(0)

new_data=[]
for i in range(len(file_data)) :
    num = file_data[i][2]
    new_data.append(float(num))

n=len(new_data)
new_data.sort()

print(new_data)

if n%2==0:
    median1=float (new_data[n//2])
    median2=float (new_data[n//2-1])
    median=(median1+median2)/2
else:
    median=float(new_data[n//2])
    print(n)
print("Median is:"+" "+str(median))
