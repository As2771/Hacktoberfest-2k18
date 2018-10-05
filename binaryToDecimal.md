```js
const binaryToDecimal = num => [...String(num)].reduce((a, c, i, nums) => a += c*(2**(nums.length-i-1)), 0);
```
- [Run Code](https://repl.it/@ezioda004/BinaryToDecimal)
