#!/usr/bin/python3

import os
from brownie import *

def main():
    recipient_address = '0xD7720c3bbF5d28f30906eB7530A5B941818A7E47'
    amount = '19 ether'
    pk = os.environ.get('ACCOUNT_PRIVATE_KEY')
    accounts.add(pk)
    account = accounts[0]
    print('Account ETH balance', account.balance())
    dai_address = '0x16684b9362C1B8276526212B3905d8bBEB595dDb'
    dai = MockDai.at(dai_address)
    print('Account Token balance', dai.balanceOf(account))
    dai.transfer(recipient_address, amount, {'from': account})
