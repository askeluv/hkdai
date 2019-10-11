#!/usr/bin/python3

import os
from brownie import *

def main():
    pk = os.environ.get('ACCOUNT_PRIVATE_KEY')
    accounts.add(pk)
    account = accounts[0]
    print('Account balance', account.balance())
    #dai = account.deploy(MockDai, "MockDAI", "DAI", 18, "1000 ether")
    #underlying_token_address = dai.address #'<INSERT DAI ADDRESS HERE>'
    underlying_token_address = '0x16684b9362C1B8276526212B3905d8bBEB595dDb'
    hkdai = account.deploy(HKDai, "TestHKDaiTwo", "TESTHKDAITWO", 18, underlying_token_address, 780)
