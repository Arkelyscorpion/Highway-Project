from function import answer

def cracking(val):
    if(val > 20):
        return [1,'Poor']
    elif(val <= 20 and val >=10):
        return [answer(20,1.1,10,2,val),'Fair']
    elif(val < 10 and val >= 0):
        return [answer(0,3,9.9,2.1,val),'Good']
    else:
        return [0,'INVALID']


