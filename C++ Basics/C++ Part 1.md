<b>


### _Why #include<bits/stdc++.h>?_
- Instead of writing one library for a single operation, at the end it will become big in numbers
- Hence, to conclude everything in a single library, there is `#include<bits/stdc++.h>` for us

### _\n vs endl_
- `\n` is faster than `endl`


### _Without using namespace_

```cpp
#include <bits/stdc++.h>
int main()
{
     std::cout << "Hey without using namespace std";
     return 0;
}
//cout is a function which is under std

```

###  _Using namespace_

```cpp
#include <bits/stdc++.h>
using namespace std;

int main()
{
     cout << "Hey using namespace std";
     return 0;
}
```

### _Print Value of X_

```cpp
#include <bits/stdc++.h>
using namespace std;

int main()
{
     int x;
     cin>>x;
     cout << "Value of X: "<<x;
     return 0;
}
```
```cpp
#include <bits/stdc++.h>
using namespace std;

int main()
{
     int x,y;
     cin>>x>>y;
     cout << "Value of X: "<<x <<" and Value of Y: "<<y;
     return 0;
}
```

## _Data types_
| Type Name | Bytes | Range |
| --- | --- | --- |
| unsigned short | 2 | 0 to 65,535 |
| int | 4 | -2,147,483,648 to 2,147,483,647 |
| unsigned long | 4 | 0 to 4,294,967,295 |
| long long | 8 | -9,223,372,036,854,775,808 to -9,223,372,036,854,775,807 |
| float | 4 | 1.2E-38 to 3.4E+38 |
| double | 8 | 2.3E-308 to 1.7E+308 |
| long double | 10 | 3.4E-4932 to 1.1E+4932 |

### _float_

```cpp
#include <iostream>
using namespace std;

int main()
{
    float x = 5.6;
    float y = 5;
    cout << "x: " << x << endl
         << "y: " << y;
}
// x: 5.6
// y: 5
```

```cpp
#include <iostream>
using namespace std;

int main()
{
    string s;
    cin >> s;
    cout << s;
}
//input: hey striverr
//output: hey
```

```cpp
#include <iostream>
using namespace std;

int main()
{
    string s1, s2;
    cin >> s1 >> s2;
    cout << s1 << " " << s2;
}

//input: hey striverr
//output: hey striverr
```
### _getline_

```cpp
#include <bits/stdc++.h>
using namespace std;

int main()
{
    string str;
    getline(cin, str);
    cout << str;
    return 0;
}

// picks only till the line break
// input: Hey Striverr Raj
// output: Hey Striverr Raj
```

### _char_ (256 characters in English)
- Always in single Quote

```cpp
#include <bits/stdc++.h>
using namespace std;
int main()
{
    char ch = 'g';
    cout << ch;
}
// g
```

### _Why can't we store suppose 10 i.e. ten in any datatype like long long_

- It's because long long may end up taking a lot of space in compare to a integer



</b>
