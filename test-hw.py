import os
import hw_no_print

failed = []

for x in range(100):
    in_file = str(x)+".in"
    out_file = str(x)+".out"
    test_dir = "D:/git/adroit/testcases"
    code_dir = "D:/git/adroit"
    #create input file from in_file
    inp = open(test_dir + "/" +in_file, 'r')
    input_file = open(code_dir + "/input.txt", 'w')
    read_lines = inp.readlines()
    for line in read_lines:
        input_file.write(line)
    input_file.close()
    #run the python script
    try:
        hw_no_print.start_processing()

        #match output.txt to out_file
        command = "fc output.txt " + test_dir + "/" + out_file;
        if (os.system(command)!=0):
            #print("Test case failed for ", in_file, "and", out_file)
            failed.append(in_file)
    except:
        failed.append(in_file)

print(len(failed), "test cases failed")
for x in failed:
    print(x)

