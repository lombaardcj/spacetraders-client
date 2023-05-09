import os
import requests
import json
from logger import logger
from dotenv import load_dotenv

from agent import Agent
from location import Location
from contract import Contract
from system import System

load_dotenv()  # Load the .env file

class SpaceTradersAPI:
    def __init__(self, baseurl = "https://api.spacetraders.io/v2/", token = os.environ.get("TOKEN")):
        logger.info("Initialising api")
        self._baseurl = baseurl
        self._token = token
        self._headers = self._auth_header()

        self._agent = None
        self._contracts = None
        self._systems = None

        self._accepted_contracts = []

        self.fetch_agent()

    def _auth_header(self):
        return {
            "Authorization": f"Bearer {self._token}"
        }

    def fetch_agent(self):
        url = self._baseurl + Agent.url_list()
        logger.debug("Fetching agent from " + url)
        response = requests.get(url, headers=self._headers)
        logger.debug("Response: " + str(response))
        if response.status_code == 200:
            data = response.json()["data"]
            logger.debug("Response data: " + str(data))
            self._agent = Agent.parse_obj(data)
        else:
            logger.error(f"Error getting agent: {response.text}")

    def fetch_contracts(self, page_nr = 1, limit = 20):
        url = self._baseurl + Contract.url_list()
        params = {
            "page": page_nr,
            "limit": limit
        }
        response = requests.get(url, headers=self._headers, params=params)
        if response.status_code == 200:
            response_data = response.json()["data"]
            self._contracts = [Contract.parse_obj(contract) for contract in response_data]
        else:
            logger.error(f"Error getting contracts: {response.text}")

    def agent(self):
        if self._agent is None:
            self.fetch_agent()
        return self._agent

    def contracts(self):
        if self._contracts is None:
            self.fetch_contracts()
        return self._contracts

    def contract_accept(self, contract):
        if contract.accepted == False:
            url = self._baseurl + contract.url_accept()
            response = requests.post(url, headers=self._headers)
            if response.status_code == 200:
                response_data = response.json()["data"]
                if response_data["accepted"] == True:
                    self._accepted_contracts.append(contract)
                    return 1
                else:
                    return -1
        else:
            return 0

    def fetch_systems(self, page_nr = 1, limit = 20):
        url = self._baseurl + Contract.url_list()
        params = {
            "page": page_nr,
            "limit": limit
        }
        response = requests.get(url, headers=self._headers, params=params)
        if response.status_code == 200:
            response_data = response.json()["data"]
            self._systems = [System.parse_obj(system) for system in response_data]
        else:
            logger.error(f"Error getting systems: {response.text}")

    def systems(self):
        if self._systems is None:
            self.fetch_systems()
        return self._systems

    def system_get(self, system_symbol):
        url = self._baseurl + System.url_get(system_symbol)
        response = requests.get(url, headers=self._headers)
        if response.status_code == 200:
            response_data = response.json()["data"]
            return System.parse_obj(response_data)
        else:
            logger.error(f"Error getting system: {response.text}")