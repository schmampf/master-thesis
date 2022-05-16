'''version from 31.03.2021

author: Oliver I.
'''

import numpy as np

def complex_binning(d, 
           fmin=False,
           fmax=False,
           Hmin=False,
           Hmax=False,
           Nf=False,
           NH=False):
    
    # Get Binning extent
    if Hmin is False:
        Hmin=np.nanmin(d['H'])
    if Hmax is False:
        Hmax=np.nanmax(d['H'])
    if fmin is False:
        fmin=np.nanmin(d['f'])
    if fmax is False:
        fmax=np.nanmax(d['f'])
    ext=[[Hmin,Hmax], [fmin,fmax]]
        
    # Get Binning resolution
    checkH=np.argmin(np.abs(d['H']-Hmax))-np.argmin(np.abs(d['H']-Hmin))+1
    if NH is False:NH=checkH
    elif NH>checkH:print('Error: Oversampling in H-direction!')
        
    checkf=np.argmin(np.abs(d['f']-fmax))-np.argmin(np.abs(d['f']-fmin))+1
    if Nf is False:Nf=checkf
    elif Nf>checkf:print('Error: Oversampling in f-direction!')
    res=[NH,Nf]
    
    # Get 2D grids
    real=d['S21'].real
    imag=d['S21'].imag
    HH, ff =np.meshgrid(d['H'],d['f'])
    
    # from 2D grids, to 1D rows
    X, Y = np.ravel(HH), np.ravel(ff)
    Zreal, Zimag = np.ravel(real), np.ravel(imag)
    
    # Bin that stuff
    real_SUM, x,y = np.histogram2d(X,Y,
                                   bins=res, 
                                   range=ext, 
                                   normed=False, 
                                   weights=Zreal)
    imag_SUM, x,y = np.histogram2d(X,Y,
                                   bins=res, 
                                   range=ext, 
                                   normed=False, 
                                   weights=Zimag)
    counter, x,y = np.histogram2d(X,Y,
                                  bins=res, 
                                  range=ext, 
                                  normed=False, 
                                  weights=None)
    
    # get that binned stuff back together.
    db={'ext(H,f)':[Hmin,Hmax,fmin,fmax],
        'res(H,f)':[NH,Nf]}
    db['S21']=(real_SUM.T+1j*imag_SUM.T)/counter.T
    db['f']=np.linspace(fmin,fmax,Nf)
    db['H']=np.linspace(Hmin,Hmax,NH)
    return db
        
def normS21(db,Hnorm='max'):
    '''
    db: H,f,S21
    Hnorm: 'max', 'min', 'ext', [-1,1]
    
    return
    dn: H, Hnorm, S21, S21norm, f
    '''
    
    H=db['H']
    real=db['S21'].real
    imag=db['S21'].imag
    
    # get Positions
    if Hnorm=='max':
        pos=[np.argmin(np.abs(H-np.nanmax(H)))]
    elif Hnorm=='min':
        pos=[np.argmin(np.abs(H-np.nanmin(H)))]
    elif Hnorm=='ext':
        pos=[np.argmin(np.abs(H-np.nanmax(H))),
             np.argmin(np.abs(H-np.nanmin(H)))]
    else:
        pos= [0 for x in range(len(Hnorm))]
        for i,h in enumerate(Hnorm):
            pos[i]=np.argmin(np.abs(H-h))
    
    
    
    # get Normalization
    lenpos=len(pos)
    Hreal, Himag=0,0
    Hnorm=[]
    for p in pos:
        Hreal=Hreal+real[:,p]/lenpos
        Himag=Himag+imag[:,p]/lenpos
        Hnorm.append(H[pos])
        
    # gridden
    X = np.ones((len(H)))
    ones, HHreal   = np.meshgrid(X,Hreal)
    ones, HHimag   = np.meshgrid(X,Himag)
    
    # Normen
    HHS21=HHreal+1j*HHimag
    norm=np.exp(-1j*np.angle(HHS21))/np.abs(HHS21)
    real=real*norm
    imag=imag*norm
    
    # Build normated Dataset
    dn={}
    dn['H']=H
    dn['Hnorm']=np.array(Hnorm)
    dn['S21']=real+1j*imag
    dn['S21norm']=Hreal+1j*Himag
    dn['f']=db['f']
    
    return dn

