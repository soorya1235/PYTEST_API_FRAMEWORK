import base64

username = "example1"
# username = "philipjfry"
password = "example1"
# password = "10.77,"

# Concatenate username and password with a colon
credentials = f"{username}:{password}"

# Encode credentials in Base64
credentials_bytes = credentials.encode('utf-8')  # <-- Corrected encoding
base64_credentials = base64.b64encode(credentials_bytes)

# Convert the Base64 bytes to a string
authorization_header = "Basic " + base64_credentials.decode('utf-8')  # <-- Corrected decoding

print(authorization_header)
