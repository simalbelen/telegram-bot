import logging

# Configurar el logger para escribir en un archivo
logging.basicConfig(filename='logs/registro.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# # Ejemplo de uso
# logging.info('Este es un mensaje informativo')
# logging.warning('¡Cuidado! Esto es una advertencia')
# logging.error('¡Algo salió mal!')