impl Solution {
    pub fn third_max(nums: Vec<i32>) -> i32 {
        let mut arr = nums;
        arr.sort_unstable_by(|x, y| y.cmp(&x)); 
        let mut i = 0;
        let mut prev = arr[0];
        let mut start = false;

        for num in arr.iter() {
            if !start {
                start = true;
                i = i + 1;
                prev = *num;
            } else if prev != *num {
                if i == 2 {
                    return *num;
                }
                i = i + 1;
                prev = *num;
            }
        }

        arr[0] 
    }
}
