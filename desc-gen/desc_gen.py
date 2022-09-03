#!/usr/bin/env python3

import json

x = "X"
default_conndef = [
    #    1     2  3  4     5  6  7  8
    ["VCC","GND", x, x,"led1", x, x, x,
    "r1", "r2", "r3", "r4", "r5", x, # 14
    "c1", "c2", "c3", "c4", "c5", "c6", "c7", x, # 22
    x, x, x, x, x, x, x, x], #30
    #    1     2  3  4     5  6  7  8
    ["VCC","GND", x, x,"led2", x, x, x,
    "r1", "r2", "r3", "r4", "r5", x, # 14
    "c7", "c8", "c9", "c10", "c11", "c12", "c13", "c14", # 22
    x, x, x, x, x, x, x, x] #30
]

default_conndef_wi2c = [
    #    1     2  3  4      5       6       7  8
    ["VCC","GND", x, "sdaL","led1", "sclL", x, x,
    "r1", "r2", "r3", "r4", "r5", x, # 14
    "c1", "c2", "c3", "c4", "c5", "c6", "c7", x, # 22
    x, x, x, x, x, x, x, x], #30
    #    1     2  3  4       5      6       7  8
    ["VCC","GND", x, "sdaR","led2", "sclR", x, x,
    "r1", "r2", "r3", "r4", "r5", x, # 14
    "c7", "c8", "c9", "c10", "c11", "c12", "c13", "c14", # 22
    x, x, x, x, x, x, x, x] #30
]

default_desc = {
    "name" : "default",
    "type" : "gh60 like",
    "layout" : [
    #esc 1  2  3  4  5  6      7  8  9  0  -  = bks
    [4,  4, 4, 4, 4, 4, 4, -2, 4, 4, 4, 4, 4, 4, 8],
    #tab q  w  e  r  t      y  u  i  o  p  [  ]  \
    [6,  4, 4, 4, 4, 4, -2, 4, 4, 4, 4, 4, 4, 4, 6],
    #cap a  s  d  f  g       h  j  k  l  ;  '  ret
    [7,  4, 4, 4, 4, 4, -2,  4, 4, 4, 4, 4, 4, 9],
    #LSH z  x  c  v  b        n  m  ,  .  /  rsh
    [9,  4, 4, 4, 4, 4, -2,   4, 4, 4, 4, 4, 11],
    #_   C  W  A  S  *        S  F  A  M  C  _
    ["2", 5, 5, 5, 8, 4, -2,  8, 5, 5, 5, 5, "3"]
    ],
    "num_rc": [5, 14],
    "key_matrix": [
    # esc   1     2     3     4     5   / 6   / 7     8     9      0      -      =      bks
    [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7],[1,8],[1,9],[1,10],[1,11],[1,12],[1,13],[1,14]],
    # tab    q     w     e     r     t   / y     u     i     o      p      [      ]      \
    [[2,1], [2,2],[2,3],[2,4],[2,5],[2,6],[2,7],[2,8],[2,9],[2,10],[2,11],[2,12],[2,13],[2,14]],
    # cap      a     s     d     f     g   / h     j     k     l      ;      '           ret
    [[3,1],   [3,2],[3,3],[3,4],[3,5],[3,6],[3,7],[3,8],[3,9],[3,10],[3,11],[3,12],     [3,14]],
    # lsh         z     x     c     v     b   / n     m     ,      .      /             rsh
    [[4,1],      [4,3],[4,4],[4,5],[4,6],[4,7],[4,8],[4,9],[4,10],[4,11],[4,12],        [4,14]],
    #LCTL  LWIN  LALT         S           *   / S     RFUN         RALT   MENU   RCTL
    [[5,1],[5,2],[5,3],      [5,6],      [5,7],[5,8],[5,9],       [5,11],[5,12],[5,13]],
    ],
    "led_conn": [
        ["led1",17,16,15,14,13,12,11,21,22,23,24,25,26,36,35,34,33,32,31,41,43,44,45,46,47,57,56,53,52,51],
        ["led2",17,18,19,110,111,112,113,114,214,213,212,211,210,29,28,27,37,38,39,310,311,312,314,414,412,411,410,49,48,58,59,511,512,513],
    ],
    "conn_def": default_conndef,
}

