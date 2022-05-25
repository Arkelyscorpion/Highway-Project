from function import answer

UR = {
    1: ["Cracking", 5, 15],
    2: ["Ravelling", 5, 10],
    3: ["Potholes", 0, 0.5],
    4: ["Settlement", 1, 5],
    5: ["Run depth (mm) using 3m straight edge", 5, 10]
}


def computeUR(key, val):
    if(val > UR[key][2]):
        return [1, 'Poor']
    elif(val <= UR[key][2] and val >= UR[key][1]):
        return [answer(UR[key][2], 1.1, UR[key][1], 2, val), 'Fair']
    elif(val < UR[key][1] and val >= 0):
        return [answer(0, 3, UR[key][1]-0.01, 2.1, val), 'Good']
    else:
        return [0, 'INVALID']
