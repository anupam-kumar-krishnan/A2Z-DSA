# _Hashing_
Suppose, an array is given
- Ask a number appearing in an array any number of times
- Ask a lot of times for any number

## _Brute Force Approach_
- First approach is using `for loops`

<b>

```cpp
int f(number, arr[])
{
  cnt=0;
  for(i=0 ; i<n ; i++)   
  {
    if(arr[i] == number)   
        cnt = cnt + 1;
  }
  return cnt;
}

// Time Complexity, TC => O(n)
```
</b>

## _Hashing Approach_
- Pre Storing / Fetching
- Suppose, an array will have at max 12 numbers
- I'll create another array, known as `Hash Array`
- And I'll initiate every element with 0 at first
- I'll do some Pre-calculation

<b>

```cpp
#include<bits/stdc++.h>
using namespace std;


int main()
{
  int n;
  cin>>n;
  int arr[n];
  for(int i=0;i<n;i++){
    cin >> arr[i];
  }

  // precompute
  int hash[13] ={0};
  for(int i=0;i<n;i++){
     hash[arr[i]] += 1;
  }

  int q;
  cin>>q;
  
  while(q--){
    int number;
    cin >> number;
    // fetch
    cout << hash[number]<<endl;
  }

  return 0;
}

// Input
// 5
// 1 3 2 1 3
// 5
// 1
// 4
// 2
// 3 
// 12
```
</b>

## _Character Hashing_










