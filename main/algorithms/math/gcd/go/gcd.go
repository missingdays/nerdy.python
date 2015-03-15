package main

import "fmt"

//Function that finds greates common division
func gcd(a, b int) int {

    //While b not equals b
    for b != 0 {

        //Assign b to a
        //and calculate new b
        a, b = b, a % b
    }

    //Return a
    return a
}

func main() {

    //First test
    fmt.Println(gcd(33, 77)) //11

    //Second test
    fmt.Println(gcd(49865, 69811)) //9973
}
