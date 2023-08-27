from mtgsdk import Set

sets = Set.all()
all_the_sets = []

for i in sets:
    all_the_sets.append(i.name)
all_the_sets.sort()
print(all_the_sets)
