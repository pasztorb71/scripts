from Cluster import Cluster
from utils_sec import password_from_file

host, port = 'localhost', 5433
c = Cluster(host=host, port=port, passw=password_from_file(host, port))
ver = c.db_command_all_db("select current_database()")
print(ver)