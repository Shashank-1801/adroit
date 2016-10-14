import time
import math

pos_inf = float("inf")
neg_inf = float("inf")
value_mat = []
board_mat = []
n = 0
depth = 0
mode = ""   #will get updated
play_symbol = ".";  #will get changed
opponent = ".";     #will get changed
neutral = ".";
steps = 0

#MIN_MAX functions
def minimax(board_state, depth):
    #let's start the recursion for the moves ;)
    best_move, val = maxi(board_state, depth-1)
    return best_move

def maxi(board_state, depth):
    global steps
    print("In maxi with depth ", depth)
    poss_moves = find_possible_moves(board_state, play_symbol)
    my_board = duplicate_board_state(board_state)
    vals=[]
    new_board_states = []
    for move in poss_moves:
        new_board = update_board(move, my_board, play_symbol);
        vals.append(get_game_val(new_board))
        new_board_states.append(update_board(move, my_board, play_symbol))
    print(poss_moves)
    print(vals)
    ret_vals = []
    ret_moves = []
    if (depth==0):
        steps +=1
        return poss_moves[vals.index(max(vals))], max(vals)
    else:
        for n_board in new_board_states:
            print_board_state(n_board)
            ret_move, move_val = (mini(n_board, depth-1))
            ret_vals.append(move_val);
            ret_moves.append(poss_moves[new_board_states.index(n_board)]);
        print("max among ", ret_moves)
        print("max among ", ret_vals)
        return poss_moves[ret_vals.index(max(ret_vals))], max(ret_vals)


def mini(board_state, depth):
    global  steps
    print("In mini with depth ", depth)
    poss_moves = find_possible_moves(board_state, opponent)
    my_board = duplicate_board_state(board_state)
    vals = []
    new_board_states = []
    for move in poss_moves:
        new_board = update_board(move, my_board, opponent);
        vals.append(get_game_val(new_board))
        new_board_states.append(update_board(move, my_board, opponent))
    print(poss_moves)
    print(vals)
    ret_vals = []
    ret_moves = []
    if (depth == 0):
        steps += 1
        return (poss_moves[vals.index(min(vals))], min(vals))
    else:
        for n_board in new_board_states:
            print_board_state(n_board)
            ret_move, move_val = (maxi(n_board, depth - 1))
            ret_vals.append(move_val);
            ret_moves.append(poss_moves[new_board_states.index(n_board)]);
        print("min among ", ret_moves)
        print("min among ", ret_vals)
        return poss_moves[ret_vals.index(min(ret_vals))], min(ret_vals)


#Alpha-beta functions
def alphabeta(board_state, depth):
    alpha = neg_inf
    beta = pos_inf
    best_move, val = alpha_max(board_state, depth - 1, alpha, beta)
    return best_move



def alpha_max(board_state, depth, alpha, beta):
    global steps
    print("In maxi with depth ", depth)
    alpha = alpha
    beta = beta
    #only aplha will be updated in alpha_max function
    poss_moves = find_possible_moves(board_state, play_symbol)
    my_board = duplicate_board_state(board_state)
    vals=[]
    new_board_states = []
    for move in poss_moves:
        new_board = update_board(move, my_board, play_symbol);
        vals.append(get_game_val(new_board))
        new_board_states.append(update_board(move, my_board, play_symbol))
    print(poss_moves)
    print(vals)
    ret_vals = []
    ret_moves = []
    if (depth==0):
        steps +=1
        return poss_moves[vals.index(max(vals))], max(vals), alpha, beta
    else:
        for n_board in new_board_states:
            print_board_state(n_board)
            ret_move, move_val = alpha_min(n_board, depth-1, alpha, beta)

            alpha = max(alpha, max(vals))
            if alpha > beta:
                return poss_moves[ret_vals.index(max(ret_vals))], max(ret_vals)

            ret_vals.append(move_val);
            ret_moves.append(poss_moves[new_board_states.index(n_board)]);
        print("max among ", ret_moves)
        print("max among ", ret_vals)
        return poss_moves[ret_vals.index(max(ret_vals))], max(ret_vals)


def alpha_min(board_state, depth, alpha, beta):
    global  steps
    print("In mini with depth ", depth)
    alpha = alpha
    beta = beta
    # only beta will be updated in alpha_min function
    poss_moves = find_possible_moves(board_state, opponent)
    my_board = duplicate_board_state(board_state)
    vals = []
    new_board_states = []
    for move in poss_moves:
        new_board = update_board(move, my_board, opponent);
        vals.append(get_game_val(new_board))
        new_board_states.append(update_board(move, my_board, opponent))
    print(poss_moves)
    print(vals)
    ret_vals = []
    ret_moves = []
    if (depth == 0):
        steps +=1
        return poss_moves[vals.index(min(vals))], min(vals)
    else:
        for n_board in new_board_states:
            print_board_state(n_board)
            ret_move, move_val = alpha_max(n_board, depth - 1, alpha, beta)

            beta = min(alpha, min(vals))
            if alpha > beta:
                return poss_moves[ret_vals.index(max(ret_vals))], max(ret_vals)

            ret_vals.append(move_val);
            ret_moves.append(poss_moves[new_board_states.index(n_board)]);
        print("min among ", ret_moves)
        print("min among ", ret_vals)
        return poss_moves[ret_vals.index(min(ret_vals))], min(ret_vals)


