pragma solidity ^0.5.0;

import "./SafeMath.sol";

contract ERC20 {
    function totalSupply() public view returns (uint);
    function balanceOf(address tokenOwner) public view returns (uint balance);
    function allowance(address tokenOwner, address spender) public view returns (uint remaining);
    function transfer(address to, uint tokens) public returns (bool success);
    function approve(address spender, uint tokens) public returns (bool success);
    function transferFrom(address from, address to, uint tokens) public returns (bool success);
    event Transfer(address indexed from, address indexed to, uint tokens);
    event Approval(address indexed tokenOwner, address indexed spender, uint tokens);
}

contract HKDai {

    using SafeMath for uint256;

    string public symbol;
    string public name;
    uint256 public decimals;
    uint256 public totalSupply;

    uint256 conversionFactor; // divide by 100 when using
    address underlyingTokenAddress; // e.g. DAI

    mapping(address => uint256) balances;
    mapping(address => mapping(address => uint256)) allowed;

    event Transfer(address from, address to, uint256 value);
    event Approval(address owner, address spender, uint256 value);
    event Mint(address minter, uint256 value);
    event Burn(address burner, uint256 value);

    constructor(
        string memory _symbol,
        string memory _name,
        uint256 _decimals,
        address _underlyingTokenAddress,
        uint256 _conversionFactor
    )
        public
    {
        symbol = _symbol;
        name = _name;
        decimals = _decimals;
        underlyingTokenAddress = _underlyingTokenAddress;
        conversionFactor = _conversionFactor;
        totalSupply = 0; // initial supply must be 0 since we have no underlying assets
    }

    function () external payable {
        revert("This contract is not payable");
    }

    function balanceOf(address _owner) public view returns (uint256) {
        return balances[_owner];
    }

    function allowance(
        address _owner,
        address _spender
    )
        public
        view
        returns (uint256)
    {
        return allowed[_owner][_spender];
    }

    function approve(address _spender, uint256 _value) public returns (bool) {
        allowed[msg.sender][_spender] = _value;
        // TODO: figure out how to do approval properly:
        ERC20(underlyingTokenAddress).approve(_spender, _value);
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    function transfer(address _to, uint256 _value) public returns (bool) {
        balances[msg.sender] = balances[msg.sender].sub(_value);
        balances[_to] = balances[_to].add(_value);
        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    function transferFrom(
        address _from,
        address _to,
        uint256 _value
    )
        public
        returns (bool)
    {
        require(allowed[_from][msg.sender] >= _value, "Insufficient allowance");
        balances[_from] = balances[_from].sub(_value);
        allowed[_from][msg.sender] = allowed[_from][msg.sender].sub(_value);
        balances[_to] = balances[_to].add(_value);
        emit Transfer(_from, _to, _value);
        return true;
    }

    function deposit(uint256 _underlyingValue) public returns (bool) {
        ERC20(underlyingTokenAddress).transferFrom(msg.sender, address(this), _underlyingValue);
        uint256 _mintValue = _underlyingValue.mul(conversionFactor).div(100);
        totalSupply = totalSupply.add(_mintValue);
        balances[msg.sender] = balances[msg.sender].add(_mintValue);
        emit Mint(msg.sender, _mintValue);
        return true;
    }

    function withdraw(uint256 _burnValue) public returns (bool) {
        require(
          balances[msg.sender] >= _burnValue,
          "Sender does not have enough tokens in their wallet to withdraw this amount."
        );
        require(
          totalSupply >= _burnValue,
          "Contract does not contain enough tokens to withdraw this amount."
        );
        totalSupply = totalSupply.sub(_burnValue);
        balances[msg.sender] = balances[msg.sender].sub(_burnValue);
        uint256 _underlyingValue = _burnValue.div(conversionFactor).mul(100);
        ERC20(underlyingTokenAddress).transferFrom(address(this), msg.sender, _underlyingValue);
        emit Burn(msg.sender, _burnValue);
        return true;
    }
}
