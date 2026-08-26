use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut diffs = HashMap::new();

        for (i, n) in nums.iter().enumerate() {
            if let Some(&idx) = diffs.get(&(target - n)) {
                return vec![idx as i32, i as i32];
            }
            diffs.insert(*n, i);
        }

        unreachable!()
    }
}
