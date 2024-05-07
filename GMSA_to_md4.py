#!/usr/bin/env python3
# Chxsec

import click
import hashlib
import base64

@click.command()
def hash_password():
    base64_input = click.prompt("Enter the GMSA_Base64_Encoded Password")
    hashed_password = hashlib.new("md4", base64.b64decode(base64_input)).hexdigest()
    print("MD4 Hash of the provided password:", hashed_password)

if __name__ == "__main__":
    hash_password()