# for H sweeps
def binning(d, 
           fmin=False,
           fmax=False,
           Hmin=False,
           Hmax=False,
           Nf=False,
           NH=False):
    
    # Get Binning extent
    if Hmin is False:
        Hmin=np.nanmin(d['H'])
    if Hmax is False:
        Hmax=np.nanmax(d['H'])
    if fmin is False:
        fmin=np.nanmin(d['f'])
    if fmax is False:
        fmax=np.nanmax(d['f'])
    ext=[[Hmin,Hmax], [fmin,fmax]]
        
    # Get Binning resolution
    checkH=np.argmin(np.abs(d['H']-Hmax))-np.argmin(np.abs(d['H']-Hmin))+1
    if NH is False:NH=checkH
    elif NH>checkH:print('Error: Oversampling in H-direction!')
        
    checkf=np.argmin(np.abs(d['f']-fmax))-np.argmin(np.abs(d['f']-fmin))+1
    if Nf is False:Nf=checkf
    elif Nf>checkf:print('Error: Oversampling in f-direction!')
    res=[NH,Nf]
    
    # Get 2D grids
    abso=d['T21']
    HH, ff =np.meshgrid(d['H'],d['f'])
    
    # from 2D grids, to 1D rows
    X, Y = np.ravel(HH), np.ravel(ff)
    Zabso = np.ravel(abso)
    
    # Bin that stuff
    abso_SUM, x,y = np.histogram2d(X,Y,
                                   bins=res, 
                                   range=ext, 
                                   normed=False, 
                                   weights=Zabso)
    counter, x,y = np.histogram2d(X,Y,
                                  bins=res, 
                                  range=ext, 
                                  normed=False, 
                                  weights=None)
    
    # get that binned stuff back together.
    db={'ext(H,f)':[Hmin,Hmax,fmin,fmax],
        'res(H,f)':[NH,Nf]}
    db['T21']=abso_SUM.T/counter.T
    db['f']=np.linspace(fmin,fmax,Nf)
    db['H']=np.linspace(Hmin,Hmax,NH)
    return db

def normT21(db,Hnorm='max'):
    '''
    db: H,f,S21
    Hnorm: 'max', 'min', 'ext', [-1,1]
    
    return
    dn: H, Hnorm, S21, S21norm, f
    '''
    
    H=db['H']
    abso=db['T21']
    
    # get Positions
    if Hnorm=='max':
        pos=[np.argmin(np.abs(H-np.nanmax(H)))]
    elif Hnorm=='min':
        pos=[np.argmin(np.abs(H-np.nanmin(H)))]
    elif Hnorm=='ext':
        pos=[np.argmin(np.abs(H-np.nanmax(H))),
             np.argmin(np.abs(H-np.nanmin(H)))]
    else:
        pos= [0 for x in range(len(Hnorm))]
        for i,h in enumerate(Hnorm):
            pos[i]=np.argmin(np.abs(H-h))
    
    
    
    # get Normalization
    lenpos=len(pos)
    Habso=0
    Hnorm=[]
    for p in pos:
        Habso=Habso+abso[:,p]/lenpos
        Hnorm.append(H[pos])
        
    # gridden
    X = np.ones((len(H)))
    ones, HHabso   = np.meshgrid(X,Habso)
    
    # Normen
    abso=abso-HHabso
    
    # Build normated Dataset
    dn={}
    dn['H']=H
    dn['Hnorm']=np.array(Hnorm)
    dn['T21']=abso
    dn['T21norm']=Habso
    dn['f']=db['f']
    
    return dn