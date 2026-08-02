# Define sample friend sets
list_A = {"Alice", "Bob", "Charlie", "David"}
list_B = {"Charlie", "David", "Eve", "Frank"}

# Common friends (intersection)
common = list_A.intersection(list_B)
print("Common friends:", common)

# Friends only in list A (difference)
only_A = list_A.difference(list_B)
print("Friends only in A:", only_A)

# All unique friends (union)
all_friends = list_A.union(list_B)
print("All unique friends:", all_friends)
