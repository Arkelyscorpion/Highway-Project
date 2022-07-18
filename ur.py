from function import answer,computeCondition
from idata import IData

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


def calculateUR():
    
    inputs = []
    wt = [1.0, 0.75, 0.5, 0.75, 1.0]
    inputs.append(IData['inum'][0])
    inputs.append(IData['inum'][1])
    inputs.append(IData['inum'][2])
    inputs.append(IData['inum'][5])
    inputs.append(IData['inum'][6])

    sum = 0
    final_list = []
    
    for i in range(len(inputs)):
        final, condition = computeUR(i+1, inputs[i])
        final_list.append(final)
        sum = sum + round(final*wt[i], 3)

    # COMPUTING THE FINAL RATING VALUE

    final_rating_value = sum/len(inputs)

    # COMPUTING CONDITION OF THE ROAD

    cond = computeCondition(final_rating_value)

    # STORE THE DATA TO PRINT IN THE PDF

    data = (
        ("Distress Type", "Input(%)", "Rating", "Weightage", "Wt Rating Value"),
        ("Cracking", str(inputs[0]), str(final_list[0]),
         str(wt[0]), str(round(final_list[0]*wt[0], 1))),
        ("Ravelling", str(inputs[1]), str(final_list[1]), str(
            wt[1]), str(round(final_list[1]*wt[1], 1))),
        ("Potholes", str(inputs[2]), str(final_list[2]),
         str(wt[2]), str(round(final_list[2]*wt[2], 1))),
        ("Settlements", str(inputs[3]), str(final_list[3]), str(
            wt[3]), str(round(final_list[3]*wt[3], 1))),
        ("Rut depth", str(inputs[4]), str(final_list[4]), str(
            wt[4]), str(round(final_list[4]*wt[4], 1))),
    )

    return (data,final_rating_value,cond)