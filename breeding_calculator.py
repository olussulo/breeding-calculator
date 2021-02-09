# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 14:41:08 2019

@author: olussulo
"""
# a crude script for calculating the amount of female mice to use in breeding
# the script assumes that approx half of the mice born
# will be of the desired genotype

import random

#average litter size
avg_litter = range(3, 9)

# mf is male/female switch: if only males or females are wanted it should be 1
# if both males and females are fine 0 should be used
def litterCalc(pupsWanted, mf):
    p = pupsWanted
    #amount of the pups of the desired genotype wanted
    fem = 0
    #calculated n of females to use in breeding
    accum_fem = 0
    accum_pup = 0
    rng = 50000
    #simulates the breeding rng times
    n = 0
    for i in range(rng):
        while n < p:
            if mf == 1:
                n += (random.choice(avg_litter)//2)//2   
            else:
                n += (random.choice(avg_litter)//2)
            fem += 1
        accum_fem += fem
        accum_pup += n
    return print(f"with {accum_fem//rng} females you will get approximately {accum_pup//rng} pups of the desired genotype")
     
# range version that also outputs the variance but doesn't work
def litterVar(pupsWanted, mf):
    p = pupsWanted
    #amount of the pups of the desired genotype wanted
    fem = 0
    #calculated n of females to use in breeding
    accum_fem = 0
    accum_pup = 0
    rng = 50000
    #simulates the breeding rng times
    n = 0
    for i in range(rng):
        max_pup = 0
        min_pup = 10000
        max_fem = 0
        min_fem = 10000
        while n < p:
            if mf == 1:
                n += (random.choice(avg_litter)//2)//2   
            else:
                n += (random.choice(avg_litter)//2)
            fem += 1
        accum_fem += fem
        accum_pup += n
        if max_pup < n:
            max_pup = n
        if max_fem < fem:
            max_fem = fem
        if min_pup > n:
            min_pup = n
        if min_fem > fem:
            min_fem = fem
    return print(f"with {accum_fem//rng} (avg: {min_fem} - {max_fem}) females you will get approximately {accum_pup//rng} (avg: {min_pup} - {max_pup}) pups of the desired genotype")   
