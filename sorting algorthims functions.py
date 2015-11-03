
def selection_sort (a):
    for i in range (len (a)):
        mini = i
        for j in range (i, len(a)):
            if (a[j] < a[mini]):
                mini = j
        temp = a[i]
        a[i] = a[mini]
        a[mini]= temp
    return a

def insertion_sort (a):
    for i in range (len (a)):
        if (a[i] < a[i-1]):
            for j in range(i,0,-1):
               if ((j > 0) and (a[j] < a[j-1])):
                   temp = a[j]
                   a[j] = a[j-1]
                   a[j-1] = temp
    return a

def insertion_sort1 (a):
    for i in range (len(a)):
        j = i
        while ((j > 0) and (a[j] < a[j-1])):
            temp = a[j]
            a[j] = a[j-1]
            a[j-1] = temp
            j -= 1
    return a
        
def shell_sort (a):
    h = 1
    while (h < len(a)/3):
        h = (3 * h) + 1
    while (h >= 1):
        for i in range (h , len(a)):
            j = i
            while ((j >= h) and (a[j] < a[j-h])):
                temp = a[j]
                a[j] = a[j-h]
                a[j-h] = temp
                j -= h
        h = h/3
    return a

def main() :
    coll = [6,5,7,2,9,8,3,4,1]
    print selection_sort (coll)
    print insertion_sort (coll)
    print insertion_sort1 (coll)
    print shell_sort (coll)
 
if __name__=='__main__' :
    main()    

"""
Note:(N means list length)

worst-case for insertion sort is :
 if the list requires ~(N^2/2) comparisions and  ~(N^2/2) exchanges for sorting a list.
 example: Reverse ordered list.

Best-case for insertion sort is:
 if the list requires (N-1) camparisions and 0 exchanges for sorting a list.
 example: 1.Sorted list
          2.Partially sorted list
          3.if list is having less no.of inversion paires
          4.small list

when compared to selection sort the insertion sort take less time to sort a list.

shell sort takes very less time when compared to insertion sort depends upon type of list.
