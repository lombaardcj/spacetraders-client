import os
from dotenv import load_dotenv

from logger import logger

# initialise the logger
logger.info("Initialising logger")

from spacetraders import SpaceTradersAPI

if __name__ == "__main__":
    api = SpaceTradersAPI()
    print(api.agent())
    print(api.contracts())

    if len(api.contracts()) >= 0:
        contract = api.contracts()[0]
        if api.contract_accept(contract) == 1:
            print("Accepted contract")
        # else if
        elif api.contract_accept(contract) == -1:
            print("Contract not accepted")
        else:
            print("Contract already accepted")

    if api.agent().headquarters is not None:
        print("printing agent system info")
        print(api.system_get(api.agent().headquarters.system))
