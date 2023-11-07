## _Summation of first N numbers_
- Parameter
- Functional

i.e N = 3, Output = 1 + 2 + 3 = 6 

<b>

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



