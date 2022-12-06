user_input=int(input("type maximum nubmer: "))
summ=0
if (user_input >= 100):
    for i in range(100,user_input+1):
        if (i%2==0):
            summ+=1
            print(i)
    print("Liczb parzystych większych od 100 i mniejszych od ", user_input," jest ",summ)
else:
    print("wprowadź poprawną liczbę, większą od 100")
