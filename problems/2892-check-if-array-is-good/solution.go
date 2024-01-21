func isGood(nums []int) bool {
    seen, l := make(map[int]int), len(nums) - 1

    for _, n := range nums {
        if n > l || n <= 0 {
            return false
        }
        seen[n] += 1
        if seen[n] == 2 && n != l {
            return false
        }
    }

    return seen[l] == 2
}
