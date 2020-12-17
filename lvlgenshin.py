#!/usr/bin/python3
# -*- coding: utf-8 -*-
#godkayaki
#This is NOT exact and precise and will be improved in the future

lvl = 1
exp0to10=0
exp10to20=0
exp20to30=0
exp30to40=0
exp40to50=0
exp50to60=0

#0-10 (7575) 757.5/lvl

while lvl<=10:
    
    expperlevel = 757.5

    #Actual lvl
    print("--------------------------------------")
    print("Actual Level: %d"%lvl)

    exp0to10=exp0to10+expperlevel

    #Total exp and progress
    print("Current exp from 0 to %d: "%lvl, end='')
    print(exp0to10)

    lvl=lvl+1

#10-20 (20525) 2052.5/lvl

while lvl<=20:
    
    expperlevel = 2052.5

    #Actual lvl
    print("--------------------------------------")
    print("Actual Level: %d"%lvl)

    exp10to20=exp10to20+expperlevel

    #Total exp and progress
    print("Current exp from 0 to %d: "%lvl, end='')
    print(exp10to20)

    lvl=lvl+1

#20-30 (44050) 4405.0/lvl

while lvl<=30:
    
    expperlevel = 4405.0

    #Actual lvl
    print("--------------------------------------")
    print("Actual Level: %d"%lvl)

    exp20to30=exp20to30+expperlevel

    #Total exp and progress
    print("Current exp from 0 to %d: "%lvl, end='')
    print(exp20to30)

    lvl=lvl+1

#30-40 (73225) 7322.5/lvl

while lvl<=40:
    
    expperlevel = 7322.5

    #Actual lvl
    print("--------------------------------------")
    print("Actual Level: %d"%lvl)

    exp30to40=exp30to40+expperlevel

    #Total exp and progress
    print("Current exp from 0 to %d: "%lvl, end='')
    print(exp30to40)

    lvl=lvl+1

#40-50 (124800) 12480.0/lvl

while lvl<=50:
    
    expperlevel = 12480.0

    #Actual lvl
    print("--------------------------------------")
    print("Actual Level: %d"%lvl)

    exp40to50=exp40to50+expperlevel

    #Total exp and progress
    print("Current exp from 0 to %d: "%lvl, end='')
    print(exp40to50)

    lvl=lvl+1

#50-60 (249600) 24960.0/lvl

while lvl<=60:
    
    expperlevel = 24960.0

    #Actual lvl
    print("--------------------------------------")
    print("Actual Level: %d"%lvl)

    exp50to60=exp50to60+expperlevel

    #Total exp and progress
    print("Current exp from 0 to %d: "%lvl, end='')
    print(exp50to60)

    lvl=lvl+1

print("--------------------------------------")

#Days in base an exponential 1525 exp plus for every level and a 2000 exp gain everyday.
print("Total days by just gaining 2000 exp a day from level 0 to 10: %d"%(exp0to10/2000))
print("Total days by just gaining 2000 exp a day from level 10 to 20: %d"%(exp10to20/2000))
print("Total days by just gaining 2000 exp a day from level 20 to 30: %d"%(exp20to30/2000))
print("Total days by just gaining 2000 exp a day from level 30 to 40: %d"%(exp30to40/2000))
print("Total days by just gaining 2000 exp a day from level 40 to 50: %d"%(exp40to50/2000))
print("Total days by just gaining 2000 exp a day from level 50 to 60: %d"%(exp50to60/2000))

totaldays = exp0to10/2000 + exp10to20/2000 + exp20to30/2000 + exp30to40/2000 + exp40to50/2000 + exp50to60/2000
print("--------------------------------------")
print("Total days (2000 exp a day) from 0 to 60: %d"%totaldays)

print("")