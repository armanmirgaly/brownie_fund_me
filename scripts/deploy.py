from brownie import FundMe, network, config
from scripts.helpful_scripts import get_account


def deploy_fund_me():
    account = get_account()
    fund_me = FundMe.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
