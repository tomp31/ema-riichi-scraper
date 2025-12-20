from math import ceil
import os

import psycopg

DBCONN = os.getenv("DBCONN", "dbname=riichi user=postgres password=admin")  # Default value if not set

def get_max_player_id(cur):
    cur.execute("select max(id) from players")
    return cur.fetchone()[0]

def calculate_rukrs_ranking(cur, player_id):
    cur.execute(
        'select tr.base_rank, t.days from tournament_results tr join tournaments t on tr.tournament_id = t.id where tr.player_id = %s;',
        [player_id])
    mers_results = cur.fetchall()
    results = []
    for (base_rank, days) in mers_results:
        for _ in range(0, days):
            results.append(base_rank)
    results.sort(reverse = True)
    result_count = len(results)
    for _ in range(result_count, 10): # add placeholder results
        results.append(0)
    part_a_count = ceil(result_count * 0.8)
    part_b_count = 8
    part_a_results = results[:part_a_count]
    part_b_results = results[:part_b_count]
    part_a_score = sum(part_a_results) / part_a_count
    part_b_score = sum(part_b_results) / part_b_count
    rukrs_ranking = (part_a_score + part_b_score) / 2
    cur.execute(
        'update players set rukrs_ranking = %s where id = %s',
        [rukrs_ranking, player_id])
  
if __name__ == '__main__':
    with psycopg.connect(DBCONN) as conn:
        with conn.cursor() as cur:    
            max_player_id = get_max_player_id(cur)
            for player_id in range(1, max_player_id + 1):
                print(f"Calculating RUKRS ranking for player id {player_id}")
                calculate_rukrs_ranking(cur, player_id)

