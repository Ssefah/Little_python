import secrets
# print(dir(secrets))
token_bytes = secrets.token_bytes(32)
token_hexs = secrets.token_hex(3)
token_urls = secrets.token_urlsafe(16)
print(token_bytes)
print(token_hexs)
print(token_urls)
