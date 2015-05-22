/*
 * Copyright (C) 2015 
 * Created by missingdays 
 *
 * Distributed under terms of the MIT license.
 */

#include <stdio.h>

// How to multiply two matrix the most efficient way
int main(){
    int i,j,k; // Iterators

    // Init
    int A[3][3]={{1,2,3},{1,2,3},{1,2,3}};
    int B[3][3]={{1,2,3},{1,2,3},{1,2,3}};

   // Matrix for answer initilized with zeros
    int answ[3][3]={0};

    
    // Create temporary matrix for transposed B
    int temp[3][3];

    // Transpose B
    for(i=0; i<3; i++){
        for(j=0; j<3; j++){
            temp[i][j]=B[j][i];
        }
    }

    // Do multiplication
    for(i=0; i<3; i++)
        for(j=0; j<3; j++)
            for(k=0; k<3; k++)
                answ[i][j] += (A[i][k] * temp[j][k]);
    // Check the answer
    for(i=0; i<3; i++)
       for(j=0; j<3; j++) 
            printf("%d ", answ[i][j]);
    printf("\n");

    return 0;
}

