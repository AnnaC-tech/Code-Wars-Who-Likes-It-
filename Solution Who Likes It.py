def likes(names):
    # code below
    n_likes = len(names)
    # assigning the length of the parameter names to the value n_likes
    if n_likes == 0: # using if and return statement to check for examples
        return "no one liked this" 
    elif n_likes == 1:
        return str(names[0]) + " likes this" # returning results using index of parameter
        #also using concatenation for string and results
    elif n_likes == 2:
        return str(names[0])  + " and "  + str(names[1]) + " like this"
    elif n_likes == 3:
        return str(names[0])+ ", " +  str(names[1]) + " and " + str(names[2]) + " like this"
    elif n_likes == 4:
        return str(names[0])+ ", " +  str(names[1]) + " and 2 others like this"
    else:
        #using the same pattern used in previous example but using length function & :-2 to get result for random examples
        return str(names[0]) + ", " +  str(names[1]) +  " and " + str(len(names [:-2])) +  " others like this"
        