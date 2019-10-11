from django.shortcuts import render
from random import sample
from django.contrib.auth.decorators import login_required
import random


def index(request):
    return render(request,"pages/index.html",{})


def create_sudoku_board(base=3):
    side  = base*base
    nums  = sample(range(1,side+1),side) # random numbers
    board = [[nums[(base*(r%base)+r//base+c)%side] for c in range(side) ] for r in range(side)]
    sudoku_id = random.randint(1000,99999)
    # Create your views here.
    return board,sudoku_id

# def conf(request):
#     return render(request,'game/basic.html',{})


def show_board(s_board, level='1'):

    # nums=[0]*9
    nums = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    index = 0
    print(level)
    while index < len(s_board):
        if level=='0':
            r= 3
        elif level == '1':
            r = random.randint(3,6)
        else:
            r= random.randint(5,7)

        zeros = sample(range(9),r)
        for i in zeros:
            nums[str(s_board[index][i])]+=1
            s_board[index][i]=0

        index = index+1

    return nums


# @login_required
def play_sudoku(request, level=1):
    board,id = create_sudoku_board()
    level_choice = {'0':"Easy",'1':"Normal",'2':"Hard"}
    c_board = [[0]*len(board)]*len(board)
    i = 0

    for line in board:
        c_board[i] = line.copy()
        i=i+1

    s = show_board(c_board, level)
    context_dict = {'sudoku_board':c_board,'main_board':board,'nums':zip(s,s.values()),'level':level_choice[level],'lev':level,'id':id}
    return render(request,'sudoku/play_sudoku.html',context=context_dict)
from django.shortcuts import render

# Create your views here.
