#!/usr/bin/python3

import pytest

@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    pass

@pytest.fixture(scope="module")
def dai(MockDai, accounts):
    dai = accounts[0].deploy(MockDai, "Mock Dai", "DAI", 18, "1000 ether")
    yield dai

@pytest.fixture(scope="module")
def hkdai(HKDai, accounts):
    underlying_token_address = "0x602C71e4DAC47a042Ee7f46E0aee17F94A3bA0B6" # TODO: find way to not hard-code this
    hkdai = accounts[0].deploy(HKDai, "HKDai", "HKDAI", 18, "0 ether", underlying_token_address, 780)
    yield hkdai
