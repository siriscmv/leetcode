type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type Obj = Record<string, JSONValue> | Array<JSONValue>;

function chunk(arr: Obj[], size: number): Obj[][] {
    const ans = [];
    const len = arr.length;
    let i = 0;  
    
    for (i = 0; i < len; i += size) {
        const chunk = [];
        for (let j = i; j < Math.min(len, i + size); j++) chunk.push(arr[j]);
        ans.push(chunk);
    }

    return ans;
};

