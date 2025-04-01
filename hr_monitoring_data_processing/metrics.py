def average(data: list) -> float:
    """
    Calculate average value of the list of numbers in data.

    Args:
        data (list[int]): list of integers representing heart rate samples.
        
    Returns:
        float: a floating point value representing the average of this list. Returns None if the input list is empty.
    """
    average = 0
    count = 0
    if data == []:
        return []
    for i in data:
        average += i
        count += 1 
    return round(average / count, 2)

def maximum(data: list) -> float:
    """
    Calculate average value of the list of numbers in data.

    Args:
        data (list[int]): list of integers representing heart rate samples.
        
    Returns:
        float: a floating point value representing the average of this list. Returns None if the input list is empty.
    """
    if  data == []:
        return []
    max_number = 0
    for value in data:
        if value > max_number:
            max_number = value
    return  max_number 

def variance(data: list) -> float:
    """
    Calculate average value of the list of numbers in data.

    Args:
        data (list[int]): list of integers representing heart rate samples.
        
    Returns:
        float: a floating point value representing the average of this list. Returns None if the input list is empty.
    """
    if data == []:
        return []
    variance = 0
   
    for number in data:
        variance += (number - average(data))**2
    return variance / len(data)

def standard_deviation(data: list) -> float:
    """
    Calculate average value of the list of numbers in data.

    Args:
        data (list[int]): list of integers representing heart rate samples.
        
    Returns:
        float: a floating point value representing the average of this list. Returns None if the input list is empty.
    """
    if  data == []:
        return []
    
    return round(variance(data)**0.5, 2) 