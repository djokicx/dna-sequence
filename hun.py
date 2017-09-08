# Student Name: Dejan Djokic
# Mentor: Patricia Francis-Lyon
# Subject: Introduction to Computer Science 110
# Date: 9/30/2013

# The program is meant for medical field
# It analyzes the DNA of the patient and analyzes whether a patient has a posibility of being diagnosed with Huntington's disease
# By analyzing the DNA, the program counts the repeats of CAG's [HTT gene sequence]
# Based on the repeats, it determinates the classification and disease status


# Function List

# Function get_input allows user to input his first name, last name and DNA code.
# It prints it out and returns DNA code to the main program.

def get_input():
    firstname = raw_input ("Enter first name of patient:  ")
    lastname = raw_input ("Enter last name of patient:  ")
    dna = raw_input ("Enter DNA of patient:  ")
    return firstname, lastname, dna


# Function counts CAG's in the DNA sequence. Comes with testing.

def countCAG(dna):
    """
    >>> countCAG("C")
    0
    >>> countCAG("CAGCA")
    1
    >>> countCAG("CAGCATCAGCAGCAG")
    1
    >>> 
    countCAG("CAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAG
    CAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCA
    GCAGCAGCAGCAGCA")
    41
    >>> countCAG("CAGCAGCAGCAG")
    4
    >>> countCAG("CAGCAGCA")
    2
    >>> countCAG("CAGCAGCATCAGCAGCAGCACACACACACACACACAG")
    2
    >>> 
    countCAG("CAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAG
    CAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCA
    GCAGCAGCAGCAGCA")
    35
    >>> countCAG("CACCACCAG")
    0
    >>> countCAG("CAGCAGCAGCA")
    3
    >>> countCAG("CATCATCAGCAGCAG")
    0
    >>> 
    countCAG("CAGCAGCAGCAGCAGCAG
    CAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCA
    GCAGCAGCAGCAGCA")
    30
    """
    index = 0
    lastindex = 3
    count = 0
    while lastindex <= len(dna):
        if dna[index : lastindex] == 'CAG':
            count += 1
        else:
           break
        index += 3
        lastindex += 3
    return count

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Function predicts the the classification and disease status based on the number of CAG counts. Comes with testing.

def prediction(numCAG):
    """
    >>> prediction(27)
    ('Normal', 'Unaffected')
    >>> prediction(35)
    ('Intermediate', 'Unaffected')
    >>> prediction(42)
    ('Reduced Penetrance', 'Somewhat Affected')
    >>> prediction(45)
    ('Full Penetrance', 'Affected')
    >>> prediction(13)
    ('Normal', 'Unaffected')
    >>> prediction(28)
    ('Intermediate', 'Unaffected')
    >>> prediction(40)
    ('Reduced Penetrance', 'Somewhat Affected')
    >>> prediction(50)
    ('Full Penetrance', 'Affected')
    >>> prediction(20)
    ('Normal', 'Unaffected')
    >>> prediction(36)
    ('Intermediate', 'Unaffected')
    >>> prediction(38)
    ('Reduced Penetrance', 'Somewhat Affected')
    >>> prediction(43)
    ('Full Penetrance', 'Affected')
    >>> prediction(22)
    ('Normal', 'Unaffected')
    >>> prediction(30)
    ('Intermediate', 'Unaffected')
    >>> prediction(37)
    ('Reduced Penetrance', 'Somewhat Affected')
    >>> prediction(100)
    ('Full Penetrance', 'Affected')
    """
    if numCAG < 28:
        return ('Normal', 'Unaffected')
    elif numCAG >= 28 and numCAG < 37:
        return ('Intermediate', 'Unaffected')
    elif numCAG >= 37 and numCAG <=42:
        return ('Reduced Penetrance', 'Somewhat Affected')
    elif numCAG > 42:
        return ('Full Penetrance', 'Affected')
    else:
        return "Invalid DNA Code"

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Main Program Body
    
firstname, lastname, dna=get_input() 
c=countCAG(dna)                      
p=prediction(c)                      

print firstname, lastname, dna, c, p



