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