def duplicate_board_state(board_state):
    new_board = [[None]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            new_board[x][y] = board_state[x][y]
    return new_board

def get_val_list(pos_list):
    vals_for_pos_list = [];
    for move in pos_list:
        vals_for_pos_list.append(get_pos_value(move));
    return vals_for_pos_list;

def get_pos_value(pos):
    global opponent;
    global n;
    x,y = pos_to_index(pos);
    total_val = value_mat[x][y];
    neighbours = get_neighbours(pos);
    for s in neighbours:
        #print(index_to_pos(s[0],s[1]), value_mat[s[0]][s[1]]);
        if(board_mat[s[0]][s[1]] == opponent):
            total_val += value_mat[s[0]][s[1]];
    return total_val;


def get_game_val(board_state):
    # value of player - value of opponent
    global play_symbol
    global opponent
    player_val = 0
    opponent_val = 0
    for x in range(n):
        for y in range(n):
            if board_state[x][y] == play_symbol:
                player_val += value_mat[x][y];
            elif board_state[x][y] == opponent:
                opponent_val += value_mat[x][y]
    return player_val-opponent_val


def get_neighbours(pos):
    x, y = pos_to_index(pos);
    neighbours = [];
    if x + 1 < n:
        neighbours.append([x + 1, y]);
    if y + 1 < n:
        neighbours.append([x, y + 1]);
    if x - 1 >= 0:
        neighbours.append([x - 1, y]);
    if y - 1 >= 0:
        neighbours.append([x, y - 1]);
    return neighbours;


#finds the possible places for next move
def find_possible_moves(board_state, player_symbol):
    global play_symbol;
    global n;
    next_possible_moves = [];
    print("player will play as " + player_symbol);
    for x in range(n):
        for y in range(n):
            if board_state[x][y]==".":
                next_possible_moves.append(index_to_pos(x,y));
    return next_possible_moves;


def pos_to_index(pos):      #C2 => x=1, y=2
    p = list(pos);
    y = ord(p[0]) - ord("A");
    x = int(pos[1])-1;
    return x,y;


def index_to_pos(x, y):     #x=1 => 2  , y=2 => C
    offset = ord("A");
    pos = str(chr(offset + y)) + str(x + 1);
    return pos;


#sets the values in the board
def analyse(lines):
    global n;
    global mode;
    global depth;
    global play_symbol;
    global opponent;
    global board_mat;
    global value_mat;
    """
    <N>
    <MODE>
    <YOUPLAY>
    <DEPTH>
    <… CELL VALUES …>
    <… BOARD STATE …>
    """
    num_lines = len(lines);
    n = int(lines[0]);
    print("Size of board is ", n, "x", n );
    mode = str(lines[1]).strip("\n");
    print("Mode of game play is ", mode);
    play_symbol = str(lines[2]).strip("\n");
    print("Playing as " , play_symbol);
    if(play_symbol=="X"):
        opponent = "O";
    else:
        opponent = "X";
    depth = int(str(lines[3]).strip("\n"))
    print("depth of search is ", depth);
    #print("Cell values are: ");
    value_mat = [[None]*n for _ in range(n)];
    for i in range(n):
        vals = lines[4+i].split(" ");
        for j in range(n):
            value_mat[i][j] = int(vals[j]);
            #print(value_mat[i][j] , end="\t");
        #print();

    #print("Board state is: ");
    board_mat = [[None]*n for _ in range(n)];
    for i in range(n):
        vals = list(lines[4 + n + i]);
        for j in range(n):
            board_mat[i][j] = str(vals[j]).strip("\n");
            #print(board_mat[i][j], end="\t");
        #print();


def get_board_value():
    global n;
    global value_mat;
    for i in range(n):
        for j in range(n):
            print(value_mat[i][j], end="\t");
        print();


def print_board_state(board_state):
    global n;
    for i in range(n):
        for j in range(n):
            print(board_state[i][j], end="\t");
        print();


def read_input(file):
    fread = open(file,'r');
    read_line = fread.readlines();
    try:
        analyse(read_line);
        print_board_state(board_mat);
        get_board_value();
    except:
        print("***Invalid file stucture");
        print(read_line)


def update_board(move, board_state, player_symbol):
    new_state = duplicate_board_state(board_state)
    if(player_symbol == play_symbol):
        other = opponent
    elif player_symbol == opponent:
        other = play_symbol
    x,y = pos_to_index(move);
    new_state[x][y] = player_symbol;
    neighbours = get_neighbours(move);
    raid = False
    for s in neighbours:
        if new_state[s[0]][s[1]] == player_symbol:
            raid = True
            break;
    if raid == True:
        for s in neighbours:
            # print(index_to_pos(s[0],s[1]), value_mat[s[0]][s[1]]);
            if (new_state[s[0]][s[1]] == other):
                new_state[s[0]][s[1]] = player_symbol;
    return new_state;


def is_raid(move, board):
    neighbours = get_neighbours(move);
    raid = False
    is_raid_possible = False
    for s in neighbours:
        if board[s[0]][s[1]] == play_symbol:
            is_raid_possible = True
            break;
    if is_raid_possible:
        for s in neighbours:
            if board[s[0]][s[1]] == opponent:
                raid = True
                break
    return raid


def file_output(move, board_state):
    global n;
    if is_raid(move, board_state):
        type = "Raid"
    else:
        type = "Stake"
    bs = update_board(best_move, board_mat, play_symbol)
    fwrite = open("output.txt",'w')
    line = move + " "+ type + "\n"
    fwrite.write(line)
    for i in range(n):
        line = ""
        for j in range(n):
            line += bs[i][j]
        fwrite.write(line + "\n")
    fwrite.close()


#start of main method
start_time = time.time()
read_input("input.txt");
print()
if mode == "MINMAX":
    best_move = minimax(board_mat, depth)
elif mode == "ALPHABETA":
    best_move = alphabeta(board_mat, depth)
else:
    print("we shouldn't be here, incorrect mode")
print("Best move is ", best_move)
print_board_state(update_board(best_move, board_mat, play_symbol))
file_output(best_move,board_mat )
end_time = time.time()
print("Done! time taken " , end_time - start_time, " after steps :", steps);