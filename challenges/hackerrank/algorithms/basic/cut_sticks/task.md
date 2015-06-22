##Problem Statement

You are given N sticks, where each stick has the length of a positive integer. A cut operation is performed on the sticks such that all of them are reduced by the length of the smallest stick.

Suppose we have six sticks of the following lengths:

5 4 4 2 2 8
Then, in one cut operation we make a cut of length 2 from each of the six sticks. For the next cut operation four sticks are left (of non-zero length), whose lengths are the following:

3 2 2 6
The above step is repeated until no sticks are left.

Given the length of N sticks, print the number of sticks that are cut in subsequent cut operations.

##Input Format
The first line contains a single integer N.
The next line contains N integers: a0, a1,...aN-1 separated by space, where ai represents the length of ith stick.

##Output Format
For each operation, print the number of sticks that are cut in separate line.

##Constraints
1 ≤ N ≤ 1000
1 ≤ ai ≤ 1000

###Sample Input

6

5 4 4 2 2 8
###Sample Output

6

4

2

1

###Sample Input

8

1 2 3 4 3 3 2 1
###Sample Output

8

6

4

1
