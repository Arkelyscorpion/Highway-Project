from function import answer

NHSH = {
    1: ["Cracking", 5, 10],
    2: ["Ravelling", 1, 10],
    3: ["Pothole", 0.1, 1],
    4: ["Shoving", 0.1, 1],
    5: ["Patching", 1, 10],
    6: ["Settlement and depression", 1, 5],
    7: ["Run depth (mm) using 3m straight edge", 5, 10]
}


def computeNHSH(key, val):
    if(val > NHSH[key][2]):
        return [1, 'Poor']
    elif(val <= NHSH[key][2] and val >= NHSH[key][1]):
        return [answer(NHSH[key][2], 1.1, NHSH[key][1], 2, val), 'Fair']
    elif(val < NHSH[key][1] and val >= 0):
        return [answer(0, 3, NHSH[key][1]-0.01, 2.1, val), 'Good']
    else:
        return [0, 'INVALID']
