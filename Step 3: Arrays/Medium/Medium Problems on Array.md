# Medium Problems on Array

# 2Sum


[Leetcoode Problem Link](https://leetcode.com/problems/two-sum/description/)

<b>
  
```cpp
vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        for(int i = 0 ; i < n - 1 ; i++){
            for(int j = i + 1 ; j < n ; j++){
                if(nums[i] + nums[j] == target){
                  return {i,j};
                }
            }
        }
 return {};
}
```
</b>

# Sort an array of 0s, 1s and 2s

[Leetcode Link](https://leetcode.com/problems/sort-colors/description/)

<b>

```cpp
class Solution {
public:
    void sortColors(vector<int>& nums) {
        sort(nums.begin(), nums.end());
    }
};
```
</b>

# Best Time to Buy and Sell Stocks

<b>

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
    int maxPro = 0;
    int n = prices.size();
    int minPrice = INT_MAX;

    for (int i = 0; i < prices.size(); i++) {
        minPrice = min(minPrice, prices[i]);
        maxPro = max(maxPro, prices[i] - minPrice);
    }
    
    return maxPro;
    }
};
```
</b>
