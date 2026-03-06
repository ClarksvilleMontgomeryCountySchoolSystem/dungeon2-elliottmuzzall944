good = r"""
                                                       ,jf
   _am,    ,_am,  ,_g_oam,    _am,   _g_ag,   _am,   koewkovg   _mm_
 ,gF  @._-gF   @-"  jf   @  ,gF  @  ^ NX  #_,gF  @     jf      qK  "
 8Y      8Y    d   j#   jF .8Y  ,d   dY     8Y   d    jf       *b,
jK   ,  jK   ,N   jN   jF  :K  ,Z  ,jF     jK  ,Z"  ,jfk,       dN.
 NbpP    NbpP    dP   dFk_o8NbpP"V^dF       NbpY"V^"dF "dYo-"*h,W"
                         ,gF',@'
                        :8K  j8
                         "*w*"
"""
bad = r"""


     _                                                 _.--.    __  _
    | |                                               ) \   `.,'  \| |
    | |                                            (`'       |     : |
    | |                             _..-.-.-.-._    )     ,),'.    | |
    | |('.                    __..-' ) ) ) ) ) )``-'    _.-| \     | |
    | | \ `...------''``--'''' \   )_____....---     ,''           ; |
    | |_(_..-......_________..._,-'_,..__....____..-'.._________..'| |
    | |____________________________________________________________| |
  __|_|_________________________________________________________SSt|_|__
"""
escaped = True
if escaped:
    outcome = "Legend: Congratulations! You have escaped!"
    print(good)
else:
    outcome = "Doom: You shall face death now!"
    print(bad)
print(outcome)