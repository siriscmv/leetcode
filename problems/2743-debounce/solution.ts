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

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */
