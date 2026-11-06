seznam=[12,5,8,21,3,16,9,14]
def vsota(seznam):
    vsota=0
    for i in seznam:
        vsota+=i
    print(vsota)
vsota(seznam)


def povprecna(seznam):
    povp=0
    for i in seznam:
        povp+=i
    print(povp/len(seznam))
povprecna(seznam)

def najvec(seznam):
    naj=seznam[0]
    for i in seznam:
        if (i>naj):
            naj=i
    print(naj)
najvec(seznam)

def najmanj(seznam):
    najmanjse=seznam[0]
    for i in seznam:
        if(i<najmanjse):
            najmanjse=i
    print(najmanjse)
najmanj(seznam)

def soda(seznam):
    sod=0
    for i in seznam:
        if(i%2==0):
            sod+=1
    print(sod)
soda(seznam)

def liha(seznam):
    lih=0
    for i in seznam:
        if(i%2==1):
            lih+=1
    print(lih)
liha(seznam)

def vecja(seznam):
    for i in seznam:
        if (i>10):
            print(i)
vecja(seznam)



def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
urejen_seznam = bubble_sort(seznam.copy())
print(urejen_seznam)