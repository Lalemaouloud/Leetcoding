'''
EASY

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}#hashmap
        for i, num in enumerate(nums):
            difference = target - num
            if difference in prevMap: 
                return prevMap[difference], i #the solution
            prevMap[num] = i


#C++ solution 

'''



#include <vector>
#include <unordered_map>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        std::unordered_map<int, int> previousMap;  // hashmap to store number and its index
        for (int i = 0; i < nums.size(); ++i) {
            int difference = target - nums[i];
            if (previousMap.find(difference) != previousMap.end()) {
                return {previousMap[difference], i};  // the solution
            }
            previousMap[nums[i]] = i;
        }
        return {};  // return an empty vector if no solution is found for the given nums - target 
    }
};



'''
