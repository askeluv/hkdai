pragma solidity ^0.5.0;

library SafeMath {
    function add(uint a, uint b) internal pure returns (uint c) {
        c = a + b;
        require(c >= a, "Overflow");
    }
    function sub(uint a, uint b) internal pure returns (uint c) {
        require(b <= a, "Underflow");
        c = a - b;
    }
    function mul(uint a, uint b) internal pure returns (uint c) {
        c = a * b;
        require(a == 0 || c / a == b, "Overflow");
    }
    function div(uint a, uint b) internal pure returns (uint c) {
        require(b > 0, "Divide by zero");
        c = a / b;
    }
}
