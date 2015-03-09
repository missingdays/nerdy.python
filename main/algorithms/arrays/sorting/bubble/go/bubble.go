package main

import "fmt"

func main() {
    //Array to be sorted
    list := []int{31, 41, 59, 26, 53, 58, 97, 93, 23, 84}

    fmt.Println("unsorted:", list)

    //Sort it!
    bubblesort(list)

    fmt.Println("sorted!  ", list)
}

func bubblesort(a []int) {

    //Iterate for length of array - 1 times
    for itemCount := len(a) - 1; ; itemCount-- {

        //Has array change since last time?
        hasChanged := false

        //Iterate through every element except last
        for index := 0; index < itemCount; index++ {

            //If element is bigger than next to it
            if a[index] > a[index+1] {

                //Swap them
                a[index], a[index+1] = a[index+1], a[index]

                //That means array has changed
                hasChanged = true
            }
        }

        //If array hasn't changed
        if hasChanged == false {

            //We can end iterating
            break
        }
    }
}
