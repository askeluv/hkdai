#!/usr/bin/python3

def test_balance(hkdai, accounts):
    assert hkdai.balanceOf(accounts[0]) == "0 ether"

def test_deposit_and_withdraw(dai, hkdai, accounts):
    assert hkdai.totalSupply() == "0 ether"
    dai.approve(hkdai.address, "1000 ether", {'from': accounts[0]})
    hkdai.approve(hkdai.address, "1000 ether", {'from': accounts[0]})
    hkdai.deposit("1 ether", {'from': accounts[0]})
    assert hkdai.totalSupply() == "7.8 ether"
    hkdai.withdraw("3.9 ether", {'from': accounts[0]})
    assert hkdai.balanceOf(accounts[0]) == "3.9 ether"
    assert hkdai.totalSupply() == "3.9 ether"
    hkdai.withdraw("3.9 ether", {'from': accounts[0]})
    assert hkdai.balanceOf(accounts[0]) == "0 ether"
    assert hkdai.totalSupply() == "0 ether"
