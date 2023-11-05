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

## _Palindrome_

```cpp
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    int revnum = 0;
    int dup = n;
    while (n > 0)
    {
        int ld = n % 10;
        revnum = (revnum * 10) + ld;
        n = n / 10;
    }

    if (dup == revnum)
        cout << "Palindrome";
    else
        cout << "Not a Palindrome";

    return 0;
}
```

## _Armstrong_

```cpp
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    int sum = 0, dup=n;
    
    while (n > 0)
    {
        int ld = n % 10;
        sum = sum + (ld*ld*ld);
        n=n/10;
    }
    
    if(sum==dup)
     cout << "true";
    else 
     cout<<"false";
     
    return 0;
}
```

## _All Divisors_

```cpp
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    for (int i = 1; i <= n; i++)
    {
        if (n % i == 0)
        {
            cout << i << endl;
        }
    }

    return 0;
} // TC: O(n)
```

## _Optimized All Divisors_

```cpp
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<int> ls;

    // O(sqrt(n))
    for (int i = 1; i * i <= n; i++)
    {
        if (n % i == 0)
        {
            ls.push_back(i);
            if ((n / i) != i)
            {
                ls.push_back(n / i);
            }
        }
    }

    // TC of sort function: O(nlog(n)) 
    // i.e. O(no. of factors * log(no. of factors))
    // n is the number of factors
    sort(ls.begin(), ls.end());
    // O(number of factors)
    for (auto i : ls)
        cout << i << " ";

    return 0;
}
```

## _Prime Number_

```cpp
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n, cnt = 0;
    cin >> n;

    // Time Complexity: O(n)
    // O(sqrt(n))
    for (int i = 1; i * i <= n; i++)
    {
        if (n % i == 0)
        {
            cnt++;
            if ((n / i) != i)
            {
                cnt++;
            }
        }
    }

    if (cnt == 2)
        cout << "Prime";
    else
        cout << "Not Prime";
    return 0;
}
```

## _Greatest Common Divisor (GCD)_

```cpp
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n1, n2, gcd = 1;
    cin >> n1 >> n2;
    for (int i = 1; i <= min(n1, n2); i++)
    {
        if (n1 % i == 0 && n2 % i == 0)
        {
            gcd = i;
            cout << gcd << endl;
        }
    }

    return 0;
}
```

## _Equilidean Algorithm_
- gcd(a,b) -> gcd(a-b, b) ... -> 0
- _**Greater % Smaller**_ -> _**If One of then is Zero**_ -> _**The Other is GCD**_

```cpp
int gcd(int a, int b)
{
   while(a > 0 && b > 0)
   {
     if(a > b) 
       a = a % b;
     else      
       b = b % a;
   }
   
   if(a==0) return b;
   return a;
}  
```


![Screenshot 2023-11-05 230054](https://github.com/anupam-kumar-krishnan/A2Z-DSA/assets/69143883/ff71c153-14f0-4d44-91e6-276f0b4ad9fe)


</b>














