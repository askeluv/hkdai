#!/usr/bin/python3

import pytest

def test_balance(hkdai, accounts):
    assert hkdai.balanceOf(accounts[0]) == "0 ether"

def test_approval(dai, hkdai, accounts):
    '''Set approval'''
    dai.approve(accounts[1], "10 ether", {'from': accounts[0]})
    hkdai.approve(accounts[1], "10 ether", {'from': accounts[0]})
    assert hkdai.allowance(accounts[0], accounts[1]) == "10 ether"
    assert hkdai.allowance(accounts[0], accounts[2]) == 0

    dai.approve(accounts[1], "6 ether", {'from': accounts[0]})
    hkdai.approve(accounts[1], "6 ether", {'from': accounts[0]})
    assert hkdai.allowance(accounts[0], accounts[1]) == "6 ether"


def test_transferFrom(dai, hkdai, accounts):
    '''Transfer hkdais with transferFrom'''
    dai.approve(hkdai.address, "1000 ether", {'from': accounts[1]})
    dai.approve(accounts[1], "1000 ether", {'from': accounts[0]})
    dai.approve(hkdai.address, "1000 ether", {'from': accounts[0]})
    hkdai.approve(hkdai.address, "1000 ether", {'from': accounts[1]})
    hkdai.approve(hkdai.address, "1000 ether", {'from': accounts[0]})
    hkdai.approve(accounts[1], "1000 ether", {'from': accounts[0]})

    hkdai.deposit("5 ether", {'from': accounts[0]})
    hkdai.transferFrom(accounts[0], accounts[2], "5 ether", {'from': accounts[1]})

    assert hkdai.balanceOf(accounts[2]) == "5 ether"
    assert hkdai.balanceOf(accounts[1]) == 0
    assert hkdai.balanceOf(accounts[0]) == "34 ether"
    assert hkdai.allowance(accounts[0], accounts[1]) == "995 ether"


def test_transferFrom_reverts(hkdai, accounts):
    '''transferFrom should revert'''
    with pytest.reverts("Insufficient allowance"):
        hkdai.transferFrom(accounts[0], accounts[2], "1 ether", {'from': accounts[1]})

    with pytest.reverts("Insufficient allowance"):
        hkdai.transferFrom(accounts[0], accounts[2], "1 ether", {'from': accounts[0]})
