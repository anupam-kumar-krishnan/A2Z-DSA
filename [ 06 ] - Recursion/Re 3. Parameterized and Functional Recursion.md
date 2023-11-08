## _Summation of first N numbers_
- Parameter
- Functional

i.e N = 3, Output = 1 + 2 + 3 = 6 

<b>

## _Parameterised Recursion_

```cpp
void sumn(int i, int sum)
{
   if(i<1)
   {
     cout<<sum;
     return;
   }
  f(i-1, sum+i);
}

int main()
{
  int n;
  cin>>n;
  sumn(n,0);
}
```
</b>

## _Functional Recursion_

- n=3
- 3 + f(2)
- f(n) -> Sum of first n numbers
- Similarly, if n=2, then 2 + f(1)

<b>

```cpp
f(n)
{
 if(n==0)
   return 0;
 return n + f(n-1);
}

main()
{
 n
 print(f(n));
}
```

### _Explanation_

![functional way](https://github.com/anupam-kumar-krishnan/A2Z-DSA/assets/69143883/0dd6047b-0a6f-4ac9-8043-890cd36e4e6b)


</b>

















