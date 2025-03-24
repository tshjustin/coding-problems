package main

import (
	"fmt"
	"strconv" // string to int 
	"strings" // split , contains etc 
)

func main() {
	var input string
	fmt.Scanln(&input) // pointer to the variable, allowing to modify directly
	
	total := countProblems(input)
	fmt.Println(total)
}

func countProblems(problemString string) int {
	sections := strings.Split(strings.TrimSpace(problemString), ";") // remove leading, threading white space, and split at ;
	totalProblems := 0
	
	// sections: is an array of strings 
	// range => iterate over this array of strings  == enumerate in python
	// for (index, element) in .. 
	// ["1-3", "5", "7" 
	
	for _, section := range sections {
		if strings.Contains(section, "-") {
			rangeParts := strings.Split(section, "-")
			start, _ := strconv.Atoi(rangeParts[0]) // converts the string to int. Atoi returns (num, err)
			end, _ := strconv.Atoi(rangeParts[1])
			totalProblems += (end - start + 1)
		} else {
			totalProblems += 1
		}
	}
	return totalProblems
}