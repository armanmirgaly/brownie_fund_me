from brownie import network, config, accounts

LOCAL_BLOACKCHAIN_EVIRONMENTS = ["development", "ganache-local"]


def get_account():
    if network.show_active() in LOCAL_BLOACKCHAIN_EVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
