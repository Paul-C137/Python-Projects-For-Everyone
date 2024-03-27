char_name = input(' Which character do you want to know about? (Starlord, Mystique, Hulk) \n').lower().capitalize()
char_stat = input('What statistic do you want to know about? (real name, powers, archenemy) \n').lower()

marvelchars= {
        "Starlord":
            {"real name": "peter quill",
            "powers": "dance moves",
            "archenemy": "Thanos"},

        "Mystique":
            {"real name": "raven darkholme",
            "powers": "shape shifter",
            "archenemy": "Professor X"},

        "Hulk":
        {"real name": "bruce banner",
        "powers": "super strength",
        "archenemy": "adrenaline"}
                }

selected_char_dict = marvelchars[char_name]
selected_stat = selected_char_dict[char_stat] 

cap_char_name = char_name.capitalize()       

print(f'{cap_char_name}\'s {char_stat} is:  {selected_stat.title()}')