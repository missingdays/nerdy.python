
typedef struct
{
	int size;
	int current_size;
	int* elems;
} stack;

stack *Stack();
void push(stack *s, int elem);
int pop(stack *s);
void print_stack(stack *s);