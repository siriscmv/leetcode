/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */

var wordBreak = function(s, wordDict, cache = {}) {
    const cached = cache[s];
    if (cached !== undefined) return cached;
    if (s === '') return true;

    const possible = wordDict.filter(w => s.startsWith(w));
    for (const p of possible) {
        if(wordBreak(s.slice(p.length), wordDict, cache)) {
            cache[s] = true;
            return true
        }
    }

    cache[s] = false;
    return false;
};
