value_mat = []
board_mat = []
n = 0
def minmax():
    print("TO-DO");

def alphabeta():
    print("TO-DO");

def analyse(lines):
    global n;
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
    depth = str(lines[3]).strip("\n");
    print("depth of search is ", depth);
    #print("Cell values are: ");
    value_mat = [[None]*5 for _ in range(n)];
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
    analyse(read_line);
    get_board_state();
    get_board_value();
    line = "add something here\n";
    for oneline in read_line:
        line += oneline;
    fwrt = open("output.txt", 'w');
    fwrt.write(line);


read_input("input.txt");
print("Done!");