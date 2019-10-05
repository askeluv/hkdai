#!/usr/bin/python3

def test_balance(hkdai, accounts):
    assert hkdai.balanceOf(accounts[0]) == "0 ether"

def test_roundtrip(dai, hkdai, accounts):
  external_agent = accounts[0]
  some_person = accounts[1]
  another_person = accounts[2]

  dai.approve(external_agent, "1000 ether", {'from': external_agent})
  #dai.approve(hkdai, "1000 ether", {'from': hkdai})

  # Give some person 1 DAI
  dai.transferFrom(external_agent, some_person, "1 ether", {'from': external_agent})
  assert dai.balanceOf(some_person) == "1 ether"

  dai.approve(hkdai.address, "1000 ether", {'from': some_person})
  hkdai.approve(hkdai.address, "1000 ether", {'from': some_person})
  hkdai.approve(some_person, "1000 ether", {'from': some_person})

  # some person deposits 1 Dai into HKDai contract, and receives 7.8 HKDai
  hkdai.deposit("1 ether", {'from': some_person})
  assert dai.balanceOf(some_person) == "0 ether"
  assert hkdai.balanceOf(some_person) == "7.8 ether"
  assert hkdai.totalSupply() == "7.8 ether"

  # some person sends 5 HKDai to another person
  hkdai.transfer(another_person, "3.9 ether", {"from": some_person})
  assert hkdai.balanceOf(some_person) == "3.9 ether"
  assert hkdai.balanceOf(another_person) == "3.9 ether"

  # some person withdraws 2.8 HKDai for Dai
  hkdai.approve(hkdai.address, "10 ether", {'from': some_person})
  #dai.approve(some_person, "1000 ether", {'from': some_person})
  hkdai.withdraw("3.9 ether", {'from': some_person})
  assert hkdai.balanceOf(some_person) == "0 ether"
  assert dai.balanceOf(some_person) == "0.5 ether"
  assert dai.balanceOf(hkdai) == "0.5 ether"
  assert hkdai.totalSupply() == "3.9 ether"

  # another person withdraws 4 HKDai for Dai
  hkdai.withdraw("3.12 ether", {'from': another_person})
  assert hkdai.balanceOf(another_person) == "0.78 ether"
  assert dai.balanceOf(hkdai) == "0.1 ether"

  # another person sends 1 HKDai to some person
  hkdai.transfer(some_person, "0.78 ether", {'from': another_person})
  assert hkdai.balanceOf(some_person) == "0.78 ether"
  assert hkdai.balanceOf(another_person) == "0 ether"

  # some person withdraws 1 HKDai for Dai
  hkdai.withdraw("0.78 ether", {'from': some_person})
  assert hkdai.balanceOf(some_person) == "0 ether"
  assert dai.balanceOf(some_person) == "0.6 ether"
  assert dai.balanceOf(hkdai) == "0 ether"