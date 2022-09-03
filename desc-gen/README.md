# Anise kbd desc format

file type: json

keys:
- `name`: name of keyboard
- `type`: not used for now, should be filled with gh60 like etc.
- `layout`: two-dimensional array, stores key width(4 stands for 1u, 5 stands for 1.25u ..., 4.5 stand for numpad ret and plus, 5.5 stands for EU/JP style return, `"2"` stand for skip, `-2` stands for split gap )
- `num_rc`: `[num_of_row, num_of_column]`
- `key_matrix`: two-dimensional array, num of row and each num of column should be same as `layout`, stores each key row-colomn index (count from 1) in layout.
- `led_conn`: two arrays, stores 2812-like led connection sequence, 11 stands for row1 column1, 514 stands for row5 column14.
- `conndef`: specify btb connector sequence. 

sample desc file:
```
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
```
