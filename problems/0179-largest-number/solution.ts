function largestNumber(nums: number[]): string {
    const sorted = nums.map(s => s.toString()).sort((a, b) => {
        const len = Math.min(a.length, b.length);
        for (let i = 0; i < len; i++) {
            if (a[i] != b[i]) return b[i] > a[i] ? 1 : -1;
        }

        if (a.length === b.length) return 0;
        return parseInt(`${a}${b}`) > parseInt(`${b}${a}`) ? -1: 1
    });

    return sorted.slice(sorted.findIndex(s => s !== '0')).join('')
};
