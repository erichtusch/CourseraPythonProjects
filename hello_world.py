__author__ = 'DaffnerLab2'

string1 = "hello"
string2 = "world"
print string1 + string2

numbers = [1, 3, 5, 6, 8]
print numbers

j = 3
if j in numbers:
    print "numbers = ", numbers
    print "j is index %d in numbers" % numbers.index(j)
print
i = 0
while i < len(numbers):
    if i in numbers:
        print str(i) + " is in numbers at index " + str(numbers.index(i))
    else:
        print "%d not in numbers :)" % i
    i += 1

