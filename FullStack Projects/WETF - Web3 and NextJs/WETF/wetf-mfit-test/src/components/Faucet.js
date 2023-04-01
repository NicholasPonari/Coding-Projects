import { useState } from "react";
import { ethers } from "ethers";
import Card from "react-bootstrap/Card";
import Button from "react-bootstrap/Button";
import Message from "./Message";

const tokenAddress = "0x5A478a6D8AFFEb35aE96C7E75339152e0d8065AB";

const Faucet = (props) => {
  const [balance, setBalance] = useState();
  const [showBalance, setShowBalance] = useState(false);

  async function getBalance() {
    if (typeof window.ethereum !== "undefined") {
      const [account] = await window.ethereum.request({
        method: "eth_requestAccounts",
      });
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const contract = new ethers.Contract(
        tokenAddress,
        props.tokenContract.abi,
        provider
      );
      const balance = await contract.balanceOf(account);
      console.log("Balance: ", balance.toString());
      setBalance(balance.toString());
      setShowBalance(true);
    }
  }

  async function faucet() {
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
      contract.faucet(account[0], "1000000000000000000000");
    }
  }
  return (
    <div>
      <Card style={{ background: "rgba(246, 207, 67, 0.73)" }}>
        <Card.Body>
          <Card.Subtitle>
            Get testnet WeTF tokens delivered right to your wallet!
          </Card.Subtitle>
          <br></br>
          <div className="d-grid gap-2">
            <Button onClick={faucet}>get 1000 WeTF tokens to play with!</Button>
            <Button onClick={getBalance} variant="warning">
              check my balance
            </Button>
            {showBalance ? (
              <Message balance={balance / 1000000000000000000} />
            ) : null}
          </div>
        </Card.Body>
      </Card>
    </div>
  );
};

export default Faucet;
