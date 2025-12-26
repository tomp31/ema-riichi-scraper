import psycopg

from datetime import date

from dbconn import get_dbconn
from repositories.player_repository import get_max_player_id
from repositories.result_repository import get_player_results
from services.mers_service import calculate_mers_ranking

DBCONN = get_dbconn()

if __name__ == '__main__':
    ranking_date = date(2025, 1, 1)

    with psycopg.connect(DBCONN) as conn:
        with conn.cursor() as cur:    
            max_player_id = get_max_player_id(cur)
            for player_id in range(1, max_player_id + 1):
                print(f"Calculating MERS ranking for player id {player_id}")
                player_results = get_player_results(cur, player_id)
                mers_ranking = calculate_mers_ranking(player_results, ranking_date)
                cur.execute(
                    'update players set mers_ranking = %s where id = %s',
                    [mers_ranking, player_id])