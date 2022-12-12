impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        match n {
            0 | 1 | 2 => n,
            k => {
                let mut count = vec![0; (n + 1) as usize];
                count[1] = 1;
                count[2] = 2;
                for i in 3..=k as usize { count[i] = count[i - 1] + count[i - 2]; }
                count[k as usize]
            }
        }
        
    }
}
