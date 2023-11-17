# Get de todas las variables del keyring
import keyring

API_TOKEN = keyring.get_password("API_TOKEN", "BTB")
BOT_USERNAME = keyring.get_password("BOT_USERNAME", "BTB")