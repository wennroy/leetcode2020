# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 10:40:44 2020

@author: lengwaifang
"""



class Solution:
    def soupServings(self, N: int) -> float:
        if N == 0:
            return 0.5
        if N >= 5600:
            return 1
        if N%25 ==0 :
            n = N//25
        else:
            n = N//25 + 1
        na = n
        nb = n
        record = {}
        def PNullA(self, na, nb):
            if na <=0 and nb > 0:
                return 1
            elif nb <= 0:
                return 0

            else:
                if (na,nb) in record:
                    return record[(na,nb)]
                record[(na,nb)] = 0.25*(PNullA(None,na-4,nb)+ PNullA(None,na-3,nb-1)+ PNullA(None,na-2,nb-2)+ PNullA(None,na-1,nb-3))
            return record[(na,nb)]
        
        record2 = {}
        def PNullAB(self,na,nb):
            if nb <= 0 or na <= 0:
                return 0

            ## na快用完的时候
            p = 0
            if na <= 3 and nb <= 1:
                p += .25
            if na <= 2 and nb <= 2:
                p +=.25
            if na <= 1 and nb <= 3:
                p +=.25
            ## na 没用完的时候
            if not p == 0:
                return p
            else:
                if (na,nb) in record2:
                    return record2[(na,nb)]
                record2[(na,nb)] = 0.25*(PNullAB(None,na-4,nb)+ PNullAB(None,na-3,nb-1)+ PNullAB(None,na-2,nb-2)+ PNullAB(None,na-1,nb-3))
            return record2[(na,nb)]
        
        return PNullA(None,na,nb) + 0.5* PNullAB(None,na,nb)
        
    
    
for i in range(1,500):
    N = i*25
    p = Solution.soupServings(None,N)
    if abs(p-1) < 1e-6:
        print(f'{i}:{p}已小于1e-6')
    else:
        print(f'{i}:{p}')