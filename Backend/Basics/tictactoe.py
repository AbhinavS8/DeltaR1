#tictactoe
inp = int(input('enter grid size: '))

for i in range(0,2*(inp)-1):
    if i%2==0:
        print('',' | '*(inp-1))
    else:
        print('-- '*inp)
