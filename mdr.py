from function import answer

MDR = {
    1: ["Cracking", 10, 20],
    2: ["Ravelling", 10, 20],
    3: ["Pothole", 0.5, 1],
    4: ["Patching", 5, 20],
    5: ["Settlement and depression", 2, 5]
}


def computeMDR(key, val):
    if(val > MDR[key][2]):
        return [1, 'Poor']
    elif(val <= MDR[key][2] and val >= MDR[key][1]):
        return [answer(MDR[key][2], 1.1, MDR[key][1], 2, val), 'Fair']
    elif(val < MDR[key][1] and val >= 0):
        return [answer(0, 3, MDR[key][1]-0.01, 2.1, val), 'Good']
    else:
        return [0, 'INVALID']


# print(computeMDR(1, 12.1))
# print(computeMDR(1, 5))
# print(computeMDR(1, 48))


# def cracking(val):
#     if(val > 20):
#         return [1,'Poor']
#     elif(val <= 20 and val >=10):
#         return [answer(20,1.1,10,2,val),'Fair']
#     elif(val < 10 and val >= 0):
#         return [answer(0,3,9.9,2.1,val),'Good']
#     else:
#         return [0,'INVALID']
