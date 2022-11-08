use std::convert::TryInto;

impl Solution {
    pub fn make_good(s: String) -> String {
        let mut st = s;

        loop {
            let mut prev: i32 = 0;
        let mut change = false;

            for (i, c) in st.chars().enumerate() {
            let res: i8 = (c as i32 - prev).try_into().unwrap_or_default();
            if res == -32 || res == 32 {
                st.replace_range(i-1..i+1, "");
                change = true;
                break;
            } else {
                prev = c as i32;
            }
        }
        if !change {
            return st;
        }
        }
    }
}
