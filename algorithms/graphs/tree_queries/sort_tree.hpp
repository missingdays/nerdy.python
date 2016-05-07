#include <vector>
#include <cmath>

namespace nd
{



template< typename tp > class sort_tree
{

private :

template <typename t> struct tree_node
{
    tree_node<t> * _left = nullptr;
    tree_node<t> * _right = nullptr;
    t * val;
};

tree_node<tp> root;

tp & build_tree(tp * arr, int a, int b, tree_node<tp> * tn)
{
	    if (a == b)
        {
            tn->val = &arr[a];
            return arr[a];
        }
        if (std::abs(a - b) == 1){
            if (arr[a] < arr[b]){
            tn->val = &arr[a]; return arr[a];}
            else{
            tn->val = &arr[b]; return arr[b];}
        }
        else
        {
            int leftId = ( a + b ) / 2 + 1; /* For right side */
            int rightId = ( a + b ) / 2; /* For left side */
            tn->_left = new tree_node<tp>;
            tn->_right = new tree_node<tp>;
            int * lSide = &(build_tree(arr, a, rightId, tn->_left));
            int * rSide = &(build_tree(arr, leftId, b, tn->_right));
            if (*lSide < *rSide) {
                tn->val = lSide;
                return *lSide;
            }
            else{
                tn->val = rSide;
                return *rSide;
            }
        }
}

public :

sort_tree(tp * arr ,int size)
{
	build_tree(arr, 0, size, &root);
}


sort_tree()
{

}

const tp & get_value ()
{
	return *root.val;
}

/* These two functions is under dev. */
void insert(int idx, tp  & value);
void change_value(int idx, tp & value);
void push_back(tp & value);
/* */

};

}