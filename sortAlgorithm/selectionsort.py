num = [2,4,82,15,36,1,36,95,24,36,24,25,85,45,157,56,6555,0,52,55]
n = len(num) 


for i in range(n):
    min_index = i
    for j in range(i+1,n):
        if num[j] < num[min_index]:
            min_index = j
    num[i],num[min_index] =  num[min_index], num[i]

print(num)        
