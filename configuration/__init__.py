# SPDX-License-Identifier: MIT

import os

from dotenv import load_dotenv

load_dotenv()

SECRETKEY = os.getenv("SECRETKEY")
SECURE_COOKIE = os.getenv("SECURE_COOKIE")
