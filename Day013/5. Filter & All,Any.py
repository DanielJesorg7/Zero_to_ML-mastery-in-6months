results = [("Adeleke", 85), ("Daniel", 45), ("Sarah", 92)]

# 1. Use filter to get only passing students (score >= 60)
passing = list(filter(lambda x: x[1] >= 60, results))
print("Passing students:", passing)

# 2. Use all to check if everyone passed
everyone_passed = all(score >= 60 for name, score in results)
print("Did everyone pass?:", everyone_passed)

# 3. Use any to check if at least one person failed
someone_failed = any(score < 60 for name, score in results)
print("Did at least one person fail?:", someone_failed)
