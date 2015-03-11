/*
    type: algorithm
    theme: arrays
    sub-theme: sorting
    name: merge sorting
    author of code: Ivan @XioYS

*/

#include <iostream>
using namespace std;


void MergeComp(int *A, int firstA, int lastA, int size_)
{
    int mid, first, last, i;
    int *arr=new int[size_];
    mid=(firstA+lastA)/2;
    first=firstA;
    last=mid+1;
    for(i=firstA; i<=lastA; i++)
    if ((first<=mid) && ((last>lastA) || (A[first]<A[last])))
    {
        arr[i]=A[first];
        first++;
    }
    else
    {
        arr[i]=A[last];
        last++;
    }
    for (i=firstA; i<=lastA; i++) A[i]=arr[i];
        delete[]arr;
};


void MergeRecurs(int *A, int first, int last, int size_)
{
    if (first<last)
    {
        MergeRecurs(A, first, (first+last)/2, size_);
        MergeRecurs(A, (first+last)/2+1, last, size_);
        MergeComp(A, first, last, size_);
    }
};




int main()
{
    int i, n;
    int *A=new int[n];
    A[0] = 43; //1
    A[1] = 1; //2
    A[2] = 7; //3
    A[3] = 78; //4
    A[4] = 446; //5
    n = 5; //=> 5
    MergeRecurs(A, 1, n, n);
    cout<<"Sorted Array   :";
    for (i=1; i<=n; i++)
        cout<<A[i]<<" ";
    delete []A;
}
