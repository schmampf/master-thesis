'''version from 04.02.2021

author: Oliver I.
'''
import glob, os
import numpy as np
from tqdm import tqdm
from datetime import datetime
import h5py

# other self made driver
# from T_over_H_binning import T_over_H
'''version from 23.12.'20
'''
import numpy as np
from datetime import datetime, timedelta

# prevent runtime warning due to division by zero. check binning!
np.seterr(divide='ignore', invalid='ignore')

def T_over_H(tds, time, H):
    '''
    bins temperature reading over magnetic field
    '''
    # read temp & time_temp
    temp, x=[],[]
    for j in tds:
        temp=np.append(temp,np.array(np.genfromtxt(j,delimiter=',',dtype='str')[:,2], dtype='float64'))
        x=np.append(x,np.array(np.genfromtxt(j,delimiter=',',dtype='str')[:,:2], dtype='str'))
    datetimedate=x[::2]
    datetimetime=x[1::2]
    time_temp=np.empty_like(datetimetime, dtype='datetime64[s]')
    for i in range(len(datetimedate)):
        time_temp[i]=datetime.strptime('%s_%s'%(datetimedate[i],datetimetime[i]),'%d-%m-%y_%H:%M:%S')
        
        
    # convert time_temp and time to floats
    nu_time_temp=np.empty_like(time_temp, dtype='float64')
    nu_time=np.empty_like(time, dtype='float64')
    for i,l in enumerate(time_temp):
        dt=datetime.strptime(str(l),'%Y-%m-%dT%H:%M:%S')
        timestamp = (dt - datetime(1970, 1, 1)) / timedelta(seconds=1)
        nu_time_temp[i] = np.float(timestamp)
    for i,l in enumerate(time):
        dt=datetime.strptime(str(l),'%Y-%m-%dT%H:%M:%S')
        timestamp = (dt - datetime(1970, 1, 1)) / timedelta(seconds=1)
        nu_time[i] = np.float(timestamp)
    
    # extend and bins ==> should be equal to time
    extents=[np.min(nu_time),np.max(nu_time)]
    resolution=int(len(nu_time))
    
    # bin tha shit out of it
    isum, edges = np.histogram(nu_time, bins=resolution, range=extents, weights=-H) # dafug. why -H?? idk
    icount, edges=np.histogram(nu_time, bins=resolution, range=extents)
    H_binned=isum/icount # ==H
    isum, edges = np.histogram(nu_time_temp, bins=resolution, range=extents, weights=temp)
    icount, edges=np.histogram(nu_time_temp, bins=resolution, range=extents)
    T_binned=isum/icount
    return T_binned

# prevent runtime warning due to division by zero. check binning!
np.seterr(divide='ignore', invalid='ignore')

