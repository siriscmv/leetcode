function map(arr: number[], fn: (n: number, i: number) => number): number[] {
    const ans = [];
    for (const [i, n] of arr.entries()) ans.push(fn(n, i));
    return ans;
};
