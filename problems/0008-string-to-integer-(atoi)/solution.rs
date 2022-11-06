use std::convert::TryInto;

impl Solution {
    pub fn my_atoi(s: String) -> i32 {
        let mut ans = 0;
        let mut sign = 0;
        let mut read_first_digit = false;

        for c in s.chars() { 
            if c == ' ' {
                if read_first_digit { break; } else { continue; }
            } else if c == '+' {
                if read_first_digit { break; } else { sign = 1 }
                read_first_digit = true;
            } else if c == '-' {
                if read_first_digit { break; } else { sign = -1 }
                read_first_digit = true;
            } else if c.is_numeric() {
                ans = ans * 10 + (c as i128 - 0x30); 
                read_first_digit = true;
            } else {
                break;
            }
        }

        if sign == -1 {
            (-1 * ans).try_into().unwrap_or(-1 * i32::MAX - 1)
        } else {
            ans.try_into().unwrap_or(i32::MAX) 
        }   
    }
}
