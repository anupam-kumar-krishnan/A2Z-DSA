# _Basic Math Concept_

## _Digit Concept_

- N = 7789
- _**Do extraction of digits:**_ All the digit individually
- Divide the number by 10

**Step 1:**  _**7789 % 10 = 9 (remainder)**_ |  **_778.9 (taking just the integer part i.e. 778)_** <br>
**Step 2:**  _**778 % 10  = 8**_ <br>
**Step 3:**  _**77 % 10   = 7**_ <br>
**Step 4:**  _**7 % 10    = 7**_  | 0.7 (Here, integer part is Zero)<br>
**Step 5:**  _**0**_

<b>

```cpp
while(N > 0){
 lastdigit = N % 10;
 N = N/10;
}
```
</b>

## _Problem based on this concept_

### _Count Digits_

<b>

```cpp
int countDigits(int n){	
       int cnt=0;

	while(n>0) {
	   cnt++;
	   n = n / 10;
	}
    return cnt;
}
```

### _Other Way_

```cpp
#include<bits/stdc++.h>
int count(int n){
   int cnt = (int)(log10(n) + 1);
   return cnt;
}
```

**_Time Complexity:_** O(log base 10 (N))

## _Reverse a Number_

```cpp
#include <bits/stdc++.h>
using namespace std;

int rev_num(int n)
{
    int revnum = 0;
    while (n > 0)
    {
        int ld = n % 10;
        n = n / 10;
        revnum = (revnum * 10) + ld;
    }
    return revnum;
}

int main()
{
    int n;
    cin >> n;
    cout << rev_num(n);

    return 0;
}
```



</b>














