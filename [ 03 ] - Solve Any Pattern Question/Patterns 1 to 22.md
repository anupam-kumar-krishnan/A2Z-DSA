<b>

```cpp
void print1(int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cout << "*";
        }
        cout << endl;
    }

    // i     j           Count
    // 0     0 1 2 3     4        ****
    // 1     0 1 2 3     4        ****
    // 2     0 1 2 3     4        ****
    // 3     0 1 2 3     4
}
```

```cpp
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
```

```cpp
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
```

```cpp
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
```

```cpp
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
        for (int j = n; j > i; j--)
        {
            cout << "*";
        }
        cout << endl;
    }
}
```

```cpp
void print6(int n)
{
    /*
    12345
    1234
    123
    12
    1
    */
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n - i + 1; j++)
        {
            cout << j;
        }
        cout << endl;
    }
}
```

```cpp
void print7(int n)
{
    // 0     *      [4,1,4]
    // 1    ***     [3,3,3]
    // 2   *****    [2,5,2]
    // 3  *******   [1,7,1]
    // 4 *********  [0,9,0]
    for (int i = 0; i < n; i++)
    {
        // spaces n-i-1(i=0)
        for (int s = 0; s < n - i - 1; s++)
        {
            cout << " ";
        }
        // stars (2*i)+1
        for (int j = 0; j < ((2 * i) + 1); j++)
        {
            cout << "*";
        }

        // spaces n-i-1(i=0)
        for (int s = 0; s < n - i - 1; s++)
        {
            cout << " ";
        }
        cout << endl;
    }
}
```

```cpp
void print8(int n)
{
    // 0  *********    [0,9,0]
    // 1   *******     [1,7,1]
    // 2    *****      [2,5,2]
    // 3     ***       [3,3,3]
    // 4      *        [4,1,4]
    for (int i = 0; i < n; i++)
    {
        // spaces
        for (int j = 0; j < i; j++)
        {
            cout << " ";
        }
        // stars
        for (int j = 0; j < 2 * n - (2 * i + 1); j++)
        {
            cout << "*";
        }

        // spaces
        for (int j = 0; j < i; j++)
        {
            cout << " ";
        }
        cout << endl;
    }
}
```

```cpp
void print9(int n)
{
    print7(n);
    print8(n);
}
```

```cpp
void print10(int n)
{
    /*
    1 *
    2 **
    3 ***
    4 ****
    5 ***** ---- Symmetry
    6 ****  4
    7 ***   3
    8 **    2
    9 *     1 (2n-i)
     */
    for (int i = 1; i <= (2 * n - 1); i++)
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
```

```cpp
void print11(int n)
{
    /*
    0 1
    1 01
    2 101
    3 0101
    4 10101
    */

    for (int i = 0; i < n; i++)
    {
        int start = 1;
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
```

```cpp
void print12(int n)
{
    /*
    0 1      1  [1,6s,1]
    1 12    21  [1,2,4s,2,1]
    2 123  321  [1,2,3,2s,3,2,1]
    3 12344321  [1,2,3,4,0s,4,3,2,1]
    */
    int space = 2 * (n - 1);
    for (int i = 1; i <= n; i++)
    {
        // number
        for (int j = 1; j <= i; j++)
        {
            cout << j;
        }

        // space 2*(n-i)
        for (int j = 1; j <= space; j++)
        {
            cout << " ";
        }

        // number
        for (int j = i; j >= 1; j--)
        {
            cout << j;
        }
        cout << endl;
        space -= 2;
    }
}
```

```cpp
void print13(int n)
{
    /*
    1
    2 3
    4 5 6
    7 8 9 10
    11 12 13 14 15
    */
    int num = 1;
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= i; j++)
        {
            cout << num << " ";
            num++;
        }
        cout << endl;
    }
}
```

```cpp
void print14(int n)
{
    /*
    A
    AB
    ABC
    ABCD
    ABCDE
    */
    for (int i = 0; i < n; i++)
    {
        for (char ch = 'A'; ch <= 'A' + i; ch++)
        {
            cout << ch;
        }
        cout << endl;
    }
}
```

```cpp
void print15(int n)
{
    /*
    ABCDE
    ABCD
    ABC
    AB
    A
    */
    for (int i = 0; i < n; i++)
    {
        for (char ch = 'A'; ch <= 'A' + (n - i - 1); ch++)
        {
            cout << ch;
        }
        cout << endl;
    }
}
```

```cpp
void print16(int n)
{
    /*
    A
    BB
    CCC
    DDDD
    EEEEE
    */
    for (int i = 0; i < n; i++)
    {
        char ch = 'A' + i;
        for (int j = 0; j <= i; j++)
        {
            cout << ch;
        }
        cout << endl;
    }
}
```

