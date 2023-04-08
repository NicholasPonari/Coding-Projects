function convertToRoman(num) {
  const roman = {
    1: "I",
    4: "IV",
    5: "V",
    9: "IX",
    10: "X",
    40: "XL",
    50: "L",
    90: "XC",
    100: "C",
    400: "CD",
    500: "D",
    900: "CM",
    1000: "M",
  };

  let answer = "";
  let keys = Object.keys(roman).reverse();
  for (let i = 0; i < keys.length; i++) {
    while (num >= keys[i]) {
      num -= keys[i];
      answer += roman[keys[i]];
    }
  }
  return answer;
}

console.log(convertToRoman(3572));
