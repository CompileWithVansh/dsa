# Maximum Value of an Ordered Triplet II

**LeetCode:** #2874
**Date:** 15thMay26
**Difficulty:** Medium
**Topics:** Array
**Link:** https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/

## Problem Statement

You are given a **0-indexed** integer array `nums`.

Return ***the maximum value over all triplets of indices*** `(i, j, k)` *such that* `i < j < k`*. *If all such triplets have a negative value, return `0`.

The **value of a triplet of indices** `(i, j, k)` is equal to `(nums[i] - nums[j]) * nums[k]`.

á

Example 1:

```
Input: nums = [12,6,1,2,7]
Output: 77
Explanation: The value of the triplet (0, 2, 4) is (nums[0] - nums[2]) * nums[4] = 77.
It can be shown that there are no ordered triplets of indices with a value greater than 77.
```

Example 2:

```
Input: nums = [1,10,3,4,19]
Output: 133
Explanation: The value of the triplet (1, 2, 4) is (nums[1] - nums[2]) * nums[4] = 133.
It can be shown that there are no ordered triplets of indices with a value greater than 133.
```

Example 3:

```
Input: nums = [1,2,3]
Output: 0
Explanation: The only ordered triplet of indices (0, 1, 2) has a negative value of (nums[0] - nums[1]) * nums[2] = -3. Hence, the answer would be 0.
```

á

**Constraints:**

	- `3 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^6`

## Hints

1. Preprocess the prefix maximum array, prefix_max[i] = max(nums[0], nums[1], à, nums[i]) and the suffix maximum array, suffix_max[i] = max(nums[i], nums[i + 1], à, nums[n - 1]).
2. For each index j, find two indices i and k such that i  and (nums[i] - nums[j]) * nums[k] is the maximum, using the prefix and suffix maximum arrays.
3. For index j, the maximum triplet value is (prefix_max[j - 1] - nums[j]) * suffix_max[j + 1].

## My Approach

### Brute Force
<!-- explain here -->

### Optimal
<!-- explain here -->