```cpp
void print17(int n)
{
    /*          spaces, alphabets, spaces
    0     A     [4,1,4]
    1    ABA    [3,3,3]
    2   ABCBA   [2,5,2]
    3  ABCDCBA  [1,7,1]
    4 ABCDEDCBA [0,9,0]
    */
    // spaces n-i-1

    for (int i = 0; i < n; i++)
    {

        // spaces n-i-1(i=0)
        for (int s = 0; s < n - i - 1; s++)
        {
            cout << " ";
        }
        char ch = 'A';
        int breakpoint = (2 * i + 1) / 2;
        // characters (2*i)+1
        for (int j = 1; j <= ((2 * i) + 1); j++)
        {
            cout << ch;
            if (j <= breakpoint)
                ch++;
            else
                ch--;
        }

        // spaces n-i-1(i=0)
        for (int s = 0; s < n - i - 1; s++)
        {
            cout << " ";
        }
        cout << endl;
    }
}
```

```cpp
void print18(int n)
{
    /*
    0 E
    1 DE
    2 CDE
    3 BCDE
    4 ABCDE
    */
    for (int i = 0; i < n; i++)
    {
        for (char ch = 'E' - i; ch <= 'E'; ch++)
        {
            cout << ch;
        }
        cout << endl;
    }
}
```


```cpp
void print19(int n)
{
    /*      [stars,spaces,stars]
    0 **********  5,0,5
    1 ****  ****  4,2 4
    2 ***    ***  3,4,3
    3 **      **  2,6,2
    4 *        *  1,8,1
    5 *        *---- symmetry 1,8,1
    6 **      **  2,6,2
    7 ***    ***  3,4,3
    8 ****  ****  4,2,4
    9 **********  5,0,5
    */
    int iniS = 0;
    for (int i = 0; i < n; i++)
    {
        // stars
        for (int j = 1; j <= n - i; j++)
        {
            cout << "*";
        }
        // spaces n-2i
        for (int j = 0; j < iniS; j++)
        {
            cout << " ";
        }
        // stars
        for (int j = 1; j <= n - i; j++)
        {
            cout << "*";
        }
        iniS += 2;
        cout << endl;
    }
    iniS = 8;
    for (int i = 1; i <= n; i++)
    {
        // stars
        for (int j = 1; j <= i; j++)
        {
            cout << "*";
        }
        // spaces n-2i
        for (int j = 0; j < iniS; j++)
        {
            cout << " ";
        }
        // stars
        for (int j = 1; j <= i; j++)
        {
            cout << "*";
        }
        iniS -= 2;
        cout << endl;
    }
}
```


```cpp
void print20(int n)
{
    /*
    1 *        *  1,8,1
    2 **      **  2,6,2
    3 ***    ***  3,4,3
    4 ****  ****  4,2,4
    5 **********  5,0,5
    6 ****  ****  4,2,4 (row==n/2)
    7 ***    ***  3,4,3
    8 **      **  2,6,2
    9 *        *  1,8,1
     */
    // Outer loop: 2n-1
    int spaces = 2 * n - 2;
    for (int i = 1; i <= 2 * n - 1; i++)
    {
        int stars = i;
        if (i > n)
            stars = 2 * n - i;

        // stars
        for (int j = 1; j <= stars; j++)
        {
            cout << "*";
        }
        // spaces
        for (int j = 1; j <= spaces; j++)
        {
            cout << " ";
        }

        // stars
        for (int j = 1; j <= stars; j++)
        {
            cout << "*";
        }
        cout << endl;
        if (i < n)
            spaces -= 2;
        else
            spaces += 2;
    }
}
```

```cpp
void print21(int n)
{
    /*
      0123
    0 ****
    1 *  *
    2 *  *
    3 ****
    */
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (i == 0 || j == 0 || i == n - 1 || j == n - 1)
            {
                cout << "*";
            }
            else
                cout << " ";
        }
        cout << endl;
    }
}
```

```cpp
void print22(int n)
{
    /*
      1 2 3 4 5 6 7
    -----------------
    1| 4 4 4 4 4 4 4
    2| 4 3 3 3 3 3 4
    3| 4 3 2 2 2 3 4
    4| 4 3 2 1 2 3 4
    5| 4 3 2 2 2 3 4
    6| 4 3 3 3 3 3 4
    7| 4 4 4 4 4 4 4
    */
    for (int i = 0; i < 2 * n - 1; i++)
    {
        for (int j = 0; j < 2 * n - 1; j++)
        {
            int top = i;
            int left = j;
            int right = (2 * n - 2) - j;
            int down = (2 * n - 2) - i;
            cout << (n - min(min(top, down), min(left, right)));
        }
        cout << endl;
    }
}
```

</b>

