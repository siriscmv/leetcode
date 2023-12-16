/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    const map = {};

    for (const char of s) {
        map[char] = (map[char] ?? 0) + 1
    }

    for (const char of t) {
        const curr = map[char];
        if (!curr) return false;
        map[char] = curr-1
    }

    for (const val of Object.values(map)) {
        if (val !== 0) return false;
    }

    return true;
};
