import pyfits,os,glob,json
from scipy.optimize import leastsq

files=glob.glob('*_slc.fits')

ut=[];uf=[]
at=[];af=[]
for i in range(len(files)):
  f=pyfits.open(files[i])
  data=f[1].data
  time=data.field('TIME')
  flux=data.field('PDCSAP_FLUX')
  sel=where(isnan(flux)==0)
  timec=time[sel];fluxc=flux[sel]
  ##Save raw LC data
  ut=append(ut,timec)
  uf=append(uf,fluxc)
  ##polynomial fits with sigma clipping
  for i in range(2):
    m=polyfit(timec,fluxc,4)
    resid=fluxc-polyval(m,timec)
    sel=where(abs(resid)<2*std(resid))
    timec=timec[sel];fluxc=fluxc[sel]
  ##plt.plot(time[sel],flux[sel],time[sel],polyval(m,time[sel]))
  ##save
  sel=where(isnan(flux)==0)
  at=append(at,time[sel])
  af=append(af,flux[sel]/polyval(m,time[sel]))

###cut bad data
#sel=where(array(at<169,dtype='int')+array(at>200,dtype='int'))

##restrict range, sort
sel=where(at<140)
cat=at[sel][argsort(at[sel])]
caf=af[sel][argsort(at[sel])]
sel=where(ut<180)
cut=ut[sel][argsort(ut[sel])]
cuf=uf[sel][argsort(ut[sel])]

numpy.set_printoptions(linewidth=inf,threshold=inf)

#save
out1='LC_raw.csv'
f=open(out1,'w')
for i in range(len(cut)): f.write('%0.5f'%cut[i]+','+'%0.0f'%cuf[i]+'\n')
f.close()
#with open(out1.replace('csv','json'), 'wb') as fp: json.dump([str(cut).replace('  ',','),str(cuf).replace('  ',',')], fp)

out2='LC_norm.csv'
f=open(out2,'w')
for i in range(len(cat)): f.write('%0.5f'%cat[i]+','+'%0.6f'%caf[i]+'\n')
f.close()
#with open(out2.replace('csv','json'), 'wb') as fp: json.dump([str(cat).replace('  ',','),str(caf).replace('  ',',')], fp)


###fold
#dips at 224.05,221.59
#middle is 224.05
#period is 2.46

#foldt=zeros(len(cat))
#for i in range(len(cat)):
  #foldt[i]=cat[i]-224.05-floor((cat[i]-224.05)/2.46)*2.46

def foldit(p,x,y):
  cx=x-p[0]-floor((x-p[0])/p[1])*p[1]
  cf=1-p[2]*exp(-(cx-(p[1]/2.))**2/(2*p[3]**2))
  r=cf-y
  return r

guess=[224.05,2.46,0.015,0.032]

best=leastsq(foldit,guess,args=(cat,caf))[0]

foldt=cat-best[0]-floor((cat-best[0])/best[1])*best[1]
plt.plot(foldt,caf,'o')



