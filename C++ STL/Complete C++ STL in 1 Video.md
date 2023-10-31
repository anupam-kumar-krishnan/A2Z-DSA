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
 // VECTOR
 vector<int> v; //this creates an empty container

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
// even if I push an element after declaring vector, it will increase it's size accordingly
// that's why it is called dynamic in nature

 vector<int> v1(5, 20);
// [20, 20, 20, 20, 20]

 vector<int> v2(v1);
// copy of v1 is v2

// ITERATORS
// Iterators points to the memory address
vector<int>::iterator it = v.begin();
it++;
cout<< *(it) << " "; 
// in order to access anything in the memory address, put an astric(star)
// this will point to the value


it = it + 2;
cout << *(it) << " ";

vector<int>::iterator it = v.end(); // [10, 20, 30, 40] end will locate after 40
vector<int>::iterator it = v.rend(); // reverse end means here before 10 [10, 20, 30, 40]
vector<int>::iterator it = v.rbegin(); // reverse iterator

cout<< v[0] <<" " <<v.at(0);

cout<< v.back() << " "; // [10, 20, 30] Output: 30

// FOR LOOP 1
for(vector<int>::iterator it = v.begin(); it != v.end(); it++){
    cout<< *(it) << " ";
}

// FOR LOOP 2
// auto: according to data, datatype will be assigned automatically
for(auto it=v.begin(); it !=v.end();i++){ 
  cout<< *(it) <<" ";
}

// FOR LOOP 3
for(auto it : v){
  cout << it << " ";
}

// ERASE
// {10, 20, 12, 23}
v.erase(v.begin() + 1); // [10, 12, 23]

// {10, 20, 12, 23, 35}
v.erase(v.begin() + 2, v.begin() + 4) // {10, 20, 35} {start, end} | END IS NOT INCLUDED

// INSERT FUNCTION
vector<int>v(2, 100); //{100, 100}
v.insert(v.begin(), 300); //{300, 100, 100} - inserts at the start
v.insert(v.begin() + 1, 2, 10); // {300, 10, 10, 100, 100}
//{position, number of elements, the number} 

vector<int> copy(2, 50); //{50, 50}
v.insert(v.begin(), copy.begin(), copy.end()); // {50, 50, 300, 10, 10, 100, 100}

//{10, 20}
cout<<v.size(); // 2

// {10, 20}
v.pop_back(); // {10}

// v1 -> {10, 20}
// v2 -> {30, 40}
v1.swap(v2); // v1-> {30, 40} , v2 -> {10, 20}

v.clear(); // erases the entire vector

cout<<v.empty();

```

## _List_
- Insert function in a VECTOR is very costly

```cpp
void explainList(){
  list<int> ls;
 
  ls.push_back(2); // 2
  ls.emplace_back(4); // {2, 4}
  
  ls.push_front(5); // {5, 2, 4}
  ls.emplace_front(); {2,4};

  // rest functions same as vector
  // begin, end, rbegin, rend, clear, insert, size, swap
}
```

## _Deque_

```cpp
void explainDeque(){
   deque<int> dq;
   dq.push_back(1); // {1}
   dq.emplace_back(2); // {1, 2}
   dq.push_front(4); // {4, 1, 2}
   dq.emplace_front(3); // {3, 4, 1, 2}
```

## _Stack_
- LIFO (Last In First Out)

```cpp
void explainStack(){
    stack<int> st;
    st.push(1); // {1}
    st.push(2); // {2, 1}
    st.push(3); // {3, 2, 1}
    st.push(3); // {3, 3, 2, 1}
    st.emplace(5); // {5, 3, 3, 2, 1}
  
    cout<< st.top(); // prints 5 "==st[2] is invalid=="
   
    st.pop(); // st looks like {3, 3, 2, 1}

    cout<< st.top(); // 3
    cout<< st.size(); // 4
    cout<< st.empty(); // False - It has 4 elements
 
    stack<int>st1, st2;
    st1.swap(st2);
}
```

## _Queue_

```cpp
void explainQueue(){
    queue<int> q;
    q.push(1); // {1}
    q.push(2); // {1, 2}
    q.emplace(4); // {1, 2, 4}
    
    q.back() += 5;

    cout<<q.back(); // prints 9

    // 0 is {1, 2, 9}
    cout<< q.front(); // prints 1

    q.pop(); // {2, 9}

    cout<<q.front(); // prints 2
  
    // size swap empty same as stack
}

```






















</b>


