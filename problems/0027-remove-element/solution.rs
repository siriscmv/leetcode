impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        let mut count = 0;

        nums.retain(|&n| {
            if (n == val) {
                return false;
            } else {
                count += 1;
                return true;
            }
        });

        return count;
    }
}
