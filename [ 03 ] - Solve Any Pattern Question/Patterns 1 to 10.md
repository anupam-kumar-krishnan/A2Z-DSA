<b>

## _Pattern 1_

```cpp
****
****
****
****
```


```cpp
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
```

## _Pattern 2_

```cpp
*
**
***
****
```


```cpp
void printPattern2(int n)
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
```

## _Pattern 3_

```cpp
1
12
123
1234
12345
```

```cpp
void printPattern3(int n)
{
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

## _Pattern 4_

```cpp
1
22
333
4444
55555
```

```cpp
void printPattern4(int n)
{
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
## _Pattern 5_
```cpp
*****
****
***
**
*
```

```cpp
void printPattern5(int n)
{
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n - i + 1; j++)
        {
            cout << "*";
        }
        cout << endl;
    }
}
```

## _Pattern 6_

```cpp
12345
1234
123
12
1
```

```cpp
void printPattern6(int n)
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
```

## _Pattern 7_
```cpp
    *    
   ***   
  *****  
 ******* 
*********
```


```cpp
void printPattern7(int n)
{
    for (int i = 0; i < n; i++)
    {
        // space
        for (int j = 0; j < n - i - 1; j++)
        {
            cout << " ";
        }

        // stars
        for (int j = 0; j < 2 * i + 1; j++)
        {
            cout << "*";
        }

        // space
        for (int j = 0; j < n - i - 1; j++)
        {
            cout << " ";
        }
        cout << endl;
    }
}
```

## _Pattern 8_
```cpp
*********
 ******* 
  *****  
   ***   
    *    
```


```cpp
void printPattern8(int n)
{
    for (int i = 0; i < n; i++)
    {
        // space
        for (int j = 0; j < i; j++)
        {
            cout << " ";
        }

        // stars
        for (int j = 0; j < 2 * n - (2 * i + 1); j++)
        {
            cout << "*";
        }

        // space
        for (int j = 0; j < i; j++)
        {
            cout << " ";
        }
        cout << endl;
    }
}
```

## _Pattern 9_
```cpp
    *    
   ***   
  *****  
 ******* 
*********
*********
 ******* 
  *****  
   ***   
    *    
```


```cpp
void printPattern9(int n)
{
    printPattern7(n);
    printPattern8(n);
}
```

## _Pattern 10_
```cpp
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

```cpp
void printPattern10(int n)
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
```

## _Initial main code_
```cpp
int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        int n;
        cin >> n;

        printPattern10(n);
    }
}
```


</b>
