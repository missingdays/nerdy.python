/*
    type: algorithm
    theme: math
    sub-theme: calculate
    name: factorial
    author of code: Evgeny @missingdays Bovykin

*/

package main

import "fmt"

func factorial(n int) int{

  if n == 0 || n == 1{

    return 1

  }

  a := 1

  for i := 1; i < n + 1; i++ {
    a = a * i
  }

  return a

}

func main() {

  for i := 0; i < 10; i++{
    fmt.Println(factorial(i))
  }

}
