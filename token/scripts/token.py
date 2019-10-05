#!/usr/bin/python3

from brownie import *

def main():
    underlying_token_address = '<INSERT DAI ADDRESS HERE>'
    accounts[0].deploy(Token, "Test Token", "TEST", 18, "1000 ether", underlying_token_address, 780)