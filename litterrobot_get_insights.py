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
username = sys.argv[1]
password = sys.argv[2]

async def main():
    # Create an account.
    account = Account()

    try:
        # Connect to the API and load robots.
        await account.connect(username=username, password=password, load_robots=True)

        # Print robots associated with account.
        for robot in account.robots:
            print(await robot.get_insight())

    finally:
        # Disconnect from the API.
        await account.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
