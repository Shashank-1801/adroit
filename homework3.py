value_mat = []
board_mat = []
n = 0
play_symbol = ".";
neutral = ".";
opponent = ".";

#MIN_MAX functions
def minmax(val_list, depth=0):
    if depth == 0:
        max_val(val_list);
    else:
        #not sure what to do here!!
        minmax(list, depth-1);

    print("TO-DO");


def min_val(val_list, depth):
    print("Will return the min value");


def max_val(val_list, depth):
    index = val_list.index()
    print("Will return the max value")


#Alpha-beta functions
def alphabeta():
    print("TO-DO");


def get_pos_value(pos):
    global opponent;
    global n;
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
    total_val = 0;
    print(neighbours)
    for s in neighbours:
        print(index_to_pos(s[0],s[1]), value_mat[s[0]][s[1]]);
        if(board_mat[s[0]][s[1]] == "." or board_mat[s[0]][s[1]] == opponent):
            total_val += value_mat[s[0]][s[1]];
    return total_val;


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


def pos_to_index(pos):
    p = list(pos);
    x = ord(p[0]) - ord("A");
    y = int(pos[1])-1;
    return x,y;


def index_to_pos(x, y):
    offset = ord("A");
    pos = str(chr(offset + x)) + str(y + 1);
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


read_input("input.txt");
pos = find_possible_moves();
vals = [];
for p in pos:
    print(p);
    vals.append(get_pos_value(p));
    ind = vals.index(max(vals));
    max_val = max(vals);
    print(max_val, " is the max value and at index ", ind, " out of ", len(vals), " positions");
    print();
print("Done!");