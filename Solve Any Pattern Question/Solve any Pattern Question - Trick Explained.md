# _Solve any Pattern Question - Trick Explained_


- For Patterns Questions, you must have a strong foundation of loops
- Patterns are not asked in Product Based Interviews
- But is plays a significant role when you are starting of your DSA Journey

## _Steps to Print any Pattern_
_(Most of the patterns will have Nested Loops)_
1. In the outer loop, connect the number of lines
2. In the inner loop, focus of the columns & connect them somewhere to the rows
3. Print the '*' inside the inner for loop
4. Observe symmetry  [Optional]


## _Pattern 1_
<b>

```
* * * *
* * * *
* * * *
* * * *
```
</b>

## _Steps_
```
1. For the Outer loop, count the number of lines: 4
2. For the Inner loop, there is also 4 number of stars ther same as row
3. Print the stars now, inside the inner for loop
```

### _Code_
<b>

```cpp
#include <bits/stdc++.h>
using namespace std;

void print(int n)
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
        print(n);
    }
}
```
## _Explanation_
![Screenshot 2023-01-03 101755](https://user-images.githubusercontent.com/91872149/210301617-dcbdd196-158a-4d96-8852-374942a308bd.png)


</b>

## _Pattern 2_

<b>

```
* 
** 
*** 
****
*****
```

### _Code_

```cpp
#include <bits/stdc++.h>

using namespace std;

void print(int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j <= i; j++)
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
        print(n);
    }
}
```
</b>

## _Pattern 3_

<b>

```
1
12
123
1234
12345
```

### _Code_

```cpp
#include <bits/stdc++.h>

using namespace std;

void print(int n)
{
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= i; j++)
        {
            cout << j << " ";
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
        print(n);
    }
}
```

## _Pattern 4_

```
1
22
333
4444
55555
```

### _**Code**_
```cpp
#include <bits/stdc++.h>
using namespace std;

void print(int n)
{
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= i; j++)
        {
            cout << i << " ";
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
        print(n);
    }
}

```

## _Pattern 5_

```
*****
****
***
**
*
```

### _Code_
```
#include <bits/stdc++.h>
using namespace std;

void print(int n)
{
    for (int i = 1; i <= n; i++)
    {
        for (int j = 0; j < n - i + 1; j++)
        {
            cout << "*"
                 << " ";
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
        print(n);
    }
}
```

## _Pattern 6_

```
12345
1234
123
12
1
```

### _Code_

```cpp
#include <bits/stdc++.h>
using namespace std;

void print(int n)
{
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n - i + 1; j++)
        {
            cout << j;
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
        print(n);
    }
}
```

## _Pattern 7_

```
    *
   ***
  *****
 *******
*********
```
### _Explanation_
![7](https://user-images.githubusercontent.com/91872149/210490220-615bb088-1c9a-42fd-a453-1077a4ffc49a.png)

### _Code_

```cpp
#include <bits/stdc++.h>
using namespace std;

void print(int n)
{
    for (int i = 0; i < n; i++)
    {
        // space
        for (int j = 0; j < n - i - 1; j++)
        {
            cout << " ";
        }
        // star
        for (int j = 0; j < 2 * i + 1; j++)
            cout << "*";
        // space
        for (int j = 0; j < n - i - 1; j++)
        {
            cout << " ";
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
        print(n);
    }
}
```
## _Pattern 8_

```
*********
 *******
  *****
   ***
    *
```

### _Code_

```cpp
/* Inverted Tree Pattern */
#include <bits/stdc++.h>
using namespace std;

void print(int n)
{
    for (int i = 0; i < n; i++)
    {
        // space
        for (int j = 0; j < i; j++)
        {
            cout << " ";
        }
        // star
        for (int j = 0; j < 2 * n - (2 * i + 1); j++)
            cout << "*";
        // space
        for (int j = 0; j < i; j++)
        {
            cout << " ";
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
        print(n);
    }
}
```

## _Pattern 9_

```
      *
     ***
    *****
   *******
  *********
   *******
    *****
     ***
      *
```

### _Code_

```cpp
/* Diamond Pattern: Combination Of Patter 7 & 8 */

#include <bits/stdc++.h>
using namespace std;

void print7(int n)
{
    for (int i = 0; i < n; i++)
    {
        // space
        for (int j = 0; j < n - i - 1; j++)
        {
            cout << " ";
        }
        // star
        for (int j = 0; j < 2 * i + 1; j++)
            cout << "*";
        // space
        for (int j = 0; j < n - i - 1; j++)
        {
            cout << " ";
        }
        cout << endl;
    }
}

void print8(int n)
{
    for (int i = 0; i < n; i++)
    {
        // space
        for (int j = 0; j < i; j++)
        {
            cout << " ";
        }
        // star
        for (int j = 0; j < 2 * n - (2 * i + 1); j++)
            cout << "*";
        // space
        for (int j = 0; j < i; j++)
        {
            cout << " ";
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
        print7(n);
        print8(n);
    }
}
```

## _Pattern 10_

```
*
**
***
****
*****
****
***
**
*
```

## _Explanation_
![symmetric](https://user-images.githubusercontent.com/91872149/210494964-31a57abe-c920-4915-954f-398fd709cafd.png)

### _Code_

```cpp
#include <bits/stdc++.h>
using namespace std;

void print(int n)
{
    for (int i = 1; i <= 2 * n - 1; i++)
    {
        int stars = i;
        if (i > n)
            stars = 2 * n - i;
        for (int j = 1; j <= stars; j++)
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
        print(n);
    }
}
```

## _Pattern 11_

```
1
01
101
0101
10101
```

### _Code_

```cpp
#include <bits/stdc++.h>
using namespace std;

void print(int n)
{
    int start = 1;
    for (int i = 0; i < n; i++)
    {

        if (i % 2 == 0)
            start = 1;
        else
            start = 0;
        for (int j = 0; j <= i; j++)
        {
            cout << start;
            start = 1 - start;
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
        print(n);
    }
}
```
</b>



