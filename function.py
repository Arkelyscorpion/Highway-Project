def answer(x1, y1, x2, y2, x):
    return round(((y2-y1)/(x2-x1) * (x-x1) + y1), 2)

# COMPUTE THE CONDITION OF THE ROAD

def computeCondition(final_rating_value):

    cond = "-"

    if(final_rating_value <= 1):
        cond = "Poor"
    elif(final_rating_value >= 1.1 and final_rating_value <= 2):
        cond = "Fair"
    elif(final_rating_value >= 2.1 and final_rating_value <= 3):
        cond = "Good"

    return cond

def is_number(n):
    try:
        float(n)   # Type-casting the string to `float`.
                   # If string is not a valid `float`, 
                   # it'll raise `ValueError` exception
    except ValueError:
        return False
    return True