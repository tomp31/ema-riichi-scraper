import psycopg

from datetime import date

from dbconn import get_dbconn
from services.mers_service import calculate_mers_ranking
from services.player_service import get_max_player_id

DBCONN = get_dbconn()

if __name__ == '__main__':
    with psycopg.connect(DBCONN) as conn:
        with conn.cursor() as cur:    
            max_player_id = get_max_player_id(cur)
            for player_id in range(1, max_player_id + 1):
                print(f"Calculating MERS ranking for player id {player_id}")
                calculate_mers_ranking(cur, player_id, date(2025, 1, 1))