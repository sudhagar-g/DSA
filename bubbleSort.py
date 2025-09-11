num = [2,4,82,15,36,1,36,95,24,36,24,25,85,45,157,56,6555,0,52,55]
n = len(num) 

for i in range(n-1):
    swap = False
    for j in range(n-i-1):
        if num[j] > num[j+1]:
            num[j],num[j+1] = num[j+1],num[j]
            swap = True

    if not swap:
        break        
print(num)            

