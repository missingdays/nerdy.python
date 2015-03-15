/*
    type: algorithm
    theme: math
    sub-theme: calculate
    name: fibonacci
    author of code: example is taken from golang.org (official golang site)

*/

package main

import "fmt"

// fib returns a function that returns
// successive Fibonacci numbers.
func fib() func() int {

  a, b := 0, 1

  return func() int {

    a, b = b, a+b

    return a
  }
}

func main() {

  f := fib()

  // Function calls are evaluated left-to-right.
  fmt.Println(f(), f(), f(), f(), f())
}
