function palindrome(str) {
  let clnstr = str.replace(/[^a-zA-Z0-9]/g, "").toLowerCase();
  let revstr = clnstr.split("").reverse().join("");
  return clnstr == revstr ? true : false;
}

palindrome("eye");
