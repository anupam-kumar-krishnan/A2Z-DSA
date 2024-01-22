## _Functions_
- Function are set of code which performs something for you
- Functions are used to modularise code
- Functions are used to increase readability
- Functions are used to use same code multiple times

### _Mainly there are 4 types of functions:_
- void -> which does not returns anything
- return ->  
- parameterised -> 
- non parameterised -> 

<b>

### _void function_

```cpp
#include<bits/stdc++.h>
using namespace std;
void printName(){
    cout<<"hey Striverr!";
}

int main(){
  printName(); // hey Striverr!
  return 0;
}
```

### _parameterised function_

```cpp
#include<bits/stdc++.h>
using namespace std;
void printName(string name){
  cout<<"hey "<<name;
}

int main(){
    string name;
    cin>> name; // striverr
    printName(name); // hey striverr
    return 0;
}
```

## _reusability_

```cpp
#include<bits/stdc++.h>
using namespace std;
void printName(string name){
  cout<<"hey "<<name;
}

int main(){
    string name;
    cin>> name; // striverr
    printName(name); // hey striverr
   
    string name2;
    cin>>name2; // raj
    printName(name2); // hey raj
    return 0;
}
```

## _Take two numbers and print its Sum_

```cpp
#include <bits/stdc++.h>
using namespace std;
int sumoftwo(int num1, int num2){
    int num3 = num1 + num2;
    return num3;
}

int main(){
    int num1, num2;
    cin >> num1 >> num2;
    int res = sumoftwo(num1, num2);
    cout << res;
    return 0;
}
```






</b>
