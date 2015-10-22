#include <stdlib.h>
#include <stdio.h>

#include "stack.h"

stack *Stack(){
	stack *s = (stack *)malloc(sizeof(stack));
	s->size = STACK_INIT_SIZE;
	s->current_size = 0;
	s->elems = (int *)malloc(sizeof(int)*s->size);

	return s;
}

void push(stack *s, int elem){
	if(s->current_size == s->size - 1){
		*(s) = realloc(s, s->size*2);
	}

	s->elems[s->current_size] = elem;
	s->current_size++;
}

int pop(stack *s){
	if(s->current_size == 0){
		stack_error = ERR_EMPTY_STACK_POP;
		return 0;
	}
	if(s->current_size < s->size/4){
		*(s) = realloc(s, s->size/2);
	}

	s->current_size--;
	int elem = s->elems[s->current_size];
	return elem;
}
int pick(stack *s){
	return s->elems[s->current_size-1];
}
void print_stack(stack *s){
	printf("[");
	for(int i = 0; i < s->current_size; i++){
		printf("%d,", s->elems[i]);
	}
	printf("]\n");
}
