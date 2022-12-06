user_input=int(input("type maximum nubmer: "))
if (user_input >= 100):
    for i in range(100,user_input+1):
        if (i%2==0):
            print(i)
else:
    print("wprowadź poprawną liczbę, większą od 100")