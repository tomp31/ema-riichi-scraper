import psycopg

from dbconn import get_dbconn
from services.player_service import get_max_player_id
from services.rukrs_service import calculate_rukrs_ranking

DBCONN = get_dbconn()

if __name__ == '__main__':
    with psycopg.connect(DBCONN) as conn:
        with conn.cursor() as cur:    
            max_player_id = get_max_player_id(cur)
            for player_id in range(1, max_player_id + 1):
                print(f"Calculating RUKRS ranking for player id {player_id}")
                calculate_rukrs_ranking(cur, player_id)