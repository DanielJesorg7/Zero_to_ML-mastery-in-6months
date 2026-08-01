def running_average():
    total = 0.0
    count = 0
    current_avg = None
    
    while True:
        # Yield the current average and wait for the next number via .send()
        num = yield current_avg
        if num is not None:
            total += num
            count += 1
            current_avg = total / count

# Testing the generator
avg = running_average()
next(avg)  # Start generator (advances to the first yield)

print(avg.send(10))  # 10.0
print(avg.send(20))  # 15.0
print(avg.send(30))  # 20.0
