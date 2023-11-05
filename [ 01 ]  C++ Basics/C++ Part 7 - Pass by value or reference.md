## _Pass by Value or Pass by Reference_

<b>

## _Pass by Value_

```cpp
#include <bits/stdc++.h>
using namespace std;

// pass by value - passed the copy original reains the same
void doSomething(int num)
{
    cout << num << endl;
    num += 5;
    cout << num << endl;
    num += 5;
    cout << num << endl;
}

int main()
{
    int num = 10;
    doSomething(num);
    cout << num << endl;
    return 0;
}
```

```cpp
#include <bits/stdc++.h>
using namespace std;

// pass by value
void doSomething(string s)
{
    s[0] = 't';
    cout << s << endl;
}

int main()
{
    string s = "raj";
    doSomething(s);
    cout << s << endl;
    return 0;
}

// taj
// raj
```



## _Pass by reference_

```cpp
#include <bits/stdc++.h>
using namespace std;

// pass by reference - sends the address(original value)
void doSomething(string &s)
{
    s[0] = 't';
    cout << s << endl;
}

int main()
{
    string s = "raj";
    doSomething(s);
    cout << s << endl;
    return 0;
}

// taj
// taj
```


```cpp
#include <bits/stdc++.h>
using namespace std;

// pass by reference - sends the address(original value)
void doSomething(int arr[], int n)
{
    arr[0] += 100;
    cout << "Value inside function: " << arr[0] << endl;
}

int main()
{
    int n = 5;
    int arr[n];

    for (int i = 0; i < n; i = i + 1)
    {
        cin >> arr[i];
    }

    doSomething(arr, n);

    cout << "Value inside int main: " << arr[0] << endl;
    return 0;
}

// Value inside function: 101
// Value inside int main: 101
```

</b>



