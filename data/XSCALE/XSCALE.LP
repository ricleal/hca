
 ******************************************************************************
                    XSCALE (VERSION  December 31, 2011)           23-Mar-2012
 ******************************************************************************

 Author: Wolfgang Kabsch
 Copy licensed until (unlimited) to
  ESRF Grenoble, license MI 1318ZWT                
 No redistribution.


 ******************************************************************************
                              CONTROL CARDS
 ******************************************************************************

 OUTPUT_FILE=alldatasets.ahkl
 FRIEDEL'S_LAW= TRUE
   INPUT_FILE= ../XDS_FF101.HKL
     INCLUDE_RESOLUTION_RANGE=100 2.0
   INPUT_FILE= ../XDS_FF102.HKL
     INCLUDE_RESOLUTION_RANGE=100 2.0
   INPUT_FILE= ../XDS_FF103.HKL
     INCLUDE_RESOLUTION_RANGE=100 2.0
   INPUT_FILE= ../XDS_FF104.HKL
     INCLUDE_RESOLUTION_RANGE=100 2.0
   INPUT_FILE= ../XDS_FF106.HKL
     INCLUDE_RESOLUTION_RANGE=100 2.0
   INPUT_FILE= ../XDS_FF201.HKL
     INCLUDE_RESOLUTION_RANGE=100 2.0
   INPUT_FILE= ../XDS_FF202.HKL
     INCLUDE_RESOLUTION_RANGE=100 2.0
   INPUT_FILE= ../XDS_FF203.HKL
     INCLUDE_RESOLUTION_RANGE=100 2.0
   INPUT_FILE= ../XDS_FF204.HKL
     INCLUDE_RESOLUTION_RANGE=100 2.0
   INPUT_FILE= ../XDS_FF206.HKL
     INCLUDE_RESOLUTION_RANGE=100 2.0
   INPUT_FILE= ../XDS_FF301.HKL
     INCLUDE_RESOLUTION_RANGE=100 2.0
   INPUT_FILE= ../XDS_FF302.HKL
     INCLUDE_RESOLUTION_RANGE=100 2.0
   INPUT_FILE= ../XDS_FF303-2.HKL
     INCLUDE_RESOLUTION_RANGE=100 2.0
   INPUT_FILE= ../XDS_FF303-4.HKL
     INCLUDE_RESOLUTION_RANGE=100 2.0
   INPUT_FILE= ../XDS_FF305.HKL
     INCLUDE_RESOLUTION_RANGE=100 2.0
   INPUT_FILE= ../XDS_FF306.HKL
     INCLUDE_RESOLUTION_RANGE=100 2.0
   INPUT_FILE= ../XDS_FF307.HKL
     INCLUDE_RESOLUTION_RANGE=100 2.0
   INPUT_FILE= ../XDS_FF308.HKL
     INCLUDE_RESOLUTION_RANGE=100 2.0
   INPUT_FILE= ../XDS_FF310.HKL
     INCLUDE_RESOLUTION_RANGE=100 2.0

 THE DATA COLLECTION STATISTICS REPORTED BELOW ASSUMES:
 SPACE_GROUP_NUMBER=   96
 UNIT_CELL_CONSTANTS=    78.58    78.58    36.91  90.000  90.000  90.000

 *****  8 EQUIVALENT POSITIONS IN SPACE GROUP # 96 *****

    If x',y',z' is an equivalent position to x,y,z, then
        x'=x*ML(1)+y*ML( 2)+z*ML( 3)+ML( 4)/12.0
        y'=x*ML(5)+y*ML( 6)+z*ML( 7)+ML( 8)/12.0
        z'=x*ML(9)+y*ML(10)+z*ML(11)+ML(12)/12.0

    #    1  2  3  4    5  6  7  8    9 10 11 12 
    1    1  0  0  0    0  1  0  0    0  0  1  0
    2   -1  0  0  0    0 -1  0  0    0  0  1  6
    3    0 -1  0  6    1  0  0  6    0  0  1  9
    4    0  1  0  6   -1  0  0  6    0  0  1  3
    5    0  1  0  0    1  0  0  0    0  0 -1  0
    6    0 -1  0  0   -1  0  0  0    0  0 -1  6
    7   -1  0  0  6    0  1  0  6    0  0 -1  9
    8    1  0  0  6    0 -1  0  6    0  0 -1  3
 

 ALL DATA SETS WILL BE SCALED TO ../XDS_FF101.HKL                                  


 ******************************************************************************
                    READING INPUT REFLECTION DATA FILES
 ******************************************************************************


 DATA    MEAN       REFLECTIONS        INPUT FILE NAME
 SET# INTENSITY  ACCEPTED REJECTED
   1  0.1446E+04   115331      0  ../XDS_FF101.HKL                                  
   2  0.1414E+04   115775      0  ../XDS_FF102.HKL                                  
   3  0.1426E+04   114277      0  ../XDS_FF103.HKL                                  
   4  0.1411E+04   115103      0  ../XDS_FF104.HKL                                  
   5  0.1408E+04   115505      0  ../XDS_FF106.HKL                                  
   6  0.1414E+04   116430      0  ../XDS_FF201.HKL                                  
   7  0.1423E+04   116310      0  ../XDS_FF202.HKL                                  
   8  0.1398E+04   115972      0  ../XDS_FF203.HKL                                  
   9  0.1401E+04   115301      0  ../XDS_FF204.HKL                                  
  10  0.1410E+04   116215      0  ../XDS_FF206.HKL                                  
  11  0.1474E+04   111187      0  ../XDS_FF301.HKL                                  
  12  0.1418E+04   115948      0  ../XDS_FF302.HKL                                  
  13  0.1427E+04   115139      0  ../XDS_FF303-2.HKL                                
  14  0.1421E+04   116020      0  ../XDS_FF303-4.HKL                                
  15  0.1409E+04   115266      0  ../XDS_FF305.HKL                                  
  16  0.1444E+04   113936      0  ../XDS_FF306.HKL                                  
  17  0.1436E+04   114770      0  ../XDS_FF307.HKL                                  
  18  0.1442E+04   115343      0  ../XDS_FF308.HKL                                  
  19  0.1431E+04   116043      0  ../XDS_FF310.HKL                                  


 ******************************************************************************
                OVERALL SCALING AND CRYSTAL DISORDER CORRECTION
 ******************************************************************************

      CORRELATIONS BETWEEN INPUT DATA SETS AFTER CORRECTIONS

 DATA SETS  NUMBER OF COMMON  CORRELATION   RATIO OF COMMON   B-FACTOR
  #i   #j     REFLECTIONS     BETWEEN i,j  INTENSITIES (i/j)  BETWEEN i,j

    1    2        7915           0.996            1.0021         0.0058
    1    3        7914           0.992            1.0006        -0.0075
    2    3        7930           0.998            0.9962         0.0025
    1    4        7950           0.995            1.0016        -0.0105
    2    4        7966           0.999            0.9964         0.0039
    3    4        7981           0.999            1.0014        -0.0059
    1    5        7937           0.997            1.0012        -0.0004
    2    5        7945           0.999            0.9982        -0.0003
    3    5        7950           0.998            1.0021        -0.0027
    4    5        7989           0.999            1.0011         0.0005
    1    6        7766           0.986            0.9984         0.0345
    2    6        7768           0.986            1.0013        -0.0091
    3    6        7785           0.990            1.0004         0.0214
    4    6        7797           0.985            1.0021         0.0017
    5    6        7782           0.988            1.0014        -0.0002
    1    7        7936           0.996            1.0017        -0.0280
    2    7        7923           0.992            0.9955        -0.0021
    3    7        7936           0.992            0.9999        -0.0128
    4    7        7968           0.991            0.9967         0.0040
    5    7        7944           0.995            0.9966        -0.0011
    6    7        7826           0.995            0.9993        -0.0309
    1    8        7824           0.988            1.0005         0.0281
    2    8        7836           0.989            1.0015        -0.0004
    3    8        7837           0.991            1.0035         0.0068
    4    8        7850           0.987            1.0039        -0.0029
    5    8        7835           0.990            1.0028        -0.0003
    6    8        7812           0.999            0.9992         0.0174
    7    8        7886           0.995            1.0082        -0.0151
    1    9        7824           0.991            0.9998         0.0128
    2    9        7821           0.992            0.9994        -0.0055
    3    9        7835           0.992            1.0021        -0.0019
    4    9        7850           0.990            1.0026        -0.0108
    5    9        7837           0.992            1.0009        -0.0059
    6    9        7790           0.997            0.9970         0.0136
    7    9        7876           0.995            1.0057        -0.0156
    8    9        7836           0.998            0.9970         0.0023
    1   10        7889           0.990            1.0016         0.0103
    2   10        7879           0.984            0.9997         0.0062
    3   10        7887           0.986            1.0023         0.0069
    4   10        7916           0.984            1.0016         0.0057
    5   10        7890           0.988            1.0014         0.0020
    6   10        7813           0.995            0.9974         0.0259
    7   10        7967           0.998            1.0085        -0.0220
    8   10        7871           0.995            0.9976         0.0143
    9   10        7845           0.992            1.0002         0.0123
    1   11        7860           0.969            1.0004         0.0210
    2   11        7854           0.962            0.9978         0.0206
    3   11        7857           0.953            0.9975         0.0440
    4   11        7904           0.964            0.9956         0.0487
    5   11        7866           0.965            0.9974         0.0324
    6   11        7724           0.933            1.0009         0.0093
    7   11        7884           0.953            0.9962         0.0665
    8   11        7780           0.935            0.9972         0.0215
    9   11        7777           0.939            0.9970         0.0393
   10   11        7847           0.942            0.9947         0.0441
    1   12        7860           0.958            0.9987         0.0192
    2   12        7870           0.953            1.0009        -0.0196
    3   12        7865           0.940            0.9961         0.0420
    4   12        7911           0.952            0.9962         0.0314
    5   12        7869           0.952            0.9986         0.0105
    6   12        7738           0.917            1.0015        -0.0080
    7   12        7893           0.937            0.9935         0.0723
    8   12        7801           0.921            1.0021        -0.0352
    9   12        7792           0.929            0.9999         0.0024
   10   12        7868           0.923            0.9983         0.0029
   11   12        7930           0.994            0.9973         0.0011
    1   13        7842           0.953            0.9984         0.0177
    2   13        7841           0.946            1.0017        -0.0295
    3   13        7853           0.931            0.9959         0.0407
    4   13        7896           0.944            0.9966         0.0250
    5   13        7851           0.945            0.9984         0.0086
    6   13        7724           0.910            1.0014        -0.0070
    7   13        7877           0.929            0.9942         0.0621
    8   13        7781           0.915            1.0032        -0.0487
    9   13        7776           0.924            1.0004        -0.0056
   10   13        7848           0.914            1.0002        -0.0149
   11   13        7905           0.986            0.9967         0.0012
   12   13        7950           0.997            0.9993         0.0012
    1   14        7799           0.967            0.9990        -0.0185
    2   14        7802           0.961            1.0033        -0.0774
    3   14        7796           0.951            0.9971        -0.0010
    4   14        7842           0.962            0.9982        -0.0202
    5   14        7800           0.963            1.0012        -0.0470
    6   14        7670           0.930            1.0044        -0.0772
    7   14        7821           0.950            0.9934         0.0427
    8   14        7734           0.933            1.0059        -0.1080
    9   14        7723           0.937            1.0034        -0.0671
   10   14        7792           0.938            1.0031        -0.0741
   11   14        7903           0.999            0.9930         0.0044
   12   14        7907           0.996            0.9964        -0.0025
   13   14        7880           0.989            0.9969        -0.0010
    1   15        7783           0.953            0.9988        -0.0098
    2   15        7793           0.949            1.0028        -0.0667
    3   15        7793           0.934            0.9994        -0.0104
    4   15        7834           0.946            1.0010        -0.0325
    5   15        7792           0.947            1.0014        -0.0399
    6   15        7664           0.911            1.0021        -0.0460
    7   15        7812           0.930            0.9955         0.0293
    8   15        7733           0.916            1.0049        -0.0962
    9   15        7715           0.925            1.0013        -0.0422
   10   15        7786           0.915            1.0031        -0.0718
   11   15        7843           0.986            0.9945        -0.0044
   12   15        7891           0.998            0.9962         0.0045
   13   15        7885           0.999            0.9969         0.0041
   14   15        7833           0.990            0.9995         0.0066
    1   16        7820           0.942            0.9993         0.0142
    2   16        7824           0.938            0.9999        -0.0130
    3   16        7830           0.924            0.9994         0.0180
    4   16        7875           0.937            0.9996         0.0098
    5   16        7831           0.937            0.9984         0.0124
    6   16        7699           0.899            0.9983         0.0187
    7   16        7853           0.917            0.9998         0.0227
    8   16        7766           0.904            1.0002        -0.0240
    9   16        7751           0.913            0.9967         0.0275
   10   16        7827           0.901            0.9993        -0.0070
   11   16        7868           0.980            1.0001        -0.0240
   12   16        7930           0.994            1.0006        -0.0099
   13   16        7917           0.995            1.0009        -0.0070
   14   16        7849           0.983            1.0030         0.0009
   15   16        7870           0.997            1.0018         0.0056
    1   17        7799           0.940            0.9985         0.0205
    2   17        7807           0.936            1.0004        -0.0198
    3   17        7809           0.919            0.9990         0.0210
    4   17        7849           0.933            0.9999         0.0066
    5   17        7806           0.933            0.9986         0.0114
    6   17        7683           0.896            0.9981         0.0182
    7   17        7828           0.914            0.9996         0.0242
    8   17        7743           0.901            1.0011        -0.0361
    9   17        7730           0.912            0.9974         0.0183
   10   17        7801           0.898            1.0006        -0.0205
   11   17        7850           0.973            0.9996        -0.0211
   12   17        7895           0.991            0.9999        -0.0046
   13   17        7905           0.996            1.0002        -0.0028
   14   17        7823           0.977            1.0023         0.0063
   15   17        7860           0.997            1.0017         0.0057
   16   17        7895           0.998            1.0002        -0.0014
    1   18        7861           0.955            0.9993         0.0186
    2   18        7863           0.950            1.0001        -0.0075
    3   18        7872           0.938            0.9969         0.0381
    4   18        7921           0.950            0.9963         0.0334
    5   18        7878           0.951            0.9979         0.0185
    6   18        7740           0.916            1.0010         0.0047
    7   18        7895           0.935            0.9952         0.0626
    8   18        7795           0.918            1.0001        -0.0099
    9   18        7786           0.924            0.9989         0.0181
   10   18        7864           0.921            0.9976         0.0153
   11   18        7940           0.994            0.9982        -0.0018
   12   18        7972           0.998            1.0010        -0.0035
   13   18        7943           0.993            1.0016        -0.0034
   14   18        7900           0.996            1.0048        -0.0032
   15   18        7884           0.994            1.0040        -0.0014
   16   18        7933           0.993            0.9995         0.0131
   17   18        7898           0.986            1.0004         0.0068
    1   19        7755           0.965            0.9997        -0.0154
    2   19        7759           0.960            1.0033        -0.0680
    3   19        7758           0.949            1.0002        -0.0145
    4   19        7794           0.960            1.0018        -0.0360
    5   19        7758           0.961            1.0023        -0.0466
    6   19        7636           0.928            1.0041        -0.0636
    7   19        7773           0.946            0.9968         0.0255
    8   19        7692           0.931            1.0065        -0.1065
    9   19        7688           0.937            1.0024        -0.0494
   10   19        7747           0.933            1.0048        -0.0808
   11   19        7843           0.995            0.9941        -0.0026
   12   19        7872           0.999            0.9947         0.0113
   13   19        7839           0.995            0.9955         0.0076
   14   19        7832           0.997            0.9975         0.0231
   15   19        7809           0.996            0.9980         0.0083
   16   19        7832           0.994            0.9969        -0.0066
   17   19        7805           0.989            0.9970        -0.0090
   18   19        7876           0.999            0.9949         0.0039


 K*EXP(B*SS) = Factor applied to intensities
    SS       = (2sin(theta)/lambda)^2

     K        B           DATA SET NAME
    1.0000   0.000    ../XDS_FF101.HKL                                  
    0.9832   0.301    ../XDS_FF102.HKL                                  
    0.9860   0.247    ../XDS_FF103.HKL                                  
    0.9848   0.252    ../XDS_FF104.HKL                                  
    0.9949   0.212    ../XDS_FF106.HKL                                  
    1.0021   0.114    ../XDS_FF201.HKL                                  
    0.9816   0.299    ../XDS_FF202.HKL                                  
    0.9875   0.362    ../XDS_FF203.HKL                                  
    0.9831   0.405    ../XDS_FF204.HKL                                  
    0.9751   0.366    ../XDS_FF206.HKL                                  
    1.0107  -0.092    ../XDS_FF301.HKL                                  
    0.9982   0.179    ../XDS_FF302.HKL                                  
    0.9967   0.181    ../XDS_FF303-2.HKL                                
    1.0087   0.107    ../XDS_FF303-4.HKL                                
    1.0068   0.194    ../XDS_FF305.HKL                                  
    1.0107  -0.019    ../XDS_FF306.HKL                                  
    1.0094   0.008    ../XDS_FF307.HKL                                  
    1.0134  -0.105    ../XDS_FF308.HKL                                  
    1.0148  -0.040    ../XDS_FF310.HKL                                  

 ******************************************************************************
           CORRECTION FACTORS AS FUNCTION OF IMAGE NUMBER & RESOLUTION
 ******************************************************************************

 RECIPROCAL CORRECTION FACTORS FOR INPUT DATA SETS MERGED TO
 OUTPUT FILE: alldatasets.ahkl                                  

 THE CALCULATIONS ASSUME         FRIEDEL'S_LAW= TRUE
 TOTAL NUMBER OF CORRECTION FACTORS DEFINED    13680
 DEGREES OF FREEDOM OF CHI^2 FIT           1983696.0
 CHI^2-VALUE OF FIT OF CORRECTION FACTORS      0.949
 NUMBER OF CYCLES CARRIED OUT                      3

 CORRECTION FACTORS for visual inspection by XDS-Viewer DECAY_001.cbf       
 XMIN=     0.1 XMAX=   179.9 NXBIN=   36
 YMIN= 0.00090 YMAX= 0.24995 NYBIN=   20
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     108616

 CORRECTION FACTORS for visual inspection by XDS-Viewer DECAY_002.cbf       
 XMIN=     0.1 XMAX=   179.9 NXBIN=   36
 YMIN= 0.00081 YMAX= 0.24995 NYBIN=   20
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     109072

 CORRECTION FACTORS for visual inspection by XDS-Viewer DECAY_003.cbf       
 XMIN=     0.1 XMAX=   179.9 NXBIN=   36
 YMIN= 0.00090 YMAX= 0.24995 NYBIN=   20
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     107778

 CORRECTION FACTORS for visual inspection by XDS-Viewer DECAY_004.cbf       
 XMIN=     0.1 XMAX=   179.9 NXBIN=   36
 YMIN= 0.00090 YMAX= 0.24995 NYBIN=   20
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     110340

 CORRECTION FACTORS for visual inspection by XDS-Viewer DECAY_005.cbf       
 XMIN=     0.1 XMAX=   179.9 NXBIN=   36
 YMIN= 0.00090 YMAX= 0.24995 NYBIN=   20
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     109478

 CORRECTION FACTORS for visual inspection by XDS-Viewer DECAY_006.cbf       
 XMIN=     0.1 XMAX=   179.9 NXBIN=   36
 YMIN= 0.00081 YMAX= 0.24995 NYBIN=   20
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     105397

 CORRECTION FACTORS for visual inspection by XDS-Viewer DECAY_007.cbf       
 XMIN=     0.1 XMAX=   179.9 NXBIN=   36
 YMIN= 0.00090 YMAX= 0.24995 NYBIN=   20
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     111046

 CORRECTION FACTORS for visual inspection by XDS-Viewer DECAY_008.cbf       
 XMIN=     0.1 XMAX=   179.9 NXBIN=   36
 YMIN= 0.00081 YMAX= 0.24995 NYBIN=   20
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     107125

 CORRECTION FACTORS for visual inspection by XDS-Viewer DECAY_009.cbf       
 XMIN=     0.1 XMAX=   179.9 NXBIN=   36
 YMIN= 0.00081 YMAX= 0.24995 NYBIN=   20
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     105647

 CORRECTION FACTORS for visual inspection by XDS-Viewer DECAY_010.cbf       
 XMIN=     0.1 XMAX=   179.9 NXBIN=   36
 YMIN= 0.00081 YMAX= 0.24995 NYBIN=   20
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     109791

 CORRECTION FACTORS for visual inspection by XDS-Viewer DECAY_011.cbf       
 XMIN=     0.1 XMAX=   179.9 NXBIN=   36
 YMIN= 0.00065 YMAX= 0.24995 NYBIN=   20
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     103701

 CORRECTION FACTORS for visual inspection by XDS-Viewer DECAY_012.cbf       
 XMIN=     0.1 XMAX=   179.9 NXBIN=   36
 YMIN= 0.00081 YMAX= 0.24995 NYBIN=   20
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     109105

 CORRECTION FACTORS for visual inspection by XDS-Viewer DECAY_013.cbf       
 XMIN=     0.1 XMAX=   179.9 NXBIN=   36
 YMIN= 0.00090 YMAX= 0.24995 NYBIN=   20
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     107039

 CORRECTION FACTORS for visual inspection by XDS-Viewer DECAY_014.cbf       
 XMIN=     0.1 XMAX=   179.9 NXBIN=   36
 YMIN= 0.00065 YMAX= 0.24995 NYBIN=   20
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     106236

 CORRECTION FACTORS for visual inspection by XDS-Viewer DECAY_015.cbf       
 XMIN=     0.2 XMAX=   179.8 NXBIN=   36
 YMIN= 0.00065 YMAX= 0.24995 NYBIN=   20
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     104832

 CORRECTION FACTORS for visual inspection by XDS-Viewer DECAY_016.cbf       
 XMIN=     0.1 XMAX=   179.9 NXBIN=   36
 YMIN= 0.00090 YMAX= 0.24995 NYBIN=   20
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     105792

 CORRECTION FACTORS for visual inspection by XDS-Viewer DECAY_017.cbf       
 XMIN=     0.2 XMAX=   179.8 NXBIN=   36
 YMIN= 0.00081 YMAX= 0.24995 NYBIN=   20
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     105061

 CORRECTION FACTORS for visual inspection by XDS-Viewer DECAY_018.cbf       
 XMIN=     0.1 XMAX=   179.9 NXBIN=   36
 YMIN= 0.00090 YMAX= 0.24995 NYBIN=   20
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     108377

 CORRECTION FACTORS for visual inspection by XDS-Viewer DECAY_019.cbf       
 XMIN=     0.1 XMAX=   179.9 NXBIN=   36
 YMIN= 0.00065 YMAX= 0.24995 NYBIN=   20
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     104969


 ******************************************************************************
  CORRECTION FACTORS AS FUNCTION OF X (fast) & Y(slow) IN THE DETECTOR PLANE
 ******************************************************************************

 RECIPROCAL CORRECTION FACTORS FOR INPUT DATA SETS MERGED TO
 OUTPUT FILE: alldatasets.ahkl                                  

 THE CALCULATIONS ASSUME         FRIEDEL'S_LAW= TRUE
 TOTAL NUMBER OF CORRECTION FACTORS DEFINED    40901
 DEGREES OF FREEDOM OF CHI^2 FIT           1982688.2
 CHI^2-VALUE OF FIT OF CORRECTION FACTORS      0.945
 NUMBER OF CYCLES CARRIED OUT                      3

 CORRECTION FACTORS for visual inspection by XDS-Viewer MODPIX_001.cbf      
 XMIN=   586.0 XMAX=  2515.1 NXBIN=   47
 YMIN=   562.5 YMAX=  2498.0 NYBIN=   47
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     108616

 CORRECTION FACTORS for visual inspection by XDS-Viewer MODPIX_002.cbf      
 XMIN=   587.9 XMAX=  2518.9 NXBIN=   47
 YMIN=   562.6 YMAX=  2498.7 NYBIN=   47
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     109072

 CORRECTION FACTORS for visual inspection by XDS-Viewer MODPIX_003.cbf      
 XMIN=   587.5 XMAX=  2515.3 NXBIN=   46
 YMIN=   559.6 YMAX=  2501.1 NYBIN=   47
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     107778

 CORRECTION FACTORS for visual inspection by XDS-Viewer MODPIX_004.cbf      
 XMIN=   590.4 XMAX=  2513.5 NXBIN=   47
 YMIN=   559.4 YMAX=  2501.7 NYBIN=   47
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     110340

 CORRECTION FACTORS for visual inspection by XDS-Viewer MODPIX_005.cbf      
 XMIN=   590.4 XMAX=  2513.6 NXBIN=   47
 YMIN=   560.1 YMAX=  2500.2 NYBIN=   47
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     109478

 CORRECTION FACTORS for visual inspection by XDS-Viewer MODPIX_006.cbf      
 XMIN=   397.1 XMAX=  2704.3 NXBIN=   46
 YMIN=   369.4 YMAX=  2692.3 NYBIN=   46
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     105397

 CORRECTION FACTORS for visual inspection by XDS-Viewer MODPIX_007.cbf      
 XMIN=   588.5 XMAX=  2513.1 NXBIN=   47
 YMIN=   562.1 YMAX=  2498.8 NYBIN=   47
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     111046

 CORRECTION FACTORS for visual inspection by XDS-Viewer MODPIX_008.cbf      
 XMIN=   583.7 XMAX=  2515.0 NXBIN=   46
 YMIN=   561.2 YMAX=  2499.6 NYBIN=   46
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     107125

 CORRECTION FACTORS for visual inspection by XDS-Viewer MODPIX_009.cbf      
 XMIN=   586.9 XMAX=  2516.2 NXBIN=   46
 YMIN=   559.6 YMAX=  2501.3 NYBIN=   46
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     105647

 CORRECTION FACTORS for visual inspection by XDS-Viewer MODPIX_010.cbf      
 XMIN=   592.1 XMAX=  2511.3 NXBIN=   47
 YMIN=   564.3 YMAX=  2496.7 NYBIN=   47
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     109791

 CORRECTION FACTORS for visual inspection by XDS-Viewer MODPIX_011.cbf      
 XMIN=   770.0 XMAX=  2329.3 NXBIN=   45
 YMIN=   742.7 YMAX=  2318.3 NYBIN=   46
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     103701

 CORRECTION FACTORS for visual inspection by XDS-Viewer MODPIX_012.cbf      
 XMIN=   765.1 XMAX=  2335.2 NXBIN=   47
 YMIN=   741.8 YMAX=  2319.5 NYBIN=   47
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     109105

 CORRECTION FACTORS for visual inspection by XDS-Viewer MODPIX_013.cbf      
 XMIN=   766.9 XMAX=  2336.5 NXBIN=   46
 YMIN=   742.2 YMAX=  2318.5 NYBIN=   46
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     107039

 CORRECTION FACTORS for visual inspection by XDS-Viewer MODPIX_014.cbf      
 XMIN=   768.2 XMAX=  2334.9 NXBIN=   46
 YMIN=   743.4 YMAX=  2317.6 NYBIN=   46
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     106236

 CORRECTION FACTORS for visual inspection by XDS-Viewer MODPIX_015.cbf      
 XMIN=   766.6 XMAX=  2334.2 NXBIN=   46
 YMIN=   742.0 YMAX=  2319.0 NYBIN=   46
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     104832

 CORRECTION FACTORS for visual inspection by XDS-Viewer MODPIX_016.cbf      
 XMIN=   586.9 XMAX=  2515.6 NXBIN=   46
 YMIN=   561.9 YMAX=  2498.9 NYBIN=   46
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     105792

 CORRECTION FACTORS for visual inspection by XDS-Viewer MODPIX_017.cbf      
 XMIN=   587.9 XMAX=  2514.0 NXBIN=   46
 YMIN=   561.9 YMAX=  2499.2 NYBIN=   46
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     105061

 CORRECTION FACTORS for visual inspection by XDS-Viewer MODPIX_018.cbf      
 XMIN=   586.6 XMAX=  2513.5 NXBIN=   46
 YMIN=   562.5 YMAX=  2498.2 NYBIN=   47
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     108377

 CORRECTION FACTORS for visual inspection by XDS-Viewer MODPIX_019.cbf      
 XMIN=   588.2 XMAX=  2517.0 NXBIN=   46
 YMIN=   563.0 YMAX=  2498.0 NYBIN=   46
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     104969


 ******************************************************************************
   CORRECTION FACTORS AS FUNCTION OF IMAGE NUMBER & DETECTOR SURFACE POSITION
 ******************************************************************************

 RECIPROCAL CORRECTION FACTORS FOR INPUT DATA SETS MERGED TO
 OUTPUT FILE: alldatasets.ahkl                                  

 THE CALCULATIONS ASSUME         FRIEDEL'S_LAW= TRUE
 TOTAL NUMBER OF CORRECTION FACTORS DEFINED     8892
 DEGREES OF FREEDOM OF CHI^2 FIT           1983694.0
 CHI^2-VALUE OF FIT OF CORRECTION FACTORS      0.942
 NUMBER OF CYCLES CARRIED OUT                      3

 CORRECTION FACTORS for visual inspection by XDS-Viewer ABSORP_001.cbf      
 XMIN=     0.1 XMAX=   179.9 NXBIN=   36
 DETECTOR_SURFACE_POSITION=    1551    1530
 DETECTOR_SURFACE_POSITION=    1878    1859
 DETECTOR_SURFACE_POSITION=    1223    1859
 DETECTOR_SURFACE_POSITION=    1223    1202
 DETECTOR_SURFACE_POSITION=    1878    1202
 DETECTOR_SURFACE_POSITION=    2292    1838
 DETECTOR_SURFACE_POSITION=    1858    2274
 DETECTOR_SURFACE_POSITION=    1243    2274
 DETECTOR_SURFACE_POSITION=     809    1838
 DETECTOR_SURFACE_POSITION=     809    1222
 DETECTOR_SURFACE_POSITION=    1243     786
 DETECTOR_SURFACE_POSITION=    1858     786
 DETECTOR_SURFACE_POSITION=    2292    1222
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     108616

 CORRECTION FACTORS for visual inspection by XDS-Viewer ABSORP_002.cbf      
 XMIN=     0.1 XMAX=   179.9 NXBIN=   36
 DETECTOR_SURFACE_POSITION=    1553    1531
 DETECTOR_SURFACE_POSITION=    1881    1859
 DETECTOR_SURFACE_POSITION=    1225    1859
 DETECTOR_SURFACE_POSITION=    1225    1202
 DETECTOR_SURFACE_POSITION=    1881    1202
 DETECTOR_SURFACE_POSITION=    2296    1839
 DETECTOR_SURFACE_POSITION=    1861    2275
 DETECTOR_SURFACE_POSITION=    1246    2275
 DETECTOR_SURFACE_POSITION=     811    1839
 DETECTOR_SURFACE_POSITION=     811    1222
 DETECTOR_SURFACE_POSITION=    1246     786
 DETECTOR_SURFACE_POSITION=    1861     786
 DETECTOR_SURFACE_POSITION=    2296    1222
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     109072

 CORRECTION FACTORS for visual inspection by XDS-Viewer ABSORP_003.cbf      
 XMIN=     0.1 XMAX=   179.9 NXBIN=   36
 DETECTOR_SURFACE_POSITION=    1551    1530
 DETECTOR_SURFACE_POSITION=    1879    1860
 DETECTOR_SURFACE_POSITION=    1224    1860
 DETECTOR_SURFACE_POSITION=    1224    1201
 DETECTOR_SURFACE_POSITION=    1879    1201
 DETECTOR_SURFACE_POSITION=    2292    1839
 DETECTOR_SURFACE_POSITION=    1858    2277
 DETECTOR_SURFACE_POSITION=    1244    2277
 DETECTOR_SURFACE_POSITION=     810    1839
 DETECTOR_SURFACE_POSITION=     810    1221
 DETECTOR_SURFACE_POSITION=    1244     784
 DETECTOR_SURFACE_POSITION=    1858     784
 DETECTOR_SURFACE_POSITION=    2292    1221
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     107778

 CORRECTION FACTORS for visual inspection by XDS-Viewer ABSORP_004.cbf      
 XMIN=     0.1 XMAX=   179.9 NXBIN=   36
 DETECTOR_SURFACE_POSITION=    1552    1531
 DETECTOR_SURFACE_POSITION=    1879    1860
 DETECTOR_SURFACE_POSITION=    1225    1860
 DETECTOR_SURFACE_POSITION=    1225    1201
 DETECTOR_SURFACE_POSITION=    1879    1201
 DETECTOR_SURFACE_POSITION=    2291    1840
 DETECTOR_SURFACE_POSITION=    1858    2277
 DETECTOR_SURFACE_POSITION=    1246    2277
 DETECTOR_SURFACE_POSITION=     813    1840
 DETECTOR_SURFACE_POSITION=     813    1221
 DETECTOR_SURFACE_POSITION=    1246     784
 DETECTOR_SURFACE_POSITION=    1858     784
 DETECTOR_SURFACE_POSITION=    2291    1221
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     110340

 CORRECTION FACTORS for visual inspection by XDS-Viewer ABSORP_005.cbf      
 XMIN=     0.1 XMAX=   179.9 NXBIN=   36
 DETECTOR_SURFACE_POSITION=    1552    1530
 DETECTOR_SURFACE_POSITION=    1879    1860
 DETECTOR_SURFACE_POSITION=    1225    1860
 DETECTOR_SURFACE_POSITION=    1225    1201
 DETECTOR_SURFACE_POSITION=    1879    1201
 DETECTOR_SURFACE_POSITION=    2291    1839
 DETECTOR_SURFACE_POSITION=    1858    2276
 DETECTOR_SURFACE_POSITION=    1246    2276
 DETECTOR_SURFACE_POSITION=     813    1839
 DETECTOR_SURFACE_POSITION=     813    1221
 DETECTOR_SURFACE_POSITION=    1246     784
 DETECTOR_SURFACE_POSITION=    1858     784
 DETECTOR_SURFACE_POSITION=    2291    1221
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     109478

 CORRECTION FACTORS for visual inspection by XDS-Viewer ABSORP_006.cbf      
 XMIN=     0.1 XMAX=   179.9 NXBIN=   36
 DETECTOR_SURFACE_POSITION=    1551    1531
 DETECTOR_SURFACE_POSITION=    1943    1925
 DETECTOR_SURFACE_POSITION=    1159    1925
 DETECTOR_SURFACE_POSITION=    1159    1136
 DETECTOR_SURFACE_POSITION=    1943    1136
 DETECTOR_SURFACE_POSITION=    2437    1901
 DETECTOR_SURFACE_POSITION=    1918    2424
 DETECTOR_SURFACE_POSITION=    1183    2424
 DETECTOR_SURFACE_POSITION=     664    1901
 DETECTOR_SURFACE_POSITION=     664    1161
 DETECTOR_SURFACE_POSITION=    1183     638
 DETECTOR_SURFACE_POSITION=    1918     638
 DETECTOR_SURFACE_POSITION=    2437    1161
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     105397

 CORRECTION FACTORS for visual inspection by XDS-Viewer ABSORP_007.cbf      
 XMIN=     0.1 XMAX=   179.9 NXBIN=   36
 DETECTOR_SURFACE_POSITION=    1551    1530
 DETECTOR_SURFACE_POSITION=    1878    1859
 DETECTOR_SURFACE_POSITION=    1224    1859
 DETECTOR_SURFACE_POSITION=    1224    1202
 DETECTOR_SURFACE_POSITION=    1878    1202
 DETECTOR_SURFACE_POSITION=    2291    1839
 DETECTOR_SURFACE_POSITION=    1857    2275
 DETECTOR_SURFACE_POSITION=    1244    2275
 DETECTOR_SURFACE_POSITION=     811    1839
 DETECTOR_SURFACE_POSITION=     811    1222
 DETECTOR_SURFACE_POSITION=    1244     786
 DETECTOR_SURFACE_POSITION=    1857     786
 DETECTOR_SURFACE_POSITION=    2291    1222
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     111046

 CORRECTION FACTORS for visual inspection by XDS-Viewer ABSORP_008.cbf      
 XMIN=     0.1 XMAX=   179.9 NXBIN=   36
 DETECTOR_SURFACE_POSITION=    1549    1530
 DETECTOR_SURFACE_POSITION=    1877    1860
 DETECTOR_SURFACE_POSITION=    1221    1860
 DETECTOR_SURFACE_POSITION=    1221    1201
 DETECTOR_SURFACE_POSITION=    1877    1201
 DETECTOR_SURFACE_POSITION=    2292    1839
 DETECTOR_SURFACE_POSITION=    1857    2275
 DETECTOR_SURFACE_POSITION=    1242    2275
 DETECTOR_SURFACE_POSITION=     807    1839
 DETECTOR_SURFACE_POSITION=     807    1222
 DETECTOR_SURFACE_POSITION=    1242     785
 DETECTOR_SURFACE_POSITION=    1857     785
 DETECTOR_SURFACE_POSITION=    2292    1222
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     107125

 CORRECTION FACTORS for visual inspection by XDS-Viewer ABSORP_009.cbf      
 XMIN=     0.1 XMAX=   179.9 NXBIN=   36
 DETECTOR_SURFACE_POSITION=    1552    1530
 DETECTOR_SURFACE_POSITION=    1879    1860
 DETECTOR_SURFACE_POSITION=    1224    1860
 DETECTOR_SURFACE_POSITION=    1224    1201
 DETECTOR_SURFACE_POSITION=    1879    1201
 DETECTOR_SURFACE_POSITION=    2293    1840
 DETECTOR_SURFACE_POSITION=    1859    2277
 DETECTOR_SURFACE_POSITION=    1244    2277
 DETECTOR_SURFACE_POSITION=     810    1840
 DETECTOR_SURFACE_POSITION=     810    1221
 DETECTOR_SURFACE_POSITION=    1244     784
 DETECTOR_SURFACE_POSITION=    1859     784
 DETECTOR_SURFACE_POSITION=    2293    1221
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     105647

 CORRECTION FACTORS for visual inspection by XDS-Viewer ABSORP_010.cbf      
 XMIN=     0.1 XMAX=   179.9 NXBIN=   36
 DETECTOR_SURFACE_POSITION=    1552    1531
 DETECTOR_SURFACE_POSITION=    1878    1859
 DETECTOR_SURFACE_POSITION=    1226    1859
 DETECTOR_SURFACE_POSITION=    1226    1202
 DETECTOR_SURFACE_POSITION=    1878    1202
 DETECTOR_SURFACE_POSITION=    2289    1838
 DETECTOR_SURFACE_POSITION=    1857    2273
 DETECTOR_SURFACE_POSITION=    1246    2273
 DETECTOR_SURFACE_POSITION=     814    1838
 DETECTOR_SURFACE_POSITION=     814    1223
 DETECTOR_SURFACE_POSITION=    1246     788
 DETECTOR_SURFACE_POSITION=    1857     788
 DETECTOR_SURFACE_POSITION=    2289    1223
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     109791

 CORRECTION FACTORS for visual inspection by XDS-Viewer ABSORP_011.cbf      
 XMIN=     0.1 XMAX=   179.9 NXBIN=   36
 DETECTOR_SURFACE_POSITION=    1550    1531
 DETECTOR_SURFACE_POSITION=    1814    1798
 DETECTOR_SURFACE_POSITION=    1285    1798
 DETECTOR_SURFACE_POSITION=    1285    1263
 DETECTOR_SURFACE_POSITION=    1814    1263
 DETECTOR_SURFACE_POSITION=    2149    1781
 DETECTOR_SURFACE_POSITION=    1798    2136
 DETECTOR_SURFACE_POSITION=    1301    2136
 DETECTOR_SURFACE_POSITION=     950    1781
 DETECTOR_SURFACE_POSITION=     950    1280
 DETECTOR_SURFACE_POSITION=    1301     925
 DETECTOR_SURFACE_POSITION=    1798     925
 DETECTOR_SURFACE_POSITION=    2149    1280
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     103701

 CORRECTION FACTORS for visual inspection by XDS-Viewer ABSORP_012.cbf      
 XMIN=     0.1 XMAX=   179.9 NXBIN=   36
 DETECTOR_SURFACE_POSITION=    1550    1531
 DETECTOR_SURFACE_POSITION=    1817    1799
 DETECTOR_SURFACE_POSITION=    1283    1799
 DETECTOR_SURFACE_POSITION=    1283    1263
 DETECTOR_SURFACE_POSITION=    1817    1263
 DETECTOR_SURFACE_POSITION=    2154    1782
 DETECTOR_SURFACE_POSITION=    1800    2137
 DETECTOR_SURFACE_POSITION=    1300    2137
 DETECTOR_SURFACE_POSITION=     947    1782
 DETECTOR_SURFACE_POSITION=     947    1279
 DETECTOR_SURFACE_POSITION=    1300     924
 DETECTOR_SURFACE_POSITION=    1800     924
 DETECTOR_SURFACE_POSITION=    2154    1279
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     109105

 CORRECTION FACTORS for visual inspection by XDS-Viewer ABSORP_013.cbf      
 XMIN=     0.1 XMAX=   179.9 NXBIN=   36
 DETECTOR_SURFACE_POSITION=    1552    1530
 DETECTOR_SURFACE_POSITION=    1818    1798
 DETECTOR_SURFACE_POSITION=    1285    1798
 DETECTOR_SURFACE_POSITION=    1285    1263
 DETECTOR_SURFACE_POSITION=    1818    1263
 DETECTOR_SURFACE_POSITION=    2155    1781
 DETECTOR_SURFACE_POSITION=    1802    2136
 DETECTOR_SURFACE_POSITION=    1302    2136
 DETECTOR_SURFACE_POSITION=     948    1781
 DETECTOR_SURFACE_POSITION=     948    1279
 DETECTOR_SURFACE_POSITION=    1302     924
 DETECTOR_SURFACE_POSITION=    1802     924
 DETECTOR_SURFACE_POSITION=    2155    1279
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     107039

 CORRECTION FACTORS for visual inspection by XDS-Viewer ABSORP_014.cbf      
 XMIN=     0.1 XMAX=   179.9 NXBIN=   36
 DETECTOR_SURFACE_POSITION=    1552    1531
 DETECTOR_SURFACE_POSITION=    1818    1798
 DETECTOR_SURFACE_POSITION=    1285    1798
 DETECTOR_SURFACE_POSITION=    1285    1263
 DETECTOR_SURFACE_POSITION=    1818    1263
 DETECTOR_SURFACE_POSITION=    2154    1781
 DETECTOR_SURFACE_POSITION=    1801    2136
 DETECTOR_SURFACE_POSITION=    1302    2136
 DETECTOR_SURFACE_POSITION=     949    1781
 DETECTOR_SURFACE_POSITION=     949    1280
 DETECTOR_SURFACE_POSITION=    1302     925
 DETECTOR_SURFACE_POSITION=    1801     925
 DETECTOR_SURFACE_POSITION=    2154    1280
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     106236

 CORRECTION FACTORS for visual inspection by XDS-Viewer ABSORP_015.cbf      
 XMIN=     0.2 XMAX=   179.8 NXBIN=   36
 DETECTOR_SURFACE_POSITION=    1550    1531
 DETECTOR_SURFACE_POSITION=    1817    1798
 DETECTOR_SURFACE_POSITION=    1284    1798
 DETECTOR_SURFACE_POSITION=    1284    1263
 DETECTOR_SURFACE_POSITION=    1817    1263
 DETECTOR_SURFACE_POSITION=    2153    1782
 DETECTOR_SURFACE_POSITION=    1800    2137
 DETECTOR_SURFACE_POSITION=    1301    2137
 DETECTOR_SURFACE_POSITION=     948    1782
 DETECTOR_SURFACE_POSITION=     948    1279
 DETECTOR_SURFACE_POSITION=    1301     924
 DETECTOR_SURFACE_POSITION=    1800     924
 DETECTOR_SURFACE_POSITION=    2153    1279
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     104832

 CORRECTION FACTORS for visual inspection by XDS-Viewer ABSORP_016.cbf      
 XMIN=     0.1 XMAX=   179.9 NXBIN=   36
 DETECTOR_SURFACE_POSITION=    1551    1530
 DETECTOR_SURFACE_POSITION=    1879    1859
 DETECTOR_SURFACE_POSITION=    1224    1859
 DETECTOR_SURFACE_POSITION=    1224    1201
 DETECTOR_SURFACE_POSITION=    1879    1201
 DETECTOR_SURFACE_POSITION=    2293    1839
 DETECTOR_SURFACE_POSITION=    1858    2275
 DETECTOR_SURFACE_POSITION=    1244    2275
 DETECTOR_SURFACE_POSITION=     810    1839
 DETECTOR_SURFACE_POSITION=     810    1222
 DETECTOR_SURFACE_POSITION=    1244     786
 DETECTOR_SURFACE_POSITION=    1858     786
 DETECTOR_SURFACE_POSITION=    2293    1222
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     105792

 CORRECTION FACTORS for visual inspection by XDS-Viewer ABSORP_017.cbf      
 XMIN=     0.2 XMAX=   179.8 NXBIN=   36
 DETECTOR_SURFACE_POSITION=    1551    1531
 DETECTOR_SURFACE_POSITION=    1878    1860
 DETECTOR_SURFACE_POSITION=    1224    1860
 DETECTOR_SURFACE_POSITION=    1224    1202
 DETECTOR_SURFACE_POSITION=    1878    1202
 DETECTOR_SURFACE_POSITION=    2291    1839
 DETECTOR_SURFACE_POSITION=    1858    2275
 DETECTOR_SURFACE_POSITION=    1244    2275
 DETECTOR_SURFACE_POSITION=     811    1839
 DETECTOR_SURFACE_POSITION=     811    1222
 DETECTOR_SURFACE_POSITION=    1244     786
 DETECTOR_SURFACE_POSITION=    1858     786
 DETECTOR_SURFACE_POSITION=    2291    1222
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     105061

 CORRECTION FACTORS for visual inspection by XDS-Viewer ABSORP_018.cbf      
 XMIN=     0.1 XMAX=   179.9 NXBIN=   36
 DETECTOR_SURFACE_POSITION=    1550    1530
 DETECTOR_SURFACE_POSITION=    1877    1859
 DETECTOR_SURFACE_POSITION=    1223    1859
 DETECTOR_SURFACE_POSITION=    1223    1202
 DETECTOR_SURFACE_POSITION=    1877    1202
 DETECTOR_SURFACE_POSITION=    2291    1839
 DETECTOR_SURFACE_POSITION=    1857    2274
 DETECTOR_SURFACE_POSITION=    1243    2274
 DETECTOR_SURFACE_POSITION=     809    1839
 DETECTOR_SURFACE_POSITION=     809    1222
 DETECTOR_SURFACE_POSITION=    1243     786
 DETECTOR_SURFACE_POSITION=    1857     786
 DETECTOR_SURFACE_POSITION=    2291    1222
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     108377

 CORRECTION FACTORS for visual inspection by XDS-Viewer ABSORP_019.cbf      
 XMIN=     0.1 XMAX=   179.9 NXBIN=   36
 DETECTOR_SURFACE_POSITION=    1553    1531
 DETECTOR_SURFACE_POSITION=    1880    1859
 DETECTOR_SURFACE_POSITION=    1225    1859
 DETECTOR_SURFACE_POSITION=    1225    1202
 DETECTOR_SURFACE_POSITION=    1880    1202
 DETECTOR_SURFACE_POSITION=    2294    1839
 DETECTOR_SURFACE_POSITION=    1860    2274
 DETECTOR_SURFACE_POSITION=    1246    2274
 DETECTOR_SURFACE_POSITION=     811    1839
 DETECTOR_SURFACE_POSITION=     811    1222
 DETECTOR_SURFACE_POSITION=    1246     787
 DETECTOR_SURFACE_POSITION=    1860     787
 DETECTOR_SURFACE_POSITION=    2294    1222
 NUMBER OF REFLECTIONS USED FOR DETERMINING CORRECTION FACTORS     104969


 ******************************************************************************
    CORRECTION PARAMETERS FOR THE STANDARD ERROR OF REFLECTION INTENSITIES
 ******************************************************************************

 The variance v0(I) of the intensity I obtained from counting statistics is
 replaced by v(I)=a*(v0(I)+b*I^2). The model parameters a, b are chosen to
 minimize the discrepancies between v(I) and the variance estimated from
 sample statistics of symmetry related reflections. This model implicates
 an asymptotic limit ISa=1/SQRT(a*b) for the highest I/Sigma(I) that the
 experimental setup can produce (Diederichs (2010) Acta Cryst D66, 733-740).
 Often the value of ISa is reduced from the initial value ISa0 due to systematic
 errors showing up by comparison with other data sets in the scaling procedure.
 (ISa=ISa0=-1 if v0 is unknown for a data set.)

     a        b          ISa    ISa0   INPUT DATA SET
 3.283E+01  2.192E-04   11.79   39.58 ../XDS_FF101.HKL                                  
 2.742E+01  2.809E-04   11.40   47.54 ../XDS_FF102.HKL                                  
 5.024E+01  3.092E-04    8.02   35.47 ../XDS_FF103.HKL                                  
 4.668E+01  1.929E-04   10.54   40.50 ../XDS_FF104.HKL                                  
 3.135E+01  2.412E-04   11.50   43.69 ../XDS_FF106.HKL                                  
 5.284E+01  5.860E-04    5.68   44.44 ../XDS_FF201.HKL                                  
 5.636E+01  4.513E-04    6.27   19.12 ../XDS_FF202.HKL                                  
 5.900E+01  4.333E-04    6.25   53.02 ../XDS_FF203.HKL                                  
 5.136E+01  4.188E-04    6.82   41.05 ../XDS_FF204.HKL                                  
 1.108E+02  3.389E-04    5.16   49.75 ../XDS_FF206.HKL                                  
 7.013E+01  5.537E-04    5.07   25.03 ../XDS_FF301.HKL                                  
 6.984E+01  4.897E-04    5.41   40.40 ../XDS_FF302.HKL                                  
 8.864E+01  4.882E-04    4.81   38.65 ../XDS_FF303-2.HKL                                
 4.299E+01  5.564E-04    6.47   44.80 ../XDS_FF303-4.HKL                                
 5.041E+01  7.883E-04    5.02   37.09 ../XDS_FF305.HKL                                  
 9.452E+01  7.414E-04    3.78   32.86 ../XDS_FF306.HKL                                  
 8.314E+01  9.076E-04    3.64   32.05 ../XDS_FF307.HKL                                  
 8.276E+01  5.962E-04    4.50   32.18 ../XDS_FF308.HKL                                  
 3.548E+01  6.670E-04    6.50   42.00 ../XDS_FF310.HKL                                  
 

 FACTOR TO PLACE ALL DATA SETS TO AN APPROXIMATE ABSOLUTE SCALE   0.6135E+02
 (ASSUMING A PROTEIN WITH 50% SOLVENT)



 ******************************************************************************
  STATISTICS OF SCALED OUTPUT DATA SET : alldatasets.ahkl                                  
  FILE TYPE:         XDS_ASCII      MERGE=FALSE          FRIEDEL'S_LAW=TRUE 

     46012 OUT OF   2189871 REFLECTIONS REJECTED
   2143859 REFLECTIONS ON OUTPUT FILE 

 ******************************************************************************
 DEFINITIONS:
 R-FACTOR
 observed = (SUM(ABS(I(h,i)-I(h))))/(SUM(I(h,i)))
 expected = expected R-FACTOR derived from Sigma(I)

 COMPARED = number of reflections used for calculating R-FACTOR
 I/SIGMA  = mean of intensity/Sigma(I) of unique reflections
            (after merging symmetry-related observations)
 Sigma(I) = standard deviation of reflection intensity I
            estimated from sample statistics

 R-meas   = redundancy independent R-factor (intensities)
 Rmrgd-F  = quality of amplitudes (F) in the scaled data set
            For definition of R-meas and Rmrgd-F see 
            Diederichs & Karplus (1997), Nature Struct. Biol. 4, 269-275.

 Anomal   = mean correlation factor between two random subsets
  Corr      of anomalous intensity differences
 SigAno   = mean anomalous difference in units of its estimated
            standard deviation (|F(+)-F(-)|/Sigma). F(+), F(-)
            are structure factor estimates obtained from the
            merged intensity observations in each parity class.
  Nano    = Number of unique reflections used to calculate
            Anomal_Corr & SigAno. At least two observations
            for each (+ and -) parity are required.


 SUBSET OF INTENSITY DATA WITH SIGNAL/NOISE >= -3.0 AS FUNCTION OF RESOLUTION
 RESOLUTION     NUMBER OF REFLECTIONS    COMPLETENESS R-FACTOR  R-FACTOR COMPARED I/SIGMA   R-meas  Rmrgd-F  Anomal  SigAno   Nano
   LIMIT     OBSERVED  UNIQUE  POSSIBLE     OF DATA   observed  expected                                      Corr

     8.95       21774     119       120       99.2%       8.7%     13.7%    21774   86.65     8.8%     2.0%    -6%   0.823      47
     6.33       45027     193       193      100.0%       9.2%     13.7%    45027   96.57     9.2%     0.6%    62%   1.269     119
     5.16       56965     233       233      100.0%      11.3%     13.8%    56965   99.05    11.3%     0.7%    47%   0.926     158
     4.47       67501     277       277      100.0%      10.6%     13.7%    67501   96.43    10.6%     0.6%    14%   0.812     196
     4.00       74632     298       298      100.0%      11.6%     13.7%    74632  102.12    11.6%     0.6%   -13%   0.668     225
     3.65       81057     332       332      100.0%      12.8%     13.8%    81057   96.24    12.8%     0.7%   -22%   0.605     253
     3.38       90171     362       362      100.0%      13.9%     14.0%    90171   96.60    13.9%     0.8%   -26%   0.549     288
     3.16       96248     381       381      100.0%      13.1%     14.1%    96248   93.75    13.1%     0.7%   -20%   0.618     300
     2.98      103754     409       409      100.0%      14.1%     14.6%   103754   88.75    14.2%     0.9%   -14%   0.611     327
     2.83      108287     415       415      100.0%      15.1%     15.3%   108287   83.82    15.1%     0.8%   -30%   0.613     345
     2.70      114730     446       446      100.0%      16.0%     16.0%   114730   78.41    16.0%     0.9%   -24%   0.603     364
     2.58      124863     473       473      100.0%      16.9%     16.8%   124863   74.97    16.9%     0.9%   -12%   0.629     394
     2.48      123983     466       466      100.0%      17.0%     17.4%   123983   73.13    17.0%     1.0%   -15%   0.593     395
     2.39      133907     506       506      100.0%      16.7%     18.1%   133907   68.36    16.7%     1.0%   -12%   0.577     424
     2.31      136246     505       505      100.0%      18.4%     18.9%   136246   68.28    18.4%     0.9%   -29%   0.591     433
     2.24      145805     547       547      100.0%      18.7%     19.5%   145805   64.39    18.7%     1.1%   -21%   0.544     461
     2.17      143771     530       530      100.0%      18.9%     21.1%   143771   60.62    18.9%     1.1%   -16%   0.531     458
     2.11      154632     576       576      100.0%      20.5%     22.1%   154632   57.55    20.5%     1.3%   -19%   0.510     491
     2.05      154997     571       571      100.0%      21.4%     23.8%   154997   54.34    21.5%     1.3%   -14%   0.517     496
     2.00      165509     609       609      100.0%      21.6%     26.0%   165509   49.82    21.6%     1.3%   -25%   0.477     528
    total     2143859    8248      8249      100.0%      14.6%     16.0%  2143859   74.97    14.6%     0.9%   -15%   0.598    6702


 ========== STATISTICS OF INPUT DATA SET ==========


  R-FACTORS FOR INTENSITIES OF DATA SET ../XDS_FF101.HKL                                  

 RESOLUTION   R-FACTOR   R-FACTOR   COMPARED
   LIMIT      observed   expected

     8.95         3.6%       6.8%      1128
     6.33         3.7%       6.9%      2328
     5.16         4.4%       7.0%      3056
     4.47         4.1%       6.9%      3596
     4.00         4.5%       6.9%      3989
     3.65         4.7%       7.0%      4242
     3.38         5.6%       7.1%      4743
     3.16         5.8%       7.2%      5081
     2.98         5.6%       7.5%      5511
     2.83         6.1%       7.9%      5790
     2.70         6.2%       8.3%      6212
     2.58         6.9%       8.8%      6618
     2.48         6.7%       9.2%      6603
     2.39         7.4%       9.7%      7065
     2.31         7.8%      10.0%      7166
     2.24         8.1%      10.3%      7726
     2.17         8.0%      11.2%      7632
     2.11         8.5%      11.8%      8164
     2.05         9.4%      12.7%      8168
     2.00        10.0%      14.2%      8767
    total         6.0%       8.3%    113585

  R-FACTORS FOR INTENSITIES OF DATA SET ../XDS_FF102.HKL                                  

 RESOLUTION   R-FACTOR   R-FACTOR   COMPARED
   LIMIT      observed   expected

     8.95         3.7%       7.0%      1159
     6.33         3.6%       7.1%      2374
     5.16         4.5%       7.2%      3057
     4.47         4.3%       7.2%      3629
     4.00         4.3%       7.1%      4040
     3.65         4.8%       7.2%      4357
     3.38         4.8%       7.3%      4801
     3.16         4.7%       7.4%      5149
     2.98         4.9%       7.7%      5587
     2.83         5.8%       8.2%      5829
     2.70         5.8%       8.6%      6190
     2.58         6.3%       9.1%      6672
     2.48         6.0%       9.4%      6637
     2.39         6.5%       9.9%      7088
     2.31         6.9%      10.4%      7227
     2.24         6.6%      10.7%      7690
     2.17         7.4%      11.7%      7685
     2.11         7.5%      12.3%      8150
     2.05         8.5%      13.3%      8274
     2.00         9.2%      14.7%      8689
    total         5.5%       8.6%    114284

  R-FACTORS FOR INTENSITIES OF DATA SET ../XDS_FF103.HKL                                  

 RESOLUTION   R-FACTOR   R-FACTOR   COMPARED
   LIMIT      observed   expected

     8.95         4.8%      10.0%      1076
     6.33         5.1%      10.0%      2338
     5.16         6.6%      10.1%      3024
     4.47         6.4%      10.1%      3576
     4.00         6.7%      10.1%      3972
     3.65         7.1%      10.1%      4248
     3.38         7.8%      10.2%      4637
     3.16         7.2%      10.3%      5005
     2.98         8.1%      10.6%      5454
     2.83         8.6%      11.0%      5714
     2.70         9.2%      11.4%      6079
     2.58         9.5%      12.0%      6578
     2.48         9.3%      12.4%      6575
     2.39         9.3%      13.0%      7036
     2.31        10.4%      13.4%      7135
     2.24        10.3%      13.9%      7719
     2.17        11.0%      14.9%      7578
     2.11        11.3%      15.6%      8187
     2.05        12.6%      16.7%      8172
     2.00        13.5%      18.8%      8750
    total         8.3%      11.6%    112853

  R-FACTORS FOR INTENSITIES OF DATA SET ../XDS_FF104.HKL                                  

 RESOLUTION   R-FACTOR   R-FACTOR   COMPARED
   LIMIT      observed   expected

     8.95         3.8%       7.6%      1040
     6.33         3.7%       7.7%      2337
     5.16         5.0%       7.8%      3046
     4.47         4.4%       7.7%      3599
     4.00         4.5%       7.7%      3989
     3.65         5.2%       7.7%      4295
     3.38         5.5%       7.8%      4754
     3.16         5.2%       7.9%      5100
     2.98         5.7%       8.2%      5562
     2.83         6.2%       8.5%      5763
     2.70         6.2%       8.9%      6160
     2.58         6.4%       9.3%      6662
     2.48         6.6%       9.6%      6607
     2.39         6.4%      10.1%      7070
     2.31         7.0%      10.4%      7175
     2.24         6.9%      10.7%      7711
     2.17         7.6%      11.5%      7620
     2.11         7.6%      12.0%      8165
     2.05         8.3%      12.9%      8185
     2.00         9.2%      14.3%      8781
    total         5.8%       8.9%    113621

  R-FACTORS FOR INTENSITIES OF DATA SET ../XDS_FF106.HKL                                  

 RESOLUTION   R-FACTOR   R-FACTOR   COMPARED
   LIMIT      observed   expected

     8.95         3.6%       6.9%      1144
     6.33         3.4%       7.0%      2357
     5.16         4.2%       7.1%      3041
     4.47         4.0%       7.1%      3629
     4.00         4.1%       7.0%      4036
     3.65         4.5%       7.1%      4321
     3.38         4.9%       7.2%      4813
     3.16         4.8%       7.3%      5157
     2.98         4.9%       7.5%      5553
     2.83         5.2%       7.9%      5809
     2.70         5.4%       8.3%      6190
     2.58         5.7%       8.7%      6663
     2.48         6.1%       9.0%      6578
     2.39         6.0%       9.5%      7071
     2.31         6.7%       9.8%      7205
     2.24         7.3%      10.3%      7627
     2.17         7.2%      11.1%      7627
     2.11         7.3%      11.6%      8179
     2.05         8.4%      12.3%      8217
     2.00         9.1%      13.8%      8760
    total         5.3%       8.3%    113977

  R-FACTORS FOR INTENSITIES OF DATA SET ../XDS_FF201.HKL                                  

 RESOLUTION   R-FACTOR   R-FACTOR   COMPARED
   LIMIT      observed   expected

     8.95        10.5%      14.1%      1174
     6.33         8.2%      14.2%      2401
     5.16        11.1%      14.4%      3051
     4.47        11.0%      14.3%      3639
     4.00        11.5%      14.3%      3997
     3.65        13.4%      14.4%      4387
     3.38        13.3%      14.6%      4873
     3.16        14.0%      14.9%      5201
     2.98        14.9%      15.5%      5553
     2.83        15.7%      16.3%      5858
     2.70        16.3%      17.1%      6240
     2.58        17.3%      18.0%      6720
     2.48        16.8%      18.8%      6688
     2.39        17.3%      20.0%      7235
     2.31        18.2%      21.2%      7281
     2.24        18.4%      22.0%      7836
     2.17        19.5%      24.4%      7671
     2.11        21.7%      26.3%      8275
     2.05        21.4%      28.8%      8274
     2.00        22.3%      34.1%      8814
    total        14.9%      17.5%    115168

  R-FACTORS FOR INTENSITIES OF DATA SET ../XDS_FF202.HKL                                  

 RESOLUTION   R-FACTOR   R-FACTOR   COMPARED
   LIMIT      observed   expected

     8.95         8.5%      12.8%      1136
     6.33         7.9%      12.9%      2334
     5.16         8.7%      13.0%      3029
     4.47         8.4%      12.9%      3609
     4.00         9.1%      12.9%      4050
     3.65        10.0%      12.9%      4365
     3.38        10.9%      13.0%      4888
     3.16        10.6%      13.1%      5203
     2.98        11.5%      13.4%      5548
     2.83        11.2%      13.8%      5836
     2.70        12.1%      14.2%      6224
     2.58        12.4%      14.7%      6679
     2.48        12.7%      15.1%      6628
     2.39        12.9%      15.5%      7162
     2.31        14.2%      15.8%      7228
     2.24        13.9%      16.1%      7764
     2.17        14.4%      16.8%      7645
     2.11        15.4%      17.4%      8199
     2.05        16.2%      18.2%      8221
     2.00        16.6%      19.7%      8780
    total        11.3%      14.2%    114528

  R-FACTORS FOR INTENSITIES OF DATA SET ../XDS_FF203.HKL                                  

 RESOLUTION   R-FACTOR   R-FACTOR   COMPARED
   LIMIT      observed   expected

     8.95         9.7%      12.8%      1183
     6.33         7.3%      13.0%      2373
     5.16         9.9%      13.1%      3014
     4.47         9.4%      13.1%      3591
     4.00        10.1%      13.0%      4038
     3.65        11.7%      13.1%      4340
     3.38        12.3%      13.3%      4779
     3.16        12.8%      13.5%      5141
     2.98        12.9%      14.1%      5481
     2.83        13.7%      14.9%      5804
     2.70        14.4%      15.7%      6146
     2.58        15.8%      16.7%      6644
     2.48        15.5%      17.5%      6577
     2.39        15.4%      18.4%      7154
     2.31        16.5%      19.5%      7218
     2.24        16.3%      19.9%      7724
     2.17        17.7%      22.0%      7644
     2.11        19.2%      23.3%      8175
     2.05        19.2%      25.5%      8218
     2.00        19.9%      29.1%      8773
    total        13.3%      15.8%    114017

  R-FACTORS FOR INTENSITIES OF DATA SET ../XDS_FF204.HKL                                  

 RESOLUTION   R-FACTOR   R-FACTOR   COMPARED
   LIMIT      observed   expected

     8.95         7.4%      11.7%      1119
     6.33         6.4%      11.9%      2343
     5.16         8.8%      12.0%      3021
     4.47         7.8%      11.9%      3529
     4.00         9.0%      11.9%      3965
     3.65        10.6%      12.0%      4233
     3.38        11.0%      12.2%      4784
     3.16        11.2%      12.4%      5085
     2.98        11.0%      12.9%      5463
     2.83        13.0%      13.6%      5780
     2.70        13.0%      14.4%      6153
     2.58        14.8%      15.3%      6627
     2.48        14.1%      16.1%      6642
     2.39        14.4%      17.0%      7160
     2.31        15.4%      17.9%      7227
     2.24        15.2%      18.6%      7796
     2.17        16.6%      20.4%      7616
     2.11        18.3%      22.1%      8212
     2.05        18.2%      24.1%      8207
     2.00        18.9%      28.2%      8781
    total        12.0%      14.6%    113743

  R-FACTORS FOR INTENSITIES OF DATA SET ../XDS_FF206.HKL                                  

 RESOLUTION   R-FACTOR   R-FACTOR   COMPARED
   LIMIT      observed   expected

     8.95         9.7%      15.5%      1179
     6.33         9.2%      15.8%      2387
     5.16        11.0%      16.0%      3030
     4.47        11.0%      15.9%      3687
     4.00        11.7%      15.8%      4085
     3.65        13.8%      15.9%      4512
     3.38        14.8%      16.1%      4893
     3.16        14.8%      16.4%      5213
     2.98        16.2%      16.9%      5597
     2.83        17.2%      17.8%      5879
     2.70        16.4%      18.6%      6219
     2.58        17.4%      19.5%      6694
     2.48        17.7%      20.2%      6630
     2.39        18.2%      21.0%      7217
     2.31        20.3%      21.8%      7272
     2.24        19.6%      22.2%      7793
     2.17        19.8%      23.8%      7650
     2.11        22.6%      24.8%      8255
     2.05        22.5%      26.4%      8237
     2.00        22.4%      29.4%      8791
    total        15.6%      18.4%    115220

  R-FACTORS FOR INTENSITIES OF DATA SET ../XDS_FF301.HKL                                  

 RESOLUTION   R-FACTOR   R-FACTOR   COMPARED
   LIMIT      observed   expected

     8.95         9.3%      15.8%      1177
     6.33        11.3%      16.0%      2356
     5.16        14.1%      16.2%      2906
     4.47        12.5%      16.1%      3386
     4.00        14.6%      16.0%      3773
     3.65        16.2%      16.1%      4059
     3.38        16.4%      16.2%      4455
     3.16        15.6%      16.4%      4793
     2.98        15.6%      16.7%      5220
     2.83        18.7%      17.4%      5410
     2.70        19.3%      18.1%      5782
     2.58        21.0%      18.7%      6313
     2.48        20.0%      19.3%      6297
     2.39        19.9%      20.0%      6862
     2.31        21.7%      20.6%      6959
     2.24        20.6%      21.1%      7488
     2.17        22.3%      22.5%      7337
     2.11        23.6%      23.2%      7948
     2.05        23.7%      24.4%      7980
     2.00        24.0%      25.9%      8564
    total        17.3%      18.0%    109065

  R-FACTORS FOR INTENSITIES OF DATA SET ../XDS_FF302.HKL                                  

 RESOLUTION   R-FACTOR   R-FACTOR   COMPARED
   LIMIT      observed   expected

     8.95         9.9%      14.8%      1175
     6.33        12.2%      15.1%      2391
     5.16        14.5%      15.3%      2943
     4.47        13.4%      15.1%      3487
     4.00        15.0%      15.1%      3794
     3.65        16.3%      15.2%      4198
     3.38        17.8%      15.3%      4716
     3.16        16.1%      15.5%      5016
     2.98        17.1%      15.9%      5346
     2.83        18.7%      16.8%      5476
     2.70        19.5%      17.4%      5732
     2.58        21.2%      18.2%      6440
     2.48        21.1%      18.9%      6345
     2.39        20.2%      19.6%      6893
     2.31        23.0%      20.5%      7087
     2.24        23.6%      21.1%      7590
     2.17        23.2%      22.9%      7443
     2.11        25.4%      23.9%      8040
     2.05        26.6%      25.5%      8042
     2.00        26.3%      27.0%      8615
    total        18.2%      17.4%    110769

  R-FACTORS FOR INTENSITIES OF DATA SET ../XDS_FF303-2.HKL                                

 RESOLUTION   R-FACTOR   R-FACTOR   COMPARED
   LIMIT      observed   expected

     8.95        10.4%      16.7%      1126
     6.33        13.0%      16.9%      2400
     5.16        15.8%      17.1%      2984
     4.47        15.1%      17.0%      3522
     4.00        16.6%      16.9%      3838
     3.65        16.7%      17.0%      4196
     3.38        19.4%      17.2%      4762
     3.16        17.4%      17.4%      5055
     2.98        20.1%      17.9%      5443
     2.83        20.1%      18.8%      5513
     2.70        22.3%      19.6%      5907
     2.58        22.5%      20.5%      6509
     2.48        23.5%      21.4%      6477
     2.39        22.2%      22.4%      7050
     2.31        25.2%      23.4%      7119
     2.24        26.9%      24.1%      7681
     2.17        25.7%      26.1%      7467
     2.11        27.7%      27.7%      8086
     2.05        29.5%      29.3%      8098
     2.00        29.1%      31.9%      8662
    total        20.0%      19.8%    111895

  R-FACTORS FOR INTENSITIES OF DATA SET ../XDS_FF303-4.HKL                                

 RESOLUTION   R-FACTOR   R-FACTOR   COMPARED
   LIMIT      observed   expected

     8.95         9.1%      12.4%      1170
     6.33        10.5%      12.8%      2373
     5.16        13.0%      13.0%      2957
     4.47        11.4%      12.8%      3455
     4.00        13.3%      12.7%      3806
     3.65        15.0%      12.9%      4206
     3.38        15.3%      13.1%      4721
     3.16        14.6%      13.3%      5042
     2.98        14.3%      13.8%      5394
     2.83        16.9%      14.9%      5547
     2.70        17.4%      15.8%      5827
     2.58        19.8%      16.7%      6554
     2.48        18.8%      17.5%      6444
     2.39        18.8%      18.5%      7007
     2.31        21.3%      19.5%      7176
     2.24        20.0%      20.1%      7627
     2.17        21.4%      22.2%      7539
     2.11        22.9%      23.0%      8100
     2.05        23.6%      25.0%      8115
     2.00        24.0%      26.8%      8673
    total        16.2%      15.6%    111733

  R-FACTORS FOR INTENSITIES OF DATA SET ../XDS_FF305.HKL                                  

 RESOLUTION   R-FACTOR   R-FACTOR   COMPARED
   LIMIT      observed   expected

     8.95        10.4%      16.0%      1150
     6.33        12.7%      16.2%      2392
     5.16        15.1%      16.4%      2948
     4.47        14.7%      16.3%      3471
     4.00        16.0%      16.2%      3781
     3.65        16.7%      16.3%      4164
     3.38        18.3%      16.5%      4684
     3.16        17.1%      16.7%      5013
     2.98        19.3%      17.2%      5301
     2.83        19.4%      18.2%      5519
     2.70        21.2%      19.0%      5730
     2.58        22.4%      19.9%      6444
     2.48        22.8%      20.8%      6364
     2.39        21.9%      21.8%      6924
     2.31        24.8%      23.0%      7157
     2.24        26.2%      23.7%      7588
     2.17        25.4%      26.1%      7534
     2.11        27.4%      27.6%      8047
     2.05        29.3%      29.9%      8129
     2.00        28.4%      32.1%      8622
    total        19.5%      19.2%    110962

  R-FACTORS FOR INTENSITIES OF DATA SET ../XDS_FF306.HKL                                  

 RESOLUTION   R-FACTOR   R-FACTOR   COMPARED
   LIMIT      observed   expected

     8.95        13.0%      21.2%      1158
     6.33        14.8%      21.4%      2418
     5.16        17.7%      21.5%      2977
     4.47        16.9%      21.4%      3573
     4.00        18.2%      21.4%      3890
     3.65        20.0%      21.5%      4237
     3.38        22.8%      21.6%      4745
     3.16        20.3%      21.8%      4989
     2.98        23.4%      22.2%      5461
     2.83        24.5%      23.1%      5696
     2.70        26.4%      23.9%      6029
     2.58        26.5%      24.8%      6455
     2.48        28.0%      25.5%      6473
     2.39        26.3%      26.3%      6933
     2.31        28.4%      27.2%      7084
     2.24        30.2%      27.7%      7614
     2.17        29.2%      29.7%      7489
     2.11        32.4%      31.0%      8096
     2.05        34.1%      33.0%      8097
     2.00        33.0%      35.2%      8663
    total        23.2%      24.0%    112077

  R-FACTORS FOR INTENSITIES OF DATA SET ../XDS_FF307.HKL                                  

 RESOLUTION   R-FACTOR   R-FACTOR   COMPARED
   LIMIT      observed   expected

     8.95        13.0%      22.0%      1156
     6.33        15.3%      22.1%      2389
     5.16        18.8%      22.3%      2997
     4.47        17.9%      22.2%      3573
     4.00        19.1%      22.1%      3925
     3.65        20.0%      22.2%      4274
     3.38        23.3%      22.4%      4763
     3.16        21.2%      22.6%      5056
     2.98        24.7%      23.0%      5518
     2.83        24.7%      23.9%      5747
     2.70        27.6%      24.7%      6157
     2.58        26.8%      25.7%      6558
     2.48        28.2%      26.5%      6513
     2.39        26.4%      27.4%      7022
     2.31        29.5%      28.4%      7184
     2.24        31.4%      29.1%      7732
     2.17        29.5%      31.3%      7537
     2.11        33.3%      32.9%      8186
     2.05        35.4%      35.1%      8138
     2.00        34.4%      38.0%      8750
    total        23.9%      25.0%    113175

  R-FACTORS FOR INTENSITIES OF DATA SET ../XDS_FF308.HKL                                  

 RESOLUTION   R-FACTOR   R-FACTOR   COMPARED
   LIMIT      observed   expected

     8.95        10.7%      17.8%      1152
     6.33        13.8%      18.0%      2400
     5.16        15.8%      18.2%      2998
     4.47        14.3%      18.1%      3563
     4.00        16.3%      18.0%      3928
     3.65        17.8%      18.1%      4261
     3.38        20.3%      18.3%      4743
     3.16        17.9%      18.4%      5015
     2.98        18.8%      18.9%      5473
     2.83        21.1%      19.7%      5722
     2.70        22.5%      20.5%      6030
     2.58        23.4%      21.3%      6552
     2.48        24.0%      21.9%      6522
     2.39        23.9%      22.5%      7056
     2.31        25.2%      23.1%      7189
     2.24        25.5%      23.7%      7702
     2.17        25.6%      25.2%      7541
     2.11        27.5%      26.1%      8152
     2.05        28.6%      27.6%      8127
     2.00        29.0%      29.5%      8703
    total        20.2%      20.3%    112829

  R-FACTORS FOR INTENSITIES OF DATA SET ../XDS_FF310.HKL                                  

 RESOLUTION   R-FACTOR   R-FACTOR   COMPARED
   LIMIT      observed   expected

     8.95         9.1%      12.3%      1172
     6.33        10.9%      12.7%      2336
     5.16        12.8%      12.9%      2886
     4.47        11.6%      12.7%      3387
     4.00        13.1%      12.6%      3736
     3.65        14.8%      12.8%      4162
     3.38        15.7%      13.0%      4617
     3.16        14.9%      13.3%      4934
     2.98        15.4%      13.9%      5289
     2.83        16.8%      15.0%      5595
     2.70        17.9%      16.0%      5723
     2.58        20.3%      17.0%      6481
     2.48        19.8%      17.9%      6383
     2.39        19.6%      18.6%      6902
     2.31        21.5%      19.5%      7157
     2.24        21.9%      20.1%      7397
     2.17        22.4%      22.3%      7516
     2.11        24.0%      23.3%      8016
     2.05        25.0%      25.5%      8098
     2.00        25.6%      27.5%      8571
    total        16.7%      15.7%    110358


 ******************************************************************************
    WILSON STATISTICS OF SCALED DATA SET: alldatasets.ahkl                                  
 ******************************************************************************

 Data is divided into resolution shells and a straight line 
 A - 2*B*SS is fitted to log<I>, where
   RES    = mean resolution (Angstrom) in shell
   SS     = mean of (sin(THETA)/LAMBDA)**2 in shell
   <I>    = mean reflection intensity in shell
   BO     = (A - log<I>)/(2*SS)
    #     = number of reflections in resolution shell

   WILSON LINE (using all data) : A=  12.424 B=  16.747 CORRELATION=  0.92
      #      RES      SS        <I>       log(<I>)       BO
     137    11.141   0.002  2.2483E+05      12.323      25.1
     205     6.963   0.005  1.2182E+05      11.710      69.2
     258     5.450   0.008  1.2306E+05      11.720      41.8
     290     4.627   0.012  1.8768E+05      12.142      12.1
     333     4.089   0.015  2.4535E+05      12.410       0.5
     361     3.699   0.018  2.2154E+05      12.308       3.2
     380     3.407   0.022  1.6431E+05      12.010       9.6
     401     3.178   0.025  1.4603E+05      11.892      10.8
     441     2.987   0.028  9.8630E+04      11.499      16.5
     466     2.823   0.031  7.5221E+04      11.228      19.1
     464     2.687   0.035  6.6298E+04      11.102      19.1
     507     2.569   0.038  5.8822E+04      10.982      19.0
     511     2.464   0.041  5.4566E+04      10.907      18.4
     539     2.372   0.044  4.6361E+04      10.744      18.9
     558     2.288   0.048  5.2299E+04      10.865      16.3
     564     2.214   0.051  4.5031E+04      10.715      16.8
     589     2.146   0.054  4.0036E+04      10.598      16.8
     598     2.084   0.058  3.8240E+04      10.552      16.3
     646     2.027   0.061  3.2896E+04      10.401      16.6


 HIGHER ORDER MOMENTS OF WILSON DISTRIBUTION OF  CENTRIC DATA
    AS COMPARED WITH THEORETICAL VALUES. (EXPECTED: 1.00)    
      #      RES        <I**2>/      <I**3>/      <I**4>/  
                         3<I>**2     15<I>**3    105<I>**4 

      79    11.141        0.596        0.308        0.130
      77     6.963        0.737        0.534        0.340
      84     5.450        0.882        0.751        0.566
      80     4.627        0.873        0.796        0.663
      81     4.089        0.825        0.543        0.304
      84     3.699        1.183        1.427        1.726
      77     3.407        0.986        0.972        0.853
      79     3.178        1.148        1.154        0.983
      82     2.987        0.884        0.650        0.397
      85     2.823        0.678        0.440        0.252
      78     2.687        0.806        0.715        0.568
      84     2.569        0.981        1.081        1.225
      82     2.464        0.744        0.529        0.356
      81     2.372        0.600        0.404        0.235
      81     2.288        0.795        0.547        0.311
      80     2.214        1.487        2.262        2.884
      88     2.146        0.527        0.264        0.108
      77     2.084        0.739        0.492        0.285
      87     2.027        0.843        0.799        0.715
    1546   overall        0.857        0.771        0.678


 HIGHER ORDER MOMENTS OF WILSON DISTRIBUTION OF ACENTRIC DATA
    AS COMPARED WITH THEORETICAL VALUES. (EXPECTED: 1.00)    
      #      RES        <I**2>/      <I**3>/      <I**4>/  
                         2<I>**2      6<I>**3     24<I>**4 

      58    11.141        1.254        1.214        1.011
     128     6.963        1.055        0.997        0.863
     174     5.450        0.910        0.778        0.634
     210     4.627        1.157        1.634        2.688
     252     4.089        0.971        0.905        0.799
     277     3.699        0.877        0.708        0.522
     303     3.407        0.865        0.658        0.447
     322     3.178        0.903        0.788        0.645
     359     2.987        0.935        0.813        0.641
     381     2.823        0.958        0.849        0.711
     386     2.687        0.977        0.894        0.777
     423     2.569        0.940        0.831        0.672
     429     2.464        0.895        0.706        0.498
     458     2.372        0.968        0.850        0.680
     477     2.288        0.956        0.956        1.039
     484     2.214        0.992        1.081        1.233
     501     2.146        1.027        1.042        1.041
     521     2.084        0.947        0.858        0.750
     559     2.027        1.005        1.105        1.401
    6702   overall        0.964        0.914        0.885

   ======= CUMULATIVE INTENSITY DISTRIBUTION =======
 DEFINITIONS:
   <I>    = mean reflection intensity
 Na(Z)exp = expected number of acentric reflections with I <= Z*<I>
 Na(Z)obs = observed number of acentric reflections with I <= Z*<I>
 Nc(Z)exp = expected number of  centric reflections with I <= Z*<I>
 Nc(Z)obs = observed number of  centric reflections with I <= Z*<I>



 Nc(Z)obs/Nc(Z)exp versus resolution and Z (0.1-1.0)
      #      RES     0.1   0.2   0.3   0.4   0.5   0.6   0.7   0.8   0.9   1.0

      79    11.141  0.82  1.03  1.00  0.96  0.95  1.04  1.00  1.03  1.00  0.98
      77     6.963  0.89  0.98  1.00  0.96  0.97  0.95  1.04  0.99  0.99  1.01
      84     5.450  0.91  0.90  0.89  0.91  0.87  0.85  0.92  0.89  0.98  0.99
      80     4.627  0.96  0.98  0.93  0.92  0.89  1.02  1.07  1.01  0.99  1.04
      81     4.089  0.85  0.96  0.86  0.97  1.00  0.97  0.95  0.92  0.96  0.96
      84     3.699  1.15  1.14  1.17  1.13  1.10  1.06  1.02  1.02  0.98  1.01
      77     3.407  0.99  1.01  1.03  1.10  1.10  1.06  1.02  1.03  1.01  1.01
      79     3.178  1.17  1.06  0.94  0.94  1.00  1.01  1.00  1.05  1.02  1.04
      82     2.987  0.69  0.92  1.02  1.03  1.01  0.98  0.96  0.97  0.95  0.97
      85     2.823  0.90  0.95  0.93  0.97  0.90  0.90  0.95  0.95  0.99  0.98
      78     2.687  0.83  1.04  0.98  1.00  0.99  1.05  1.05  1.08  1.07  1.07
      84     2.569  0.67  0.86  0.97  0.91  0.91  0.93  0.94  1.00  1.01  1.03
      82     2.464  0.64  1.02  1.05  0.98  1.01  1.06  1.00  1.01  0.98  0.97
      81     2.372  0.89  0.96  1.01  0.94  1.04  1.01  1.03  1.04  1.07  1.07
      81     2.288  0.85  0.86  0.98  0.97  0.90  0.92  0.97  1.00  1.00  1.07
      80     2.214  0.96  1.05  1.08  1.03  1.08  1.09  1.11  1.07  1.05  1.04
      88     2.146  0.82  0.95  0.98  0.94  0.96  1.01  1.05  1.03  1.00  1.03
      77     2.084  0.68  0.75  0.87  0.91  1.00  1.02  0.98  1.01  0.99  1.01
      87     2.027  0.79  0.90  1.08  1.07  1.10  1.06  1.08  1.06  1.05  1.03
    1546   overall  0.86  0.96  0.99  0.98  0.99  1.00  1.01  1.01  1.00  1.02


 Na(Z)obs/Na(Z)exp versus resolution and Z (0.1-1.0)
      #      RES     0.1   0.2   0.3   0.4   0.5   0.6   0.7   0.8   0.9   1.0

      58    11.141  0.36  1.24  1.06  0.99  0.88  0.88  0.79  0.85  0.81  0.79
     128     6.963  0.99  1.03  0.96  0.88  0.85  0.92  0.90  0.92  0.96  1.00
     174     5.450  0.60  0.86  0.86  0.87  0.86  0.94  0.96  0.97  0.92  0.99
     210     4.627  1.00  0.92  0.97  1.08  1.03  0.96  0.95  0.99  0.98  1.00
     252     4.089  0.92  1.14  1.04  1.11  1.05  1.01  1.02  1.02  1.00  0.99
     277     3.699  0.68  0.82  0.93  0.96  0.93  0.94  0.95  0.92  0.95  0.99
     303     3.407  0.90  0.82  0.81  0.83  0.80  0.83  0.87  0.88  0.90  0.98
     322     3.178  0.75  0.81  0.86  0.87  0.91  0.92  0.94  0.98  0.99  0.98
     359     2.987  0.76  0.85  0.95  1.01  1.00  0.97  1.01  0.98  1.00  1.00
     381     2.823  0.66  0.94  0.88  0.92  0.94  0.92  0.96  0.99  0.98  0.98
     386     2.687  0.46  0.87  0.87  0.97  0.97  0.96  0.99  0.98  0.99  0.96
     423     2.569  0.60  0.81  0.99  0.98  0.98  0.99  1.00  1.00  1.00  1.02
     429     2.464  0.64  0.87  0.94  0.97  0.91  0.92  0.95  0.94  0.93  0.94
     458     2.372  0.46  0.75  0.83  0.91  0.94  0.93  0.91  0.94  0.95  0.96
     477     2.288  0.68  0.76  0.83  0.91  0.96  0.95  0.95  0.97  0.98  0.97
     484     2.214  0.50  0.73  0.81  0.91  0.96  0.96  0.99  0.99  1.02  1.03
     501     2.146  0.40  0.75  0.89  0.99  0.95  0.95  0.95  0.94  0.98  0.99
     521     2.084  0.69  0.94  0.98  0.95  0.93  0.94  0.96  0.97  0.97  0.97
     559     2.027  0.55  0.76  0.83  0.90  0.94  0.96  0.97  0.97  0.96  1.00
    6702   overall  0.64  0.84  0.89  0.94  0.94  0.94  0.96  0.96  0.97  0.99

 cpu time used by XSCALE      197.0 sec
 elapsed wall-clock time       64.3 sec
