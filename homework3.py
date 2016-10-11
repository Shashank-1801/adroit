value_mat = []
board_mat = []
n = 0
play_symbol = ".";  #will get changed
opponent = ".";     #will get changed
neutral = ".";

#MIN_MAX functions
def minmax(move_list, depth, board_state):
    #get the possible moves that can be made
    #for each of these move calculate the value
    #find the max among these values
    max_val(move_list, depth, board_state)

    print("TO-DO");


def min_val(move_list, depth):
    #return the min of all the values given
    print("Will return the min value");


def max_val(move_list, depth, board_state):
    #return the max of the values given
    index = move_list.index()
    print("Will return the max value")


#Alpha-beta functions
def alphabeta():
    print("TO-DO");

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
def find_possible_moves():
    global play_symbol;
    global n;
    next_possible_moves = [];
    print("player will play as " + play_symbol);
    for x in range(n):
        for y in range(n):
            if board_mat[x][y]==".":
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
    depth = str(lines[3]).strip("\n");
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
    board_mat = [[None]*5 for _ in range(n)];
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


def get_board_state():
    global n;
    global board_mat;
    for i in range(n):
        for j in range(n):
            print(board_mat[i][j], end="\t");
        print();


def read_input(file):
    fread = open(file,'r');
    read_line = fread.readlines();
    try:
        analyse(read_line);
        get_board_state();
        get_board_value();
    except:
        print("***Invalid file stucture");
    line = "add something here\n";
    for oneline in read_line:
        line += oneline;
    fwrt = open("output.txt", 'w');
    fwrt.write(line);

def update_board(best_move, board_state):
    x,y = pos_to_index(best_move);
    board_mat[x][y] = play_symbol;
    neighbours = get_neighbours(best_move);
    for s in neighbours:
        # print(index_to_pos(s[0],s[1]), value_mat[s[0]][s[1]]);
        if (board_mat[s[0]][s[1]] == opponent):
            board_mat[s[0]][s[1]] = play_symbol;



#start of main method
read_input("input.txt");
possible_moves = find_possible_moves();
best_move = minmax(possible_moves);
print("best move is " , best_move);
print(get_pos_value(best_move));
update_board(best_move);
get_board_state();
"""
vals = [];
for p in possible_moves:
    print(p);
    vals.append(get_pos_value(p));
    ind = vals.index(max(vals));
    max_val = max(vals);
    print(max_val, " is the max value and at index ", ind, " out of ", len(vals), " positions");
    print();
"""
print("Done!");