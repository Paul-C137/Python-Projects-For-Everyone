farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

'''for i in farms[0].get("agriculture"):
    print(i)

choice = input("Please choose a farm: (NE Farm, W Farm, or SE Farm) >>> ")
for i in farms:
    if choice in i.values():
        for i in i.get(f"agriculture"):
            print(f"There are {i} on the {choice}.")'''

vegetable_list = ["carrots", "celery"]

choice = input("Please choose a farm: (NE Farm, W Farm, or SE Farm) >>> ")
for i in farms:
    if choice in i.values():
        for i in i.get(f"agriculture"):
            if i not in vegetable_list:
                print(f"There are {i} on the {choice}.")
            else:
                continue
