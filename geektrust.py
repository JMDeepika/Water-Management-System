from sys import argv
from src import GeekHeights

def main():
    """
    Sample code to read inputs from the file

    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    Lines = f.readlines()
    //Add your code here to process the input commands
    
    if len(argv) != 2:
        raise Exception("Filepath not entered")
    """
    #file_path = 'sample_input/input4.txt'
    file_path = argv[1]
    with open(file_path,'r') as input_:
        file_data = input_.readlines()
    for i in range(len(file_data)):
        file_data[i] = file_data[i].split()
    a = GeekHeights.Geekheights(file_data)
    output = [a.total_water_consumption(), a.total_bill()]
    print(output[0], output[1])

if __name__ == "__main__":
    main()
