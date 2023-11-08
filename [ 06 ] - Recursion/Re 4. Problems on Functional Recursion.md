## _Reverse an array (using Recursion)_

![reverse array](https://github.com/anupam-kumar-krishnan/A2Z-DSA/assets/69143883/da2f0aa6-733b-4151-9a03-8b465bdd82a2)


### _Using Two Pointers Method_

<b>

```cpp
f(l,r)
{
  if(l>=r) return;
  swap(a[l], a[r]);
  f(l+1, r-1);
}

main()
{
  arr // take array input
  f(0, n-1);
}
```

### _Using One Pointer Method_

![one pointer-one](https://github.com/anupam-kumar-krishnan/A2Z-DSA/assets/69143883/ad4064ef-3637-435c-8474-70e9b5664b45)

```cpp
f(i)
{
  if(i>=n/2)
     return;
   swap(a[i], a[n-i-1]);
   f(i+1);
}

main()
{
   arr; //take array input
   f(0);
}
```

</b>


