def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """
    if a == b:
        return "Numbers are equal"
    elif a > b:
        return "First number is greater"
    else:
        return "Second number is greater" 
    
    # Test
print(number_compare(2,2))
print(number_compare(5,2))
    