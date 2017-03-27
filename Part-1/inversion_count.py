########################<<<<<<<This is a program to count the number of inversions present in the list.>>>>>#########
##<<<<<<<<<<<<<<<<<Created_by: Mahavir Dwivedi ,mahaviredx@gmail.com >>>>>>>>>>>>>######################
#############<<<<<<<<<<<<<<<Based on Divide and Conquer Technique>>>>>>>>>>#########################################

def inversion_recurse(alist):
    global count
    print("Counting ",alist)
    if len(alist)>1:
        mid = len(alist)//2

        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        print "lefthalf", lefthalf
        print "righthalf",righthalf

        inversion_recurse(lefthalf)
        inversion_recurse(righthalf)

        count_inversion(lefthalf, righthalf)

    else:
        print "Alist_Inversion_Count_in _progress"


def count_inversion(lefthalf,righthalf):
    i = 0
    j = 0
    global count
    print "Inside Counting function",lefthalf, righthalf

    while (i < len(lefthalf) and j < len(righthalf)):
        if lefthalf[i] < righthalf[j]:
            count = count
            print "i,j", i, j
            print "left:",lefthalf[i], 'is less than right: ', righthalf[j]
            print "count", count
            j = j + 1

        else:
            count = count + 1
            print "i,j", i, j
            print "left:",lefthalf[i], 'is greater than right: ', righthalf[j]
            print "count", count
            j = j + 1

        if (j == len(righthalf)):
            count = count
            i = i + 1
            j = 0
            #print "i,j reboot", i, j
            #print "count", count





alist = [1,3,5,2,4,6,0]
print(alist)
count = 0
inversion_recurse(alist)
print(alist)
print "Final_Count", count
