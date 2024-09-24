# Medium Problems on Array

## 2Sum


[Leetcoode Link](https://leetcode.com/problems/two-sum/description/)

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

## Sort an array of 0s, 1s and 2s

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

## Stocks Buy and Sell

[Leetcode Link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)

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

## Rearrange Array Elements by Sign

[Leetcode Link](https://leetcode.com/problems/rearrange-array-elements-by-sign/description/)

<b>

```cpp
class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        
        int n=nums.size();
        vector<int> pos;
        vector<int> neg;
        

        for(int i=0;i<n;i++){
            if(nums[i]>0)
                pos.push_back(nums[i]);
            else
                neg.push_back(nums[i]);
        }

        for(int i=0;i<n/2;i++){
            nums[2*i] = pos[i];
            nums[2*i+1] = neg[i];
        }

        return nums;
        
    }
};
```
</b>

## Majority Elements

<b>

```cpp
int majorityElement(vector<int> v) {

	int n = v.size();

    for (int i = 0; i < n; i++) {

        int cnt = 0;
        for (int j = 0; j < n; j++) {
   
            if (v[j] == v[i]) {
                cnt++;
            }
        }


        if (cnt > (n / 2))
            return v[i];
    }

    return -1;
}
```
</b>

## Maximum Subarray

<b>
	
```cpp
int maxSubarraySum(int arr[], int n) {
    int maxi = INT_MIN; // maximum sum

    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            // subarray = arr[i.....j]
            int sum = 0;

            //add all the elements of subarray:
            for (int k = i; k <= j; k++) {
                sum += arr[k];
            }

            maxi = max(maxi, sum);
        }
    }

    return maxi;
}

```
</b>
