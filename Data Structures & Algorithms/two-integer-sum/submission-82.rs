use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut seen_at = HashMap::new();

        for (i, n) in nums.iter().enumerate() {
            if let Some(&idx) = seen_at.get(&(target - n)) {
                return vec![idx as i32, i as i32];
            }
            seen_at.insert(*n, i);
        }

        unreachable!()
    }
}
