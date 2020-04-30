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


    while len(series):
        