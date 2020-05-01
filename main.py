#Fibonicci number sequence
#Have the user enter a number
#generate a fibonicci sequence
#which the size is equal to that number

def fibonicci_seq(num):
    """
    generates the fibonicci sequence 
    with the size of num
    """

    assert num > 0

    series = [1]


    while len(series) < num:
        if len(series) == 1:
            series.append(1)
        else:
            series.append(series[-1] + series[-2])
    
    #convert int to strings
    for i in range(len(series)):
        series[i] = str(series[i])
        
    return(', '.join(series)) 