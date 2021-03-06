####from pyXSteam.XSteam import XSteam
####stm = XSteam(XSteam.UNIT_SYSTEM_MKS)
####print(stm.h_pt(30,250))
##
##
####Input arvot##
##qm=float(input('Polttoaineen massavirta [kg/s]:'))
##

lkm=int(input('Polttoaineiden määrä: '))

b = {}

for x in range(lkm):
    y = x+1
    osuus=float(input('polttoaineen osuus:'))
    b[f'{y}.osuus'] = osuus
    kosteus=float(input('Polttoaineen kosteus [%]:'))
    b[f'{y}.kosteus'] = kosteus
    tuhka=float(input('Tuhkapitoisuus [%]:'))
    b[f'{y}.tuhka'] = tuhka
    nC=float(input('C [m% kuiva-aineessa]:'))
    b[f'{y}.nC'] = nC
    nH2=float(input('H [m% kuiva-aineessa]:'))
    b[f'{y}.nH2'] = nH2
    nO2=float(input('O [m% kuiva-aineessa]:'))
    b[f'{y}.nO2'] = nO2
    nN2=float(input('N [m% kuiva-aineessa]:'))
    b[f'{y}.nN2'] = nN2
    nS=float(input('S [m% kuiva-aineessa]:'))
    b[f'{y}.nS'] = nS
    nCl=float(input('Cl[m% kuiva-aineessa]:'))
    b[f'{y}.nCl'] = nCl
    LHVar=float(input('Lämpöarvo saapumistilassa [MJ/kg]:'))
    b[f'{y}.LHVar'] = LHVar


c=[]
for i in range(lkm):
    osuus = b[f'{i+1}.osuus']
    kosteus = b[f'{i+1}.kosteus']
    kuiva = (osuus/100)*(1-(kosteus/100))
    c.append(kuiva)

kuivapa=sum(c)

k=[]
t=[]
C=[]
H2=[]
O2=[]
N2=[]
S=[]
Cl=[]
l=[]

for i in range(lkm):
    osuus = b[f'{i+1}.osuus']
    kosteus = b[f'{i+1}.kosteus']
    kuiva = (osuus/100)*(1-(kosteus/100))
    osuusk = kuiva/kuivapa
    kosteus=b[f'{y}.kosteus']*(osuus/100)
    k.append(kosteus)
    LHVar=b[f'{i+1}.LHVar']*(osuus/100)
    l.append(LHVar)
    nC = b[f'{i+1}.nC']*osuusk
    C.append(nC)
    nH2 = b[f'{i+1}.nH2']*osuusk
    H2.append(nH2)
    nO2 = b[f'{i+1}.nO2']*osuusk
    O2.append(nO2)
    nN2 = b[f'{i+1}.nN2']*osuusk
    N2.append(nN2)
    nS = b[f'{i+1}.nS']*osuusk
    S.append(nS)
    nCl =  b[f'{i+1}.nCl']*osuusk
    Cl.append(nCl)
    tuhka =  b[f'{i+1}.tuhka']*osuusk
    t.append(tuhka)
    
kosteus=sum(k)   
nC=sum(C)
nH2=sum(H2)
nO2=sum(O2) 
nN2=sum(N2)
nS=sum(S)
nCl=sum(Cl)
tuhka=sum(t)
LHVar=sum(l)


