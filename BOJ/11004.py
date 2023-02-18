n, k = map(int, input().split())
a = list(map(int, input().split()))

def quicksort(s, e, k):
    global a
    if s < e:
        pivot = partions(s, e)
        if pivot == k:
            return
        elif k < pivot:
            quicksort(s, pivot -1, k)
        else: 
            quicksort(pivot+1, e, k)

def swap(i, j):
    global a
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def partions(s, e):
    global a

    if s+1 == e: 
        if a[s] > a[e]:
            swap(s,e)
        return e

    m = (s+e)//2
    swap(s, m)
    pivot = a[s]
    i = s+1
    j = e

    while i<=j:
        while pivot < a[j] and j>0:
            j-=1
        while pivot > a[i] and i< len(a)-1:
            i +=1
        if i<=j:
            swap(i, j)
            i += 1
            j -= 1
    a[s] = a[j]
    a[j] = pivot
    return j

quicksort(0, n-1, k-1)
print(a[k-1])

