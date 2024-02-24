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
f(i, arr, n)
{
  if(i>=n/2)
     return;
   swap(a[i], a[n-i-1]);
   f(i+1, arr, n);
}

main()
{  
   n;    // take input
   arr[n];  // take array input
   f(0, arr, n);
}
```


## _Code using One Pointer_

```cpp
void onepointerreversearray(int i, int arr[], int n){
 if(i>= n/2) return;
 swap(arr[i], arr[n-i-1]);
  onepointerreversearray(i+1, arr, n);
}

int main()
{
 int n;
 cin>>n;
 int arr[n];
 for(int i=0;i<n;i++)
   cin >> arr[i];
 onepointerreversearray(0, arr, n);
 for(int i=0;i<n;i++) 
   cout << arr[i] << " ";
 return 0;
}
```
</b>

## _Check if String is Palindrome or not_
- A string on reversal reads the same e,g, **_MADAM_**, **_11211_**
- Instead of swapping, check if they are equal

<b>

```cpp
f(i)
{
 if(i>=n/2) return true;
 if(s[i] != s[n-i-1])
   return false;
 return f(i+1);
}

main()
{
  cout << f(0);
}
```

### _Code_

```cpp
bool f(int i, string &s){
  if(i>= s.size() / 2) return true;
  if(s[i] != s[s.size() - i - 1]) return false;
  return f(i+1, s);
}

int main()
{
  string s="madam";
  cout<< f(0, s);
  return 0;
}
// TC -> n/2
// SC -> n/2
```



</b>










