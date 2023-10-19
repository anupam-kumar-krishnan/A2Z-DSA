# _Pattern 1_
## _Steps to Print any Pattern_
_(Most of the patterns will have Nested Loops)_
1. In the outer loop, connect the number of lines
2. In the inner loop, focus of the columns & connect them somewhere to the rows
3. Print the '*' inside the inner for loop
4. Observe symmetry  [Optional]

## _Execution_
<b><i>1. Outer loop will be running for 4 times</i></b>

<b>

```cpp
for(int i=0;i<n;i++)
```

<b><i>2. In the inner loop, we have 4 rows & everytime we are printing 4 stars</i></b>
We can say,<br>
For row 0 -> Print 4 Stars<br>
```cpp
0 -> 4
1 -> 4
2 -> 4
3 -> 4
```

```cpp
for(int i = 0; i < n ; i++) {
     for(j = 0 ; j < n ;  j++) {
   }
}
```

<b><i>3. Print the '*' inside the inner for loop</i></b>

```cpp
for(int i = 0; i < n ; i++) {
     for(j = 0 ; j < n ;  j++) {
        cout<<"*";
   }
  cout<<endl;
}
```



## _Pattern 1_

```cpp
****
****
****
****
```

## _Code_


```cpp
#include <bits/stdc++.h>
using namespace std;
void printPattern1(int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cout << "*";
        }
        cout << endl;
    }
}

int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        int n;
        cin >> n;
        printPattern1(n);
    }
}
```
</b>

