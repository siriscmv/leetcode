function map(arr: number[], fn: (n: number, i: number) => number): number[] {
    const ans = [];
    let i = 0;

    for (const num of arr) {
      ans.push(fn(num, i));
      i++;
    }
    
    return ans;
};
