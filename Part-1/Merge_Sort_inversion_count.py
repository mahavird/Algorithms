########################<<<<<<<This is a program to sort the elements in an array,using merge sort.>>>>>#########
##<<<<<<<<<<<<<<<<<Created_by: Mahavir Dwivedi ,mahaviredx@gmail.com >>>>>>>>>>>>>######################
#############<<<<<<<<<<<<<<<Based on Divide and Conquer Technique>>>>>>>>>>#########################################


def mergeSort(alist):
    global l
    global count
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        #print "mid", mid
        lefthalf = alist[:mid]
        #print len(lefthalf)
        righthalf = alist[mid:]
        print "lefthalf", lefthalf
        print "righthalf",righthalf

        mergeSort(lefthalf)

        mergeSort(righthalf)


        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1

            else:
                alist[k]=righthalf[j]
                j=j+1
                print "Count"
                print "left_half",lefthalf[i]
                print "right_half", righthalf[j-1]

                count = count + len(lefthalf)-i
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

alist = [9,8,7,6,5,4,3,2,1,0]
print(alist)
count=0
mergeSort(alist)

print(alist)
print count