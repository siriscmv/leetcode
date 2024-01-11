type F = (x: number) => number;

function compose(functions: F[]): F {
    const funs = [...functions];
    funs.reverse();

    return function(x) {
        let ans = x
        for (const fun of funs) ans = fun(ans);
        return ans; 
    }
};
