from datetime import date
import psycopg

from dbconn import get_dbconn

from repositories.player_repository import get_max_player_id
from repositories.result_repository import get_player_results
from services.rukrs_service import calculate_rukrs_ranking

DBCONN = get_dbconn()

if __name__ == '__main__':
    ranking_date = date(2025, 1, 1)
    min_date = date(ranking_date.year - 2, ranking_date.month, ranking_date.day)

    with psycopg.connect(DBCONN) as conn:
        with conn.cursor() as cur:    
            max_player_id = get_max_player_id(cur)
            for player_id in range(1, max_player_id + 1):
                print(f"Calculating RUKRS ranking for player id {player_id}")
                player_results = get_player_results(cur, player_id)
                rukrs_ranking = calculate_rukrs_ranking(cur, player_id, ranking_date, min_date)
                cur.execute(
                    'update players set rukrs_ranking = %s where id = %s',
                    [rukrs_ranking, player_id])