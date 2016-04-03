/* Segmented tree small example : 
	* Searching minimum. - Done
	* Searching maximum. - ToDo
	* Updating tree. - ToDo 
	* Sum tree. - ToDo
	* Display tree in terminal - Todo
XioNOverMazeS
*/

#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

template <typename t> struct tree_node;

template <typename t>struct tree_node {
    tree_node<t> * _left = NULL;
    tree_node<t> * _right = NULL;
    t val;
};



typedef tree_node<int> int_tn;

int_tn TREE;

int build_tree(int A[], int a, int b, int_tn * tn) {
        if (a == b)
        {
            tn->val = a;
            return a;
        }
        if (abs(a - b) == 1){
            cout << "If " << a << "  " << b << "\n";
            if (A[a] < A[b]){
            tn->val = a; return a;}
            else{
            tn->val = b; return b;}
        }
        else
        {
            std::cout << "Else " << a << "  " << b << "\n";
            int n;
            int leftId = ( a + b ) / 2 + 1; /* For right side */
            int rightId = ( a + b ) / 2; /* For left side */
            tn->_left = new int_tn;
            tn->_right = new int_tn;
            int lSide = build_tree(A, a, rightId, tn->_left);
            int rSide = build_tree(A, leftId, b, tn->_right);
            std::cout << "lSide " << lSide << "  rSide " << rSide << "\n";
            if (A[lSide] < A[rSide]){
                tn->val = lSide;
                return lSide;
            }
            else {
                tn->val = rSide;
                return rSide;
            }

        }

}

int RMQ(const int_tn & TREE, int val)
{

}


int main(int argc, char * argv[]) {
    int A[] = { 1 , 20, 0, 5, 13, 3, 7, 2, 6, 1, 4, 2, 6 , -1 , 19, 53};
    build_tree(A, 0, 6, &TREE);
    std::cout << endl << endl <<TREE.val;
    return 0;
}

