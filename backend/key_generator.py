import secrets

# Generierung des SECRET_KEY
secret_key = secrets.token_hex(32)
print(f'SECRET_KEY: {secret_key}')

# Generierung des JWT_SECRET_KEY
jwt_secret_key = secrets.token_hex(32)
print(f'JWT_SECRET_KEY: {jwt_secret_key}')
