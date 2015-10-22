
#include <stdio.h>
#include <assert.h>
#include "stack.h"

int main(void){

	stack *s = Stack();

	s = push(s, 1);
	assert(s->elems[0] == 1);

	s = push(s, 2);
	s = push(s, 3);
	s = push(s, 4);

	assert(s->elems[3] == 4);
	assert(s->size == 8);

    int elem;
    s = pop(s, &elem);
	assert(elem == 4);

	s = pop(s, &elem);
	assert(elem == 3);
	s = pop(s, &elem);
	assert(elem == 2);

	assert(s->size == 8);

	s = pop(s, &elem);
	assert(elem == 1);

    assert(s->size == 4);

	s = pop(s, &elem);
	assert(stack_error == ERR_EMPTY_STACK_POP);

	s = push(s, 10);
	s = push(s, 20);
	s = push(s, 30);
	s = push(s, 40);

	elem = pick(s);
	assert(elem == 40);
	assert(s->size == 8);
}

