from public.config import *
from models import *

# apagar o arquivo, se houver
if os.path.exists(db_file):
    os.remove(db_file)
    
db.create_all()

print("Tabelas criadas")
