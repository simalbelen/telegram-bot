# Get de todas las variables del keyring
import keyring

BOT_TOKEN = keyring.get_password("BOT_TOKEN", "BTB")
BOT_USERNAME = keyring.get_password("BOT_USERNAME", "BTB")