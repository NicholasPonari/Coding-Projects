const hre = require("hardhat");

async function main() {
  const [deployer] = await hre.ethers.getSigners();

  console.log("Deploying contracts with the account:", deployer.address);

  const WETFToken = await hre.ethers.getContractFactory("WETFToken");
  const wetfToken = await WETFToken.deploy("WETFToken", "WETF");

  await wetfToken.deployed();

  console.log("Token deployed to:", wetfToken.address);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
