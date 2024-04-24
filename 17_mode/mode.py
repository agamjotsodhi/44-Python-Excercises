def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    # Counter that tracks # of num reps
    counter = {}

    for num in nums:
        counter[num] = counter.get(num, 0) + 1
    
    # finds the highest value (most freq number)
     
    max_value = max(counter.values())
    
    # which index the highest value is at
    for (num, rep) in counter.items():
        if rep == max_value:
            return num
    
    # test
    print(mode([1, 2, 1]))
        
    
    