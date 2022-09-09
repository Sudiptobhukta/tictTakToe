                                   # '''wE HAVEN'T SET RULES FOR THE WINNING SO THIS PROGRAM IS NOT COMPLETE'''
theBoard ={'TL': "TL",
'TM': 'TM',
'TR':'TR',
'ML':'ML',
'MM':'MM',
'MR':'MR',
'LL':"LL",
'LM':'LM',
'LR':'LRTR'}

def PrintBoard(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['LL'] + '|' + board['LM'] + '|' + board['LR'])

turn ='X'

for i in range(9):
    PrintBoard(theBoard)
    print('Turn for '+ turn + '. Move for which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn ='O'
    else:
        turn = 'X'

PrintBoard(theBoard)