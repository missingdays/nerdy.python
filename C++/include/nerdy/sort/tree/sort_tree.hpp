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

typedef std::vector< tree_node<tp>* > path_home;

tree_node<tp> root;
tp * _arr = 0;
int size = 0;

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

tree_node<tp> & find_node(int idx, path_home * ph, tree_node<tp> * current, int &a , int &b)
{
	if (std::abs(a-b) != 1 || a!=b)
	{
		ph->push_back(current);
		int mid = (a+b) / 2;
		if ( idx <= mid )
		{
			find_node(idx , ph, &current->_left, a, mid);
		}
		else
		{
			find_node(idx, ph, &current->right, mid+1 , b);
		}
	}
	else
	{
		return current;			
	}
}

tp & rebuild_part(int a , int b, tree_node<tp> * tn, tp & new_value)
{
	
}

public :

sort_tree(tp * arr ,int size_)
{
	build_tree(arr, 0, size_, &root);
	_arr = arr;
	size = size_;
}


sort_tree()
{

}

const tp & get_value ()
{
	return *root.val;
}

/* These two functions is under dev. */
void insert(int idx, tp  & value)
{

}

void change_value(int idx, tp & value)
{
	int mid = size / 2;
	if (idx < mid)
	{
		_arr[idx] = value;
				
	}
	else
	{
		
	}
}

void push_back(tp & value);
/* */

};

}



/*int main () //test
{
	int uiui [] = { 1, 2, 0 ,2, 5, 6};
	nd::sort_tree<int> st(uiui, 6);
	return 0;

}*/