dnav_desc = {
    "name" : "anysplit60-dnav",
    "type" : "gh60 like",
    "layout" : [
        #esc 1  2  3  4  5  6      7  8  9  0  -  = bks
        [4,  4, 4, 4, 4, 4, 4, -2, 4, 4, 4, 4, 4, 4, 8],
        #tab q  w  e  r  t      y  u  i  o  p  [  ]  \
        [6,  4, 4, 4, 4, 4, -2, 4, 4, 4, 4, 4, 4, 4, 6],
        #cap a  s  d  f  g      h  j  k  l  ;  '  ret
        [7,  4, 4, 4, 4, 4, -2, 4, 4, 4, 4, 4, 4, 9],
        #lsh z  x  c  v  b      n  m  ,  .  /      u       rsh
        [9,  4, 4, 4, 4, 4, -2, 4, 4, 4, 4, 4,"1", 4, "1", 5],
        #_   C  W  A  S  *       S  A  W       l  d  r
        ["2", 5, 5, 5, 8, 4, -2, 8, 4, 4, "1", 4, 4, 4, "2"]
    ],
    "num_rc": [5, 14],
    "key_matrix": [
    # esc   1     2     3     4     5   / 6   / 7     8     9      0      -      =      bks
    [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7],[1,8],[1,9],[1,10],[1,11],[1,12],[1,13],[1,14]],
    # tab    q     w     e     r     t   / y     u     i     o      p      [      ]      \
    [[2,1], [2,2],[2,3],[2,4],[2,5],[2,6],[2,7],[2,8],[2,9],[2,10],[2,11],[2,12],[2,13],[2,14]],
    # cap      a     s     d     f     g   / h     j     k     l      ;      '           ret
    [[3,1],   [3,2],[3,3],[3,4],[3,5],[3,6],[3,7],[3,8],[3,9],[3,10],[3,11],[3,12],     [3,14]],
    # lsh         z     x     c     v     b   / n     m     ,      .      /       u      rsh
    [[4,1],      [4,3],[4,4],[4,5],[4,6],[4,7],[4,8],[4,9],[4,10],[4,11],[4,12], [4,13], [4,14]],
    #LCTL  LWIN  LALT         S           *   / S     RFUN   RALT    l      d       r
    [[5,1],[5,2],[5,3],      [5,6],      [5,7],[5,8],[5,9], [5,11],[5,12],[5,13], [5,14]],
    ],
    "led_conn": [
        ["led1",17,16,15,14,13,12,11,21,22,23,24,25,26,36,35,34,33,32,31,41,43,44,45,46,47,57,56,53,52,51],
        ["led2",17,18,19,110,111,112,113,114,214,213,212,211,210,29,28,27,37,38,39,310,311,312,314,414,413,412,411,410,49,48,58,59,511,512,513,514],
    ],
    "conn_def": default_conndef_wi2c,
}

key_map_split_scad_hhkb = [
    #esc 1  2  3  4  5  6      7  8  9  0  -  =  `  \
    [4,  4, 4, 4, 4, 4, 4, -2, 4, 4, 4, 4, 4, 4, 4, 4],
    #tab q  w  e  r  t      y  u  i  o  p  [  ]  bks
    [6,  4, 4, 4, 4, 4, -2, 4, 4, 4, 4, 4, 4, 4, 6],
    #cap a  s  d  f  g      h  j  k  l  ;  '  ret
    [7,  4, 4, 4, 4, 4, -2, 4, 4, 4, 4, 4, 4, 9],
    #lsh z  x  c  v  b      n  m  ,  .  /  rsh, fn
    [9,  4, 4, 4, 4, 4, -2, 4, 4, 4, 4, 4, 7,  4],
    #_    A  W  S  S      S   W  A  _
    ["6", 4, 6, 9, 4, -2, 11, 6, 4, "10"]
]

key_map_split_scad_minila = [
    #esc 1  2  3  4  5  6      7  8  9  0  -  =  `  bks
    [4,  4, 4, 4, 4, 4, 4, -2, 4, 4, 4, 4, 4, 4, 4, 4],
    #tab q  w  e  r  t      y  u  i  o  p  [  ]  \
    [6,  4, 4, 4, 4, 4, -2, 4, 4, 4, 4, 4, 4, 4, 6],
    #cap a  s  d  f  g      h  j  k  l  ;  '  ret
    [7,  4, 4, 4, 4, 4, -2, 4, 4, 4, 4, 4, 4, 9],
    #lsh z  x  c  v  b      n  m  ,  .  /  rsh up rsh
    [8,  4, 4, 4, 4, 4, -2, 4, 4, 4, 4, 4, 4,  4, 4],
    #C   W  A  F  S         S  F  W  A  l  d  r
    [7,  5, 5, 5, 6,    -2, 6, 5, 5, 4, 4, 4, 4]
]

key_map_split_scad_minj = [
    #esc 1  2  3  4  5  6      7  8  9  0  -  =  `  bks
    [4,  4, 4, 4, 4, 4, 4, -2, 4, 4, 4, 4, 4, 4, 4, 4],
    #tab q  w  e  r  t      y  u  i  o  p  [  ]  ret
    [6,  4, 4, 4, 4, 4, -2, 4, 4, 4, 4, 4, 4, 4, "6"],
    #cap a  s  d  f  g      h  j  k  l  ;  '  \  ret
    [7,  4, 4, 4, 4, 4, -2, 4, 4, 4, 4, 4, 4, 4, 5.5],
    #lsh z  x  c  v  b      n  m  ,  .  /  rsh up rsh
    [8,  4, 4, 4, 4, 4, -2, 4, 4, 4, 4, 4, 4,  4, 4],
    #C   W  A  F  S         S  F  W  A  l  d  r
    [7,  5, 5, 5, 6,    -2, 6, 5, 5, 4, 4, 4, 4]
]

