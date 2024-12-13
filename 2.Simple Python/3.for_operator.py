i=0
n=5
while i<n:
    print(f"i = {i+1}")
    i+=1 # C# i++ == i+=1

#масив значень від 1 до 10
mas = range(1,10)
print("Ось так працює for(foreach)")
for item in mas:
    if item==3:
        continue
    print(item)

#break - перериває цикл
#continue - повтор до умови - на нову ітерацію