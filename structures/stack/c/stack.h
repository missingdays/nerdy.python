#define ERR_EMPTY_STACK_POP 1
#define STACK_INIT_SIZE 4
int stack_error;

typedef struct
{
	int size;
	int current_size;
	int* elems;
} stack;

stack *Stack();
void push(stack *s, int elem);
int pop(stack *s);
int pick(stack *s);
void print_stack(stack *s);