key_map_split_scad_poker = [
    #esc 1  2  3  4  5  6      7  8  9  0  -  = bks
    [4,  4, 4, 4, 4, 4, 4, -2, 4, 4, 4, 4, 4, 4, 8],
    #tab q  w  e  r  t      y  u  i  o  p  [  ]  \
    [6,  4, 4, 4, 4, 4, -2, 4, 4, 4, 4, 4, 4, 4, 6],
    #cap a  s  d  f  g      h  j  k  l  ;     ret
    [7,  4, 4, 4, 4, 4, -2, 4, 4, 4, 4, 4,    9],
    #lsh z  x  c  v  b      n  m  ,  .  /  rsh
    [9,  4, 4, 4, 4, 4, -2, 4, 4, 4, 4, 4, 11],
    # C  W  A  S  *         S  A  W  F  C
    [ 5, 5, 5, 9, 5,    -2, 11, 5, 5, 5, 5]
]

key_map_split_scad_poker_fn = [
    #esc 1  2  3  4  5  6      7  8  9  0  -  = bks
    [4,  4, 4, 4, 4, 4, 4, -2, 4, 4, 4, 4, 4, 4, 8],
    #tab q  w  e  r  t      y  u  i  o  p  [  ]  \
    [6,  4, 4, 4, 4, 4, -2, 4, 4, 4, 4, 4, 4, 4, 6],
    #cap a  s  d  f  g      h  j  k  l  ;     ret
    [7,  4, 4, 4, 4, 4, -2, 4, 4, 4, 4, 4,    9],
    #lsh z  x  c  v  b      n  m  ,  .  /  rsh fn
    [9,  4, 4, 4, 4, 4, -2, 4, 4, 4, 4, 4, 7,  4],
    # C  W  A  S  *         S  A  W  F  C
    [ 5, 5, 5, 9, 5,    -2, 11, 5, 5, 5, 5]
]

key_map_split_scad_poker_eu = [
    #esc 1  2  3  4  5  6      7  8  9  0  -  = bks
    [4,  4, 4, 4, 4, 4, 4, -2, 4, 4, 4, 4, 4, 4, 8],
    #tab q  w  e  r  t      y  u  i  o  p  [  ]  ret
    [6,  4, 4, 4, 4, 4, -2, 4, 4, 4, 4, 4, 4, 4, "6"],
    #cap a  s  d  f  g      h  j  k  l  ;  '  ret
    [7,  4, 4, 4, 4, 4, -2, 4, 4, 4, 4, 4, 4, 5.5],
    #lsh < z  x  c  v  b      n  m  ,  .  /  rsh
    [5, 4, 4, 4, 4, 4, 4, -2, 4, 4, 4, 4, 4, 11],
    # C  W  A  S  *         S  A  W  F  C
    [ 5, 5, 5, 9, 5,    -2, 11, 5, 5, 5, 5]
]

key_map_split_scad_poker_fn_eu = [
    #esc 1  2  3  4  5  6      7  8  9  0  -  = bks
    [4,  4, 4, 4, 4, 4, 4, -2, 4, 4, 4, 4, 4, 4, 8],
    #tab q  w  e  r  t      y  u  i  o  p  [  ]  ret
    [6,  4, 4, 4, 4, 4, -2, 4, 4, 4, 4, 4, 4, 4, "6"],
    #cap a  s  d  f  g      h  j  k  l  ;  '      ret
    [7,  4, 4, 4, 4, 4, -2, 4, 4, 4, 4, 4, 4,    5.5],
    #lsh < z  x  c  v  b      n  m  ,  .  /  rsh fn
    [5, 4, 4, 4, 4, 4, 4, -2, 4, 4, 4, 4, 4, 7,  4],
    # C  W  A  S  *         S  A  W  F  C
    [ 5, 5, 5, 9, 5,    -2, 11, 5, 5, 5, 5]
]

def gen_desc(name, desc, stab_type="plate", r4lshift=False, six2right=False):
    assert "layout" in desc
    assert "num_rc" in desc
    assert "key_matrix" in desc
    assert "led_conn" in desc
    assert "conn_def" in desc
    desc["stab_type"] = stab_type
    desc["r4lshift" ] = r4lshift
    desc["six2right"] = six2right
    with open(name + ".json", "w") as f: json.dump(desc, f)

if __name__ == "__main__":
    gen_desc("anysplit60-def", default_desc, "plate")
    gen_desc("anysplit60-dnav", dnav_desc, "plate")
    #gen_desc("anysplit60-happy", key_map_split_scad_hhkb, "plate")
    #gen_desc("anysplit60-poker", key_map_split_scad_poker, "plate")
    #gen_desc("anysplit60-minilike", key_map_split_scad_minila, "plate", r4lshift=True)
    #gen_desc("anysplit60-minij", key_map_split_scad_minj, "plate", r4lshift=True)
    pass
