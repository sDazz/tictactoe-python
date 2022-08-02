"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    counter_X = 0
    counter_O = 0

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == X:
                 counter_X += 1
            elif board[i][j] == O:
                counter_O += 1

    if counter_X == counter_O:
        return X
    else:
        return O



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                actions.add((i,j))

    return actions

def check_action(action):
    if type(action) != tuple:
        raise Exception("Invalid action: Not a tuple")
    elif type(action[0]) != int and type(action[1]) != int:
        raise Exception("Action values should be integers")
    elif action[0] >= 3 and action[1] >= 3:
        raise Exception("Action values greater than board!")
        
def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    check_action(action)
    result_board = copy.deepcopy(board)
    if player(board) == X:
        result_board[action[0]][action[1]] = X
    else:
        result_board[action[0]][action[1]] = O

    return result_board



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if terminal(board):

        if check_row(board)[0]:
            return check_row(board)[1]

        elif check_column(board)[0]:
            return check_column(board)[1]

        elif check_diagonal(board)[0]:
            return check_diagonal(board)[1]

        elif check_anti_diagonal(board)[0]:
            return check_anti_diagonal(board)[1]
         
        elif len(actions(board)) == 0:
            return None
    

def check_row(board):
    
    for i in range(len(board)):
        is_equal = True
        comparer = board[i][0]
        for j in range(len(board)):
            if board[i][j]  != comparer or board[i][j] == EMPTY:
                is_equal = False
                break
        if is_equal:
            return (True,comparer)
        
    return (False,None)

def check_column(board):

    comparer = None;
    for i in range(len(board)):
        is_equal = True
        comparer = board[0][i]
        for j in range(len(board)):
            if board[j][i]  != comparer or board[j][i] == EMPTY:
                is_equal = False
                break
        if is_equal:
            return (True,comparer)

    return (False,None)

def check_diagonal(board):

    comparer = board[0][0]
    for i in range(len(board)):
        if board[i][i]  != comparer or board[i][i] == EMPTY:
            return (False,None)
        
    return (True,comparer)

def check_anti_diagonal(board):

    n = len(board) - 1
    comparer = board[0][n]
    for i in range(len(board)):
        if board[i][n-i]  != comparer or board[i][n-i] == EMPTY:
            return (False,None)

    return (True,comparer)

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (len(actions(board)) == 0 or
       check_row(board)[0] or
       check_column(board)[0] or
       check_diagonal(board)[0] or
       check_anti_diagonal(board)[0]):
        return True
    
     
    return False
        



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if terminal(board):
        if winner(board) == X: return 1
         
        elif winner(board) == O: return -1
         
        elif winner(board) == None: return 0
    
    current_player = player(board)
    action_list = actions(board)
    utility_list = []

    #alpha-beta prunning    
    if current_player == X:
        find_value = 1
    else:
        find_value = -1

    for action in action_list:
        new_board = result(board,action)
        current_utility = utility(new_board)
        utility_list.append(current_utility)
        if find_value in utility_list:
            break

    if current_player == X:
        return max(utility_list)
    else:
        return min(utility_list)
    


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    Note that here I need to implement that tree.
    I'll try recursion
    """
    if terminal(board): return None
    
    action_dict = {}
    for action in actions(board):
        action_dict[action] = utility(result(board,action))

    if player(board) == X:
        return max(action_dict, key=action_dict.get) #type: ignore
    else:
        return min(action_dict, key=action_dict.get) #type: ignore
    
   
    




    

