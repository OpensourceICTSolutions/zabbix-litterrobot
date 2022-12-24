#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2022 Opensource ICT Solutions B.V.
# https://oicts.com
#
#version: 1.0.0
#date: 25-12-2022
#
import asyncio
import sys

from pylitterbot import Account

# Set email and password for initial authentication.
username = "EMAIL HERE"
password = "PASSWORD HERE"

async def main():
    # Create an account.
    account = Account()

    try:
        # Connect to the API and load robots.
        await account.connect(username=username, password=password, load_robots=True)

        # Print robots associated with account.
        print("Robots:")
        for robot in account.robots:
            print(robot)
    finally:
        # Disconnect from the API.
        await account.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
