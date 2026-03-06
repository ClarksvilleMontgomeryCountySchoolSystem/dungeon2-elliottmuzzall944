good = r"""
                              z
                             z
                              Z
                    .--.  Z Z
                   / _(c\   .-.     __
                  | / /  '-;   \'-'`  `\______
                  \_\/'/ __/ )  /  )   |      \--,
                  | \`""`__-/ .'--/   /--------\  \
                   \\`  ///-\/   /   /---;-.    '-'
             jgs                (________\  \
                                          '-'
"""
bad = r"""

                        ,////,
                        /// 6|
                        //  _|
                       _/_,-'
                  _.-/'/   \   ,/;,
               ,-' /'  \_   \ / _/
               `\ /     _/\  ` /
                 |     /,  `\_/
                 |     \'
 pb  /\_        /`      /\
   /' /_``--.__/\  `,. /  \
  |_/`  `-._     `\/  `\   `.
            `-.__/'     `\   |
                          `\  \
                            `\ \
                              \_\__
                               \___)
"""
guard_awake = False
if not guard_awake:
    outcome = "Shadow: He is not awake! You better be quiet"
    print(good)
else:
    outcome = "Doom: You better run or find a place to hide before he finds you!"
    print(bad)
print(outcome)