/*
    type: algorithm
    theme: arrays
    sub-theme: search
    name: binary-search
    author of code: Evgeny @missingdays Bovykin

*/


package main

import "fmt"

//Function that looks up some value in sorted array
func binarySearch(a []float64, value float64) int {

    //The beginning of the array
    low := 0

    //The end of the array
    high := len(a) - 1

    //While we didn't collapse full array
    for low <= high {

        //Select middle point
        mid := (low + high) / 2

        //If our value is less than middle point
        if value < a[mid] {

            //We will search in the left part of the array
            high = mid - 1

        }
        // Else if our value if greater than middle point
        else if a[mid] < value {

            //We will search in the right part of the array
            low = mid + 1

        }
        //Else we found our value
        else {
            return mid
        }
    }

    //We didnt' find our value
    return -1
}

func main() {

  //Array that we will search our value in
  a := []float64{1, 2, 3, 4, 5, 6, 7, 9}

  fmt.Println(binarySearch(a, 4)) //3 (index)

  fmt.Println(binarySearch(a, 8)) //-1 (not found)

}
