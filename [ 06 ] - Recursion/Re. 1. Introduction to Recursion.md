# _Recursion_
- _**When a function calls itself until a specified condition is met**_
- Without a _**terminating condition**_, recursion is not written as it would end up doing _**StackOverflow**_


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
</b>

![recursion](https://github.com/anupam-kumar-krishnan/A2Z-DSA/assets/69143883/dcc01b7a-faab-403e-b4cd-90b80d392d67)

## _StackOverflow_
- Happen when there is no terminating condition, that's why recursion has a termination condition

![WhatsApp Image 2023-11-06 at 11 02 20 PM](https://github.com/anupam-kumar-krishnan/A2Z-DSA/assets/69143883/332aa3c5-bfae-4ca8-8eec-c62943ddc7ec)

## _Recursion_
- This is Recursion in true form, calling the function itself until the condition is met
- The condition which is used to stop the calling of the function itelf is called the **_Base Condition._**

<b>

```cpp
cnt = 0 // Initially the cnt is zero

void f()
{
  if( cnt == 3 ) // this specified condition is called "Base Condition"
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
```
</b>

## _Recursion Tree_

![WhatsApp Image 2023-11-06 at 11 24 39 PM](https://github.com/anupam-kumar-krishnan/A2Z-DSA/assets/69143883/94c2619b-ea90-4911-88f5-f63fab5abf0a)



