#!/usr/bin/env python
import sys

# main: this is the main function of this Python
#
def main(argv):

    floor = 0;

    # Define the input file name from which to read the parentheses
    filename="day1star1.txt"

    # Try to open the file and read each character until the end of file.
    # If the read character is '(', increment the floor on which Santa is.
    # If the read character is ')', decrement the floor on which Santa is.
    # If the try fails, print out a warning to the user.
    try:
        with open(filename) as f:
            while True:
                c = f.read(1)
                if not c:
                    print "End of file"
                    break
                else:
                    if (c == '('):
                        floor += 1
                    elif(c == ')'):
                        floor -= 1
                        
        # Print out the final floor
        print ("Santa ends up on floor %d" %(floor))

    except IOError:
        print("ERROR >> Missing file day1star1.txt")

# begin gracefully
#
if __name__ == "__main__":
    main(sys.argv[0:])

#
# end of file

                        
                
                
