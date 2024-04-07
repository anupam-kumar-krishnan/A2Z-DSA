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
int sum(int a, int b){
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

### 🎯 _Note: Before learning `containers`, learn `pairs`(a part of utility library)_

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
  ls.emplace_front(); // {2,4};

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
- FIFO (First In First Out)

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

## _Priority Queue_
- As the name suggests i.e. Priority, the guys which has the largest value stays at the top
- Data is not stored in a linear fashion (inside a tree is maintained)
- Main functions: push, top, pop
- Max Heap and Min Heap
- push -> log n
- top  -> O(1)
- pop  -> log n



```cpp
void explainPQ(){
 // Maximum Heap
  priority_queue<int>pq;
  
  pq.push(5); // {5}
  pq.push(2); // {5, 2}
  pq.push(8); // {8, 5, 2}
  pq.emplace(10); // {10, 8, 5, 2}
  
  cout<<pq.top(); // prints 10

  pq.pop(); // {8, 5, 2}

  cout<< pq.top(); // prints 8

  // size swap empty function same as others
  
  // Minimum Heap
  priority_queue<int, vector<int>, greater<int>> pq;
  pq.push(5); // {5}
  pq.push(2); // {2, 5}
  pq.push(8); // {2, 5, 8}
  pq.emplace(10); // {2, 5, 8, 10}

  cout<< pq.top(); // prints 2
}
```

## _Set_
- Stores Everything in sorted order
- Everything is unique
- in Set, Everything happens in log(n) time complexity


```cpp
void explainSet(){
  set<int>st;
  st.insert(1); // {1}
  st.emplace(2); // {1, 2}
  st.insert(2); // {1, 2} - didn't store 2 again as it stores only unique
  st.insert(4); // {1, 2, 4}
  st.insert(3); // {1, 2, 3, 4}

  // Functionality of insert in vector
  // can be used also, that only increases
  // efficiently

  // begin(), end(), rbegin(), rend(), size(),
  // empty() and swap are same as those of above

  // {1, 2, 3, 4, 5}
  auto it = st.find(3); // returns an iterator which points to 3

  // {1, 2, 3, 4, 5}
  auto it = st.find(6); // if element is not in the set | st.end()
  
  // {1, 4, 5}
  st.erase(5); // erases 5 // takes logarithmic time

  int cnt = st.count(1); // if exists -> 1 occurance only, else 0
  
  auto it = st.find(3);
  st.erase(it); // it takes constant time

  // {1, 2, 3, 4, 5}
  auto it1=st.find(2);
  auto it2=st.find(4);
  st.erase(it1, it2); // after erase {1, 4, 5} {first, last}
  
  // lower_bound() and upper_bound() function works in the same way
  // as in vector it does

  // this is the syntax
  auto it = st.lower_bound(2);
  auto it = st.upper_bound(3); 
}
```

## _Multiset_
- Everything is same as set
- Only difference is it stores duplicate elemets also

```cpp
void explainMultiSet(){
 multiset<int>ms;
   ms.insert(1);
   ms.insert(1);
   ms.insert(1);

   ms.erase(1);

   int cnt = ms.count(1);

   // only a single one erased
   ms.erase(ms.find(1));

   ms.erase(ms.find(1), ms.find(1)+2);

   // rest all function same as set
}
```

## _Unordered Set_
- Only thing which is different, is that it doesn't save in a sorted order
- It will have unique elements


```cpp
void explainUnorderedSet(){
 unordered_set<int> st;
 // lower_bound and upper_bound function
 // doest not works, rest all functions are same
 // as above, it does not stores in any
 // particular order it has a better complexity
 // rthan set in most cases, except some when collision happens
}
```

##  _Map_
- everything is in form of {key, value}
- Map stores unique keys
- Everything is stored in sorted order of key


```cpp
void explainMap(){
 map<int, int> map;
 map<int, pair<int, int>> mpp;
 map pair<int, int>, int> mpp;
 
 mpp[1] = 2;
 mpp.emplace({3, 1});
 mpp.insert({2, 4});
 mpp({2, 3}) = 10;
 {
   {1, 2}
   {2, 4}
   {3, 1}
 }

 for(auto it:mpp){
   cout<< it.first << " " << it.second << endl;
 }

 cout<<mpp[1];
 cout<<mpp[5];
 
 auto it = mpp.find(3);
 cout<< *(it).second;
 
 auto it = mpp.find(5); // if doesn't find 5, points to end after the map
 
 // This is syntax
 auto it = mpp.lower_bound(2);
 auto it = mpp.upper_bound(3);

 // erase, swap, size, empty, are same as above
```

## _Multimap_
- Everything is same as map, only it can store multiple keys
- Only map[key] cannot be used here
- Can store duplicate keys, but everything in a sorted order


## _Unordered Map_
- Same as set and unordered_Set difference.
- Difference is Map works in Logarithmic time log(n) while unordered Map works in Constant Time O(1)

## _Algorithms_
- Sorting

```cpp
bool comp(pair<int, int> p1, pair<int, int> p2){
  if(p1.second < p2.second) return true;
  if(p1.second > p2.second) return false;
  
  // they are same
  
  if(p1.first > p2.first) return true;
  return false;
}

void explainExtra(){
 sort(a, a+n); // sort in ascending order
 sort(v.begin(), v.end());
 
 sort(a+2, a+4); // sorting only for a particular portion
 sort(a, a+n, greater<int>); // sort in descending order

 pair<int, int> a[] = {{1, 2}, {2, 1}, {4, 1}};

 // sort it according to second element
 // if second element is same, then sort
 // it according to first element but in descending

  sort(a, a+n, comp);  // Here comp means self written "comparator"
  // {{4,1}, {2,1}, {1,2}};

  int num=7;
  int cnt = __builtin_popcount(); // In binary 7 is | 1 1 1 |
  // builtin_popcount says how manys one's are there 
  // here the answer will be 3(for 7)

  long long num = 165786578687;
  int cnt = __builtin_popcountll(); // for long long ll wil be added in builtin_popcount

  // NEXT PERMUTATION
  string s="123";
  sort(s.begin(), s.end());


  do {
   cout<< s << endl;
  } while(next_permutation(s.begin(), s.end()));

  int maxi = *max_element(a, a+n);
}
```









































</b>


