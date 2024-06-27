#include <iostream>
using namespace std;

int main() {
    int a[15][15]={};
   int n;
   int x=1,y=0,l=1;
   cin>>n;
   while (l<=n*n){
       while (y+1<=n&&a[x][y+1]==0){
           a[x][y+1]=l;y++;
           l++;
       }
       
       while (x+1<=n&&a[x+1][y]==0){
           a[x+1][y]=l;x++;
           l++;
       }
       
       while (y-1>=1&&a[x][y-1]==0){
           a[x][y-1]=l;y--;
           l++;
       }
       
       while (x-1>=1&&a[x-1][y]==0){
           a[x-1][y]=l;x--;
           l++;
       }
       
   }
    for (int i=1; i<=n; i++){
        for (int j=1; j<=n; j++){
            if (a[i][j]<=9&&a[i][j]>=1){
                cout<<" ";
            }
            cout<<a[i][j]<<' ';
        }
        cout<<endl;
    }
    
    return 0;
}
 