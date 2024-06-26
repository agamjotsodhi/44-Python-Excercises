def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    count = {}
    
    for ltr in phrase:
        count[ltr] = count.get(ltr, 0) + 1
        
    return count

# Test
print(multiple_letter_count('ice cream sundae'))