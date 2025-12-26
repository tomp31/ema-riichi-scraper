from datetime import date, timedelta
import psycopg

from dbconn import get_dbconn
from repositories.player_repository import get_max_player_id
from repositories.result_repository import get_player_results
from services.mers_service import calculate_mers_ranking

DBCONN = get_dbconn()

if __name__ == '__main__':
    end_date = date(2025, 1, 1)
    start_date = date(2023, 1, 1)

    ranking_date = end_date

    with psycopg.connect(DBCONN) as conn:
        with conn.cursor() as cur:    
            while ranking_date >= start_date:
                max_player_id = get_max_player_id(cur)
                for player_id in range(1, max_player_id + 1):
                    print(f"Calculating MERS ranking for player id {player_id} on date {ranking_date}")
                    player_results = get_player_results(cur, player_id)
                    mers_ranking = calculate_mers_ranking(player_results, ranking_date)
                    cur.execute(
                        'select * from mers_ranking where player_id = %s and ranking_date = %s',
                        [player_id, ranking_date])
                    if cur.fetchone() is None:
                        cur.execute("""
                                    insert into mers_ranking (player_id, ranking_date, ranking)
                                    values %s, %s, %s
                                    """, [player_id, ranking_date, mers_ranking])
                    else:
                        cur.execute("""
                                    update mers_ranking
                                    set ranking = %s
                                    where player_id = %s
                                    and ranking_date = %s
                                    """, [mers_ranking, player_id, ranking_date])
                ranking_date -= timedelta(days = 7)