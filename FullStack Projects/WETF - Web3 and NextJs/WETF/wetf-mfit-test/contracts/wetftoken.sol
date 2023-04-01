pragma solidity ^0.8.3;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract WETFToken is ERC20 {

    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
      _mint(msg.sender, 100000 * (10 ** 18));
    }

    function faucet (address recipient , uint256 amount) external {
      _mint(recipient, amount);
    }

    function vote (address sender, address recipient, uint amount) external {
      _transfer(sender, recipient, amount);
    }
}
