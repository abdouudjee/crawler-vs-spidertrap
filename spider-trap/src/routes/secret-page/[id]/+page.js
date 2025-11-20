export const ssr = true;
export const csr = false;
export function load() {
    const random = Math.floor(Math.random() * 1_000_000_000);
    return { random };
}