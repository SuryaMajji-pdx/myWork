from queue import Queue
import display

def main():
    filename = input("enter the filename: ")
    debug = int(input("do you want to debug your statements: "))
    counter = 0
    inst_queue = Queue(maxsize=16)
    counter_array = Queue(maxsize=16)
    print(inst_queue.qsize())
    display.display(filename, debug)
    #file = open(filename)
    time = 0
    # read the content of the file opened
    #print(type(file))
    #while
    if(inst_queue.qsize()<16):
            with open(filename, 'r') as f:
                print(type(f))
                for line in f:
                    display.display(line, debug)

    counter += 1

main ()