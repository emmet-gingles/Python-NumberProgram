
# function to allow user to input numbers and calculate the smallest and largest 
def calcSmallestAndLargest():
    # default values for variables that will store the smallest and largest numbers respectively
    smallest = None
    largest = None     
    # counters for smallest and largest numbers
    countSmallest = 0
    countLargest = 0
    print 'Enter a list of numbers'
    print 'Type 0 when finished'
    # loop will continue unless specified to exit 
    while True:
        # string input 
        s_num = raw_input('Enter a number: ')        
        # if 0 is typed, exit the loop
        if s_num == '0':
            break 
            print 'Goodbye'
        # check that a valid integer has been entered. If not continue looping
        try:
            num = int(s_num)            
            # if smallest is set to default value or number is less than smallest, then set 
            # smallest to number and set count to 1 
            if smallest is None or num < smallest:
                smallest = num 
                countSmallest = 1
            # if number is equal to smallest, then increment count 
            elif num == smallest:
                countSmallest = countSmallest + 1
            # if largest is set to default value or number is greater than largest, then set 
            # largest to number and set count to 1
            elif largest is None or num > largest:
                largest = num 
                countLargest = 1
            # if number is equal to largest, then increment count 
            elif num == largest:
                countLargest = countLargest + 1
        except: 
            print 'Please enter a valid integer'
    # now out of loop - print variables         
    print 'Largest Number Entered: %d ' % largest
    print 'Occurrence of largest number: %d ' % countLargest
    print 'Smallest Number Entered: %d ' % smallest
    print 'Occurrence of smallest number: %d ' % countSmallest

# call function
calcSmallestAndLargest()    