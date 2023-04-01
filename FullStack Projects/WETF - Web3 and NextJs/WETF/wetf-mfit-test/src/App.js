import "./App.css";
import WETFToken from "./artifacts/contracts/wetftoken.sol/WETFToken.json";
import "bootstrap/dist/css/bootstrap.min.css";
import { Container, Row, Col } from "react-bootstrap";
import Faucet from "./components/Faucet.js";
import TokenSend from "./components/TokenSend.js";
import { useState } from "react";
import { ethers } from "ethers";
import Poll from "./components/Poll";
import Button from "react-bootstrap/Button";
import Modal from "react-bootstrap/Modal";
import { Chart } from "react-google-charts";

function App() {
  // properties

  const Token = WETFToken;
  const [walletAddress, setWalletAddress] = useState("");

  // Helper Functions

  async function requestAccount() {
    console.log("requesting account");
    if (window.ethereum) {
      console.log("detected");
      try {
        const accounts = await window.ethereum.request({
          method: "eth_requestAccounts",
        });
        setWalletAddress(accounts[0]);
      } catch (error) {
        console.log("Error Connecting");
      }
    } else {
      console.log("Not Found");
    }
  }

  async function connectWallet() {
    if (typeof window.ethereum !== "undefined") {
      await requestAccount();

      const provider = new ethers.providers.Web3Provider(window.ethereum);
    }
  }

  const [show, setShow] = useState(false);

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  const data = [
    ["Security", "Allocation"],
    ["Google", 14],
    ["Tesla", 8],
    ["NetFlix", 20],
    ["Apple", 55],
  ];

  const options = {
    title: "Portfolio Breakdown: Week of December 4, 2022",
  };

  return (
    <div className="App">
      <Container>
        <Row>
          <header className="App-header">
            <button onClick={requestAccount}>Connect Wallet</button>
            <h4>This is your Wallet Address: {walletAddress} </h4>
          </header>
        </Row>
        <Row className="justify-content-md-center">
          <Faucet tokenContract={Token} />;
        </Row>
        <Row>
          <h1>Cast your vote!</h1>
        </Row>
        <Row>
          <Poll />
        </Row>
        <Row>
          <TokenSend tokenContract={Token} />
        </Row>
        <Row>
          <Button variant="primary" onClick={handleShow}>
            Show me the results!
          </Button>

          <Modal show={show} onHide={handleClose}>
            <Modal.Header closeButton>
              <Modal.Title>This week's Portfolio Allocation</Modal.Title>
            </Modal.Header>
            <Modal.Body>
              <Row>
                    You have invested 500 WETF Tokens! Your tokens are LOCKED
              </Row>
              <Row>    until December 11, 2022.</Row>
              <Row> </Row>
              <Row>
                    This round, a total of 9,500 WETF Tokens were invested!
              </Row>
              <Row> </Row>
              <Row>
                    Total Net Invested Asset Value of $1,909,513.93 USD.
              </Row>
              <Row> </Row>
              <Row>
                    Net Investable Assets in Treasury: $2,750,797.82 USD
              </Row>
              <Row> </Row>
              <Row>    Fully Diluted Token Amount: 27,000 Tokens</Row>
              <Row> </Row>
              <Row>    Current Value of WETF Token by NAV: $101.88 USD</Row>
              <Row> </Row>
              <Row>
                    WETF will redeem tokens at the above price for cash.
              </Row>
              <Row> </Row>
              <Chart
                chartType="PieChart"
                data={data}
                options={options}
                width={"100%"}
                height={"400px"}
              />
            </Modal.Body>
            <Modal.Footer>
              <Button variant="secondary" onClick={handleClose}>
                Close
              </Button>
            </Modal.Footer>
          </Modal>
        </Row>
      </Container>
    </div>
  );
}

export default App;
