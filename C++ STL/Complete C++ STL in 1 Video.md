# _Standard Template Library (STL)_

<b>

## _Skleton Code_
```cpp
#include<bits/stdc++.h>
using namespace std;
int main()
{
 
return 0;
}
```

## _Void Function_
- A function which doesn't return anything

```cpp
#include<bits/stdc++.h>
using namespace std;
void print(){
    cout<<"Raj";
}

int main()
{
  print();
  return 0;
}
```


## _Return Type Function_
- A function which returns something
```cpp
#include<bits/stdc++.h>
using namespace std;
void sum(int a, int b){
    return a+b;
}

int main()
{
  int s=sum(4,5);
  cout<<s; //9

  return 0;
}
```

## _C++ STL is divided into 4 Parts_
- Algorithms
- Containers
- Functions
- Iterators

### 🎯 _Note: Before learning cotainers, learn pairs(a part of utility library)_

## _Pair_
- If you want to store couple of integers {1,3}, the only way we can store this is in a Pair

```cpp
pair<int, int> p = {1, 3};
cout<< p.first <<" "<<p.second; // 1 3
```

## _Nested Pair_

```cpp
pair<int, pair<int, int>> p = {1, {3, 4}};
cout << p.first << " " << p.second.first << " " << p.second.second << endl; // 1 3 4
```

## _Pair Array_

```cpp
pair<int, int> arr[] = {{1,2},{2,5},{5,1}}
cout<<arr[1].second; // 5
```
</b>


## _Vectors_
- Vector is a container which is **dynamic** in nature
- **emplace_back** is faster than **push_back**

<b>

```cpp
void explainVector(){
 v.push_back(1);
 v.emplace_back(2);
 
 vector.pair<int, int>vec;

 v.push_back({1,2});
 // In push_back, we need to write in curly brackets to make it a pair

 v.emplace_back(1, 2);  
 // In emplace_back, it automatically assumes it to be a pair without curly brackets

 vector<int> v(5, 100);
 // v(size, element) i.e. [100, 100, 100, 100, 100]
 
 vector<int> v(5); 
// without element will make a container with garbage value
 
 vector<int> v1(5, 20);
// [20, 20, 20, 20, 20]

 vector<int> v2(v1);
// copy of v1 is v2

vector<int>::iterator it = v.begin();
it++;

cout<< *(it) << " ";

```









</b>


