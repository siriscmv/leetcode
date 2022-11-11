/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let i = 0;
    let prev = 0;

    do {
        const n = nums[i];
        if (n === undefined) break;

        if (i > 0 && prev === n) {
            nums.splice(i, 1);
        } else {
            prev = n;
            ++i;
        }
    } while(1)
    
    return i; 
};
