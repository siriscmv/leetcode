type F = (...args: number[]) => void

function debounce(fn: F, t: number): F {
    let job = null;
    
    return (...args) => {
      if (job) clearTimeout(job);

      job = setTimeout(() => {
        job = null;
        fn(...args);
      }, t);
    } 
};
