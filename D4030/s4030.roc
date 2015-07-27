
smr # respin

#vb 150
#mdelay 999
#getib

module 4030

rddac ia24-trim32-lab
rdtrim ia24-trim32-lab

dac 13  90  # VIBias_Bus (max 137)
dac 22 255  # VIColOr

pixt 12 39 76 15
pixm 12 39 76
pixd 12 39 76

pixt 12 39 75 15
pixt 12 38 76 10
pixt  4 51 24  1
pixt  1  9 21  6
pixt 6 0 52 6
pixt 6 0 66 9
pixt 12 6 77 8

modmap 20
