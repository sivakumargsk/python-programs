
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
    print selection_sort ([6,5,7,2,9,8,3,4,1])
    print insertion_sort ([6,5,7,2,9,8,3,4,1])
    print insertion_sort1 ([6,5,7,2,9,8,3,4,1])
    print shell_sort ([6,5,7,2,9,8,3,4,1])
 
if __name__=='__main__' :
    main()    


