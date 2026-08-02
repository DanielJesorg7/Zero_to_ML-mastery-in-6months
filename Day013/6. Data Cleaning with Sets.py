registered = [101, 102, 103, 104, 105]
attended = [102, 104, 105, 107, 108]

# Convert lists to sets for analysis
reg_set = set(registered)
att_set = set(attended)

# Who registered AND attended
print("Registered and attended:", reg_set.intersection(att_set))

# Who registered but did NOT attend
print("Registered but did not attend:", reg_set.difference(att_set))

# Who attended but did NOT register
print("Attended but did not register:", att_set.difference(reg_set))

# Total unique people involved
print("Total unique people:", reg_set.union(att_set))
