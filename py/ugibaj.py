import random
def pridobi_in_primerjaj(x):
    n=int(input())
    return n==x
def ugibanje(x):
    if pridobi_in_primerjaj(x):
        print("Bravo!")
    else:
        print("LoL")
        ugibanje(x)
ugibanje(random.randrange(1,10))
