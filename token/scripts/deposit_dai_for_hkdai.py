#!/usr/bin/python3

import os
from brownie import *

def main():
    recipient_address = '0xD7720c3bbF5d28f30906eB7530A5B941818A7E47'
    dai_amount = '1 ether'
    hkd_amount = '3.8 ether'
    pk = os.environ.get('ACCOUNT_PRIVATE_KEY')
    accounts.add(pk)
    account = accounts[0]
    print('ETH balance', account.balance())
    dai_address = '0x16684b9362C1B8276526212B3905d8bBEB595dDb'
    dai = MockDai.at(dai_address)
    print('MockDai balance', dai.balanceOf(account))
    hkdai_address = '0xC1e2cf5dFe3D4A0c3cA0Beb9bC0e911A8A70dD59'
    hkdai = HKDai.at(hkdai_address)
    print('HKDai balance', hkdai.balanceOf(account))
    print('Approving ...')
    dai.approve(hkdai.address, "1000 ether", {'from': account})
    #hkdai.approve(accounts[1], "10 ether", {'from': accounts[0]})
    print('Depositing ... ')
    hkdai.deposit(dai_amount, {'from': account})
    print('MockDai balance', dai.balanceOf(account))
    print('HKDai balance', hkdai.balanceOf(account))
    print('Transferring ... ')
    hkdai.transfer(recipient_address, hkd_amount, {'from': account})
    print('MockDai balance', dai.balanceOf(account))
    print('HKDai balance', hkdai.balanceOf(account))
