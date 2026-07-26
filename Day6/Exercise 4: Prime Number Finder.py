start = int(input("Start: "))
end = int(input("End: "))

print("Prime numbers: ", end="")

for num in range(start, end + 1):
    if num <= 1:
        continue
    
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
            
    if is_prime:
        print(num, end=" ")
print() 
