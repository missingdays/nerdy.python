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

stack *realloc_stack(stack *s, int size){
    s->size = size;
    return realloc(s, sizeof(int)*size);
}

stack *push(stack *s, int elem){
	if(s->current_size == s->size - 1){
		s = realloc_stack(s, s->size*2);
	}
	s->elems[s->current_size] = elem;
	s->current_size++;
    
    return s;
}

stack *pop(stack *s, int *to){
	if(s->current_size == 0){
		stack_error = ERR_EMPTY_STACK_POP;
        return s;
	}
	if(s->current_size < s->size/4 && s->size > 4){
		s = realloc_stack(s, s->size/2);
	}

	s->current_size--;
	*(to) = s->elems[s->current_size];

    return s;
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
