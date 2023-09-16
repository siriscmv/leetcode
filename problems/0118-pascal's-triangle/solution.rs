impl Solution {
    pub fn generate(num_rows: i32) -> Vec<Vec<i32>> {
        let mut rows: Vec<Vec<i32>> = Vec::with_capacity(num_rows as usize);

        for i in 1..=num_rows {
            match i {
                1 => rows.push(vec![1]),
                2 => rows.push(vec![1, 1]),
                _ => {
                    let prev = &rows[(i-2) as usize];
                    let mut row: Vec<i32> = Vec::with_capacity(i as usize);
                    row.push(1);

                    for j in 2..i {
                        row.push(prev[(j-2) as usize] + prev[(j-1) as usize]);
                    }

                    row.push(1);
                    rows.push(row);
                }
            }
        }

        rows
    }
}
