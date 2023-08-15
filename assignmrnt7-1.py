def welcome():
    n=int(input('enter your n:'))
    m=int(input('enter your m:'))
    for i in range(1,n+1):
       for j in range(1,m+1):
        print (str(i*j).rjust(4,' '),end=' ')
       print('\n')
welcome()