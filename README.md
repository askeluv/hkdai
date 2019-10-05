# HKDai: A permissionless, bankless Hong Kong Dollar for the people, backed by Dai.

** NOTE: This is an experimental, work-in-progress project **

## Motivation: Why HKDai?
The HKDai gives Hongkongers a bankless alternative to the Hong Kong Dollar, with full transparency, and backing by Dai.

## Background: Dollar peg and Dai stablecoin
The Hong Kong Dollar (HKD) is pegged to the US Dollar (USD) at a rate of 7.8 HKD to 1 USD.

The peg is maintained by the Hong Kong Monetary Authority (HKMA) market-making HKD vs USD. The HKMA buys low (7.75 HKD/USD) and sells high (7.85 HKD/USD). In other words, HKMA maintains a soft peg through trading in the open market.

Dai is a stablecoin on the Ethereum blockchain, soft-pegged to the US Dollar.

## Solution: How does it work?
HKDai is implemented as a smart contract on Ethereum. It simply lets you deposit x Dai, and mint 7.8x HKDai. The deposited Dai will stay locked in the smart contract, until someone redeems it with the inverse operation; anyone who holds 7.8x HKDai can redeem x Dai at any time.

This means every HKDai in circulation is backed by an exact number of Dai locked in the HKDai smart contract.

Once some HKDai has been minted, it can be traded between people, digitally, with no banks needed. Since it's implemented on the blockchain, there can be no double-spending, and all assets backing HKDai are transparently verifiable at all times. Furthermore, HKDai cannot be shut down, as the smart contract exists on the blockchain, with no central controlling entitity.

## Incentive: Why should we lock up Dai and mint HKDai?
The Dai that's locked up in the HKDai smart contract generates interests via the Compound protocol. The interests are channeled as donations into <TBD> to help support Hong Kong people.