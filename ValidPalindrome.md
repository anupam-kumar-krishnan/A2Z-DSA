## Valid Palindrome

<b>

```cpp
class Solution {
public:
    bool isPalindrome(string s) {
        string nS = "";
        
        for(char c : s) {
            if(isalnum(c)){
              nS += tolower(c);
            }
        }

        string rev = nS;
        reverse(rev.begin(), rev.end());

        return nS == rev;
    }
};
```
</b>
