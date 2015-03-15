/*
    type: algorithm
    theme: math
    sub-theme: calculate
    name: Euclidian algorithm (greatest common division)
    author of code: Evgeny @missingdays Bovykin

*/

#include <stdio.h>

//Function that finds greates common division
int gcd(int a, int b) {

  //Buffer
  int c;

  //While b not equals 0
  while (b) {

    //Assign buffer to a
    c = a;

    //Assign a to b
    a = b;

    //Calculate b
    b = c % b;
  }

  //Return absolute value of a
  return a < 0 ? -a : a;

}

int main(void){

  int a, b;

  //Read two values
  scanf("%d", &a);
  scanf("%d", &b);

  //Calculate gcd
  c = gcd(a, b);

  //Print it
  printf("%d", c);

}
