# _Multiple Recursion Calls_

## _Fibonacci_
_0 1 1 2 3 5 8 13 21 34 ......_ 

 0 = 0th Fibonacci Number <br>
 1 = 1st <br>
 1 = 2nd <br>
 2 = 3rd <br>
 3 = 4th <br>

```cpp
f[0]=0  f[1]=1

for(i = 2->n)
 f[i] = f[i-1] + f[i-2]
```

- f(n) -> f(n-1) + f(n-2)

```cpp
f(n)
{
 if(n<=1)
   return n;
 return f(n-1) + f(n-2);
}
```

```cpp
f(n)
{
 if(n<=1)
   return n;
 last = f(n-1)
 start = f(n-2)
 return last + start;
}

main()
{
  n; //4
  print(f(4));
}
```

## _Code_

```cpp
int fibonacci(int n)
{
 if(n<=1)
   return n;
 int last = fibonacci(n-1);
 int start = fibonacci(n-2);
 return last + start;
}

int main()
{
  int n; //4
  cin>>n;
  cout<<fibonacci(4);
  return 0;
}

// Time Complexity
// (2^n) Exponential
```














