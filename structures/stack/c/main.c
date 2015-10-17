
#include <stdio.h>
#include <assert.h>
#include "stack.h"

int main(void){

	stack *s = Stack();

	push(s, 1);
	assert(s->elems[0] == 1);

	push(s, 2);
	push(s, 3);
	push(s, 4);

	assert(s->elems[3] == 4);
	assert(s->size == 8);

	int elem = pop(s);
	assert(elem == 4);

	elem = pop(s);
	assert(elem == 3);
	elem = pop(s);
	assert(elem == 2);

	assert(s->size == 4);

	elem = pop(s);
	assert(elem == 1);

	pop(s);
	assert(stack_error == ERR_EMPTY_STACK_POP);

	push(s, 10);
	push(s, 20);
	push(s, 30);
	push(s, 40);

	elem = pick(s);
	assert(elem == 40);
	assert(s->size == 8);
}

