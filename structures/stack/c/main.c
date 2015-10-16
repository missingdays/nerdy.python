
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
}

