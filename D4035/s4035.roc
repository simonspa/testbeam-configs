
smr # respin

#vb 150
#mdelay 999
#getib

module 4035

rddac ia24-trim32-lab
rdtrim ia24-trim32-lab

dac 13  90  # VIBias_Bus (max 119)
dac 22 255  # VIColOr

dac 1 9 # Vdig against readout errors

modmap 20
