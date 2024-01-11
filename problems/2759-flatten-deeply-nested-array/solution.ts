type MultiDimensionalArray = (number | MultiDimensionalArray)[];

var flat = function (arr:  MultiDimensionalArray, n: number):  MultiDimensionalArray {
    if (n === 0) return arr;  
    return flatten(arr, n, -1);
};

const flatten = (arr: MultiDimensionalArray, depth: number, currentDepth: number): MultiDimensionalArray => {
    if (depth === currentDepth) return [arr];
    const ans = [];
    
    for (const element of arr) {
        if (!Array.isArray(element)) ans.push(element);
        else ans.push(...flatten(element, depth, currentDepth + 1));
    }

    return ans;
}
