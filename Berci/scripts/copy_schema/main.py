import Environment
from Database import Database

print('Forrás adatbázis megadása')
env = Environment.environment_selector()
print('\n'.join(env.database_names))
