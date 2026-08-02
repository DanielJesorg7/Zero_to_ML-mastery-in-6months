import time

# Get input words from user
user_input = input("Enter words separated by spaces: ").split()

# 1. List method (Preserves original order)
start_list = time.perf_counter()
list_result = []
for word in user_input:
    if word not in list_result:
        list_result.append(word)
end_list = time.perf_counter()

# 2. Set method (Loses order, but executes faster)
start_set = time.perf_counter()
set_result = list(set(user_input))
end_set = time.perf_counter()

print("List method (Ordered):", list_result)
print("Set method (Unordered):", set_result)
print(f"List time: {end_list - start_list:.6f}s | Set time: {end_set - start_set:.6f}s")
