def print_rangoli(size):
    n=size
    #create a list that holds the alphabet
    alphabet = list(map(chr,range(97,123)))
    #making a lst for the middle line of the rangoli
    lst = alphabet[n-1:0:-1]+alphabet[0:n]
    #describing the width of the lst when joined by the character '-'
    width = len('-'.join(lst))

    #printing out the first n-1 lines
    for i in range(1, n):
        print('-'.join(alphabet[n - 1:n - i:-1] + alphabet[n - i:n]).center(width, '-'))
    #printing out the remainder n lines
    for i in range(n, 0, -1):
        print('-'.join(alphabet[n - 1:n - i:-1] + alphabet[n - i:n]).center(width, '-'))

print_rangoli(26)


