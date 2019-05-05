"""Main configuration file. Can either pull from the
environment or from this file.
"""

import os

"""
===== WEB SPECIFIC =====
"""

# What's this app called?
APP_NAME = os.environ.get("APP_NAME", "faqbot")

# App network port.
PORT = int(os.environ.get("PORT", 8114))

# Is the app running in debug mode?
DEBUG = bool(os.environ.get("DEBUG", False))

# Secret for JWTs.
SECRET = os.environ.get("SECRET", "CHANGE_ME")

# Admin password.
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "CHANGE_ME")

# MongoDB Storage URL
MONGO_URL = os.environ.get("MONGO_URL", "mongodb://localhost/faqbot")

"""
===== MAIL SPECIFIC =====
"""

# IMAP server details.
IMAP_SERVER = "imap.gmail.com"
SMTP_SERVER = "smtp.gmail.com"
MAIL_USER = "communications@hack.gt"
MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD", "CHANGE_ME")

# SMTP server details.
SEND_MAIL_USER = MAIL_USER
SEND_MAIL_PASSWORD = MAIL_PASSWORD
MAIL_FROM = "hello@hack.gt"

# This footer is appended at the end of _every_ email
# sent by this bot. Just to make sure people can reach
# out again if they want to.
FOOTER = """
<br><br> <i>~~ This was an automated message, please <a href="mailto:hello@hack.gt">email us</a> again if this didn't help! ~~</i>
"""

TRIGGERS = ["@faqbot", "@fb"]
