/*
    type: algorithm
    theme: arrays
    sub-theme: search
    name: binary-search
    author of code: Evgeny @missingdays Bovykin

*/


package main

import "fmt"



func binarySearch(a []float64, value float64) int {
    low := 0
    high := len(a) - 1
    for low <= high {
        mid := (low + high) / 2
        if a[mid] > value {
            high = mid - 1
        } else if a[mid] < value {
            low = mid + 1
        } else {
            return mid
        }
    }
    return -1
}

func main() {

  a := []float64{1, 2, 3, 4, 5, 6, 7, 9}

  fmt.Println(binarySearch(a, 4)) //3 (index)

  fmt.Println(binarySearch(a, 8)) //-1 (not found)

}
