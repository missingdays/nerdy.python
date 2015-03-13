/*
    type: algorithm
    theme: arrays
    sub-theme: sorting
    name: insertion sorting
    author of code: Evgeny @missingdays Bovykin

*/

package main

import "fmt"

//Sort given array using insertion sort algorithm
func insertionSort(a []int) {

    //For every element in array
    for i := 1; i < len(a); i++ {

        //Get its value
        value := a[i]

        //Decrease iterator by one
        j := i - 1

        //Insert element to a place where it belongs
        for j >= 0 && a[j] > value {

            //shifting all elements after it to the right by one
            a[j+1] = a[j]
            j = j - 1
        }

        //Write number to place where it should be
        a[j+1] = value
    }
}

func main() {

    //Array to be sorted
    list := []int{31, 41, 59, 26, 53, 58, 97, 93, 23, 84}
    fmt.Println("unsorted:", list)

    //Sort it!
    insertionSort(list)
    fmt.Println("sorted!  ", list)
}
