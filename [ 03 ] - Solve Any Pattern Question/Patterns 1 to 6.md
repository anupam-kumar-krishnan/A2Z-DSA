## _Patterns 1 to 6_


<b>

```cpp
#include <iostream>
using namespace std;
void print1(int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cout << "* ";
        }
        cout << endl;
    }

    // i     j           Count
    // 0     0 1 2 3     4        ****
    // 1     0 1 2 3     4        ****
    // 2     0 1 2 3     4        ****
    // 3     0 1 2 3     4
}

void print2(int n)
{
    /*
     *
     **
     ***
     ****
     *****
     */

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j <= i; j++)
        {
            cout << "*";
        }
        cout << endl;
    }
}

void print3(int n)
{
    /**
     1
     12
     123
     1234
     12345
    */
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= i; j++)
        {
            cout << j;
        }
        cout << endl;
    }
}

void print4(int n)
{
    /**
     1
     22
     333
     4444
     55555
    */

    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= i; j++)
        {
            cout << i;
        }
        cout << endl;
    }
}

void print5(int n)
{
    /*
    *****
    ****
    ***
    **
    *
    */
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n - i; j++)
        {
            cout << "*";
        }
        cout << endl;
    }
}

void print6(int n)
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
        print6(n);
    }

    // 1. Outer loop, count the number of lines
    // 2. for inner loop, focus on the columns & connect them somehow to the rows
    // 3. print *, print inside inner for loop
    // 4. observe symmetry

    return 0;
}
```
</b>



