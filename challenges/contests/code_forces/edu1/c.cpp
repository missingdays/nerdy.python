#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <climits>
#include <algorithm>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <cassert>
#include <vector>
#define all(x) x.begin() , x.end()
#define fi first
#define se second
#define pb push_back
#define umax( x , y ) x = max( x , (y) )
#define umin( x , y ) x = min( x , (y) )
#define For( i , a ) for(int i=1;i<=a;i++)
#define ort (b+s)/2
#define y2 asrwjaelkf
#define y1 asseopirwjaelkf
#define hash ____hash
#define pi 3.141592653589793238462643383279502884197169399375105820974944592307816406286L

using namespace std;

const int maxn = 100020;
const int maxm = 1000020;
const int P = 37;

typedef long long Lint;
typedef long double db;
typedef pair<int,int> ii;
typedef pair<int,ii> iii;
typedef pair<char,int> ci;
typedef pair<int,ci> ici;

struct node {
    int x, y, id;
    db deg;
    friend bool operator < ( const node &a, const node &b ) { return a.deg < b.deg; }
}ar[maxn];

int a, b;
char bs[maxn];

db atann( int y, int x ) {
    db t = atan2( y, x );
    if( t < 0 ) t += pi+pi;
    return t;
}

int main() {
    
    scanf("%d",&a);
    
    for(int i=1;i<=a;i++) {
        scanf("%d %d",&ar[i].x,&ar[i].y);
        ar[i].id = i;
        ar[i].deg = atann( ar[i].y, ar[i].x );
    }
    
    sort( ar+1, ar+1+a );
    
    db mini = ar[1].deg+pi+pi-ar[a].deg;
    ii ans = ii( ar[1].id, ar[a].id );
    
    for(int i=1;i<a;i++) {
        db t = ar[i+1].deg-ar[i].deg;
        if( t < mini ) {
            mini = t;
            ans = ii( ar[i].id, ar[i+1].id );
        }
    }
    
    printf("%d %d\n",ans.fi,ans.se);
    
    return 0;
}
