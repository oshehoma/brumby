


import pandas as pd

import matplotlib.pyplot as plt


df = pd.read_csv('mean_conner.csv')


# output of print(list(df))

#['Unnamed: 0', 'peaks', 'chrom', 'start', 'stop', 'Input.0.1', 'Input.0.2', 'Input.60.1', 'Input.60.2', 'Rap1.0.1', 'Rap1.0.2', 'Rap1.60.1', 'Rap1.60.2', 'FLAG.0.1', 'FLAG.0.2', 'FLAG.10.1', 'FLAG.10.2', 'FLAG.20.1', 'FLAG.20.2', 'FLAG.30.1', 'FLAG.30.2', 'FLAG.40.1', 'FLAG.40.2', 'FLAG.50.1', 'FLAG.50.2', 'FLAG.60..1', 'FLAG.60.2', 'FLAG.90.1', 'FLAG.90.2', 'FLAG.120.1', 'FLAG.120.2', 'FLAG.150.1', 'FLAG.150.2', 'MYC.0..2', 'MYC.0.1', 'MYC.10.1', 'MYC.10.2', 'MYC.20.1', 'MYC.20.2', 'MYC.30.1', 'MYC.30.2', 'MYC.40.1', 'MYC.40.2', 'MYC.50.1', 'MYC.50.2', 'MYC.60.1', 'MYC.60.2', 'MYC.90.1', 'MYC.90.2', 'MYC120.2', 'MYC.120.1', 'MYC.150.1', 'MYC.150.2']

# hand edited file to correct three ('.') labeling inconsitencies (FLAG.60..1, MYC.0..2, MYC120.2)


time = [0, 10, 20, 30, 40, 50, 60, 90, 120, 150]

for tag in (['FLAG.', 'MYC.']):
    for t in time:
        rep1 = tag + str(t) + '.1'
        rep2 = tag  + str(t) + '.2'
        avg = tag + str(t) + '.avg'
        sd = tag + str(t) + '.sd'
        df[avg] = df[[rep1, rep2]].mean(axis=1)
        df[sd] = df[[rep1, rep2]].std(axis=1)

raptime = [0, 60]
for tag in (['Rap1.', 'Input.']):
    for rt in raptime:
        rep1 = tag + str(rt) + '.1'
        rep2 = tag  + str(rt) + '.2'
        avg = tag + str(rt) + '.avg'
        sd = tag + str(rt) + '.sd'
        df[avg] = df[[rep1, rep2]].mean(axis=1)
        df[sd] = df[[rep1, rep2]].std(axis=1)




# output of print(list(df))

#['Unnamed: 0', 'peaks', 'chrom', 'start', 'stop', 'Input.0.1', 'Input.0.2', 'Input.60.1', 'Input.60.2', 'Rap1.0.1', 'Rap1.0.2', 'Rap1.60.1', 'Rap1.60.2', 'FLAG.0.1', 'FLAG.0.2', 'FLAG.10.1', 'FLAG.10.2', 'FLAG.20.1', 'FLAG.20.2', 'FLAG.30.1', 'FLAG.30.2', 'FLAG.40.1', 'FLAG.40.2', 'FLAG.50.1', 'FLAG.50.2', 'FLAG.60.1', 'FLAG.60.2', 'FLAG.90.1', 'FLAG.90.2', 'FLAG.120.1', 'FLAG.120.2', 'FLAG.150.1', 'FLAG.150.2', 'MYC.0.2', 'MYC.0.1', 'MYC.10.1', 'MYC.10.2', 'MYC.20.1', 'MYC.20.2', 'MYC.30.1', 'MYC.30.2', 'MYC.40.1', 'MYC.40.2', 'MYC.50.1', 'MYC.50.2', 'MYC.60.1', 'MYC.60.2', 'MYC.90.1', 'MYC.90.2', 'MYC.120.2', 'MYC.120.1', 'MYC.150.1', 'MYC.150.2', 'FLAG.0_avg', 'FLAG.10_avg', 'FLAG.20_avg', 'FLAG.30_avg', 'FLAG.40_avg', 'FLAG.50_avg', 'FLAG.60_avg', 'FLAG.90_avg', 'FLAG.120_avg', 'FLAG.150_avg', 'MYC.0_avg', 'MYC.10_avg', 'MYC.20_avg', 'MYC.30_avg', 'MYC.40_avg', 'MYC.50_avg', 'MYC.60_avg', 'MYC.90_avg', 'MYC.120_avg', 'MYC.150_avg']

