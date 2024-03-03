# _Hashing_
_Suppose, an array is given_
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

### _Brute Force Code_

<b>

```cpp
#include<bits/stdc++.h> 
using namespace std;
int computeNumbers(int num, int arr[], int n) {
    int cnt = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] == num)
            cnt++;
    }
    return cnt;
}

int main() {
    int n;
    cin >> n;

    int arr[n];

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    int times;
    cin>>times;

    while(times--){
      int num;
      cin>>num;
    int count = computeNumbers(num, arr, n);
    cout << count << endl;
    }

    return 0;
}

// TC => O(n)
```
</b>



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
    cout << hash[number] << endl;
  }

  return 0;
}

// Input        Output
// 5
// 1 3 2 1 3
// 5
// 1            2
// 4            0 
// 2            1
// 3            2
// 12           0
```
</b>

## _Maximum hash Array size (Main vs Global)_
- Array has max element till **10^9**
### _Main_
- Can we declare arr[10^9 + 1] ❌ No we can't
- At max, we can declare arr[10^6] inside main
- arr[10^7] will throw Segmentation Fault, it doesn't allocate that much memory

### _Global_
- If we declare globally, int arr[1e7] then it can go till 10^7


## _Character Hashing_
- We can do Charecter Hasing using Arrays
- Suppose there is a string given, `s="abcdabefc"`
- And asked, how many times does `a` appears?
- Times appears, a => 2, c => 2, z => 0 

<b>

```cpp
if(char c, string s)
{
   cnt=0;
   for(i=0;i<n;i++
   {
     if(s[i]==c)
         cnt++;
   }
  return cnt;
}
```
</b>


### _Hash the above string in Arrays_
- Suppose, Array only has lowercase alphabets
- Since, there are 26 alphabets, Array of size 26, indexed from 0 to 25
- Correspond a to 0, b to 1, c to 2.......z to 26
- Every character has an index
- We  can visualize a=0,b=1 but how can I visualize in program, this is where **_ASCII value_** comes in

<b>

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
  string s;
  cin >> s;

  // pre compute
  int hash[26] = {0};
  for (int i = 0; i < s.size(); i++) {
    hash[s[i] - 'a']++;
  }

  int q;
  cin >> q;
  while (q--) {
    char c;
    cin >> c;
    cout << hash[c - 'a'] << endl;
  }
  return 0;
}
```
</b>

















