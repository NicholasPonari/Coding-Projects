import { useState } from "react";
import { ethers } from "ethers";
import Card from "react-bootstrap/Card";
import Button from "react-bootstrap/Button";

//contract address
const tokenAddress = "0x5A478a6D8AFFEb35aE96C7E75339152e0d8065AB";

const TokenSend = (props) => {
  const [userAccount, setUserAccount] = useState();
  const [amount, setAmount] = useState();

  // request access to the user's MetaMask account
  async function requestAccount() {
    await window.ethereum.request({ method: "eth_requestAccounts" });
  }

  async function sendCoins() {
    if (typeof window.ethereum !== "undefined") {
      const account = await window.ethereum.request({
        method: "eth_requestAccounts",
      });
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const signer = provider.getSigner();
      const contract = new ethers.Contract(
        tokenAddress,
        props.tokenContract.abi,
        signer
      );
      const transaction = await contract.vote(
        account[0],
        "0x074606aEFC0f56BB3102440E264Fb7424cBA1994",
        "500000000000000000000"
      );
      await transaction.wait();
      console.log(`${amount} Coins successfully sent to ${userAccount}`);
    }
  }
  return (
    <Card style={{ background: "rgba(246, 207, 67, 0.73)", width: "100%" }}>
      <Card.Body>
        <Card.Subtitle>
          {" "}
          How many tokens would you like to invest in this round of votes? The
          amount will be sent to the DAO Contract Wallet listed below:
        </Card.Subtitle>
        <br></br>
        <div className="d-grid gap-2">
          <input
            onChange={(e) => setUserAccount(e.target.value)}
            placeholder="0x074606aEFC0f56BB3102440E264Fb7424cBA1994"
          />
          <input
            onChange={(e) => setAmount(e.target.value)}
            placeholder="Amount"
          />
          <Button onClick={sendCoins} variant="success">
            send{" "}
          </Button>
        </div>
      </Card.Body>
    </Card>
  );
};

export default TokenSend;
