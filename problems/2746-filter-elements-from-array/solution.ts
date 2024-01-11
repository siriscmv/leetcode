type Fn = (n: number, i: number) => any

function filter(arr: number[], fn: Fn): number[] {
    const ans = []
    for (const [i, n] of arr.entries()) {
        if (fn(n, i)) ans.push(n);
    }
    return ans;
};
