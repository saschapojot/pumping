from consts import *

#this module contains functions that are used to compute the ode

def S2(psiQ,q):
    '''
    2nd order Strang splitting
    :param psiQ: input wavefunction at time step q
    :param q: current time step

    :return: wavefunction at next time step, q+1
    '''

    psiQ1=[elem*np.exp(-1j*g*np.abs(elem)**2*dt/2) for elem in psiQ]
    #propagator U
    h0Tmp=H0((q+1/2)*dt)
    U=slin.expm(-1j*dt*h0Tmp)
    psiQ2=U.dot(psiQ1)
    psiQp1=[elem*np.exp(-1j*g*np.abs(elem)**2*dt/2) for elem in psiQ2]
    return psiQp1


def meanX(psiQ):
    '''

    :param psiQ: wavefunction at time q

    :return: mean position at time step q
    '''

    xOut=0
    for j in range(0,len(psiQ)):
        xOut+=j*np.abs(psiQ[j])**2
    return xOut