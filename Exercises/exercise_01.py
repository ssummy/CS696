"""
Exercise 1
Place this script inside a new folder in your github repository called "Exercises".
This will be the directory for all of your in-class exercises this semester.

By the end of class on Thursday 1/25, students should have:
    - Created a private github repo for this class
    - Added their information to this sheet:
        https://docs.google.com/spreadsheets/d/1EKNYOqTnxelmBT4jqotRbUer5eVvWYM9RloN5doScyo/edit?usp=sharing
    - Added my github account (kylelevi) as a collaborator for their private repository
    - Completed these definitions and pushed this script to a folder called "Exercises" in their repo

"""

def hello():
    """
    Prints "Hello World"
    :return: None
    """
    print("Hello World")
    return

def percent_decimal(i):
    """
    Converts a percentage to a decimal or a decimal to a percentage depending on the input i
    :param i: a float between 0 and 100
    :return: a float between 0 and 100
    """
    ret = 0
    if(i > 1):
        ret = i/100.0
    else:
        ret = i*100.0
    return ret


k = percent_decimal(.99)
kk = percent_decimal(98)

def exponent(integer, power):
    """
    Using a loop (no imports!), raise the integer given to the power provided. (integer^power)
    :param integer: a positive, non zero, integer
    :param power: a positive, non zero, integer
    :return: an integer
    """
    ret = 1
    for i in range(power):
        ret = ret * integer
    return ret#(integer ** power)

ans = exponent(2, 3)
ans2 = exponent(5, 3)

def complement(dna):
    """
    Returns the complement strand of DNA to the input.  C <--> G,  A <--> T
    :param dna: String containing only C, T, A, and G
    :return: String containing only C, T, A, and G
    """
    map = {'C': 'G', 'A': 'T', 'G':'C', 'T':'A'}
    ret = [map[amino] for amino in dna]
    return ret
ans3 = complement("CGAT")
k=0