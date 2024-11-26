# Documentacao lib psycopg
# https://www.psycopg.org/psycopg3/docs/basic/usage.html
from settings import config
import psycopg

def teste():
        
    # Conectar ao banco de dados
    with psycopg.connect(f"dbname={config["DB_NAME"]} user={config["DB_USER"]} password={config["DB_PASSWORD"]} host={config["DB_HOST"]} port={config["DB_PORT"]}") as conn:
        # Criar um cursor
        with conn.cursor() as cur:
            # Executar a consulta
            cur.execute("SELECT * FROM nomes")
            
            # Buscar os resultados
            rows = cur.fetchall()

            conn.close()

    # Imprimir os resultados
    for row in rows:
        print(row)
