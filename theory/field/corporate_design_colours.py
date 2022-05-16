'''version from 19.02.21
author: Oliver Irtenkauf

features: Coporate Design Colors of University Konstanz
and inverse colors for more contrast

'''
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import gridspec, cm
from matplotlib.colors import ListedColormap

def curves(plotter=False, fig=100, inverse=False):
    if inverse is False:
        # corporate design (for curves)
        H,V,S=.5409,.8784,np.linspace(1,0,256)
        R,G=V*(1-S),V*(1-S*(H*6-np.floor(H*6)))
        B,A=V*np.ones(256),np.ones(256)
        cpd_curves = ListedColormap(np.array([R,G,B,A]).T)
        if plotter==True:
            plt.close(fig)
            plt.figure(fig)
            plt.plot(1-S,R,'--r',1-S,G,'--g',1-S,B,'--b')
            plt.plot(1-S,(R+G+B)/3,'--',c=cpd_curves(1))
            plt.grid()
            plt.ylim([-.05,1.05])
            plt.legend(['$R$','$G$','$B$','$(R+G+B)/3$'])
    else:
        R=np.array([255,255,255,255,255,255,255])/256
        G=np.array([1,37,73,109,146,182,218])/256
        B=np.array([225,229,233,237,242,246,250])/256
        x=np.linspace(0,1,7)
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
        cpd_curves=ListedColormap(mapped)

        if plotter==True:
            plt.close(fig)
            plt.figure(fig)
            plt.plot(x,R,'xr',x,G,'xg',x,B,'xb',x,(R+G+B)/3,'xk')
            plt.plot(xx,mapped[:,0],'--r',label='$R$')
            plt.plot(xx,mapped[:,1],'--g',label='$G$')
            plt.plot(xx,mapped[:,2],'--b',label='$B$')
            plt.plot(xx,(np.sum(mapped, axis=1)-1)/3,
                     '--',c=cpd_curves(1),label='$(R+G+B)/3$')
            plt.grid()
            plt.ylim([-.05,1.05])
            plt.legend()
            plt.xticks(x)
        
    return cpd_curves

def images(plotter=False, fig=101, inverse=False, flip=False):
    if inverse is False:
        # corporate design (for images)
        R=np.array([-89,0,89,160,200,255])/256
        G=np.array([0,154,182,211,229,292])/256
        B=np.array([0,209,220,230,239,305])/256
        x=np.array([0,2.4,2.9,3.7,4.2,5])/5
        polyRcoeff=np.polyfit(x,R,deg=4)
        polyGcoeff=np.polyfit(x,G,deg=4)
        polyBcoeff=np.polyfit(x,B,deg=4)
    else:
        R=np.array([0,209,220,230,239,305])/256
        G=np.array([-89,0,89,160,200,255])/256
        B=np.array([0,154,182,211,229,292])/256
        x=np.array([0,2.4,2.9,3.7,4.2,5])/5
        polyRcoeff=np.polyfit(x,R,deg=4)
        polyGcoeff=np.polyfit(x,G,deg=4)
        polyBcoeff=np.polyfit(x,B,deg=4)
    
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
    if flip is not False:
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
    
def show_colors(fits=True):
    if fits is not False:
        images(plotter=True,fig=1)
        images(plotter=True, inverse=True, fig=2)
        curves(plotter=True, fig=3)
        curves(plotter=True, fig=4,inverse=True)
    
    plt.figure(0)
    try:
    	plt.style.use('thesis_half.mplstyle')
    except:
        print('no thesis_half.mplstyle in current driver folder.')
    x,y=np.meshgrid(np.linspace(0,1,445),np.linspace(0,1,256))
    plt.subplots_adjust(wspace=0, hspace=0, left=0, right=1, bottom=0, top=1)

    fig, ax = plt.subplots(2, 2)
    ax[0,0].imshow(y,cmap=curves())
    ax[0,0].text(100,100,'curves',color=curves(inverse=True)(1))
    ax[0,1].imshow(y,cmap=curves(inverse=True))
    ax[0,1].text(100,100,'curves inverted',color=curves()(1))
    ax[1,0].imshow(y,cmap=images())
    ax[1,0].text(100,100,'images',color=images(inverse=True)(.5))
    ax[1,1].imshow(y,cmap=images(inverse=True))
    ax[1,1].text(100,100,'images inverted',color=images()(.5))

    ax[0,0].axis('off')
    ax[0,1].axis('off')
    ax[1,0].axis('off')
    ax[1,1].axis('off')
