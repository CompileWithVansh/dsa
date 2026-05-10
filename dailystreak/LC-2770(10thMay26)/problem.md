# Maximum Number of Jumps to Reach the Last Index

**LeetCode:** #2770
**Date:** 10thMay26
**Difficulty:** Medium
**Topics:** Array, Dynamic Programming
**Link:** https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/

## Problem Statement

You are given a **0-indexed** array `nums` of `n` integers and an integer `target`.

You are initially positioned at index `0`. In one step, you can jump from index `i` to any index `j` such that:

	- `0 <= i < j < n`

	- `-target <= nums[j] - nums[i] <= target`

Return *the **maximum number of jumps** you can make to reach index* `n - 1`.

If there is no way to reach index `n - 1`, return `-1`.

á

Example 1:

```
Input: nums = [1,3,6,4,1,2], target = 2
Output: 3
Explanation: To go from index 0 to index n - 1 with the maximum number of jumps, you can perform the following jumping sequence:
- Jump from index 0 to index 1. 
- Jump from index 1 to index 3.
- Jump from index 3 to index 5.
It can be proven that there is no other jumping sequence that goes from 0 to n - 1 with more than 3 jumps. Hence, the answer is 3.
```

Example 2:

```
Input: nums = [1,3,6,4,1,2], target = 3
Output: 5
Explanation: To go from index 0 to index n - 1 with the maximum number of jumps, you can perform the following jumping sequence:
- Jump from index 0 to index 1.
- Jump from index 1 to index 2.
- Jump from index 2 to index 3.
- Jump from index 3 to index 4.
- Jump from index 4 to index 5.
It can be proven that there is no other jumping sequence that goes from 0 to n - 1 with more than 5 jumps. Hence, the answer is 5.
```

Example 3:

```
Input: nums = [1,3,6,4,1,2], target = 0
Output: -1
Explanation: It can be proven that there is no jumping sequence that goes from 0 to n - 1. Hence, the answer is -1.
```

á

**Constraints:**

	- `2 <= nums.length == n <= 1000`

	- `-10^9á<= nums[i]á<= 10^9`

	- `0 <= target <= 2 * 10^9`

## Hints

1. Use a dynamic programming approach.
2. Define a dynamic programming arrayádpáof sizeán, whereádp[i]árepresents the maximum number of jumps from indexá0áto indexái.
3. For eachájáiterate over allái < j. Setádp[j] = max(dp[j], dp[i] + 1)áifá-target <= nums[j] - nums[i] <= target.

## My Approach

### Brute Force
<!-- explain here -->

### Optimal
<!-- explain here -->

