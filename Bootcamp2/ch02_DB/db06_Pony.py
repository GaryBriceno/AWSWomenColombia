from pony.orm import Database, db_session
import statsmodels.api as sm

# Establezco el uso de la base de datos en memoria
db = Database('sqlite', ':memory:')

with db_session:
    data_loader = sm.datasets.sunspots.load_pandas()
    df = data_loader.data
    df.to_sql("sunspots", db.get_connection())
    print(db.select("count(*) FROM sunspots"))
