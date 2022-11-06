function twoSum(nums: number[], target: number): number[] {
    let index = 0;
    do {
        const num = nums.shift();
        let i = index + 1;

        for (const n of nums) {
            if (n + num === target) return [index, i];
            i += 1;
        }
       
        index += 1;
    } while(1);

    return [0, 0];
};
