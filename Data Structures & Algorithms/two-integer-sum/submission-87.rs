impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut diffs: HashMap<i32, i32> = HashMap::new();
        
        for (i, n) in nums.iter().enumerate() {
            let mut diff = target - n;
            if diffs.contains_key(&diff) {
                return vec![diffs[&diff], i as i32];
            }
            diffs.insert(*n, i as i32);
        }
        unreachable!()
    }
}
