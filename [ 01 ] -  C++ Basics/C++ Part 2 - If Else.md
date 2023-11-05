### _Write a program that takes an input of age and prints if you are adult or not_
<b>

```cpp
#include<bits/stdc++.h>
using namespace std;
int main()
{
  int age;
  cin>>age;

  if(age >= 18)
      cout<<"You are an Adult";
  else
      cout<<"You are Not an Adult";
  return 0;
}
```

### _A school has following rules for grading system:_
```
a. Below 25 - F
b. 25 to 44 - E
c. 45 to 49 - D
d. 50 to 59 - C
e. 60 to 79 - B
f. 80 to 100 - A
```
Ask user to enter marks and print the corresponding grade.

```cpp
#include<bits/stdc++.h>
using namespace std;

int main()
{
 int marks;
 cin>>marks;
 if(marks<25)
  cout<<"F";
 if(marks>=25 && marks<=44)
  cout<<"E";
 if(marks>=45 && marks<=49)
  cout<<"D";
 if(marks>=50 && marks<=59)
  cout<<"C";
 if(marks>=60 && marks<=79)
  cout<<"B";
 if(marks>=80 && marks<=100)
  cout<<"A";
 return 0;
}
```
Here, all the ifs are running even if they get the result

## _This is not the best way, Why?_
Suppose, you take 86
- first iteration - False
- second iteration - False
- third iteration - False
- fourth iteration - False
- fifth iteration - False
- sixth iteration - True

Again Suppose, 24
- first iteration - True
- second iteration - False
- third iteration - False
- fourth iteration - False
- fifth iteration - False
- sixth iteration - False

First got True but still all the ifs excuted and results false in iteration(time consuming)

## _Better way_
- use else if to skip iterations(less time consuming)

```cpp
#include<bits/stdc++.h>
using namespace std;

int main()
{
 int marks;
 cin>>marks;
 if(marks<25)
  cout<<"F";
 else if(marks>=25 && marks<=44)
  cout<<"E";
 else if(marks>=45 && marks<=49)
  cout<<"D";
 else if(marks>=50 && marks<=59)
  cout<<"C";
 else if(marks>=60 && marks<=79)
  cout<<"B";
 else if(marks>=80 && marks<=100)
  cout<<"A";
 return 0;
}
```

### _Even Better Way_
- this get clear idea to remove the and and makes the code short (even less time consuming compare to && above)

```cpp
#include<bits/stdc++.h>
using namespace std;

int main()
{
 int marks;
 cin>>marks;
 if(marks<25)
  cout<<"F";
 else if(marks<=44)
  cout<<"E";
 else if(marks<=49)
  cout<<"D";
 else if(marks<=59)
  cout<<"C";
 else if(marks<=79)
  cout<<"B";
 else if(marks<=100)
  cout<<"A";
 return 0;
}
```

### _Take the age from the user amd then decide accordingly_
1. If age < 18
   print -> "not eligible for job"
2. If age >= 18
   print -> "eligible for job"
3. If age >= 55 and age <= 57
   print -> "eligible for job, but retirement soon."
4. If age > 57
   print -> "retirement time"

```cpp
#include <bits/stdc++.h>
using namespace std;
int main()
{
    int age;
    cin >> age;
    if (age < 18)
        cout << "Not Eligible for job";
    else if (age >= 18 && age <= 54)
        cout << "eligible for job";
    else if (age <= 57)
        cout << "eligible for job, but retirement soon.";
    else 
        cout << "Retirement Time";
}
```
```cpp
#include <bits/stdc++.h>
using namespace std;
int main()
{
    int age;
    cin >> age;
    if (age < 18)
        cout << "Not Eligible for job";
    else if (age <= 57){
        cout << "eligible for job";
        if(age >=55){
            cout << "eligible for job, but retirement soon.";
        }
    } 
    else 
        cout << "Retirement Time";
}
```
























</b>

