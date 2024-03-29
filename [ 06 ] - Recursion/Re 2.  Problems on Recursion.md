## _Basic Recursion Problems_
### _Print Name 5 times_

<b>

```cpp
int printFiveTimes(int i, int n)
{
    if (i > n)
        return 0;
    cout << "Anupam" << endl;
    printFiveTimes(i + 1, n);
}

int main()
{
    int n;
    cin >> n;
    printFiveTimes(1, n);
}
// Time Complexity: O(N)
// Space Complexity: O(N)
```
</b>

### _Print Linearly from 1 to N_

<b>

```cpp
int printLinearly(int i, int n)
{
    if (i > n)
        return 0;
    cout << i << " ";
    printLinearly(i + 1, n);
}

int main()
{
    int n;
    cin >> n;
    printLinearly(1, n);
}
```
</b>

### _Print in terms of N to 1_

<b>

```cpp
int printFromNToOne(int i, int n)
{
    if (i < 1)
        return 0;
    cout << i << endl;
    printFromNToOne(i - 1, n);
}

int main()
{
    int n;
    cin >> n;
    printFromNToOne(n, n);
    return 0;
}
```
</b>


###  _My Aproach: Print in terms of N to 1_

<b>

```cpp
int printFromNToOne(int n, int i)
{
    if (n < i)
        return 0;
    cout << n << endl;
    printFromNToOne(n - 1, i);
}

int main()
{
    int n;
    cin >> n;
    printFromNToOne(n, 1);
    return 0;
}
```
</b>

### _Print from 1 to N (Without using f(i+1,n))_

<b>

```cpp
int printFromOneToNW(int i, int n)
{
    if (i < 1)
        return 0;
    printFromOneToNW(i-1, n);
    cout<<i;
}

int main()
{
    int n;
    cin >> n;
    printFromOneToNW(n, n);
    return 0;
}
```
</b>


### _Print N to 1 using recursion but with backtracking_

<b>

```cpp
void printOneToNWithBacktracking(int i, int num)
{
    if(i>num)
       return;
    printOneToNWithBacktracking(i+1, num);
    cout<<i;
}

main()
{
  printOneToNWithBacktracking(1, num);
}
```
</b>











