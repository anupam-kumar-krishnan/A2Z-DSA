# _Recursion_
- _**When a function calls itself until a specified condition is met**_

<b>

```cpp
void f()
{
  cout << "1" << endl;
  f();
}
main()
{
  f();
}

```
![recursion](https://github.com/anupam-kumar-krishnan/A2Z-DSA/assets/69143883/dcc01b7a-faab-403e-b4cd-90b80d392d67)

```cpp
cnt = 0 // Initially the cnt is zero

void f()
{
  if( cnt == 4 ) // specified condition
    return;
  cout<<cnt;
  cnt++;
  f();
}

main()
{
   f();
}

// Output
// 0
// 1
// 2
// 3
```



</b>


