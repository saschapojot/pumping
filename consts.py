import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as slin
import inspect
# total lattice number
N = 2 ** 8

# Gaussian wave packet in momentum space
# center
kc = (2 * N - 1) / 2
# width
sgm = 1.5

# nonlinearity
g = 2

# init gamma, delta tilde

gmTildeAll = [np.exp(-((2 * k - kc) * np.pi / (N * sgm)) ** 2) for k in range(0, N)]
dltTildeAll = [np.exp(-((2 * k + 1 - kc) * np.pi / (N * sgm)) ** 2) for k in range(0, N)]

# normalization const
tmpC02 = 0
for elem in gmTildeAll:
    tmpC02 += np.abs(elem) ** 2
for elem in dltTildeAll:
    tmpC02 += np.abs(elem) ** 2
C0 = np.sqrt(tmpC02)

gmValsAll = [elem / C0 for elem in gmTildeAll]
dltValsAll = [elem / C0 for elem in dltTildeAll]
# transform to physical space
# tfMat=np.zeros((N,N),dtype=complex)
# for a in range(0,N):
#     for b in range(0,N):
#         tfMat[a,b]=1/np.sqrt(N)*np.exp(1j*2*np.pi*a*b/N)
# alphaValsAll=tfMat.dot(gmValsAll)
# betaValsAll=tfMat.dot(dltValsAll)

kltNorm = [np.abs(gmValsAll[j]) ** 2 + np.abs(dltValsAll[j]) for j in range(0, N)]
# first use the gaussian dist
alphaValsAll = gmValsAll
betaValsAll = dltValsAll

psi0 = []
# init wavefunction
for j in range(0, N):
    psi0.append(alphaValsAll[j])
    psi0.append(betaValsAll[j])

# L=2N
L = len(psi0)

# parameters of linear part of Hamiltonian
omega = 0.1
#tilt strength
omegaF = 4
T=2*np.pi/omega
Q=2**10
tTot=T
dt=tTot/Q

def u(t):
    return np.sin(omega * t)**2


def v(t):
    return np.cos(omega * t)**2


def w(t):
    return 6*(np.sin(omega * t) + np.cos(omega * t))**2


def x(n):
    return 2 * n * omegaF


def y(n):
    return (2 * n + 1) * omegaF


def H0(t):
    h0 = np.zeros((L, L), dtype=float)
    uVal=u(t)
    vVal=v(t)
    wVal=w(t)
    xVals=[x(n) for n in range(0,N)]
    yVals=[y(n) for n in range(0,N)]
    #fill v
    for n in range(0,2*N-1,2):
        h0[n,n+1]=vVal
        h0[n+1,n]=vVal

    for n in range(1,2*N-2,2):
        h0[n,n+1]=wVal
        h0[n+1,n]=wVal

    #fill u+x
    for n in range(0,N):
        h0[2*n,2*n]=uVal+xVals[n]
    #fill -u+y
    for n in range(0,N):
        h0[2*n+1,2*n+1]=-uVal+yVals[n]

    #pbc
    h0[2*N-1,0]=wVal
    h0[0,2*N-1]=wVal
    return h0






