function fact(x) {
   if (x === 0) {
      return 1;
   }
   return x * fact(x - 1);  // recursion
}

function run(number) {
  if (typeof number === "number") // validation
    alert(fact(number));
  else
    alert('Enter number');
}

run(5) // returns 120
