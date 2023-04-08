function checkCashRegister(price, cash, cid) {
  const currencyUnits = [
    { name: "ONE HUNDRED", value: 100.0 },
    { name: "TWENTY", value: 20.0 },
    { name: "TEN", value: 10.0 },
    { name: "FIVE", value: 5.0 },
    { name: "ONE", value: 1.0 },
    { name: "QUARTER", value: 0.25 },
    { name: "DIME", value: 0.1 },
    { name: "NICKEL", value: 0.05 },
    { name: "PENNY", value: 0.01 },
  ];

  let changeDue = cash - price;
  let change = [];

  let totalCID = cid.reduce((acc, curr) => acc + curr[1], 0);
  if (totalCID < changeDue) {
    return { status: "INSUFFICIENT_FUNDS", change: [] };
  }
  if (totalCID === changeDue) {
    return { status: "CLOSED", change: cid };
  }

  for (let i = 0; i < currencyUnits.length; i++) {
    let currencyUnit = currencyUnits[i];
    let currencyUnitInCID = cid.find((unit) => unit[0] === currencyUnit.name);
    if (!currencyUnitInCID) {
      continue;
    }
    let currencyUnitValue = currencyUnitInCID[1];
    let currencyUnitCount = 0;
    while (currencyUnitValue > 0 && changeDue >= currencyUnit.value) {
      changeDue -= currencyUnit.value;
      changeDue = Math.round(changeDue * 100) / 100;
      currencyUnitValue -= currencyUnit.value;
      currencyUnitCount++;
    }
    if (currencyUnitCount > 0) {
      change.push([currencyUnit.name, currencyUnit.value * currencyUnitCount]);
    }
    if (changeDue === 0) {
      break;
    }
  }

  if (changeDue > 0) {
    return { status: "INSUFFICIENT_FUNDS", change: [] };
  }
  return { status: "OPEN", change: change };
}

console.log(
  checkCashRegister(3.26, 100, [
    ["PENNY", 1.01],
    ["NICKEL", 2.05],
    ["DIME", 3.1],
    ["QUARTER", 4.25],
    ["ONE", 90],
    ["FIVE", 55],
    ["TEN", 20],
    ["TWENTY", 60],
    ["ONE HUNDRED", 100],
  ])
);
