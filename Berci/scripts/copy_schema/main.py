from classes import Environment

print('Forrás adatbázis megadása')
env = Environment.environment_selector()
print('\n'.join(env.database_names))
