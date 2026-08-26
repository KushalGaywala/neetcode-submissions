impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut diffs: HashMap<i32, usize> = HashMap::with_capacity(nums.len());
        
        for (i, &n) in nums.iter().enumerate() {
            let mut diff = target - n;
            if diffs.contains_key(&diff) {
                return vec![diffs[&diff] as i32, i as i32];
            }
            diffs.insert(n, i);
        }

        return vec![]
    }
}
