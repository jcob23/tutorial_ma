def summ(x,y):
    return(x+y)
def dif(x,y):
    return(x-y)
while True:
    user_input=input('1 - Dodawanie, 2 - odejmowanie, 3- wyjście z kalkulatora: ')
    if user_input == '1':
        a=int(input('Wpisz pierwsza liczbe: '))
        b=int(input('Wpisz drugą liczbe: '))
        print(a,'+',b,'=',summ(a,b) )
        continue
    elif user_input == '2':
        a=int(input('Wpisz pierwsza liczbe: '))
        b=int(input('Wpisz drugą liczbe: '))
        print(a,'-',b,'=',dif(a,b))
        continue
    elif user_input == '3':
        break
    else:
        print('wprowadź 1 lub 2 lub 3')
        continue
         