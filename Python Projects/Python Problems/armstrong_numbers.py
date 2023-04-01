def is_armstrong_number(number):
    #Convert number to an array of integers and create empty array
    array = [int(i) for i in str(number)]
    armstrongarray = []
    #Get length of the array
    armstrong = len(array)
    #Exponentiate every number in the array by the length of the array
    for item in array:
        armstrongarray.append(item ** armstrong)
