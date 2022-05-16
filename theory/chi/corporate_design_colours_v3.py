'''version from 11.03.21
author: Oliver Irtenkauf

features: Coporate Design Colors of University Konstanz
and inverse colors for more contrast

'''
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import gridspec, cm
from matplotlib.colors import ListedColormap
try:
    plt.style.use('thesis_half.mplstyle')
except:
    print('no style found')

def curves(color='seeblau',plotter=False, fig=100):
    # corporate design (for curves)
    if color=='seeblau':
        H,V,S=.5409,.8784,np.linspace(1,0,256)
        R,G=V*(1-S),V*(1-S*(H*6-np.floor(H*6)))
        B,A=V*np.ones(256),np.ones(256)
    elif color=='magenta':
        H,V,S=.5409,.8784,np.linspace(1,0,256)
        G,B=V*(1-S),V*(1-S*(H*6-np.floor(H*6)))
        R,A=V*np.ones(256),np.ones(256)
    elif color=='black':
        R=np.linspace(0,.65,256)
        G,B=R,R
        A=np.ones(256)
        S=np.linspace(1,0,256)
    else:
        print("Please choose color from: 'seeblau', 'magenta' or 'black'")
        
    cpd_curves = ListedColormap(np.array([R,G,B,A]).T)
    if plotter==True:
        plt.close(fig)
        plt.figure(fig)
        plt.plot(1-S,R,'--r',1-S,G,'--g',1-S,B,'--b')
        plt.plot(1-S,(R+G+B)/3,'--',c=cpd_curves(1))
        plt.grid()
        plt.ylim([-.05,1.05])
        plt.legend(['$R$','$G$','$B$','$(R+G+B)/3$'])
        cpd_curves = ListedColormap(np.array([R,G,B,A]).T)        
    return cpd_curves

def images(color='seeblau', plotter=False, fig=101, inverse=False):
    # corporate design (for images)
    if color=='seeblau':
        R=np.array([-89,0,89,160,200,255])/256
        G=np.array([0,154,182,211,229,292])/256
        B=np.array([0,209,220,230,239,305])/256
        x=np.array([0,2.4,2.9,3.7,4.2,5])/5
        polyRcoeff=np.polyfit(x,R,deg=4)
        polyGcoeff=np.polyfit(x,G,deg=4)
        polyBcoeff=np.polyfit(x,B,deg=4)
    elif color=='magenta':
        R=np.array([0,209,220,230,239,305])/256
        G=np.array([-89,0,89,160,200,255])/256
        B=np.array([0,154,182,211,229,292])/256
        x=np.array([0,2.4,2.9,3.7,4.2,5])/5
        polyRcoeff=np.polyfit(x,R,deg=4)
        polyGcoeff=np.polyfit(x,G,deg=4)
        polyBcoeff=np.polyfit(x,B,deg=4)
    elif color=='grey':
        R=np.array([0,209,220,230,239,255])/256
        G=np.array([0,0,89,160,200,255])/256
        B=np.array([0,154,182,211,229,255])/256
        x=np.array([0,2,2.9,3.7,4.2,5])/5
        RGB=(R+G+B)/3
        R,G,B,A=RGB,RGB,RGB,RGB
        polyRGBcoeff=np.polyfit(x,RGB,deg=4)
        polyRcoeff=polyRGBcoeff
        polyGcoeff=polyRGBcoeff
        polyBcoeff=polyRGBcoeff
    else:
        print("Please choose color from: 'seeblau','magenta' or 'grey'")
    
    xx=np.linspace(0,1,256)
    polyRcoeff=np.polyfit(x,R,deg=4)
    polyGcoeff=np.polyfit(x,G,deg=4)
    polyBcoeff=np.polyfit(x,B,deg=4)
    polyR=np.poly1d(polyRcoeff)(xx)
    polyG=np.poly1d(polyGcoeff)(xx)
    polyB=np.poly1d(polyBcoeff)(xx)
    mapped=np.array([polyR.T,polyG.T,
                    polyB.T,np.ones(256).T]).T
    mapped[mapped<=0]=0
    mapped[mapped>=1]=1
    cpd_img=ListedColormap(mapped)
    
    if inverse is not False:
        cpd_img=ListedColormap(np.flip(mapped,axis=0))

    if plotter==True:
        plt.close(fig)
        plt.figure(fig)
        plt.plot(x,R,'xr',x,G,'xg',x,B,'xb',x,(R+G+B)/3,'xk')
        plt.plot(xx,mapped[:,0],'--r',label='$R$')
        plt.plot(xx,mapped[:,1],'--g',label='$G$')
        plt.plot(xx,mapped[:,2],'--b',label='$B$')
        plt.plot(xx,(np.sum(mapped, axis=1)-1)/3,
                 '--',c=cpd_img(.5),label='$(R+G+B)/3$')
        plt.grid()
        plt.ylim([-.05,1.05])
        plt.legend()
        plt.xticks(x)
    return cpd_img

def show_all(fitter=False):
    if fitter==True:
        images(color='seeblau',plotter=True,fig=1)
        images(color='magenta',plotter=True,fig=2)
        images(color='grey',plotter=True,fig=3)
        
        curves(color='seeblau',plotter=True,fig=4)
        curves(color='magenta',plotter=True,fig=5)
        curves(color='black',plotter=True,fig=6)
        
    plt.figure(0)
    x,y=np.meshgrid(np.linspace(0,1,445),np.linspace(0,1,256))
    #plt.subplots_adjust(wspace=0, hspace=0, left=0, right=1, bottom=0, top=1)
    fig, ax = plt.subplots(2, 6)
    ax[0,0].imshow(y,cmap=images(color='seeblau'), aspect='auto')
    ax[0,1].imshow(y,cmap=images(color='seeblau',inverse=True), aspect='auto')
    ax[0,2].imshow(y,cmap=images(color='magenta'), aspect='auto')
    ax[0,3].imshow(y,cmap=images(color='magenta',inverse=True), aspect='auto')
    ax[0,4].imshow(y,cmap=images(color='grey'), aspect='auto')
    ax[0,5].imshow(y,cmap=images(color='grey',inverse=True), aspect='auto')

    ax[0,0].axis('off')
    ax[0,1].axis('off')
    ax[0,2].axis('off')
    ax[0,3].axis('off')
    ax[0,4].axis('off')
    ax[0,5].axis('off')

    ax[1,1].imshow(y,cmap=curves(color='seeblau'), aspect='auto')
    ax[1,3].imshow(y,cmap=curves(color='magenta'), aspect='auto')
    ax[1,5].imshow(y,cmap=curves(color='black'), aspect='auto')

    ax[1,0].text(0,0,'seeblau')
    ax[1,2].text(0,0,'magenta')
    ax[1,4].text(0,0,'black/grey')
    
    ax[1,0].axis('off')
    ax[1,1].axis('off')
    ax[1,2].axis('off')
    ax[1,3].axis('off')
    ax[1,4].axis('off')
    ax[1,5].axis('off')
    