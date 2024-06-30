#include<bits/stdc++.h>
using namespace std;
//函数声明
bool is_prime(int x);

int main(){
	int n;
	cin >> n;
	for(int i=2;i<=n;i++){
		if (is_prime(i)){
		    cout<<i<<' ';
		}
	}
		    
	return 0;
}

bool is_prime(int x){
    for (int i=2; i<=sqrt(x); i++){
        if (x%i==0) {
            return false;
        }
        return true;
    }
    
}
