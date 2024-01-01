type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type Obj = Record<string, JSONValue> | Array<JSONValue>;

function compactObject(obj: Obj): Obj {
    const result: Obj = {};
    const arr = Array.isArray(obj);

    for (const [key, value] of Object.entries(obj)) {
      if (Boolean(value) === false) continue
      if (typeof value === 'object') result[key] = compactObject(value);
      else result[key] = value;
    }

    if (!arr) return result;
    return Object.values(result);
}
