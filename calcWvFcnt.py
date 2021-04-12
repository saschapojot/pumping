from funcs import *
from datetime import  datetime

tStart=datetime.now()
datAll=[]

datAll.append(psi0)
for q in range(0,Q):
    psiCurr=datAll[q]
    psiNext=S2(psiCurr,q)
    datAll.append(psiNext)

tEnd=datetime.now()
print("time: ",tEnd-tStart)
outDir="./pump1/"
# for q in range(0,Q):
#     plt.figure()
#     nmTmp=[np.abs(elem)**2 for elem in datAll[q]]
#     plt.plot(range(0,L),nmTmp,color="black")
#     plt.xlabel("position"
#                )
#     plt.title("time = "+str(q*dt)+", g = "+str(g))
#     plt.ylabel("magnitude")
#     outFile=outDir+"q"+str(q)+".png"
#     plt.savefig(outFile)
#     plt.close()
xPos=[]
for q in range(0,Q):
    vecTmp=datAll[q]
    xTmp=meanX(vecTmp)
    xPos.append(xTmp)

posMax=np.max(xPos)
posMin=np.min(xPos)

posDiff=0.1
tickNum=int((posMax-posMin)/posDiff)
yTicks=[posMin+j*posDiff for j in range(0,tickNum+2)]
tAll=[dt*q for q in range(0,Q)]
plt.figure()
plt.yticks(yTicks)
plt.plot(tAll,xPos,color="black")
plt.xlabel("time")
plt.ylabel("ave position")
plt.title("g = "+str(g))
plt.savefig(outDir+"position.png")
plt.close()

#write params info
outTxt=outDir+"info.txt"

fptr=open(outTxt,"w+")
fptr.write("g="+str(g)+"\n")
fptr.write("omega="+str(omega)+"\n")
fptr.write("omegaF="+str(omegaF)+"\n")
fptr.write(inspect.getsource(x))
fptr.write(inspect.getsource(y))
fptr.write(inspect.getsource(u))
fptr.write(inspect.getsource(v))
fptr.write(inspect.getsource(w))
fptr.close()