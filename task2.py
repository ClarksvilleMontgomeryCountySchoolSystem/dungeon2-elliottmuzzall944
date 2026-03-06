good = r"""
 __
                  /o \_____
                  \__/-="="`
"""
bad = r"""
            __________
           |  __  __  |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |  __  __()|
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
ejm        |__________|
"""
has_key = True
if has_key:
    outcome = "Click: you may enter the door"
    print(good)
else:
    outcome = "Doom: Oh no! You better find the key!"
    print(bad)
print(outcome)
