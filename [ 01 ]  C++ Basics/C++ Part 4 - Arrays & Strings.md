## _Arrays_
- Similar data types stored multiple times
- Index starts from zero(0)
- Size: Length of array - 1

<b>

## 1D Array
```cpp
#include <bits/stdc++.h>
using namespace std;
int main()
{
    int arr[5];
    cin >> arr[0] >> arr[1] >> arr[2] >> arr[3] >> arr[4]; // 1 2 3 4 5

    arr[3] = 10;
    cout << arr[3]; // 10
    return 0;
}
```

## 2D Array

```cpp
#include <bits/stdc++.h>
using namespace std;
int main(){  
  //2D Array
  int arr[3][5]; // 5 boxes, 3 times | row, column
  arr[1][3]=78;
  cout<<arr[1][3]; // 78
return 0;
}
```

## _String_
- String also stores every charecter in terms of indexes


```cpp
#include <bits/stdc++.h>
using namespace std;
int main(){ 
  string s="Striver";
  int len = s.size();
  cout<< s(len - 1); //r
  cout<<s[1]; //t   
  return 0;
}
```




</b>




