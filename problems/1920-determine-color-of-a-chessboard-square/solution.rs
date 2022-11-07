

impl Solution {
    pub fn square_is_white(coordinates: String) -> bool {
        let mut itr = coordinates.chars();
        let a = itr.next().unwrap();
        let b = itr.next().unwrap();

        (a.to_digit(18).unwrap() + b.to_digit(9).unwrap()) % 2 == 0
    }
}
