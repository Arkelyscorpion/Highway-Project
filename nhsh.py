# -------------------------------------------------------------------------------------- 

#                          NATIONAL HIGHWAY / STATE HIGHWAY 

# --------------------------------------------------------------------------------------

from function import answer,computeCondition
from idata import IData

NHSH = {
    1: ["Cracking", 5, 10],
    2: ["Ravelling", 1, 10],
    3: ["Pothole", 0.1, 1],
    4: ["Shoving", 0.1, 1],
    5: ["Patching", 1, 10],
    6: ["Settlement and depression", 1, 5],
    7: ["Run depth (mm) using 3m straight edge", 5, 10]
}

def computeNHSHRating(key, val):

    if(val > NHSH[key][2]):
        return 1
    elif(val <= NHSH[key][2] and val >= NHSH[key][1]):
        return answer(NHSH[key][2], 1.1, NHSH[key][1], 2, val)
    elif(val < NHSH[key][1] and val >= 0):
        return answer(0, 3, NHSH[key][1]-0.01, 2.1, val)
    else:
        return 0


def calculateNHSH():

    inputs = []
    wt = [1.0, 0.75, 0.5, 1.0, 0.75, 0.75, 1.0]

    # STORE THE USER INPUT INTO AN ARRAY

    inputs.append(IData['inum'][0])
    inputs.append(IData['inum'][1])
    inputs.append(IData['inum'][2])
    inputs.append(IData['inum'][3])
    inputs.append(IData['inum'][4])
    inputs.append(IData['inum'][5])
    inputs.append(IData['inum'][6])

    sum = 0
    final_list = []

    for i in range(len(inputs)):
        final = computeNHSHRating(i+1, inputs[i])
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
        ("Shoving", str(inputs[3]), str(final_list[3]),
         str(wt[3]), str(round(final_list[3]*wt[3], 1))),
        ("Patching", str(inputs[4]), str(final_list[4]),
         str(wt[4]), str(round(final_list[4]*wt[4], 1))),
        ("Settlements", str(inputs[5]), str(final_list[5]), str(
            wt[5]), str(round(final_list[5]*wt[5], 1))),
        ("Run Depth", str(inputs[6]), str(final_list[6]), str(
            wt[6]), str(round(final_list[6]*wt[6], 1))),
    )

    return (data,final_rating_value,cond)