use std::collections::HashMap;

impl Solution {
    pub fn most_frequent_even(nums: Vec<i32>) -> i32 {
        let mut map: HashMap<i32, i32> = HashMap::new();
        let mut ans = (0, 0); 

        for num in nums {
            if num % 2 == 0 {
                let v = *map.get(&num).unwrap_or(&0) + 1;
                map.insert(num, v);
               
                if (v > ans.1) || (v == ans.1 && (&num < &ans.0 || &ans.1 == &0)) {
                    ans = (num, v);
                }
            }
        }

        if ans.1 != 0 {
            return ans.0;
        }

        return -1;
    }
}
