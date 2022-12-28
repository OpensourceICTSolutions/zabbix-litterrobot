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
from datetime import datetime
import json
import time
import re
import sys
from datetime import datetime

from pylitterbot import Account

# Set email and password for initial authentication.
username = sys.argv[1]
password = sys.argv[2]

# Declare search variable
date = datetime.today().strftime('%Y-%m-%d')
clean_cycle_complete = r"{}[A-Za-z0-9:.+\s]+Clean Cycle Complete".format(date)
drawer_full = r"{}[A-Za-z0-9:.+\s]+Drawer[\sA-Za-z]+Full".format(date)

async def main():
    # Create an account.
    account = Account()

    try:
        # Connect to the API and load robots.
        await account.connect(username=username, password=password, load_robots=True)

        # Print robots associated with account.
        print("")
        for robot in account.robots:
            rawact = await robot.get_activity_history()

        result_string = ','.join(str(v) for v in rawact)
        ccc = re.findall(clean_cycle_complete,result_string)
        df = re.findall(drawer_full,result_string)

        # Create JSON for sending to Zabbix
        print("{\"data\":[{\"CCC\":",len(ccc),",\"DF\":",len(df),"}]}")

    finally:
        # Disconnect from the API.
        await account.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