##O2sk=float(input('Kuivan savukaasun happipitoisuus:'))
##ilmankosteus=float(input('ilman kosteus [kgH2O/kgilmaa]:'))
##
####Laskenta##
##ilmakerroin=1+((O2sk/100)/(0.209-(O2sk/100)))
##
###Lähtöaineet
##mH2O=(kosteus/100)*qm*1000
##mC=(qm*1000-mH2O)*(nC/100)
##mH2=(qm*1000-mH2O)*(nH2/100)
##mO2=(qm*1000-mH2O)*(nO2/100)
##mN2=(qm*1000-mH2O)*(nN2/100)
##mS=(qm*1000-mH2O)*(nS/100)
##mCl=(qm*1000-mH2O)*(nCl/100)
##mtuhka=(qm*1000-mH2O)*(tuhka/100)
##
##nH2O=mH2O/18.02
##nC=mC/12.01
##nH2=mH2/2.02
##nO2=mO2/32
##nN2=mN2/28.01
##nS=mS/32.07
##nCl=mCl/35.45
##
##ilmantarve=nC+(nH2/2)-nO2+nS
##
####ainemäärät
##nH2Osk=nH2O+nH2+(ilmankosteus*(28.964/18.01528)*ilmakerroin*4.77*ilmantarve)
##nCO2=nC
##nSO2=nS
##nO2sk=(ilmakerroin-1)*ilmantarve
##nN2sk=nN2+(3.77*ilmakerroin*ilmantarve)
##nHCl=nCl
##
##ntotsk=nH2Osk+nCO2+nSO2+nN2+nO2+nHCl
##
##mooliosuusH2Osk=nH2Osk/ntotsk
##mooliosuusCO2=nCO2/ntotsk
##mooliosuusSO2=nSO2/ntotsk
##mooliosuusO2=nO2sk/ntotsk
##mooliosuusN2=nN2sk/ntotsk
##mooliosuusHCl=nHCl/ntotsk         
##
####tilavuudet
##volH2O=22*nH2Osk/1000
##volCO2=22.26*nCO2/1000
##volSO2=21.89*nSO2/1000                     
##volO2=22.39*nO2sk/1000
##volN2=22.4*nN2sk/1000
##volHCl=22.25*nHCl/1000
##
##voltot=volCO2+volH2O+volSO2+volO2+volN2+volHCl                
##
##volosuusH2O=volH2O/voltot
##volosuusCO2=volCO2/voltot
##volosuusSO2=volSO2/voltot                
##volosuusO2=volO2/voltot
##volosuusN2=volN2/voltot
##volosuusHCl=volHCl/voltot
##
####massat
##massaH2O=18.01528*nH2Osk/1000
##massaCO2=44.01*nCO2/1000               
##massaSO2=64.066*nSO2/1000              
##massaO2=(15.999*2)*nO2sk/1000
##massaN2=(14.0067*2)*nN2sk/1000
##massaHCl=36.458*nHCl/1000
##                 
##massatot=massaH2O+massaCO2+massaSO2+massaO2+massaN2+massaHCl
##
##massaosuusH2O=massaH2O/massatot
##massaosuusCO2=massaCO2/massatot               
##massaosuusSO2=massaSO2/massatot               
##massaosuusO2=massaO2/massatot
##massaosuusN2=massaN2/massatot
##massaosuusHCl=massaHCl/massatot
##
####Yhteenveto
##teho=qm*LHVar
##volosuusO2kuiva=volO2/(voltot-volH2O)*100
##volosuusO2kostea=volO2/voltot*100
##nstökömetrinenilma=ilmantarve
##npalamisilmakuiva=ilmantarve+(3.77*ilmakerroin*ilmantarve)+(ilmakerroin-1)*ilmantarve
##volpalamisilmakuiva=npalamisilmakuiva/1000*22.4
##npalamisilmakostea=ilmantarve+(3.77*ilmakerroin*ilmantarve)+(ilmakerroin-1)*ilmantarve+nH2Osk
##volpalamisilmakostea=npalamisilmakostea/1000*22.4
##volskkostea=voltot
##massaskkostea=massatot
##volskkuiva=voltot-volH2O               
##massaskkuiva=massatot-massaH2O
##
##
##
##print(f'teho: {teho} MW')
##print(f'O2 kuiva: {volosuusO2kuiva}% - O2 kostea: {volosuusO2kostea}%')
##print(f'Stökiömetrinen ilmantarve: {ilmantarve}mol')
##print(f'Kuiva palamisilma: {npalamisilmakuiva}mol - {volpalamisilmakuiva} nm3')
##print(f'Kostea palamisilma: {npalamisilmakostea}mol - {volpalamisilmakostea} nm3')
##print(f'Kostea savukaasu: {volskkostea}mol - {massaskkostea}kg')
##print(f'Kuiva savukaasu: {volskkuiva}mol - {massaskkuiva}kg')
##
##
##
