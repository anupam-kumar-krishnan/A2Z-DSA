# _Switch_
### _Problem Statement_
<b>

```
Take the day no and print the corresponding day
For 1 Print Monday,
For 2 Print Tuesday and so on for 7 print Sunday
```


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
        cout << "OOPs!! Wrong Input";
    }
return 0;
}
```
</b>