# plot 'randomly' selected rows
    
fname = 'myc_vs_flag_over_time_some_peaks'

#print(df[sd])

# adjust plotting parameters
fs = 18 #font size
lw = 4	# line width
parameters = {'axes.labelsize': fs,
	'axes.labelweight': 'bold',
	'axes.linewidth' : lw,
	'axes.titlesize': fs,
	'axes.titleweight': 'bold',
	'xtick.labelsize': fs,
	'axes.spines.top': False,
	'axes.spines.right': False,
	'ytick.labelsize': fs,
	'font.weight': 'bold',
	'legend.fontsize': 18
 	}
plt.rcParams.update(parameters)


fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(15,15))

fig.suptitle('Some "randomly" selected peaks.', fontsize=fs, fontweight='bold')

rows = list([[0, 15, 33],
            [168, 370, 450],
            [502, 672, 759]])

for i in range(0,3):
    for j in range (0,3):

        myc = list()
        flag = list()
        myc_sd = list()
        flag_sd = list()
        
        for t in time:
            col_myc = 'MYC.' + str(t) + '.avg'
            col_flag = 'FLAG.' + str(t) + '.avg'
            col_myc_sd = 'MYC.' + str(t) + '.sd'
            col_flag_sd = 'FLAG.' + str(t) + '.sd'
        
            flag.append(df[col_myc][rows[i][j]])
            myc.append(df[col_flag][rows[i][j]])
            flag_sd.append(df[col_myc_sd][rows[i][j]])
            myc_sd.append(df[col_flag_sd][rows[i][j]])

        rap1 = list()
        rap1_sd = list()
        inpu = list()
        inpu_sd = list()
            
        for rt in raptime:
            col_rap1 = 'Rap1.' + str(rt) + '.avg'
            col_rap1_sd = 'Rap1.' + str(rt) + '.sd'
            col_inpu = 'Input.' + str(rt) + '.avg'
            col_inpu_sd = 'Input.' + str(rt) + '.sd'
            
            rap1.append(df[col_rap1][rows[i][j]])
            rap1_sd.append(df[col_rap1_sd][rows[i][j]])
            inpu.append(df[col_inpu][rows[i][j]])
            inpu_sd.append(df[col_inpu_sd][rows[i][j]])
            
        #print(rap1)
        #print(rap1_sd)
        
            
        curAx = axes[i,j]
        curAx.errorbar(time, myc, yerr=myc_sd, fmt='o',
                color='blue', ecolor='lightblue',
                elinewidth=3, capsize=0, label='Myc')
        curAx.errorbar(time, flag, yerr=flag_sd, fmt='o',
                color='red', ecolor='pink',
                elinewidth=3, capsize=0, label='Flag')
        curAx.errorbar(raptime, rap1, yerr=rap1_sd, fmt='x',
                color='black', ecolor='gray',
                elinewidth=9, capsize=0, label='Rap1')
        curAx.errorbar(raptime, inpu, yerr=inpu_sd, fmt='x',
                color='green', ecolor='lightgreen',
                elinewidth=9, capsize=0, label='Input')
    #curAx.scatter(time, myc, color='blue', label='Myc')
        #curAx.scatter(time, flag, color='red', label='Flag')
        curAx.set_title(df['peaks'][rows[i][j]])
        curAx.set_xlabel('Time (min)', fontsize=fs, fontweight='bold')
        curAx.set_ylabel('Signal', fontsize=fs, fontweight='bold')
        curAx.legend(loc='lower right')
        curAx.tick_params(labelsize=fs)
        curAx.set_xlim([-10, 150])
        #curAx.set_ylim([3000, 12000])

    
    
plt.subplots_adjust(top=0.91, bottom=0.06,
			left = 0.1, right = 0.97,
			wspace=0.374, hspace = 0.336)

plt.show()

fig.savefig(fname)
