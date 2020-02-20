import random

def bubble_sort(arr):
    n = len(arr)
    s={"♠":0,"♥":1,"♦":2,"♣":3}
    f={"A":1,"J":11,"Q":12,"K":13}
    
    for i in range(n):
        for j in range(0, n-i-1):
            a = arr[j]
            b = arr[j+1]

            aface  = a[0:len(a)-1];
            asuit  = a[len(a)-1];
            avalue = f[aface] if aface in f else int(aface)

            bface  = b[0:len(b)-1];
            bsuit  = b[len(b)-1];
            bvalue = f[bface] if bface in f else int(bface)

            if (asuit > bsuit or (asuit == bsuit and avalue > bvalue)):
                arr[j], arr[j+1] = arr[j+1], arr[j]

def shuffle(arr):
    n = len(arr)
    for i in range(n-1,0,-1): 
        j = random.randint(0,i+1) 
        arr[i],arr[j] = arr[j],arr[i]

def deal():
    d=[]
    s=["♠","♥","♦","♣"]
    f={1:"A",11:"J",12:"Q",13:"K"}
    for i in range(4):
        for j in range(1,14):
            d.append(f"{f[j] if j in f else j}{s[i]}")
    return d

###

cards = deal()
print("Before shuffle: ")
print(cards)

shuffle(cards)
print("After shuffle: ")
print(cards)

bubble_sort(cards)
print("After sort: ")
print(cards)
# Python program for implementation of Bubble Sort
 
def bubbleSort(arr):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
 
# Driver code to test above
arr1 = [64, 34, 25, 12, 22, 11, 90]
arr2 = [64, 34, 25, 12, 22, 11]
arr3 = [-64, 34, 25]
arr4 = []
 
bubbleSort(arr1)
bubbleSort(arr2)
bubbleSort(arr3)
bubbleSort(arr4)
 
print ("Sorted array1 is:")
print(arr1)

print ("Sorted array2 is:")
print(arr2)

print ("Sorted array3 is:")
print(arr3)

print ("Sorted array4 is:")
print(arr4)

cards = ['5♣', '8♠', '4♠', '9♣', 'K♣', '6♣', '5♥', '3♣', '8♥', 'A♥', 'K♥', 'K♦', '10♣', 'Q♣', '7♦', 'Q♦', 'K♠', 'Q♠', 'J♣', '5♦', '9♥', '6♦', '2♣', '7♠', '10♠', '5♠', '4♣', '8♣', '9♠', '6♥', '9♦', '3♥', '3♠', '6♠', '2♥', '10♦', '10♥', 'A♠', 'A♣', 'J♥', '7♣', '4♥', '2♦', '3♦', '2♠', 'Q♥', 'A♦', '7♥', '8♦', 'J♠', 'J♦', '4♦']
bubbleSort(cards)
print("Sorted cards:" )
print(cards)
