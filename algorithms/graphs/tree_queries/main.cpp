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
            if (A[a] < A[b]){
            tn->val = a; return a;}
            else{
            tn->val = b; return b;}
        }
        else
        {
            int n;
            int leftId = ( a + b ) / 2 + 1; /* For right side */
            int rightId = ( a + b ) / 2; /* For left side */
            tn->_left = new int_tn;
            tn->_right = new int_tn;
            int lSide = build_tree(A, a, rightId, tn->_left);
            int rSide = build_tree(A, leftId, b, tn->_right);
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

void set_value(int A [], int size, int idx, int val)
{
	int mididx = size / 2 + 1;

	A[idx] = val;

	if (idx < mididx)
	{
		/* We must update left branch of tree 
			cause index < mid*/
		int rval = TREE._right->val; //Get right branch minimum value
		int lval = build_tree(A, 0, size/2, &TREE);
		if (A[rval] > A[lval]) {
			TREE.val = lval;
			return ;
		}
		else 
		{
			TREE.val = rval;
			return ;
		}

	}
	else // If index < mid ( in right part)
	{
		int lval = TREE._left->val;
		int rval = build_tree(A, (size/2)+1, size, &TREE); /* Updating right branch*/
		if (A[rval] > A[lval]) {
			TREE.val = lval;
			return ;
		}
		else 
		{
			TREE.val = rval;
			return ;
		}
	}
}


int main(int argc, char * argv[]) {
    int A[] = {10, 20, 8, 4, 0, 2, 9};
    build_tree(A, 0, 6, &TREE);
   	set_value(A, 6, 4, 30);
    std::cout << endl << endl <<TREE.val;
    return 0;
}

