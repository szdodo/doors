#!/usr/bin/env python3

doors=[]
for each in range(100):
    doors.append(False)
    #print(doors[each])

def door_opening(number):
    if number != 101:
        for each in range(100):
            if (each+1) % number == 0:
                if doors[each] == False:
                    doors[each]=True
                else:
                    doors[each]=False
        number = number + 1
        door_opening(number)
    

def results():
    result=[]
    for each in range(100):
        #print(each+1)    
        if doors[each] == True:
            result.append(each+1)
        #print(doors[each])
    print("The following doors were open after the 100th round: ",result)

door_opening(1)
results()