########################<<<<<<<This is a program to sort the elements in an array,using merge sort.>>>>>#########
##<<<<<<<<<<<<<<<<<Created_by: Mahavir Dwivedi ,mahaviredx@gmail.com >>>>>>>>>>>>>######################
#############<<<<<<<<<<<<<<<Based on Divide and Conquer Technique>>>>>>>>>>#########################################


def mergeSort(alist):
    global l
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

alist = [54,26,93,17]
print(alist)

mergeSort(alist)

print(alist)