#!/usr/bin/python3
# -*- coding: utf-8 -*-
#godkayaki
#This is NOT exact and precise and will be improved in the future

def levelcalculator(lvl, expfromto, maxlevel):
    while lvl<=maxlevel:
        expperlevel = 757.5
        if lvl>55:
            expperlevel = 312175.0
        elif lvl>50:
            expperlevel = 15600.0
        elif lvl>40:
            expperlevel = 14880.0
        elif lvl>30:
            expperlevel = 7322.5
        elif lvl>20:
            expperlevel = 4405.0
        elif lvl>10:
            expperlevel = 2052.5
        elif lvl>0:
            expperlevel = 757.5
        #Actual lvl
        print("Actual Level: %d"%lvl)

        expfromto=expfromto+expperlevel

        #Total exp and progress
        print("Current exp from 0 to %d: "%lvl, end='')
        print(expfromto)

        print("--------------------------------------")

        if lvl==60:
            print("---- Experiencia total: %d ----"%expfromto)

        lvl=lvl+1

lvl = 1
#execution from levl 0 to 10
levelcalculator(lvl,0,10)
#execution from levl 10 to 20
levelcalculator(lvl,0,20)
#execution from levl 20 to 30
levelcalculator(lvl,0,30)
#execution from levl 30 to 40
levelcalculator(lvl,0,40)
#execution from levl 40 to 50
levelcalculator(lvl,0,50)
#execution from levl 50 to 60
levelcalculator(lvl,0,60)

totaldays=1933050/2000
print("")
print("Total days to go from level 0 to level 60 by only doing daily misions and spending little resin: %d"%totaldays)

#print("--------------------------------------")

#days in base an exponential 1525 exp plus for every level and a 2000 exp gain everyday.
#print("Total days (2000 exp a day) from 0 to 60: %d"%totaldays)

#print("")