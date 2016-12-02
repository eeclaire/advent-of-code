package main

import (
       "bufio"
       "encoding/csv"
       "fmt"
       "io"
       "os"
       "strconv"
)

// Convenience function to obtain absolute value of an int
func abs(n int) int {
    if n < 0 {
        n = -n
    }
    return n
}

// Read in the directions input from the indicated csv
func readInputs(filename string) []string {

    // declare the input file
    fin, _ := os.Open(filename)

    var steps []string

    // Read in the file
    reader := csv.NewReader(bufio.NewReader(fin))
    for {
        record, err := reader.Read()
	if err ==io.EOF {
	    break
    	}
	// Append to the steps slice in	the main scope
	for i:=0; i<len(record); i++ {
            steps = append(steps,record[i])
	}
    }
    return steps
}

func main() {

    // declare the input file
    //fin, _ := os.Open("star1_input.csv")

    inputFile := "star1_input.csv"

    // Use a numeric code to track current direction.
    // North is 3, and numbers decrease clockwise
    currentDirection := 3

    // Use x and y to keep track of current location
    x := 0
    y := 0

    // Iterate through the given steps
    steps := readInputs(inputFile)

    // Add a space to the beginning of the first value so that all of them are consistent
    steps[0] = " " + steps[0]
    for i:=0; i<len(steps); i++ {
	
    	// Obtain the direction and the number of steps 
    	newDir := steps[i][1]
	dirStepsStr := steps[i][2:]
	dirSteps,_ := strconv.Atoi(dirStepsStr)

	// Increment the current direction
	if newDir == 76 {
	    currentDirection = currentDirection + 1
	} else if newDir == 82 {
	    currentDirection = currentDirection - 1
	}

	// Make sure the current is cyclical
	if currentDirection < 0 {
	    currentDirection = 3
	} else if currentDirection > 3 {
	    currentDirection = 0
	}

	// Use this new code direction to figure out which direction to increment the steps in
	if currentDirection == 0 {
	    x = x - dirSteps
	} else if currentDirection == 1 {
	    y = y - dirSteps
	} else if currentDirection == 2 {
	    x = x + dirSteps
	} else if currentDirection == 3 {
	    y = y + dirSteps
	}

    }

    // Compute and print the number of blocks this represents
    numOfBlocks := abs(x) + abs(y)
    fmt.Println("Number of Blocks:")
    fmt.Println(numOfBlocks)
} 