#!/usr/bin/env python
import sys

# main: this is the main function of this Python
#
def main(argv):

    # Define the input file name from which to read the directions
    filename="day3star1.txt"
    
    # Try to open the file and read each line. 
    try:
        with open(filename) as f:

            row = 0    # Santa coordinates
            col = 0

            roborow = 0    # Robo-Santa coordinates
            robocol = 0
            
            coord = set()    # Empty set of house coordinates
            
            coord.add((row,col))    # Add the original location tuple
            
            # Read in 1 byte at a time
            while True:

                # Read Santa's move ----------
                c = f.read(1)

                # End case
                if not c:
                    print "End of file"
                    break
                
                # Fun case
                else:
                    if (c == '^'):
                        row -= 1
                    elif (c == '>'):
                        col += 1
                    elif(c == 'v'):
                        row += 1
                    elif(c == '<'):
                        col -= 1

                    coord.add((row,col))    # Add the new location tuple

                # Read Robo-Santa's move ----------
                roboc = f.read(1)

                # End case
                if not roboc:
                    print "End of file"
                    break
                
                # Fun case
                else:
                    if (roboc == '^'):
                        roborow -= 1
                    elif (roboc == '>'):
                        robocol += 1
                    elif(roboc == 'v'):
                        roborow += 1
                    elif(roboc == '<'):
                        robocol -= 1

                    coord.add((roborow,robocol))    # Add the new location tuple
                    

            numberOfHouses = len(coord)
            
            print("Santa delivered at least one present to %d houses!" %(numberOfHouses))
            
        # Print out the total wrapping paper needed
        #print("The elves need %d square feet of wrapping paper" %(sum))
        
    except IOError:
        print("ERROR >> Missing file day2star1.txt")

    return


# begin gracefully
#
if __name__ == "__main__":
    main(sys.argv[0:])

#
# end of file
