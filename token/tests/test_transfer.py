#!/usr/bin/python3

def test_balance(hkdai, accounts):
    assert hkdai.balanceOf(accounts[0]) == "0 ether"

def test_transfer(dai, accounts):
    assert dai.totalSupply() == "1000 ether"
    dai.transfer(accounts[1], "0.1 ether", {'from': accounts[0]})
    assert dai.balanceOf(accounts[1]) == "0.1 ether"
    assert dai.balanceOf(accounts[0]) == "999.9 ether"
