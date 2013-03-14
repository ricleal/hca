

class SpaceGroups :
    """
    
    """
    
    sgList = [[1,1,1,"P1","PG1","TRICLINIC","P 1"],\
        [2,2,2,"P-1","PG1bar","TRICLINIC","P -1"],\
        [3,2,2,"P2","PG2","MONOCLINIC","P 1 2 1"],\
        [4,2,2,"P21","PG2","MONOCLINIC","P 1 21 1"],\
        [5,4,2,"C2","PG2","MONOCLINIC","C 1 2 1"],\
        [6,2,2,"Pm","PGm","MONOCLINIC","P 1 m 1"],\
        [7,2,2,"Pc","PGm","MONOCLINIC","P 1 c 1"],\
        [8,4,2,"Cm","PGm","MONOCLINIC","C 1 m 1"],\
        [9,4,2,"Cc","PGm","MONOCLINIC","C 1 c 1"],\
        [10,4,4,"P2/m","PG2/m","MONOCLINIC","P 1 2/m 1"],\
        [11,4,4,"P21/m","PG2/m","MONOCLINIC","P 1 21/m 1"],\
        [12,8,4,"C2/m","PG2/m","MONOCLINIC","C 1 2/m 1"],\
        [13,4,4,"P2/c","PG2/m","MONOCLINIC","P 1 2/c 1"],\
        [14,4,4,"P21/c","PG2/m","MONOCLINIC","P 1 21/c 1"],\
        [15,8,4,"C2/c","PG2/m","MONOCLINIC","C 1 2/c 1"],\
        [16,4,4,"P222","PG222","ORTHORHOMBIC","P 2 2 2"],\
        [17,4,4,"P2221","PG222","ORTHORHOMBIC","P 2 2 21"],\
        [18,4,4,"P21212","PG222","ORTHORHOMBIC","P 21 21 2"],\
        [19,4,4,"P212121","PG222","ORTHORHOMBIC","P 21 21 21"],\
        [20,8,4,"C2221","PG222","ORTHORHOMBIC","C 2 2 21"],\
        [21,8,4,"C222","PG222","ORTHORHOMBIC","C 2 2 2"],\
        [22,16,4,"F222","PG222","ORTHORHOMBIC","F 2 2 2"],\
        [23,8,4,"I222","PG222","ORTHORHOMBIC","I 2 2 2"],\
        [24,8,4,"I212121","PG222","ORTHORHOMBIC","I 21 21 21"],\
        [25,4,4,"Pmm2","PGmm2","ORTHORHOMBIC","P m m 2"],\
        [26,4,4,"Pmc21","PGmm2","ORTHORHOMBIC","P m c 21"],\
        [27,4,4,"Pcc2","PGmm2","ORTHORHOMBIC","P c c 2"],\
        [28,4,4,"Pma2","PGmm2","ORTHORHOMBIC","P m a 2"],\
        [29,4,4,"Pca21","PGmm2","ORTHORHOMBIC","P c a 21"],\
        [30,4,4,"Pnc2","PGmm2","ORTHORHOMBIC","P n c 2"],\
        [31,4,4,"Pmn21","PGmm2","ORTHORHOMBIC","P m n 21"],\
        [32,4,4,"Pba2","PGmm2","ORTHORHOMBIC","P b a 2"],\
        [33,4,4,"Pna21","PGmm2","ORTHORHOMBIC","P n a 21"],\
        [34,4,4,"Pnn2","PGmm2","ORTHORHOMBIC","P n n 2"],\
        [35,8,4,"Cmm2","PGmm2","ORTHORHOMBIC","C m m 2"],\
        [36,8,4,"Cmc21","PGmm2","ORTHORHOMBIC","C m c 21"],\
        [37,8,4,"Ccc2","PGmm2","ORTHORHOMBIC","C c c 2"],\
        [38,8,4,"Amm2","PGmm2","ORTHORHOMBIC","A m m 2"],\
        [39,8,4,"Abm2","PGmm2","ORTHORHOMBIC","A b m 2"],\
        [40,8,4,"Ama2","PGmm2","ORTHORHOMBIC","A m a 2"],\
        [41,8,4,"Aba2","PGmm2","ORTHORHOMBIC","A b a 2"],\
        [42,16,4,"Fmm2","PGmm2","ORTHORHOMBIC","F m m 2"],\
        [43,16,4,"Fdd2","PGmm2","ORTHORHOMBIC","F d d 2"],\
        [44,8,4,"Imm2","PGmm2","ORTHORHOMBIC","I m m 2"],\
        [45,8,4,"Iba2","PGmm2","ORTHORHOMBIC","I b a 2"],\
        [46,8,4,"Ima2","PGmm2","ORTHORHOMBIC","I m a 2"],\
        [47,8,8,"Pmmm","PGmmm","ORTHORHOMBIC","P 2/m 2/m 2/m","P m m m"],\
        [48,8,8,"Pnnn","PGmmm","ORTHORHOMBIC","P 2/n 2/n 2/n","P n n n"],\
        [49,8,8,"Pccm","PGmmm","ORTHORHOMBIC","P 2/c 2/c 2/m","P c c m"],\
        [50,8,8,"Pban","PGmmm","ORTHORHOMBIC","P 2/b 2/a 2/n","P b a n"],\
        [51,8,8,"Pmma","PGmmm","ORTHORHOMBIC","P 21/m 2/m 2/a","P m m a"],\
        [52,8,8,"Pnna","PGmmm","ORTHORHOMBIC","P 2/n 21/n 2/a","P n n a"],\
        [53,8,8,"Pmna","PGmmm","ORTHORHOMBIC","P 2/m 2/n 21/a","P m n a"],\
        [54,8,8,"Pcca","PGmmm","ORTHORHOMBIC","P 21/c 2/c 2/a","P c c a"],\
        [55,8,8,"Pbam","PGmmm","ORTHORHOMBIC","P 21/b 21/a 2/m","P b a m"],\
        [56,8,8,"Pccn","PGmmm","ORTHORHOMBIC","P 21/c 21/c 2/n","P c c n"],\
        [57,8,8,"Pbcm","PGmmm","ORTHORHOMBIC","P 2/b 21/c 21/m","P b c m"],\
        [58,8,8,"Pnnm","PGmmm","ORTHORHOMBIC","P 21/n 21/n 2/m","P n n m"],\
        [59,8,8,"Pmmn","PGmmm","ORTHORHOMBIC","P 21/m 21/m 2/n","P m m n"],\
        [60,8,8,"Pbcn","PGmmm","ORTHORHOMBIC","P 21/b 2/c 21/n","P b c n"],\
        [61,8,8,"Pbca","PGmmm","ORTHORHOMBIC","P 21/b 21/c 21/a","P b c a"],\
        [62,8,8,"Pnma","PGmmm","ORTHORHOMBIC","P 21/n 21/m 21/a","P n m a"],\
        [63,16,8,"Cmcm","PGmmm","ORTHORHOMBIC","C 2/m 2/c 21/m","C m c m"],\
        [64,16,8,"Cmca","PGmmm","ORTHORHOMBIC","C 2/m 2/c 21/a","C m c a"],\
        [65,16,8,"Cmmm","PGmmm","ORTHORHOMBIC","C 2/m 2/m 2/m","C m m m"],\
        [66,16,8,"Cccm","PGmmm","ORTHORHOMBIC","C 2/c 2/c 2/m","C c c m"],\
        [67,16,8,"Cmma","PGmmm","ORTHORHOMBIC","C 2/m 2/m 2/a","C m m a"],\
        [68,16,8,"Ccca","PGmmm","ORTHORHOMBIC","C 2/c 2/c 2/a","C c c a"],\
        [69,32,8,"Fmmm","PGmmm","ORTHORHOMBIC","F 2/m 2/m 2/m","F m m m"],\
        [70,32,8,"Fddd","PGmmm","ORTHORHOMBIC","F 2/d 2/d 2/d","F d d d"],\
        [71,16,8,"Immm","PGmmm","ORTHORHOMBIC","I 2/m 2/m 2/m","I m m m"],\
        [72,16,8,"Ibam","PGmmm","ORTHORHOMBIC","I 2/b 2/a 2/m","I b a m"],\
        [73,16,8,"Ibca","PGmmm","ORTHORHOMBIC","I 21/b 21/c 21/a","I b c a"],\
        [74,16,8,"Imma","PGmmm","ORTHORHOMBIC","I 21/m 21/m 21/a","I m m a"],\
        [75,4,4,"P4","PG4","TETRAGONAL","P 4"],\
        [76,4,4,"P41","PG4","TETRAGONAL","P 41"],\
        [77,4,4,"P42","PG4","TETRAGONAL","P 42"],\
        [78,4,4,"P43","PG4","TETRAGONAL","P 43"],\
        [79,8,4,"I4","PG4","TETRAGONAL","I 4"],\
        [80,8,4,"I41","PG4","TETRAGONAL","I 41"],\
        [81,4,4,"P-4","PG4bar","TETRAGONAL","P -4"],\
        [82,8,4,"I-4","PG4bar","TETRAGONAL","I -4"],\
        [83,8,8,"P4/m","PG4/m","TETRAGONAL","P 4/m"],\
        [84,8,8,"P42/m","PG4/m","TETRAGONAL","P 42/m"],\
        [85,8,8,"P4/n","PG4/m","TETRAGONAL","P 4/n"],\
        [86,8,8,"P42/n","PG4/m","TETRAGONAL","P 42/n"],\
        [87,16,8,"I4/m","PG4/m","TETRAGONAL","I 4/m"],\
        [88,16,8,"I41/a","PG4/m","TETRAGONAL","I 41/a"],\
        [89,8,8,"P422","PG422","TETRAGONAL","P 4 2 2"],\
        [90,8,8,"P4212","PG422","TETRAGONAL","P 4 21 2"],\
        [91,8,8,"P4122","PG422","TETRAGONAL","P 41 2 2"],\
        [92,8,8,"P41212","PG422","TETRAGONAL","P 41 21 2"],\
        [93,8,8,"P4222","PG422","TETRAGONAL","P 42 2 2"],\
        [94,8,8,"P42212","PG422","TETRAGONAL","P 42 21 2"],\
        [95,8,8,"P4322","PG422","TETRAGONAL","P 43 2 2"],\
        [96,8,8,"P43212","PG422","TETRAGONAL","P 43 21 2"],\
        [97,16,8,"I422","PG422","TETRAGONAL","I 4 2 2"],\
        [98,16,8,"I4122","PG422","TETRAGONAL","I 41 2 2"],\
        [99,8,8,"P4mm","PG4mm","TETRAGONAL","P 4 m m"],\
        [100,8,8,"P4bm","PG4mm","TETRAGONAL","P 4 b m"],\
        [101,8,8,"P42cm","PG4mm","TETRAGONAL","P 42 c m"],\
        [102,8,8,"P42nm","PG4mm","TETRAGONAL","P 42 n m"],\
        [103,8,8,"P4cc","PG4mm","TETRAGONAL","P 4 c c"],\
        [104,8,8,"P4nc","PG4mm","TETRAGONAL","P 4 n c"],\
        [105,8,8,"P42mc","PG4mm","TETRAGONAL","P 42 m c"],\
        [106,8,8,"P42bc","PG4mm","TETRAGONAL","P 42 b c"],\
        [107,16,8,"I4mm","PG4mm","TETRAGONAL","I 4 m m"],\
        [108,16,8,"I4cm","PG4mm","TETRAGONAL","I 4 c m"],\
        [109,16,8,"I41md","PG4mm","TETRAGONAL","I 41 m d"],\
        [110,16,8,"I41cd","PG4mm","TETRAGONAL","I 41 c d"],\
        [111,8,8,"P-42m","PG4bar2m","TETRAGONAL","P -4 2 m"],\
        [112,8,8,"P-42c","PG4bar2m","TETRAGONAL","P -4 2 c"],\
        [113,8,8,"P-421m","PG4bar2m","TETRAGONAL","P -4 21 m"],\
        [114,8,8,"P-421c","PG4bar2m","TETRAGONAL","P -4 21 c"],\
        [115,8,8,"P-4m2","PG4barm2","TETRAGONAL","P -4 m 2"],\
        [116,8,8,"P-4c2","PG4barm2","TETRAGONAL","P -4 c 2"],\
        [117,8,8,"P-4b2","PG4barm2","TETRAGONAL","P -4 b 2"],\
        [118,8,8,"P-4n2","PG4barm2","TETRAGONAL","P -4 n 2"],\
        [119,16,8,"I-4m2","PG4barm2","TETRAGONAL","I -4 m 2"],\
        [120,16,8,"I-4c2","PG4barm2","TETRAGONAL","I -4 c 2"],\
        [121,16,8,"I-42m","PG4bar2m","TETRAGONAL","I -4 2 m"],\
        [122,16,8,"I-42d","PG4bar2m","TETRAGONAL","I -4 2 d"],\
        [123,16,16,"P4/mmm","PG4/mmm","TETRAGONAL","P 4/m 2/m 2/m","P4/m m m"],\
        [124,16,16,"P4/mcc","PG4/mmm","TETRAGONAL","P 4/m 2/c 2/c","P4/m c c"],\
        [125,16,16,"P4/nbm","PG4/mmm","TETRAGONAL","P 4/n 2/b 2/m","P4/n b m"],\
        [126,16,16,"P4/nnc","PG4/mmm","TETRAGONAL","P 4/n 2/n 2/c","P4/n n c"],\
        [127,16,16,"P4/mbm","PG4/mmm","TETRAGONAL","P 4/m 21/b 2/m","P4/m b m"],\
        [128,16,16,"P4/mnc","PG4/mmm","TETRAGONAL","P 4/m 21/n 2/c","P4/m n c"],\
        [129,16,16,"P4/nmm","PG4/mmm","TETRAGONAL","P 4/n 21/m 2/m","P4/n m m"],\
        [130,16,16,"P4/ncc","PG4/mmm","TETRAGONAL","P 4/n 2/c 2/c","P4/n c c"],\
        [131,16,16,"P42/mmc","PG4/mmm","TETRAGONAL","P 42/m 2/m 2/c","P42/m m c"],\
        [132,16,16,"P42/mcm","PG4/mmm","TETRAGONAL","P 42/m 2/c 2/m","P42/m c m"],\
        [133,16,16,"P42/nbc","PG4/mmm","TETRAGONAL","P 42/n 2/b 2/c","P42/n b c"],\
        [134,16,16,"P42/nnm","PG4/mmm","TETRAGONAL","P 42/n 2/n 2/m","P42/n n m"],\
        [135,16,16,"P42/mbc","PG4/mmm","TETRAGONAL","P 42/m 21/b 2/c","P42/m b c"],\
        [136,16,16,"P42/mnm","PG4/mmm","TETRAGONAL","P 42/m 21/n 2/m","P42/m n m"],\
        [137,16,16,"P42/nmc","PG4/mmm","TETRAGONAL","P 42/n 21/m 2/c","P42/n m c"],\
        [138,16,16,"P42/ncm","PG4/mmm","TETRAGONAL","P 42/n 21/c 2/m","P42/n c m"],\
        [139,32,16,"I4/mmm","PG4/mmm","TETRAGONAL","I 4/m 2/m 2/m","I4/m m m"],\
        [140,32,16,"I4/mcm","PG4/mmm","TETRAGONAL","I 4/m 2/c 2/m","I4/m c m"],\
        [141,32,16,"I41/amd","PG4/mmm","TETRAGONAL","I 41/a 2/m 2/d","I41/a m d"],\
        [142,32,16,"I41/acd","PG4/mmm","TETRAGONAL","I 41/a 2/c 2/d","I41/a c d"],\
        [143,3,3,"P3","PG3","TRIGONAL","P 3"],\
        [144,3,3,"P31","PG3","TRIGONAL","P 31"],\
        [145,3,3,"P32","PG3","TRIGONAL","P 32"],\
        [146,9,3,"H3","PG3","TRIGONAL","H 3"],\
        [1146,3,3,"R3","PG3","TRIGONAL","R 3"],\
        [147,6,6,"P-3","PG3bar","TRIGONAL","P -3"],\
        [148,18,6,"H-3","PG3bar","TRIGONAL","H -3"],\
        [1148,6,6,"R-3","PG3bar","TRIGONAL","R -3"],\
        [149,6,6,"P312","PG312","TRIGONAL","P 3 1 2"],\
        [150,6,6,"P321","PG321","TRIGONAL","P 3 2 1"],\
        [151,6,6,"P3112","PG312","TRIGONAL","P 31 1 2"],\
        [152,6,6,"P3121","PG321","TRIGONAL","P 31 2 1"],\
        [153,6,6,"P3212","PG312","TRIGONAL","P 32 1 2"],\
        [154,6,6,"P3221","PG321","TRIGONAL","P 32 2 1"],\
        [155,18,6,"H32","PG321","TRIGONAL","H 3 2"],\
        [1155,6,6,"R32","PG32","TRIGONAL","R 3 2"],\
        [156,6,6,"P3m1","PG3m1","TRIGONAL","P 3 m 1"],\
        [157,6,6,"P31m","PG31m","TRIGONAL","P 3 1 m"],\
        [158,6,6,"P3c1","PG3m1","TRIGONAL","P 3 c 1"],\
        [159,6,6,"P31c","PG31m","TRIGONAL","P 3 1 c"],\
        [160,18,6,"H3m","PG3m","TRIGONAL","H 3 m"],\
        [1160,6,6,"R3m","PG3m","TRIGONAL","R 3 m"],\
        [161,18,6,"H3c","PG3m","TRIGONAL","H 3 c"],\
        [1161,6,6,"R3c","PG3m","TRIGONAL","R 3 c"],\
        [162,12,12,"P-31m","PG3bar1m","TRIGONAL","P -3 1 2/m","P -3 1 m"],\
        [163,12,12,"P-31c","PG3bar1m","TRIGONAL","P -3 1 2/c","P -3 1 c"],\
        [164,12,12,"P-3m1","PG3barm1","TRIGONAL","P -3 2/m 1","P -3 m 1"],\
        [165,12,12,"P-3c1","PG3barm1","TRIGONAL","P -3 2/c 1","P -3 c 1"],\
        [166,36,12,"H-3m","PG3barm","TRIGONAL","H -3 2/m","H -3 m"],\
        [1166,12,12,"R-3m","PG3barm","TRIGONAL","R -3 2/m","R -3 m"],\
        [167,36,12,"H-3c","PG3barm","TRIGONAL","H -3 2/c","H -3 c"],\
        [1167,12,12,"R-3c","PG3barm","TRIGONAL","R -3 2/c","R -3 c"],\
        [168,6,6,"P6","PG6","HEXAGONAL","P 6"],\
        [169,6,6,"P61","PG6","HEXAGONAL","P 61"],\
        [170,6,6,"P65","PG6","HEXAGONAL","P 65"],\
        [171,6,6,"P62","PG6","HEXAGONAL","P 62"],\
        [172,6,6,"P64","PG6","HEXAGONAL","P 64"],\
        [173,6,6,"P63","PG6","HEXAGONAL","P 63"],\
        [174,6,6,"P-6","PG6bar","HEXAGONAL","P -6"],\
        [175,12,12,"P6/m","PG6/m","HEXAGONAL","P 6/m"],\
        [176,12,12,"P63/m","PG6/m","HEXAGONAL","P 63/m"],\
        [177,12,12,"P622","PG622","HEXAGONAL","P 6 2 2"],\
        [178,12,12,"P6122","PG622","HEXAGONAL","P 61 2 2"],\
        [179,12,12,"P6522","PG622","HEXAGONAL","P 65 2 2"],\
        [180,12,12,"P6222","PG622","HEXAGONAL","P 62 2 2"],\
        [181,12,12,"P6422","PG622","HEXAGONAL","P 64 2 2"],\
        [182,12,12,"P6322","PG622","HEXAGONAL","P 63 2 2"],\
        [183,12,12,"P6mm","PG6mm","HEXAGONAL","P 6 m m"],\
        [184,12,12,"P6cc","PG6mm","HEXAGONAL","P 6 c c"],\
        [185,12,12,"P63cm","PG6mm","HEXAGONAL","P 63 c m"],\
        [186,12,12,"P63mc","PG6mm","HEXAGONAL","P 63 m c"],\
        [187,12,12,"P-6m2","PG6barm2","HEXAGONAL","P -6 m 2"],\
        [188,12,12,"P-6c2","PG6barm2","HEXAGONAL","P -6 c 2"],\
        [189,12,12,"P-62m","PG6bar2m","HEXAGONAL","P -6 2 m"],\
        [190,12,12,"P-62c","PG6bar2m","HEXAGONAL","P -6 2 c"],\
        [191,24,24,"P6/mmm","PG6/mmm","HEXAGONAL","P 6/m 2/m 2/m","P 6/m m m"],\
        [192,24,24,"P6/mcc","PG6/mmm","HEXAGONAL","P 6/m 2/c 2/c","P 6/m c c"],\
        [193,24,24,"P63/mcm","PG6/mmm","HEXAGONAL","P 63/m 2/c 2/m","P 63/m c m"],\
        [194,24,24,"P63/mmc","PG6/mmm","HEXAGONAL","P 63/m 2/m 2/c","P 63/m m c"],\
        [195,12,12,"P23","PG23","CUBIC","P 2 3"],\
        [196,48,12,"F23","PG23","CUBIC","F 2 3"],\
        [197,24,12,"I23","PG23","CUBIC","I 2 3"],\
        [198,12,12,"P213","PG23","CUBIC","P 21 3"],\
        [199,24,12,"I213","PG23","CUBIC","I 21 3"],\
        [200,24,24,"Pm-3","PGm3bar","CUBIC","P 2/m -3","P m -3"],\
        [201,24,24,"Pn-3","PGm3bar","CUBIC","P 2/n -3","P n -3"],\
        [202,96,24,"Fm-3","PGm3bar","CUBIC","F 2/m -3","F m -3"],\
        [203,96,24,"Fd-3","PGm3bar","CUBIC","F 2/d -3","F d -3"],\
        [204,48,24,"Im-3","PGm3bar","CUBIC","I 2/m -3","I m -3"],\
        [205,24,24,"Pa-3","PGm3bar","CUBIC","P 21/a -3","P a -3"],\
        [206,48,24,"Ia-3","PGm3bar","CUBIC","I 21/a -3","I a -3"],\
        [207,24,24,"P432","PG432","CUBIC","P 4 3 2"],\
        [208,24,24,"P4232","PG432","CUBIC","P 42 3 2"],\
        [209,96,24,"F432","PG432","CUBIC","F 4 3 2"],\
        [210,96,24,"F4132","PG432","CUBIC","F 41 3 2"],\
        [211,48,24,"I432","PG432","CUBIC","I 4 3 2"],\
        [212,24,24,"P4332","PG432","CUBIC","P 43 3 2"],\
        [213,24,24,"P4132","PG432","CUBIC","P 41 3 2"],\
        [214,48,24,"I4132","PG432","CUBIC","I 41 3 2"],\
        [215,24,24,"P-43m","PG4bar3m","CUBIC","P -4 3 m"],\
        [216,96,24,"F-43m","PG4bar3m","CUBIC","F -4 3 m"],\
        [217,48,24,"I-43m","PG4bar3m","CUBIC","I -4 3 m"],\
        [218,24,24,"P-43n","PG4bar3m","CUBIC","P -4 3 n"],\
        [219,96,24,"F-43c","PG4bar3m","CUBIC","F -4 3 c"],\
        [220,48,24,"I-43d","PG4bar3m","CUBIC","I -4 3 d"],\
        [221,48,48,"Pm-3m","PGm3barm","CUBIC","P 4/m -3 2/m","P m -3 m"],\
        [221,48,48,"Pm-3m","PGm3barm","CUBIC,'P 4/m -3 2/m","P m -3 m"],\
        [222,48,48,"Pn-3n","PGm3barm","CUBIC,'P 4/n -3 2/n' P n -3 n"],\
        [223,48,48,"Pm-3n","PGm3barm","CUBIC,'P 42/m -3 2/n","P m -3 n"],\
        [224,48,48,"Pn-3m","PGm3barm","CUBIC","P 42/n -3 2/m","P n -3 m"],\
        [225,192,48,"Fm-3m","PGm3barm","CUBIC","F 4/m -3 2/m","F m -3 m"],\
        [226,192,48,"Fm-3c","PGm3barm","CUBIC","F 4/m -3 2/c","F m -3 c"],\
        [227,192,48,"Fd-3m","PGm3barm","CUBIC","F 41/d -3 2/m","F d -3 m"],\
        [228,192,48,"Fd-3c","PGm3barm","CUBIC","F 41/d -3 2/c","F d -3 c"],\
        [229,96,48,"Im-3m","PGm3barm","CUBIC","I 4/m -3 2/m","I m -3 m"],\
        [230,96,48,"Ia-3d","PGm3barm","CUBIC","I 41/a -3 2/d","I a -3 d"] ]
    
    @staticmethod
    def getSpaceGroupNumber(spaceGroupName):
        
        spaceGroupNameNoSpaces = spaceGroupName.replace(' ','')
        
        for el in SpaceGroups.sgList :
            if el[3] ==  spaceGroupNameNoSpaces or el[6].replace(' ','') == spaceGroupName :
                return el[0]
        return None
    
    
if __name__ == "__main__":
    
    spt = 'P 21 21 21'
    spn = SpaceGroups.getSpaceGroupNumber(spt)
    print spt, " --> " , spn 
    
    spt = 'I 213'
    spn = SpaceGroups.getSpaceGroupNumber(spt)
    print spt, " --> " , spn 

    spt = 'P2'
    spn = SpaceGroups.getSpaceGroupNumber(spt)
    print spt, " --> " , spn 




    

