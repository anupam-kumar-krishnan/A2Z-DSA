# _Starting from Basics ( C++ Basics )_

## _Data Types:_    
- int, long, long long,  float, double
- string and getline
- char - 256 charecter in english

##  _Q. Write a program that takes an input age and prints if you are an adult or not_
  `>=18, yes`
  `< 18, no`

<b>

```cpp
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int age;
    cout << "Enter your age: ";
    cin >> age;

    if (age >= 18)
    {
        cout << "You're an adult now";
    }
    else if (age < 18)
    {
        cout << "Not an adult";
    }
    return 0;
}
// if you are having an `if` it is not mandatory to have an `else` statement

```

## _A school has following rules for grading system:_
   - a. Below 25 - F
   - b. 25 to 44 - E
   - c. 45 to 49 - D
   - d. 50 to 59 - C
   - e. 60 to 79 - B
   - f. 80 to 100 - A
     Ask user to enter marks and print thr corresponding grade.

```cpp
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int marks;
    cin >> marks;

    if (marks < 25)
    {
        cout << "F";
    }
    else if (marks <= 44)
    {
        cout << "E";
    }
    else if (marks <= 49)
    {
        cout << "D";
    }
    else if (marks <= 59)
    {
        cout << "C";
    }
    else if (marks <= 79)
    {
        cout << "B";
    }
    else if (marks <= 100)
    {
        cout << "A";
    }

    return 0;
}
```

## _Take the age from the user and then decide accordingly_

1. If age < 18<br>
   print -> not eligible for job

2. If age >= 18 and age <= 54<br>
   print -> "eligible for job"

3. If age >= 55 and age <= 57<br>
   print -> "eligible for job, but retirement soon."

4. If age > 57<br>
   print -> "retirement time"

```cpp
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int age;
    cin >> age;
    if (age < 18)
    {
        cout << "not eligible for job";
    }
    else if (age <= 57)
    {
        cout << "eligible for job";
        if (age >= 55)
        {
            cout << "but retirement soon.";
        }
    }
    else
    {
        cout << "retirement time";
    }

    return 0;
}
```

## _Take the day no and print the corresponding day(switch case)_
 - For 1 print Mondy,
 - For 2 print Tuesday and so on for 7 print Sunday

```cpp
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int day;
    cin >> day;

    switch (day)
    {
    case 1:
        cout << "Monday";
        break;
    case 2:
        cout << "Tuesday";
        break;
    case 3:
        cout << "Wednesday";
        break;
    case 4:
        cout << "Thrusday";
        break;
    case 5:
        cout << "Friday";
        break;
    case 6:
        cout << "Saturday";
        break;
    case 7:
        cout << "Sunday";
        break;
    default:
        cout << "Invalid":
    }

    return 0;
}
```

## _Arrays - when the entire data is of similar type_

```cpp
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int arr[5];
    cin >> arr[0] >> arr[1] >> arr[2] >> arr[3] >> arr[4];

    arr[3] += 10;
    cout << arr[3] << endl;

    arr[3] = 16;
    cout << arr[3];
    return 0;
}
// Input 3 4 5 7 10
// Output 17 16
```

## _2D Array_

```cpp
#include <bits/stdc++.h>
using namespace std;

int main()
{
    // 2D Array
    int arr[3][5];

    arr[1][3] = 78;
    cout << arr[1][3];
    return 0;
}
```

## _String_

```cpp
#include <bits/stdc++.h>
using namespace std;

int main()
{
    // String
    string s = "Striver";
    int len = s.size();
    s[len - 1] = 'z';
    cout << s[len - 1];
}
```

## _For Loops_

```cpp
#include <bits/stdc++.h>
using namespace std;

int main()
{
    // For Loops
    for (int i = 1; i <= 10; i++)
    {
        cout << i << " "
             << "Striver" << endl;
    }
    return 0;
}
```

_**Output**_

```cpp
1 Striver
2 Striver
3 Striver
4 Striver
5 Striver
6 Striver
7 Striver
8 Striver
9 Striver
10 Striver
```

## _While Loop_

```cpp
#include <bits/stdc++.h>
using namespace std;

int main()
{
    // While Loops
    int i = 1;
    while (i <= 5)
    {
        cout << "Striver " << i << endl;
        i = i + 1;
    }
}
```

_**Output**_
```cpp
Striver 1
Striver 2
Striver 3
Striver 4
Striver 5
```

## _Do While Loop(Prints at least once)_

_**Code**_
```cpp
#include <bits/stdc++.h>
using namespace std;

int main()
{
    // Do While Loops
    int i = 2;
    do
    {
        cout << "Striver " << i << endl;
        i = i + 1;
    } while (i <= 1);
    cout << i;
}
```

_**Outputs**_
```
Striver 2
3
```

## _Functions_
- Functions are set of code which performs something for you
- Functions are used to modularise code
- Functions are used to increase readability
- Functions are used to use same code multiple times

### _Types of Functions:_
- <b>_void:_</b> Which does not return aything
- <b>_return:_</b>
- <b>_paramaterised:_</b>
- <b>_non paramaterised:_</b>

_**Code**_
```cpp
#include <bits/stdc++.h>
using namespace std;

// Functions are set of code which performs something for you
// Functions are used to modularise code
// Functions are used to increase readability
// Functions are used to use same code multiple times
// void -> which does not return aything
// return
// paramaterised
// non paramaterised

// void function example
void printName()
{
    cout << "hey Striverr!";
}

// paramaterised function example
void paraprintName(string name)
{
    cout << "hey Striverr! Name: " << name << endl;
}

int main()
{
    string name;
    cin >> name;
    printName();
    cout << endl;
    paraprintName(name); // void function

    string name2;
    cin >> name2;
    paraprintName(name2);
    return 0;
}
```

## _Sum Function_

```cpp
#include <bits/stdc++.h>
using namespace std;

// Take two numbers ad print its sum
int sum(int a, int b)
{
    return (a + b);
}

int main()
{
    int num1, num2;
    cin >> num1 >> num2;
    cout << "Sum: " << sum(num1, num2) << endl;
    return 0;
}
```

## _Minimum of two numbers_

```cpp
#include <bits/stdc++.h>
using namespace std;

int minn(int a, int b)
{
    if (a > b)
    {
        return b;
    }
    return a;
}

int main()
{
    int num1, num2;
    cin >> num1 >> num2;
    int minimum = minn(num1, num2);
    cout << "Minimum: " << minimum << endl;
    return 0;
}
```

## _Pass By Value_

```cpp
#include <bits/stdc++.h>
using namespace std;

// Pass By Value
void doSomething(int n)
{
    cout << n << endl;
    n += 5;
    cout << n << endl;
    n += 5;
    cout << n << endl;
}

int main()
{
    int num;
    cin >> num;

    doSomething(num); // this sends the copy, not the original value
    cout<< num;  // prints 5 if input is 5
  
    return 0;
}
```

**_Output_**
```cpp
// Input
5
// Output
5
10
15
5
```

## _Pass By Refernce_

```cpp
#include <bits/stdc++.h>
using namespace std;

// Pass By Refernce
void doSomething(string &s)
{
    s[0] = 't';
    cout << s << endl;
}

int main()
{
    string s = "raj";
    doSomething(s);
    cout << s << endl;
    return 0;
}

// Output
// taj
// taj
```


</b>