def read(ds='FH Cobulk30nm downsweep',loc='../messungen/'):
    '''return data from datasets:
    
    BF CPW8
    - 'BF CPW8 100mK lowbw wopa'
    - 'BF CPW8 warmup'
    - 'BF CPW8 100mK lowbw'
    - 'BF CPW8 4K'
    
    BF CPW7
    - 'BF CPW7 warmup'
    
    FH CoBulky32nm-2
    - 'FH CoBulky32nm-2'
    
    VNA(T)
    - 'VNA(T) with boxxed preamplifier'
    - 'VNA(T) without preamplifier'
    - 'VNA(T) with preamplifier'
    - 'VNA(T) with boxxed and tempered preamplifier'
    
    BF CPWG-4
    - 'BF CPWG4 50mK'
    - 'BF CPWG4 4K'
    - 'BF CPWG4 50mK pwer test'
    - 'BF CPWG4 temp test'
    
    BF Cobulky32nm-1
    Sergej
    - 'BF Cobulky32nm HSWEEP down'
    - 'BF Cobulky32nm HSWEEP up'
    - 'BF Cobulky32nm RFSWEEP down'
    - 'BF Cobulky32nm RFSWEEP up'
    Olli
    - 'BF Cobulky32nm LONG'
    - 'BF Cobulky32nm FAST'
    - 'BF Cobulky32nm TEST'
    
    BF Cobulky3nm
    - 'BF Cobulky3nm HSWEEP up'
    - 'BF Cobulky3nm HSWEEP down'
    
    BF Cobulk30nm
    - 'BF Cobulk30nm HSWEEP up'
    - 'BF Cobulk30nm HSWEEP dwon'
    
    FH Cobulk30nm
    - 'FH Cobulk30nm down'
    - 'FH Cobulk30nm up'
    - 'FH Cobulk30nm all'
    - 'FH Ref WG'
            
    loc: where all the measurement folders are.
    ../ one folder up, 
    messungen/ folder messungen down
    '''
    
    # False initializing
    f=False
    H=False
    S21=False
    time=False
    temp=False
    time_temp=False
    vna_config=False
    comment=False
    
    df={'version':'version from 20210422'}
        
        
    ########################################################################################################################
    #### BF CPW8 
    ########################################################################################################################   
    if ds=='BF CPW8 100mK lowbw wopa':
        # comments?
        comment='without preamplifier'
        
        # Read Data from Files
        locloc='21 04 15 Blue Fors FMR CPW8 Tbase 95mK lowbw wopa/'
        filenames = glob.glob(loc+locloc+'/fsweep_data'+"/*.csv")
        tds_RT=[loc+locloc+'thermo_data/GIR2002_logVNA(RT)_2021-04-16 15-56-13.csv']
        tds_sample=[loc+locloc+'thermo_data/21-04-17/CH7 T 21-04-17.log',
                    loc+locloc+'thermo_data/21-04-18/CH7 T 21-04-18.log',
                    loc+locloc+'thermo_data/21-04-19/CH7 T 21-04-19.log',
                    loc+locloc+'thermo_data/21-04-20/CH7 T 21-04-20.log',
                    loc+locloc+'thermo_data/21-04-21/CH7 T 21-04-21.log']

        # Initialize and frequency
        f=np.genfromtxt(filenames[0],delimiter=',',dtype='float64')[1:,1]*1e-9 
        H_unsorted=np.zeros(len(filenames), dtype='float64')
        time_unsorted=np.zeros(len(filenames), dtype='datetime64[s]')
        sdata=np.zeros([len(f),len(H_unsorted),2],dtype='float64')

        # read Data, H, time
        for i, filename in enumerate(tqdm(filenames)):
            H_unsorted[i]=filename[-38:-31] #1e-4T
            time_unsorted[i]=datetime.strptime(filename[-23:-4], '%Y-%m-%d %H-%M-%S')
            sdata[:,i,:] = np.genfromtxt(filename,delimiter=',',dtype='float64')[1:,2:]
            
        # sort Data, time by H
        H_sort_ind=H_unsorted.argsort()
        H=H_unsorted[H_sort_ind]*1e-4
        time=time_unsorted[H_sort_ind]
        data=sdata[:,H_sort_ind,:]
        
        # Calculate S21
        S21=data[:,:,0]+1j*data[:,:,1]
        
        # vna config
        vna_config={"ZNB40": "frequency sweep",
                     "sample_name": "CPWG-08_95mK_bw50",
                     "timestamp_setup": "2021-04-01 16:03:32.529208",
                     "s_param": "S21",
                     "start": 2000000000,
                     "stop": 40000000000,
                     "points": 1901,
                     "bandwidth": 30,
                     "power": -5,
                     "average": 3,
                     "sweeptime": 69.5145}
        # temperature & time
        df['T_RT(H)']=T_over_H(tds_RT, time, H)
        df['T_sample(H)']=T_over_H(tds_sample, time, H)
        
    elif ds=='BF CPW8 warmup':
        # comments?
        comment='with temped and boxxed preamplifier (25°C)'
        
        # Read Data from Files
        locloc='21 04 08 Blue Fors FMR CPW8 Warm-up/'
        filenames = glob.glob(loc+locloc+'/fsweep_data'+"/*.csv")
        tds_RT=[loc+locloc+'thermo_data/GIR2002_logVNA(RT)_2021-04-08 13-10-18.csv']
        tds_sample=[loc+locloc+'thermo_data/21-04-08/CH7 T 21-04-08.log',
                    loc+locloc+'thermo_data/21-04-09/CH7 T 21-04-09.log',
                    loc+locloc+'thermo_data/21-04-10/CH7 T 21-04-10.log',
                    loc+locloc+'thermo_data/21-04-11/CH7 T 21-04-11.log',
                    loc+locloc+'thermo_data/21-04-12/CH7 T 21-04-12.log']
        tds_magnet=[loc+locloc+'thermo_data/21-04-08/CH3 T 21-04-08.log',
                    loc+locloc+'thermo_data/21-04-09/CH3 T 21-04-09.log',
                    loc+locloc+'thermo_data/21-04-10/CH3 T 21-04-10.log',
                    loc+locloc+'thermo_data/21-04-11/CH3 T 21-04-11.log',
                    loc+locloc+'thermo_data/21-04-12/CH3 T 21-04-12.log']

        # Initialize and frequency
        f=np.genfromtxt(filenames[0],delimiter=',',dtype='float64')[1:,1]*1e-9 
        H_unsorted=np.zeros(len(filenames), dtype='float64')
        time_unsorted=np.zeros(len(filenames), dtype='datetime64[s]')
        sdata=np.zeros([len(f),len(H_unsorted),2],dtype='float64')

        # read Data, H, time
        for i, filename in enumerate(tqdm(filenames)):
            H_unsorted[i]=filename[-38:-31] #1e-4T
            time_unsorted[i]=datetime.strptime(filename[-23:-4], '%Y-%m-%d %H-%M-%S')
            sdata[:,i,:] = np.genfromtxt(filename,delimiter=',',dtype='float64')[1:,2:]
            
        # sort Data, time by H
        H_sort_ind=H_unsorted.argsort()
        H=H_unsorted[H_sort_ind]*1e-4
        time=time_unsorted[H_sort_ind]
        data=sdata[:,H_sort_ind,:]
        
        # Calculate S21
        S21=data[:,:,0]+1j*data[:,:,1]
        
        # vna config
        vna_config={"ZNB40": "frequency sweep",
                     "sample_name": "CPWG-08_warmup",
                     "timestamp_setup": "2021-04-08 13:10:15.614766",
                     "s_param": "S21",
                     "start": 2000000000,
                     "stop": 40000000000,
                     "points": 1901,
                     "bandwidth": 30,
                     "power": -5,
                     "average": 1,
                     "sweeptime": 69.5145}

        # temperature & time
        df['T_RT(H)']=T_over_H(tds_RT, time, H)
        df['T_sample(H)']=T_over_H(tds_sample, time, H)
        df['T_magnet(H)']=T_over_H(tds_magnet, time, H)
        
    elif ds=='BF CPW8 100mK lowbw':
        # comments?
        comment='with temped and boxxed preamplifier (25°C)'
        
        # Read Data from Files
        locloc='21 03 25 Blue Fors FMR CPW8 Tbase 95mK lowbw/'
        filenames = glob.glob(loc+locloc+'/fsweep_data'+"/*.csv")
        tds_RT=[loc+locloc+'thermo_data/GIR2002_logVNA(RT)_2021-04-01 16-03-32.csv']
        tds_sample=[loc+locloc+'thermo_data/21-04-01/CH7 T 21-04-01.log',
                    loc+locloc+'thermo_data/21-04-02/CH7 T 21-04-02.log',
                    loc+locloc+'thermo_data/21-04-03/CH7 T 21-04-03.log',
                    loc+locloc+'thermo_data/21-04-04/CH7 T 21-04-04.log',
                    loc+locloc+'thermo_data/21-04-05/CH7 T 21-04-05.log',
                    loc+locloc+'thermo_data/21-04-06/CH7 T 21-04-06.log']

        # Initialize and frequency
        f=np.genfromtxt(filenames[0],delimiter=',',dtype='float64')[1:,1]*1e-9 
        H_unsorted=np.zeros(len(filenames), dtype='float64')
        time_unsorted=np.zeros(len(filenames), dtype='datetime64[s]')
        sdata=np.zeros([len(f),len(H_unsorted),2],dtype='float64')

        # read Data, H, time
        for i, filename in enumerate(tqdm(filenames)):
            H_unsorted[i]=filename[-38:-31] #1e-4T
            time_unsorted[i]=datetime.strptime(filename[-23:-4], '%Y-%m-%d %H-%M-%S')
            sdata[:,i,:] = np.genfromtxt(filename,delimiter=',',dtype='float64')[1:,2:]
            
        # sort Data, time by H
        H_sort_ind=H_unsorted.argsort()
        H=H_unsorted[H_sort_ind]*1e-4
        time=time_unsorted[H_sort_ind]
        data=sdata[:,H_sort_ind,:]
        
        # Calculate S21
        S21=data[:,:,0]+1j*data[:,:,1]
        
        # vna config
        vna_config={"ZNB40": "frequency sweep",
                     "sample_name": "CPWG-08_95mK_bw50",
                     "timestamp_setup": "2021-04-01 16:03:32.529208",
                     "s_param": "S21",
                     "start": 2000000000,
                     "stop": 40000000000,
                     "points": 1901,
                     "bandwidth": 30,
                     "power": -5,
                     "average": 3,
                     "sweeptime": 69.5145}

        # temperature & time
        df['T_RT(H)']=T_over_H(tds_RT, time, H)
        df['T_sample(H)']=T_over_H(tds_sample, time, H)
        
        
    elif ds=='BF CPW8 4K':
        # comments?
        comment='with temped preamplifier (25°C)'
        
        # Read Data from Files
        filenames = glob.glob(loc+'21 03 19 Blue Fors FMR CPW8/fsweep_data'+"/*.csv")
        tds_RT=[loc+'21 03 19 Blue Fors FMR CPW8/thermo_data/GIR2002_logVNA(RT)_2021-03-19 10-14-18.csv']
        tds_sample=[loc+'21 03 19 Blue Fors FMR CPW8/thermo_data/21-03-19/CH7 T 21-03-19.log',
                    loc+'21 03 19 Blue Fors FMR CPW8/thermo_data/21-03-20/CH7 T 21-03-20.log',
                    loc+'21 03 19 Blue Fors FMR CPW8/thermo_data/21-03-21/CH7 T 21-03-21.log']
        tds_magnet=[loc+'21 03 19 Blue Fors FMR CPW8/thermo_data/21-03-19/CH3 T 21-03-19.log',
                    loc+'21 03 19 Blue Fors FMR CPW8/thermo_data/21-03-20/CH3 T 21-03-20.log',
                    loc+'21 03 19 Blue Fors FMR CPW8/thermo_data/21-03-21/CH3 T 21-03-21.log']

        # Initialize and frequency
        f=np.genfromtxt(filenames[0],delimiter=',',dtype='float64')[1:,1]*1e-9 
        H_unsorted=np.zeros(len(filenames), dtype='float64')
        time_unsorted=np.zeros(len(filenames), dtype='datetime64[s]')
        sdata=np.zeros([len(f),len(H_unsorted),2],dtype='float64')

        # read Data, H, time
        for i, filename in enumerate(tqdm(filenames)):
            H_unsorted[i]=filename[-38:-31] #1e-4T
            time_unsorted[i]=datetime.strptime(filename[-23:-4], '%Y-%m-%d %H-%M-%S')
            sdata[:,i,:] = np.genfromtxt(filename,delimiter=',',dtype='float64')[1:,2:]
            
        # sort Data, time by H
        H_sort_ind=H_unsorted.argsort()
        H=H_unsorted[H_sort_ind]*1e-4
        time=time_unsorted[H_sort_ind]
        data=sdata[:,H_sort_ind,:]
        
        # Calculate S21
        S21=data[:,:,0]+1j*data[:,:,1]
        
        # vna config
        vna_config={"ZNB40": "frequency sweep",
                     "sample_name": "BlueFors CPW-8 4K FAST",
                     "timestamp_setup": "2021-03-19 10:14:17.354616",
                     "s_param": "S21",
                     "start": 2000000000,
                     "stop": 40000000000,
                     "points": 1901,
                     "bandwidth": 1000,
                     "power": -5,
                     "average": 30,
                     "sweeptime": 2.0626}

        # temperature & time
        df['T_RT(H)']=T_over_H(tds_RT, time, H)
        df['T_sample(H)']=T_over_H(tds_sample, time, H)
        df['T_magnet(H)']=T_over_H(tds_magnet, time, H)
        
    ########################################################################################################################
    #### BF CPW7 warmup
    ######################################################################################################################## 
    elif ds=='BF CPW7 warmup':
        # comments?
        comment='no pa'
        
        # Read Data from Files
        locloc='21 02 15 BlueFors FMR CPWG-7  warm up/'
        filenames = glob.glob(loc+locloc+'/fsweep_data'+"/*.csv")
        tds_RT=[loc+locloc+'thermo_data/GIR2002_logVNA(RT)_2021-02-19 14-36-51.csv']
        tds_sample=[loc+locloc+'thermo_data/21-02-19/CH7 T 21-02-19.log',
                    loc+locloc+'thermo_data/21-02-20/CH7 T 21-02-20.log',
                    loc+locloc+'thermo_data/21-02-21/CH7 T 21-02-21.log',
                    loc+locloc+'thermo_data/21-02-22/CH7 T 21-02-22.log']
        tds_magnet=[loc+locloc+'thermo_data/21-02-19/CH3 T 21-02-19.log',
                    loc+locloc+'thermo_data/21-02-20/CH3 T 21-02-20.log',
                    loc+locloc+'thermo_data/21-02-21/CH3 T 21-02-21.log',
                    loc+locloc+'thermo_data/21-02-22/CH3 T 21-02-22.log']

        # Initialize and frequency
        f=np.genfromtxt(filenames[0],delimiter=',',dtype='float64')[1:,1]*1e-9 
        H_unsorted=np.zeros(len(filenames), dtype='float64')
        time_unsorted=np.zeros(len(filenames), dtype='datetime64[s]')
        sdata=np.zeros([len(f),len(H_unsorted),2],dtype='float64')

        # read Data, H, time
        for i, filename in enumerate(tqdm(filenames)):
            H_unsorted[i]=filename[-38:-31] #1e-4T
            time_unsorted[i]=datetime.strptime(filename[-23:-4], '%Y-%m-%d %H-%M-%S')
            sdata[:,i,:] = np.genfromtxt(filename,delimiter=',',dtype='float64')[1:,2:]
            
        # sort Data, time by H
        H_sort_ind=H_unsorted.argsort()
        H=H_unsorted[H_sort_ind]*1e-4
        time=time_unsorted[H_sort_ind]
        data=sdata[:,H_sort_ind,:]
        
        # Calculate S21
        S21=data[:,:,0]+1j*data[:,:,1]
        
        # vna config
        vna_config={"ZNB40": "frequency sweep",
                     "sample_name": "BlueFors CPWG-7 WARM UP",
                     "timestamp_setup": "2021-02-19 14:36:49.936820",
                     "s_param": "S21",
                     "start": 20000000,
                     "stop": 40000000000,
                     "points": 2000,
                     "bandwidth": 2000,
                     "power": -5,
                     "average": 48,
                     "sweeptime": 1.085}

        # temperature & time
        df['T_RT(H)']=T_over_H(tds_RT, time, H)
        df['T_sample(H)']=T_over_H(tds_sample, time, H)
        df['T_magnet(H)']=T_over_H(tds_magnet, time, H)
        
    ########################################################################################################################
    #### FH CoBulky32nm-2
    ########################################################################################################################   
    elif ds=='FH CoBulky32nm-2':
        # comments?
        comment='without preamplifier'
        
        # Read Data from Files
        filenames = glob.glob(loc+'21 02 01 FH CoBulky32nm-2/fsweep_data'+"/*.csv")
        tds_RT=[loc+'21 02 01 FH CoBulky32nm-2/thermo_data/GIR2002_logFH_CoBulk32nm-2_2021-02-04 11-21-47.csv']
        tds_sample=[loc+
             '21 02 01 FH CoBulky32nm-2/thermo_data/LakeShore370AC_logFH_CoBulk32nm-2_2021-02-04 11-21-47.csv']

        # Initialize and frequency
        f=np.genfromtxt(filenames[0],delimiter=',',dtype='float64')[1:,1]*1e-9 
        H_unsorted=np.zeros(len(filenames), dtype='float64')
        time_unsorted=np.zeros(len(filenames), dtype='datetime64[s]')
        sdata=np.zeros([len(f),len(H_unsorted),2],dtype='float64')

        # read Data, H, time
        for i, filename in enumerate(tqdm(filenames)):
            H_unsorted[i]=filename[-38:-31] #1e-4T
            time_unsorted[i]=datetime.strptime(filename[-23:-4], '%Y-%m-%d %H-%M-%S')
            sdata[:,i,:] = np.genfromtxt(filename,delimiter=',',dtype='float64')[1:,2:]
            
        # sort Data, time by H
        H_sort_ind=H_unsorted.argsort()
        H=H_unsorted[H_sort_ind]*1e-4
        time=time_unsorted[H_sort_ind]
        data=sdata[:,H_sort_ind,:]
        
        # Calculate S21
        S21=data[:,:,0]+1j*data[:,:,1]
        
        # vna config
        vna_config={"ZNB40": "frequency sweep",
                     "sample_name": "VNA(RT)",
                     "timestamp_setup": "2021-01-29 16:22:21.544290",
                     "s_param": "S21",
                     "start": 2000000000,
                     "stop": 27000000000,
                     "points": 1251,
                     "bandwidth": 1000,
                     "power": -5,
                     "average": 48,
                     "sweeptime": 1.3573}

        # temperature & time
        df['T_RT(H)']=T_over_H(tds_RT, time, H)
        df['T_sample(H)']=T_over_H(tds_sample, time, H)
        
    
    ########################################################################################################################
    #### VNA(T)
    ########################################################################################################################   
    elif ds=='VNA(T) with boxxed and tempered preamplifier':
        # comments?
        comment='tempered at 25°C'
        
        # Read Data from Files
        filenames = glob.glob(loc+'21 04 12 VNA(T) (boxxed v2)/fsweep_data'+"/*.csv")
        tds=[loc+'21 04 12 VNA(T) (boxxed v2)/thermo_data/GIR2002_logVNA(RT)_2021-04-13 15-56-13.csv',
             loc+'21 04 12 VNA(T) (boxxed v2)/thermo_data/GIR2002_logVNA(RT)_2021-04-15 10-04-28.csv']

        # Initialize and frequency
        f=np.genfromtxt(filenames[0],delimiter=',',dtype='float64')[1:,1]*1e-9 
        H_unsorted=np.zeros(len(filenames), dtype='float64')
        time_unsorted=np.zeros(len(filenames), dtype='datetime64[s]')
        sdata=np.zeros([len(f),len(H_unsorted),2],dtype='float64')

        # read Data, H, time
        for i, filename in enumerate(tqdm(filenames)):
            H_unsorted[i]=filename[-38:-31] #1e-4T
            time_unsorted[i]=datetime.strptime(filename[-23:-4], '%Y-%m-%d %H-%M-%S')
            sdata[:,i,:] = np.genfromtxt(filename,delimiter=',',dtype='float64')[1:,2:]
            
        # sort Data, time by H
        H_sort_ind=H_unsorted.argsort()
        H=H_unsorted[H_sort_ind]*1e-4
        time=time_unsorted[H_sort_ind]
        data=sdata[:,H_sort_ind,:]
        
        # Calculate S21
        S21=data[:,:,0]+1j*data[:,:,1]
        
        # vna config
        vna_config={"ZNB40": "frequency sweep",
                     "sample_name": "VNA(RT)",
                     "timestamp_setup": "2021-04-15 10:04:28.744223",
                     "s_param": "S21",
                     "start": 2000000000,
                     "stop": 27000000000,
                     "points": 1251,
                     "bandwidth": 1000,
                     "power": -5,
                     "average": 48,
                     "sweeptime": 1.3573}

        # temperature & time
        df['T_RT(H)']=T_over_H(tds, time, H)
        
    elif ds=='VNA(T) with boxxed preamplifier':
        # comments?
        comment='no comment'
        
        # Read Data from Files
        filenames = glob.glob(loc+'21 01 29 VNA(T) (boxxed)/fsweep_data'+"/*.csv")
        tds=[loc+'21 01 29 VNA(T) (boxxed)/thermo_data/GIR2002_logVNA(RT)_2021-01-29 16-46-59.csv']

        # Initialize and frequency
        f=np.genfromtxt(filenames[0],delimiter=',',dtype='float64')[1:,1]*1e-9 
        H_unsorted=np.zeros(len(filenames), dtype='float64')
        time_unsorted=np.zeros(len(filenames), dtype='datetime64[s]')
        sdata=np.zeros([len(f),len(H_unsorted),2],dtype='float64')

        # read Data, H, time
        for i, filename in enumerate(tqdm(filenames)):
            H_unsorted[i]=filename[-38:-31] #1e-4T
            time_unsorted[i]=datetime.strptime(filename[-23:-4], '%Y-%m-%d %H-%M-%S')
            sdata[:,i,:] = np.genfromtxt(filename,delimiter=',',dtype='float64')[1:,2:]
            
        # sort Data, time by H
        H_sort_ind=H_unsorted.argsort()
        H=H_unsorted[H_sort_ind]*1e-4
        time=time_unsorted[H_sort_ind]
        data=sdata[:,H_sort_ind,:]
        
        # Calculate S21
        S21=data[:,:,0]+1j*data[:,:,1]
        
        # vna config
        vna_config={"ZNB40": "frequency sweep",
                     "sample_name": "VNA(RT)",
                     "timestamp_setup": "2021-01-29 16:22:21.544290",
                     "s_param": "S21",
                     "start": 2000000000,
                     "stop": 27000000000,
                     "points": 1251,
                     "bandwidth": 1000,
                     "power": -5,
                     "average": 48,
                     "sweeptime": 1.3573}

        # temperature & time
        df['T_RT(H)']=T_over_H(tds, time, H)
        
    elif ds=='VNA(T) without preamplifier':
        # comments?
        comment='no comment'
        
        # Read Data from Files
        filenames = glob.glob(loc+'21 01 26 VNA(T) (without preamplifier)/fsweep_data'+"/*.csv")
        tds=[loc+'21 01 26 VNA(T) (without preamplifier)/thermo_data/GIR2002_logVNA(RT)_2021-01-26 11-24-52.csv']

        # Initialize and frequency
        f=np.genfromtxt(filenames[0],delimiter=',',dtype='float64')[1:,1]*1e-9 
        H_unsorted=np.zeros(len(filenames), dtype='float64')
        time_unsorted=np.zeros(len(filenames), dtype='datetime64[s]')
        sdata=np.zeros([len(f),len(H_unsorted),2],dtype='float64')

        # read Data, H, time
        for i, filename in enumerate(tqdm(filenames)):
            H_unsorted[i]=filename[-38:-31] #1e-4T
            time_unsorted[i]=datetime.strptime(filename[-23:-4], '%Y-%m-%d %H-%M-%S')
            sdata[:,i,:] = np.genfromtxt(filename,delimiter=',',dtype='float64')[1:,2:]
            
        # sort Data, time by H
        H_sort_ind=H_unsorted.argsort()
        H=H_unsorted[H_sort_ind]*1e-4
        time=time_unsorted[H_sort_ind]
        data=sdata[:,H_sort_ind,:]
        
        # Calculate S21
        S21=data[:,:,0]+1j*data[:,:,1]
        
        # vna config
        vna_config={"ZNB40": "frequency sweep",
                     "sample_name": "VNA(RT)",
                     "timestamp_setup": "2021-01-26 11:24:52.762019",
                     "s_param": "S21",
                     "start": 2000000000,
                     "stop": 27000000000,
                     "points": 1251,
                     "bandwidth": 1000,
                     "power": -5,
                     "average": 48,
                     "sweeptime": 1.3573}

        # temperature & time
        print('Wait at least up to 5 min.')
        df['T_RT(H)']=T_over_H(tds, time, H)
        
    elif ds=='VNA(T) with preamplifier':
        # comments?
        comment='no comment'
        
        # Read Data from Files
        filenames = glob.glob(loc+'21 01 12 VNA(T)/fsweep_data'+"/*.csv")
        tds=[loc+'21 01 12 VNA(T)/thermo_data/GIR2002_logVNA(RT)_2021-01-22 09-53-25.csv']

        # Initialize and frequency
        f=np.genfromtxt(filenames[0],delimiter=',',dtype='float64')[1:,1]*1e-9 
        H_unsorted=np.zeros(len(filenames), dtype='float64')
        time_unsorted=np.zeros(len(filenames), dtype='datetime64[s]')
        sdata=np.zeros([len(f),len(H_unsorted),2],dtype='float64')

        # read Data, H, time
        for i, filename in enumerate(tqdm(filenames)):
            H_unsorted[i]=filename[-38:-31] #1e-4T
            time_unsorted[i]=datetime.strptime(filename[-23:-4], '%Y-%m-%d %H-%M-%S')
            sdata[:,i,:] = np.genfromtxt(filename,delimiter=',',dtype='float64')[1:,2:]
            
        # sort Data, time by H
        H_sort_ind=H_unsorted.argsort()
        H=H_unsorted[H_sort_ind]*1e-4
        time=time_unsorted[H_sort_ind]
        data=sdata[:,H_sort_ind,:]
        
        # Calculate S21
        S21=data[:,:,0]+1j*data[:,:,1]
        
        # vna config
        vna_config={"ZNB40": "frequency sweep",
                     "sample_name": "VNA(RT)",
                     "timestamp_setup": "2021-01-22 09:53:25.666770",
                     "s_param": "S21",
                     "start": 2000000000,
                     "stop": 27000000000,
                     "points": 1251,
                     "bandwidth": 1000,
                     "power": -5,
                     "average": 48,
                     "sweeptime": 1.3573}

        # temperature & time
        print('Wait at least up to 5 min.')
        df['T_RT(H)']=T_over_H(tds, time, H)

   
    ########################################################################################################################
    #### BF CPWG - 4
    ########################################################################################################################
    elif ds=='BF CPWG4 50mK':
        # comments?
        comment=['sample Temperature not trustful. more like 50mK, stable.',
                 '2min break between each sweep',
                 'no idea of fieldcooling',
                 'ramping magnetic field']
        
        # Read Data from Files
        filenames = glob.glob(loc+'20 12 23 Blue Fors FMR CPWG-4/fsweep_data_50mK'+"/*.csv")
        tds=[loc+'20 12 23 Blue Fors FMR CPWG-4/thermo_data_50mK/20-12-30/CH7 T 20-12-30.log',
            loc+'20 12 23 Blue Fors FMR CPWG-4/thermo_data_50mK/20-12-31/CH7 T 20-12-31.log',
            loc+'20 12 23 Blue Fors FMR CPWG-4/thermo_data_50mK/21-01-01/CH7 T 21-01-01.log',
            loc+'20 12 23 Blue Fors FMR CPWG-4/thermo_data_50mK/21-01-02/CH7 T 21-01-02.log',
            loc+'20 12 23 Blue Fors FMR CPWG-4/thermo_data_50mK/21-01-03/CH7 T 21-01-03.log',
            loc+'20 12 23 Blue Fors FMR CPWG-4/thermo_data_50mK/21-01-04/CH7 T 21-01-04.log']

        # Initialize and frequency
        f=np.genfromtxt(filenames[0],delimiter=',',dtype='float64')[1:,1]*1e-9 
        H_unsorted=np.zeros(len(filenames), dtype='float64')
        time_unsorted=np.zeros(len(filenames), dtype='datetime64[s]')
        sdata=np.zeros([len(f),len(H_unsorted),2],dtype='float64')

        # read Data, H, time
        for i, filename in enumerate(tqdm(filenames)):
            H_unsorted[i]=filename[-38:-31] #1e-4T
            time_unsorted[i]=datetime.strptime(filename[-23:-4], '%Y-%m-%d %H-%M-%S')
            sdata[:,i,:] = np.genfromtxt(filename,delimiter=',',dtype='float64')[1:,2:]
            
        # sort Data, time by H
        H_sort_ind=H_unsorted.argsort()
        H=H_unsorted[H_sort_ind]*1e-4
        time=time_unsorted[H_sort_ind]
        data=sdata[:,H_sort_ind,:]
        
        # Calculate S21
        S21=data[:,:,0]+1j*data[:,:,1]
        
        # vna config
        vna_config={"ZNB40": "frequency sweep",
                     "sample_name": "CPWG-04_Hup_25-50mK_FAST_",
                     "timestamp_setup": "2020-12-30 09:57:47.543519",
                     "s_param": "S21",
                     "start": 2000000000,
                     "stop": 27000000000,
                     "points": 1251,
                     "bandwidth": 1000,
                     "power": -15,
                     "average": 48,
                     "sweeptime": 1.3573,
                     "allH":'(-.6,.6,2401)'}

        # temperature & time
        df['T_sample(H)']=T_over_H(tds, time, H)
        
    elif ds=='BF CPWG4 4K':
        # comments?
        comment='no comment'
        
        # Read Data from Files
        filenames = glob.glob(loc+'20 12 23 Blue Fors FMR CPWG-4/fsweep_data_4K'+"/*.csv")
        tds=[loc+'20 12 23 Blue Fors FMR CPWG-4/thermo_data_4K/20-12-27/CH7 T 20-12-27.log',
            loc+'20 12 23 Blue Fors FMR CPWG-4/thermo_data_4K/20-12-28/CH7 T 20-12-28.log']
        # Initialize and frequency
        f=np.genfromtxt(filenames[0],delimiter=',',dtype='float64')[1:,1]*1e-9 
        H_unsorted=np.zeros(len(filenames), dtype='float64')
        time_unsorted=np.zeros(len(filenames), dtype='datetime64[s]')
        sdata=np.zeros([len(f),len(H_unsorted),2],dtype='float64')

        # read Data, H, time
        for i, filename in enumerate(tqdm(filenames)):
            H_unsorted[i]=filename[-38:-31] #1e-4T
            time_unsorted[i]=datetime.strptime(filename[-23:-4], '%Y-%m-%d %H-%M-%S')
            sdata[:,i,:] = np.genfromtxt(filename,delimiter=',',dtype='float64')[1:,2:]
            
        # sort Data, time by H
        H_sort_ind=H_unsorted.argsort()
        H=H_unsorted[H_sort_ind]*1e-4
        time=time_unsorted[H_sort_ind]
        data=sdata[:,H_sort_ind,:]
        
        # Calculate S21
        S21=data[:,:,0]+1j*data[:,:,1]
        
        # vna config
        vna_config={"ZNB40": "frequency sweep",
                     "sample_name": "CPWG-04_Hup_FAST_",
                     "timestamp_setup": "2020-12-27 09:20:12.904852",
                     "s_param": "S21",
                     "start": 2000000000,
                     "stop": 27000000000,
                     "points": 1251,
                     "bandwidth": 1000,
                     "power": -5,
                     "average": 48,
                     "sweeptime": 1.3573,
                     "allH":'(-.6,.6,2401)'}
        
        # temperature & time
        df['T_sample(H)']=T_over_H(tds, time, H)
        
    elif ds=='BF CPWG4 50mK power test':
        # comments?
        comment='@base temp, power=-35'
        
        filenames = glob.glob(loc+'20 12 23 Blue Fors FMR CPWG-4/power_test'"/CPWG-4 30mK*.csv")
        vna_config={'sample_name':'CPWG-4 30mK P-15',
                                'start':2e9,
                                'stop':40e9,
                                'points':3801,
                                'bandwidth':1000,
                                'average':20}

        f=np.genfromtxt(filenames[0],delimiter=',',dtype='float64')[1:,1]*1e-9 
        P_unsorted=np.zeros(len(filenames), dtype='float64')
        time_unsorted=np.zeros(len(filenames), dtype='datetime64[s]')
        sdata=np.zeros([len(f),len(P_unsorted),2],dtype='float64')
        
        for i, filename in enumerate(tqdm(filenames)):
            P_unsorted[i]=filename[-43:-40] #1e-4T
            time_unsorted[i]=datetime.strptime(filename[-23:-4], '%Y-%m-%d %H-%M-%S')
            sdata[:,i,:] = np.genfromtxt(filename,delimiter=',',dtype='float64')[1:,2:]
            
        # sort Data, time by P
        H_sort_ind=P_unsorted.argsort()
        P=P_unsorted[H_sort_ind]
        time=time_unsorted[H_sort_ind]
        data=sdata[:,H_sort_ind,:]
        S21=data[:,:,0]+1j*data[:,:,1]

        df['P']=P
        df['deltaT']=np.array([0,1,2,17,27,43,80])
        df['t_relax']=np.array([0,90,90,150,150,180,np.nan])
        
    elif ds=='BF CPWG4 temp test':
        filenames = glob.glob(loc+'20 12 23 Blue Fors FMR CPWG-4/temp_test/'"*.csv")
        vna_config={'sample_name':'CPWG-4 4K Frequenzgang (zusammengebaut)',
                                'start':2e9,
                                'stop':40e9,
                                'points':3801,
                                'bandwidth':1000,
                                'power':-5,
                                'average':50}
        f=np.genfromtxt(filenames[0],delimiter=',',dtype='float64')[1:,1]*1e-9 
        time=np.zeros(len(filenames), dtype='datetime64[s]')
        data=np.zeros([len(f),len(time),2],dtype='float64')

        df['labels']=np.array(['4K','60K','Base','open cup','RT'])
        for i, filename in enumerate(tqdm(filenames)):
            time[i]=datetime.strptime(filename[-23:-4], '%Y-%m-%d %H-%M-%S')
            data[:,i,:] = np.genfromtxt(filename,delimiter=',',dtype='float64')[1:,2:]
        S21=data[:,:,0]+1j*data[:,:,1]
    
        
    ########################################################################################################################
    #### BF CoBulk32nm-1
    ########################################################################################################################
    
    #### Sergej
    
    elif ds=='BF Cobulky32nm HSWEEP down':
        # comments?
        comment='geometric averaging already happend'
        
        file = h5py.File(loc+'20 11 26 Blue Fors FMR CoBulky32nm HSWEEP/20201126_CoBulky32nm_001.h5', 'r')
        downsweepset=file['Sample_CoBulky32nm_001']['FMR']['BF20201126_Hsweep']['data_measured']['data_downsweep']
        downsweeplist=list(downsweepset.keys())
        H=np.linspace(-1.300,1.300,1301)
        f=np.zeros(np.shape(downsweeplist)[0])
        T21=np.zeros((np.shape(f)[0],np.shape(H)[0]))
        phi21=np.zeros((np.shape(f)[0],np.shape(H)[0]))
        C=np.zeros(np.shape(T21))
        #print(H)
        for i,l in enumerate(tqdm(downsweeplist)):
            trans=np.array(np.array(downsweepset[l])[:,5])
            phase=np.array(np.array(downsweepset[l])[:,6])
            f[i]=(np.mean(np.array(np.array(downsweepset[l])[:,4]))*1e-3)
            h_field=np.array(np.array(downsweepset[l])[:,3])*1e-3
            for k in range(np.shape(h_field)[0]):
                pos=np.argmin(np.abs(H-h_field[k]))
                C[i][pos]+=1
                T21[i][pos]+=trans[k]
                phi21[i][pos]+=phase[k]
        C[C==0]=np.nan
        T21=T21/C
        phi21=phi21/C

        for i in range(np.shape(T21)[0]):
            for j in range(np.shape(T21)[1]):
                if T21[i][j] is np.nan:
                    print('du bist scheiße',i,j)
        for i in range(np.shape(phi21)[0]):
            for j in range(np.shape(phi21)[1]):
                if phi21[i][j] is np.nan:
                    print('du bist scheiße',i,j)
        f[-1]=40
        df['T21']=T21
        df['phi21']=phi21
        
    elif ds=='BF Cobulky32nm HSWEEP up':
        # comments?
        comment='geometric averaging already happend'
        
        f = h5py.File(loc+'20 11 26 Blue Fors FMR CoBulky32nm HSWEEP/20201126_CoBulky32nm_001.h5', 'r')
        upsweepset=f['Sample_CoBulky32nm_001']['FMR']['BF20201126_Hsweep']['data_measured']['data_upsweep']
        upsweeplist=list(upsweepset.keys())
        H=np.linspace(-1.300,1.300,1301)
        f=np.zeros(np.shape(upsweeplist)[0])
        T21=np.zeros((np.shape(f)[0],np.shape(H)[0]))
        phi21=np.zeros((np.shape(f)[0],np.shape(H)[0]))
        C=np.zeros(np.shape(T21))
        #print(H)
        for i,l in enumerate(tqdm(upsweeplist)):
            trans=np.array(np.array(upsweepset[l])[:,5])
            phase=np.array(np.array(upsweepset[l])[:,6])
            f[i]=(np.mean(np.array(np.array(upsweepset[l])[:,4]))*1e-3)
            h_field=np.array(np.array(upsweepset[l])[:,3])*1e-3
            for k in range(np.shape(h_field)[0]):
                pos=np.argmin(np.abs(H-h_field[k]))
                C[i][pos]+=1
                T21[i][pos]+=trans[k]
                phi21[i][pos]+=phase[k]
        C[C==0]=np.nan
        T21=T21/C
        phi21=phi21/C

        for i in range(np.shape(T21)[0]):
            for j in range(np.shape(T21)[1]):
                if T21[i][j] is np.nan:
                    print('du bist scheiße',i,j)
        for i in range(np.shape(phi21)[0]):
            for j in range(np.shape(phi21)[1]):
                if phi21[i][j] is np.nan:
                    print('du bist scheiße',i,j)
        f[-1]=40
        df['T21']=T21
        df['phi21']=phi21
        
    elif ds=='BF Cobulky32nm RFSWEEP down':
        f = h5py.File(loc+'20 11 26 Blue Fors FMR CoBulky32nm HSWEEP/20201205_CoBulky32nm_RFsweep.h5', 'r')
        sweepset=f['Sample_CoBulky32nm']['FMR']['BF20201205_RFsweep']['data_measured']['data_downsweep']
        sweeplist=list(sweepset.keys())
        f=np.array(sweepset[sweeplist[0]])[:,3]*1e-3 #GHz
        
        H_unsorted=np.zeros(np.shape(sweeplist)[0])
        time=np.zeros(np.shape(sweeplist)[0])
        T21=np.zeros((np.shape(H_unsorted)[0],np.shape(f)[0]))
        phi21=np.zeros((np.shape(H_unsorted)[0],np.shape(f)[0]))
        for i,l in enumerate(tqdm(sweeplist)):
            H_unsorted[i]=np.array(sweepset[l])[0,1]*1e-3 #T
            T21[i]=np.array(np.array(sweepset[l])[:,4])
            phi21[i]=np.array(np.array(sweepset[l])[:,5])
        T21=T21.transpose()
        phi21=phi21.transpose()
        
        # sort Data, time by H
        H_sort_ind=H_unsorted.argsort()
        H=H_unsorted[H_sort_ind]
        T21=T21[:,H_sort_ind]
        phi21=phi21[:,H_sort_ind]
        df['T21']=T21
        df['phi21']=phi21
        
    elif ds=='BF Cobulky32nm RFSWEEP up':
        f = h5py.File(loc+'20 11 26 Blue Fors FMR CoBulky32nm HSWEEP/20201205_CoBulky32nm_RFsweep.h5', 'r')
        sweepset=f['Sample_CoBulky32nm']['FMR']['BF20201205_RFsweep']['data_measured']['data_upsweep']
        sweeplist=list(sweepset.keys())
        f=np.array(sweepset[sweeplist[0]])[:,3]*1e-3 #GHz
        H_unsorted=np.zeros(np.shape(sweeplist)[0])
        time=np.zeros(np.shape(sweeplist)[0])
        T21=np.zeros((np.shape(H_unsorted)[0],np.shape(f)[0]))
        phi21=np.zeros((np.shape(H_unsorted)[0],np.shape(f)[0]))
        for i,l in enumerate(tqdm(sweeplist)):
            H_unsorted[i]=np.array(sweepset[l])[0,1]*1e-3 #T
            T21[i]=np.array(np.array(sweepset[l])[:,4])
            phi21[i]=np.array(np.array(sweepset[l])[:,5])
        T21=T21.transpose()
        phi21=phi21.transpose()
        
        # sort Data, time by H
        H_sort_ind=H_unsorted.argsort()
        H=H_unsorted[H_sort_ind]
        T21=T21[:,H_sort_ind]
        phi21=phi21[:,H_sort_ind]
        df['T21']=T21
        df['phi21']=phi21
        
        # ch_00 relative time at log data, sec
        # ch_01 setpoint field, mT
        # ch_02 field, mT
        # ch_03 freq, MHz
        # ch_04 amplitude S21, dB
        # ch_05 phase S21, degree
        # ch_06 RF level, dBm
        # ch_07 4K
        
        
    #### Olli
    
    elif ds=='BF Cobulky32nm LONG':

        # comments?
        comment='no comment'
        
        # Read Data from Files
        filenames = glob.glob(loc+'20 12 11 Blue Fors FMR CoBulk32nm LONG/fsweep_data'+"/*.csv")
        tds=[loc+'20 12 11 Blue Fors FMR CoBulk32nm LONG/thermo_data/20-12-14/CH7 T 20-12-14.log',
             loc+'20 12 11 Blue Fors FMR CoBulk32nm LONG/thermo_data/20-12-15/CH7 T 20-12-15.log',
             loc+'20 12 11 Blue Fors FMR CoBulk32nm LONG/thermo_data/20-12-16/CH7 T 20-12-16.log',
             loc+'20 12 11 Blue Fors FMR CoBulk32nm LONG/thermo_data/20-12-17/CH7 T 20-12-17.log']
        
        # Initialize and frequency
        f=np.genfromtxt(filenames[0],delimiter=',',dtype='float64')[1:,1]*1e-9 
        H_unsorted=np.zeros(len(filenames), dtype='float64')
        time_unsorted=np.zeros(len(filenames), dtype='datetime64[s]')
        sdata=np.zeros([len(f),len(H_unsorted),2],dtype='float64')

        # read Data, H, time
        for i, filename in enumerate(tqdm(filenames)):
            H_unsorted[i]=filename[-38:-31] #1e-4T
            time_unsorted[i]=datetime.strptime(filename[-23:-4], '%Y-%m-%d %H-%M-%S')
            sdata[:,i,:] = np.genfromtxt(filename,delimiter=',',dtype='float64')[1:,2:]
            
        # sort Data, time by H
        H_sort_ind=H_unsorted.argsort()
        H=H_unsorted[H_sort_ind]*1e-4
        time=time_unsorted[H_sort_ind]
        data=sdata[:,H_sort_ind,:]
        
        # Calculate S21
        S21=data[:,:,0]+1j*data[:,:,1]
        
        # vna config
        vna_config={"ZNB40": "frequency sweep",
                     "sample_name": "CoBulky32nm-1_Fsweep_Hdown_LONG_",
                     "timestamp_setup": "2020-12-14 09:51:58.841773",
                     "s_param": "S21",
                     "start": 2000000000,
                     "stop": 40000000000,
                     "points": 153,
                     "bandwidth": 500,
                     "power": -5,
                     "average": 160,
                     "sweeptime": 0.332,
                     "allH":'(1.3,-1.3,5201)'}
        
        # temperature & time
        df['T_sample(H)']=T_over_H(tds, time, H)
        
        
    elif ds=='BF Cobulky32nm FAST':
        # comments?
        comment='no comment'
        # Read Data from Files
        filenames = glob.glob(loc+'20 12 11 Blue Fors FMR CoBulk32nm FAST/fsweep_data'+"/*.csv")
        tds=[loc+'20 12 11 Blue Fors FMR CoBulk32nm FAST/thermo_data/20-12-14/CH7 T 20-12-14.log',
             loc+'20 12 11 Blue Fors FMR CoBulk32nm FAST/thermo_data/20-12-12/CH7 T 20-12-12.log',
             loc+'20 12 11 Blue Fors FMR CoBulk32nm FAST/thermo_data/20-12-13/CH7 T 20-12-13.log']
        
        # Initialize and frequency
        f=np.genfromtxt(filenames[0],delimiter=',',dtype='float64')[1:,1]*1e-9 
        H_unsorted=np.zeros(len(filenames), dtype='float64')
        time_unsorted=np.zeros(len(filenames), dtype='datetime64[s]')
        sdata=np.zeros([len(f),len(H_unsorted),2],dtype='float64')

        # read Data, H, time
        for i, filename in enumerate(tqdm(filenames)):
            H_unsorted[i]=filename[-38:-31] #1e-4T
            time_unsorted[i]=datetime.strptime(filename[-23:-4], '%Y-%m-%d %H-%M-%S')
            sdata[:,i,:] = np.genfromtxt(filename,delimiter=',',dtype='float64')[1:,2:]
            
        # sort Data, time by H
        H_sort_ind=H_unsorted.argsort()
        H=H_unsorted[H_sort_ind]*1e-4
        time=time_unsorted[H_sort_ind]
        data=sdata[:,H_sort_ind,:]
        
        # Calculate S21
        S21=data[:,:,0]+1j*data[:,:,1]
        
        # vna config
        vna_config={"ZNB40": "frequency sweep",
                     "sample_name": "CoBulky32nm-1_Fsweep_Hup_FAST_",
                     "timestamp_setup": "2020-12-12 11:30:12.240404",
                     "s_param": "S21",
                     "start": 2000000000,
                     "stop": 27000000000,
                     "points": 1251,
                     "bandwidth": 1000,
                     "power": -5,
                     "average": 48,
                     "sweeptime": 1.3573,
                     "allH":(-.6,.6,2401)}
        
        # temperature & time
        df['T_sample(H)']=T_over_H(tds, time, H)
    
    elif ds=='BF Cobulky32nm TEST':
        # comments?
        comment='restarted at: -1.1905, -0.0975, 0, 0,1025, aborted at 0.1555T'
        
        # Read Data from Files
        filenames = glob.glob(loc+'20 11 20 Blue Fors FMR CoBulk32nm TEST/fsweep_data'+"/*.csv")
        tds=[loc+'20 11 20 Blue Fors FMR CoBulk32nm TEST/thermo_data/20-12-09/CH7 T 20-12-09.log',
             loc+'20 11 20 Blue Fors FMR CoBulk32nm TEST/thermo_data/20-12-10/CH7 T 20-12-10.log',
             loc+'20 11 20 Blue Fors FMR CoBulk32nm TEST/thermo_data/20-12-11/CH7 T 20-12-11.log']
        
        # Initialize and frequency
        f=np.genfromtxt(filenames[0],delimiter=',',dtype='float64')[1:,1]*1e-9 
        H_unsorted=np.zeros(len(filenames), dtype='float64')
        time_unsorted=np.zeros(len(filenames), dtype='datetime64[s]')
        sdata=np.zeros([len(f),len(H_unsorted),2],dtype='float64')

        # read Data, H, time
        for i, filename in enumerate(tqdm(filenames)):
            H_unsorted[i]=filename[-38:-31].replace('m','-').replace('p','0') #1e-4T
            time_unsorted[i]=datetime.strptime(filename[-23:-4], '%Y-%m-%d %H-%M-%S')
            sdata[:,i,:] = np.genfromtxt(filename,delimiter=',',dtype='float64')[1:,2:]
            
        # sort Data, time by H
        H_sort_ind=H_unsorted.argsort()
        H=H_unsorted[H_sort_ind]*1e-4
        time=time_unsorted[H_sort_ind]
        data=sdata[:,H_sort_ind,:]
        
        # Calculate S21
        S21=data[:,:,0]+1j*data[:,:,1]
        
        # vna config
        vna_config={"ZNB40": "frequency sweep",
                     "sample_name": "CoBulky32nm-1_Fsweep_Hup",
                     "timestamp_setup": "2020-12-11 17:48:19.046673",
                     "s_param": "S21",
                     "start": 2000000000,
                     "stop": 40000000000,
                     "points": 3801,
                     "bandwidth": 1000,
                     "power": -5,
                     "average": 5,
                     "sweeptime": 4.1241,
                     "allH":(-1.3,1.3,5201)}
        
        # temperature & time
        df['T_sample(H)']=T_over_H(tds, time, H)
    
    ########################################################################################################################
    #### BF Cobulky3nm
    ########################################################################################################################
    elif ds=='BF Cobulky3nm HSWEEP up':
        # comments?
        comment='interrupted measurement at 32 GHz'
        file = h5py.File(loc+'20 10 16 BlueFors FMR CoBulky3nm/20201016_CoBulk3nm.h5', 'r')
        upsweepset=file['Sample_CoBulk3nm']['FMR']['BF20201016_Hsweep']['data_measured']['data_upsweep']
        upsweeplist=list(upsweepset.keys())
        H=np.linspace(-1.300,1.300,1301)
        f=np.zeros(np.shape(upsweeplist)[0])
        T21=np.zeros((np.shape(f)[0],np.shape(H)[0]))
        C=np.zeros(np.shape(T21))
        for i,l in enumerate(tqdm(upsweeplist)):
            trans=np.array(np.array(upsweepset[l])[:,5])
            f[i]=(np.mean(np.array(np.array(upsweepset[l])[:,4]))*1e-3)
            h_field=np.array(np.array(upsweepset[l])[:,3])*1e-3
            for k in range(np.shape(h_field)[0]):
                pos=np.argmin(np.abs(H-h_field[k]))
                C[i][pos]+=1
                T21[i][pos]+=trans[k]
        C[C==0]=np.nan
        df['T21']=T21/C

        for i in range(np.shape(T21)[0]):
            for j in range(np.shape(T21)[1]):
                if T21[i][j] is np.nan:
                    print('du bist scheiße',i,j)
        
    elif ds=='BF Cobulky3nm HSWEEP down':
        # comments?
        comment='interrupted measurement at 32 GHz'
        file = h5py.File(loc+'20 10 16 BlueFors FMR CoBulky3nm/20201016_CoBulk3nm.h5', 'r')
        downsweepset=file['Sample_CoBulk3nm']['FMR']['BF20201016_Hsweep']['data_measured']['data_downsweep']
        downsweeplist=list(downsweepset.keys())
        H=np.linspace(-1.300,1.300,1301)
        f=np.zeros(np.shape(downsweeplist)[0])
        T21=np.zeros((np.shape(f)[0],np.shape(H)[0]))
        C=np.zeros(np.shape(T21))
        for i,l in enumerate(tqdm(downsweeplist)):
            trans=np.array(np.array(downsweepset[l])[:,5])
            f[i]=(np.mean(np.array(np.array(downsweepset[l])[:,4]))*1e-3)
            h_field=np.array(np.array(downsweepset[l])[:,3])*1e-3
            for k in range(np.shape(h_field)[0]):
                pos=np.argmin(np.abs(H-h_field[k]))
                C[i][pos]+=1
                T21[i][pos]+=trans[k]
        C[C==0]=np.nan
        df['T21']=T21/C

        for i in range(np.shape(T21)[0]):
            for j in range(np.shape(T21)[1]):
                if T21[i][j] is np.nan:
                    print('du bist scheiße',i,j)
    
    ########################################################################################################################
    #### BF Cobulk30nm
    ########################################################################################################################
    elif ds=='BF Cobulk30nm HSWEEP down':
        # comments?
        comment='no comment'
        f = h5py.File(loc+'20 09 15 BlueFors FMR Cobulk30nm/20200921_CoBulk.h5', 'r')
        downsweepset=f['Sample_CoBulk']['FMR']['BF20200921_Hsweep']['data_measured']['data_downsweep']
        downsweeplist=list(downsweepset.keys())
        H=np.linspace(-1.300,1.300,1301)
        f=np.zeros(np.shape(downsweeplist)[0])
        T21=np.zeros((np.shape(f)[0],np.shape(H)[0]))
        C=np.zeros(np.shape(T21))
        #print(H)
        for i,l in enumerate(tqdm(downsweeplist)):
            trans=np.array(np.array(downsweepset[l])[:,5])
            f[i]=(np.mean(np.array(np.array(downsweepset[l])[:,4]))*1e-3)
            h_field=np.array(np.array(downsweepset[l])[:,3])*1e-3
            for k in range(np.shape(h_field)[0]):
                pos=np.argmin(np.abs(H-h_field[k]))
                C[i][pos]+=1
                T21[i][pos]+=trans[k]
        C[C==0]=np.nan
        df['T21']=T21/C
        f[-1]=40

    elif ds=='BF Cobulk30nm HSWEEP up':
        # comments?
        comment='no comment'
        f = h5py.File(loc+'20 09 15 BlueFors FMR Cobulk30nm/20200921_CoBulk.h5', 'r')
        upsweepset=f['Sample_CoBulk']['FMR']['BF20200921_Hsweep']['data_measured']['data_upsweep']
        upsweeplist=list(upsweepset.keys())
        H=np.linspace(-1.300,1.300,1301)
        f=np.zeros(np.shape(upsweeplist)[0])
        T21=np.zeros((np.shape(f)[0],np.shape(H)[0]))
        C=np.zeros(np.shape(T21))
        #print(H)
        for i,l in enumerate(tqdm(upsweeplist)):
            trans=np.array(np.array(upsweepset[l])[:,5])
            f[i]=(np.mean(np.array(np.array(upsweepset[l])[:,4]))*1e-3)
            h_field=np.array(np.array(upsweepset[l])[:,3])*1e-3
            for k in range(np.shape(h_field)[0]):
                pos=np.argmin(np.abs(H-h_field[k]))
                C[i][pos]+=1
                T21[i][pos]+=trans[k]
        C[C==0]=np.nan
        df['T21']=T21/C
        f[-1]=40
        
    ########################################################################################################################
    #### FH Cobulk30nm
    ########################################################################################################################
    elif ds=='FH Cobulk30nm down':
        # comments?
        comment='Initialized with +3T'
        
        # Read Data from Files
        filenames = glob.glob(loc+'20 08 06 FoninHeliox FMR Cobulk30nm closer up downsweep/data'+"/*.csv")
                
        # Initialize and frequency
        f=np.genfromtxt(filenames[0],delimiter=',',dtype='float64')[1:,1]*1e-9 
        H_unsorted=np.zeros(len(filenames), dtype='float64')
        time_unsorted=np.zeros(len(filenames), dtype='datetime64[s]')
        sdata=np.zeros([len(f),len(H_unsorted),2],dtype='complex128')

        # read Data, H, time
        for i, filename in enumerate(tqdm(filenames)):
            H_unsorted[i]=filename[-30:-24] #1e-4T
            time_unsorted[i]=datetime.strptime(filename[-23:-4], '%Y-%m-%d %H-%M-%S')
            sdata[:,i,:] = np.genfromtxt(filename,delimiter=',',dtype='complex128')[1:,2:]
            
        # sort Data, time by H
        H_sort_ind=H_unsorted.argsort()
        H=H_unsorted[H_sort_ind]*1e-4
        time=time_unsorted[H_sort_ind]
        data=sdata[:,H_sort_ind,:]
        
        # Calculate S21
        S21=data[:,:,0]+1j*data[:,:,1]
        
        vna_config={"timestamp": "2020-08-06 10:38:28.902323",
                     "s_param": "['S21']",
                     "start": 40000000.0,
                     "stop": 18000000000.0,
                     "points": 1797,
                     "bandwidth": 250,
                     "power": "-10dbm",
                     "sweeptype": "linear",
                     "average": 5,
                     "sweeptime": 6.4987,
                     "bfield": 0.32,
                     "temperature": 6,
                     "sample": "Cobulk WG",
                     "comment": "downsweep, preamplifier, magnetized 3T"}
        
    elif ds=='FH Cobulk30nm up':
        # comments?
        comment='Initialized with +3T'
        
        # Read Data from Files
        filenames = glob.glob(loc+'20 08 06 FoninHeliox FMR Cobulk30nm closer up upsweep/data'+"/*.csv")
                
        # Initialize and frequency
        f=np.genfromtxt(filenames[0],delimiter=',',dtype='float64')[1:,1]*1e-9 
        H_unsorted=np.zeros(len(filenames), dtype='float64')
        time_unsorted=np.zeros(len(filenames), dtype='datetime64[s]')
        sdata=np.zeros([len(f),len(H_unsorted),2],dtype='complex128')

        # read Data, H, time
        for i, filename in enumerate(tqdm(filenames)):
            H_unsorted[i]=filename[-30:-24] #1e-4T
            time_unsorted[i]=datetime.strptime(filename[-23:-4], '%Y-%m-%d %H-%M-%S')
            sdata[:,i,:] = np.genfromtxt(filename,delimiter=',',dtype='complex128')[1:,2:]
                              
        # sort Data, time by H
        H_sort_ind=H_unsorted.argsort()
        H=H_unsorted[H_sort_ind]*1e-4
        time=time_unsorted[H_sort_ind]
        data=sdata[:,H_sort_ind,:]
        
        # Calculate S21
        S21=data[:,:,0]+1j*data[:,:,1]
        
        vna_config={"timestamp": "2020-08-06 14:46:01.022690",
                     "s_param": "['S21']",
                     "start": 20000000.0,
                     "stop": 18000000000.0,
                     "points": 900,
                     "bandwidth": 250,
                     "power": "-10dbm",
                     "sweeptype": "linear",
                     "average": 5,
                     "sweeptime": 3.2548,
                     "bfield": -0.32,
                     "temperature": 6,
                     "sample": "Cobulk WG",
                     "comment": "downsweep, preamplifier, magnetized 3T"}
        
    elif ds=='FH Cobulk30nm all':
        # comments?
        comment='upsweep, transfer of helium between -80 to -90 mT, wpa, nonlinear Haxis'
        
        vna_config={"timestamp": "2020-08-06 17:27:31.168071",
                     "s_param": "['S21']",
                     "start": 10000000.0,
                     "stop": 18000000000.0,
                     "points": 1800,
                     "bandwidth": 250,
                     "power": "-10dbm",
                     "sweeptype": "linear",
                     "average": 5,
                     "sweeptime": 6.5096,
                     "bfield": -10.0,
                     "temperature": 6,
                     "sample": "test",
                     "comment": "upsweep"}
        
        # Read Data from Files
        filenames = glob.glob(loc+'20 08 07 FoninHeliox FMR Cobulk30nm closest up/data'+"/*.csv")
        
        # Initialize and frequency
        f=np.genfromtxt(filenames[0],delimiter=',',dtype='float64')[1:,1]*1e-9 
        H_unsorted=np.zeros(len(filenames), dtype='float64')
        time_unsorted=np.zeros(len(filenames), dtype='datetime64[s]')
        sdata=np.zeros([len(f),len(H_unsorted),2],dtype='complex128')

        # read Data, H, time
        for i, filename in enumerate(tqdm(filenames)):
            H_unsorted[i]=filename[-30:-24] #1e-4T
            time_unsorted[i]=datetime.strptime(filename[-23:-4], '%Y-%m-%d %H-%M-%S')
            sdata[:,i,:] = np.genfromtxt(filename,delimiter=',',dtype='complex128')[1:,2:]
                              
        # fehlerhaftes abspeichern mit falschem magnetfeld
        H_corr=H_unsorted
        H_corr=np.round(H_corr,decimals=4)
        for h in range(len(H_corr)):
            if H_corr[h-1]==H_corr[h]:
                if H_corr[h]>0:
                    H_corr[h]=H_corr[h]+1e-4
                if H_corr[h]<0:
                    H_corr[h]=H_corr[h]-1e-4        
        
        # sort Data, time by H
        H_sort_ind=H_corr.argsort()
        H=H_corr[H_sort_ind]*1e-4
        time=time_unsorted[H_sort_ind]
        data=sdata[:,H_sort_ind,:]
        
        # fehlerhafter nullwert
        data[:,list(H).index(0)]=(data[:,list(H).index(0.0001)]+data[:,list(H).index(-0.0001)])/2
        S21=data[:,:,0]
        
    elif ds=='FH Ref WG':
        # comments?
        comment=['upsweep',
                 'non linear Haxis',
                 'Magnet shutdown, empty helium, transfer, restart, @ - 0.1371T',
                 'Restarted (Windwos update) @ -0.1014T',
                 'then helium transfer while measurement',
                 'explanation: for higher temperatur Transmission get worse.',
                 'try to achieve const. temperature, with less H resolution',
                 'less than 80h of measuring']                 
        
        vna_config={ "timestamp": "2020-08-11 10:06:27.037019",
                     "s_param": "['S21']",
                     "start": 10000000.0,
                     "stop": 18000000000.0,
                     "points": 1800,
                     "bandwidth": 250,
                     "power": "-10dbm",
                     "sweeptype": "linear",
                     "average": 5,
                     "sweeptime": 6.5096,
                     "bfield": -10.0,
                     "temperature": 6,
                     "sample": "ref WG",
                     "comment": "upsweep"}
        
        # Read Data from Files
        filenames = glob.glob(loc+'20 08 10 FoninHeliox FMR RefWG/data'+"/*.csv")
        
        # Initialize and frequency
        f=np.genfromtxt(filenames[0],delimiter=',',dtype='float64')[1:,1]*1e-9 
        H_unsorted=np.zeros(len(filenames), dtype='float64')
        time_unsorted=np.zeros(len(filenames), dtype='datetime64[s]')
        sdata=np.zeros([len(f),len(H_unsorted),2],dtype='complex128')

        # read Data, H, time
        for i, filename in enumerate(tqdm(filenames)):
            H_unsorted[i]=filename[-30:-24] #1e-4T
            time_unsorted[i]=datetime.strptime(filename[-23:-4], '%Y-%m-%d %H-%M-%S')
            sdata[:,i,:] = np.genfromtxt(filename,delimiter=',',dtype='complex128')[1:,2:]
            
        # fehlerhaftes abspeichern mit falschem magnetfeld
        H_corr=H_unsorted
        H_corr=np.round(H_corr,decimals=4)
        for h in range(len(H_corr)):
            if H_corr[h-1]==H_corr[h]:
                if H_corr[h]>0:
                    H_corr[h]=H_corr[h]+1e-4
                if H_corr[h]<0:
                    H_corr[h]=H_corr[h]-1e-4        
        
        # sort Data, time by H
        H_sort_ind=H_corr.argsort()
        H=H_corr[H_sort_ind]*1e-4
        time=time_unsorted[H_sort_ind]
        data=sdata[:,H_sort_ind,:]
        
        # fehlerhafter nullwert
        data[:,list(H).index(0)]=(data[:,list(H).index(0.0001)]+data[:,list(H).index(-0.0001)])/2
        S21=data[:,:,0]
        
    ########################################################################################################################
    #### Return Block
    ########################################################################################################################
    else:
        print('ERROR: no such dataset!')
    
    
    if comment != 'no comment':
        print(comment)
        df['comment']=comment
    
    df['f']=f
    df['H']=H
    df['S21']=S21
    df['t']=time
    df['vna_config']=vna_config
    return df
    
        



