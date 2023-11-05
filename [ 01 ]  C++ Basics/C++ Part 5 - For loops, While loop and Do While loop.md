# _For loops_

<b>

- Print 5 times

```cpp
#include <bits/stdc++.h>
using namespace std;
int main()
{
    // Print 5 times
    cout << "Striver" << endl;
    cout << "Striver" << endl;
    cout << "Striver" << endl;
    cout << "Striver" << endl;
    cout << "Striver" << endl;
    return 0;
}
```

- 5 was easy, but what if 500 times: for loop does it for you


```cpp
#include <bits/stdc++.h>
using namespace std;
int main()
{
    // Print 10 times
    for (int i = 1; i <= 10; i = i + 1)
    {
        cout << "Microsoft " << i << endl;
    }
    return 0;
}
```

//Output
```
Microsoft 1
Microsoft 2
Microsoft 3
Microsoft 4
Microsoft 5
Microsoft 6
Microsoft 7
Microsoft 8
Microsoft 9
Microsoft 10
```

## _While loops_
- Executing some lines of code, for some numbers of time

```cpp
#include <bits/stdc++.h>
using namespace std;
int main()
{
    int i = 1;
    while (i <= 5)
    {
        cout << "Striverr " << i << endl;
        i = i + 1;
    }
    return 0;
}

//Output
/*
Striverr 1
Striverr 2
Striverr 3
Striverr 4
Striverr 5
*/
```


## _Do While loop_
```cpp
#include <bits/stdc++.h>
using namespace std;
int main()
{
    int i = 1;
    do
    {
        cout << "Striverr " << i << endl;
        i = i + 1;
    } while (i <= 1);

    return 0;
}
// Output
// Striverr 1
```
</b>
