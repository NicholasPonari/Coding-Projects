//Convert String to Numbers

const decoder = [
  "A",
  "B",
  "C",
  "D",
  "E",
  "F",
  "G",
  "H",
  "I",
  "J",
  "K",
  "L",
  "M",
  "N",
  "O",
  "P",
  "Q",
  "R",
  "S",
  "T",
  "U",
  "V",
  "W",
  "X",
  "Y",
  "Z",
];

function rot13(str) {
  let splitString = str.split("");

  for (let i = 0; i < splitString.length; i++) {
    if (decoder.includes(splitString[i])) {
      if (decoder.indexOf(splitString[i]) < 13) {
        splitString[i] = decoder[decoder.indexOf(splitString[i]) + 13];
      } else if (decoder.indexOf(splitString[i]) >= 13) {
        splitString[i] = decoder[decoder.indexOf(splitString[i]) - 13];
      }
    }
  }
  return splitString.join("");
}

rot13("SERR PBQR PNZC");
