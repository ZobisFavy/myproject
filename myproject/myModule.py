def top_n(items, n):
    """_Return the top n in array, in desc order.
    
    Args:
        items (array): list or array-like object
        n (int): number of items to return
        
    Return:
        array: top n items in desc order
        
    Egs:
        >>> top n([8,3,2,7,4], 3)
        [8,7,4]
    """
    
    for i in range(n): # keep sorting until we have the top n items
        for j in range(len(items)-1-i):
            
            if items[j] > items[j+1]: # if the item is bigger than the next items
                items[j], items[j+1] = items[j+1], items[j] # swap the two
                
    # get last two items
    top_n = items[-n:]
    
    # Return in desc order
    return top_n[::-1]
