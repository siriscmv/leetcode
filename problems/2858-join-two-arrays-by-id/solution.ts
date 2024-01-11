type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type ArrayType = { "id": number } & Record<string, JSONValue>;

function join(arr1: ArrayType[], arr2: ArrayType[]): ArrayType[] {
    arr1.sort((a, b) => a.id - b.id);
    arr2.sort((a, b) => a.id - b.id);

    const ans = [];
    let i = 0, j = 0, l1 = arr1.length, l2 = arr2.length;
    
    while (i < l1 && j < l2) {
        if (arr1[i].id < arr2[j].id) ans.push(arr1[i++]);
        else if (arr1[i].id > arr2[j].id) ans.push(arr2[j++]);
        else {
            const obj1 = arr1[i++];
            const obj2 = arr2[j++];
            
            for (const [k, v] of Object.entries(obj2)) obj1[k] = v;
            ans.push(obj1);
        }
    }
    
    while (i<l1) ans.push(arr1[i++]);
    while (j<l2) ans.push(arr2[j++]);

    return ans;
};
