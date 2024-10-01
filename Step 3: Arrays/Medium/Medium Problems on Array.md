# _Medium Problems on Array_

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
int maxSubArray(vector<int>& nums) {
        int sum=0, maxi=INT_MIN;
        for(auto it : nums) {
            sum+=it;
            maxi=max(sum,maxi);
            if(sum < 0) sum=0;
        }
        return maxi;
}

```
</b>


## Next Permutation

```cpp
vector<int> nextGreaterPermutation(vector<int> &A) {
    int n = A.size(); 

    int ind = -1;
    for (int i = n - 2; i >= 0; i--) {
        if (A[i] < A[i + 1]) {
            ind = i;
            break;
        }
    }

    if (ind == -1) {
        reverse(A.begin(), A.end());
        return A;
    }

    for (int i = n - 1; i > ind; i--) {
        if (A[i] > A[ind]) {
            swap(A[i], A[ind]);
            break;
        }
    }

    reverse(A.begin() + ind + 1, A.end());

    return A;
}

int main()
{
    vector<int> A = {2, 1, 5, 4, 3, 0, 0};
    vector<int> ans = nextGreaterPermutation(A);

    cout << "The next permutation is: [";
    for (auto it : ans) {
        cout << it << " ";
    }
    cout << "]n";
    return 0;
}
```
