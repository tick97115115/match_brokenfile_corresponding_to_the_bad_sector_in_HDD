#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import subprocess


def LBA_to_CHS(Cluster,Sector,LBA):
    try:
        CS = Cluster / Sector
    except TypeError:
        print('''
        The type of \'Cluster\' was %s
        and the type of \'Sector\' was %s
        Both of them must be int.
        ''' % (type(Cluster),type(Sector)))
    
    result = []
    for x in LBA:
        result.append(int(x)/CS)

    return result


def mapping(CHS):
    #disk = 'd:'#input('Please type the target disk letter after here:')
    for x in CHS:
        subprocess.run(['fsutil','volume','querycluster','d:',str(int(x))],shell=True)




if __name__ == "__main__":
    mapping(LBA_to_CHS(4096,512,12394496))