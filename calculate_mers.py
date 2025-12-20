import datetime
from math import ceil
import os

import psycopg

DBCONN = os.getenv("DBCONN", "dbname=riichi user=postgres password=admin")  # Default value if not set

def get_max_player_id(cur):
    cur.execute("select max(id) from players")
    return cur.fetchone()[0]

def calculate_mers_ranking(cur, player_id):
    cur.execute(
        'select tr.base_rank, t.weight, t.date from tournament_results tr join tournaments t on tr.tournament_id = t.id where tr.player_id = %s;',
        [player_id])
    results = cur.fetchall()
    results = [get_weight_adjusted_result(result) for result in results]
    results.sort(key = lambda r: r[0], reverse = True) # sort on base rank
    result_count = len(results)
    for _ in range(result_count, 5): # add placeholder results
        results.append((0, 1, datetime.date.today()))
    part_a_count = 5 + ceil((result_count - 5) * 0.8)
    part_b_count = 4
    part_a_results = results[:part_a_count]
    part_b_results = results[:part_b_count]
    part_a_weight_sum = sum([r[1] for r in part_a_results])
    part_a_numerator = sum([r[0] * r[1] for r in part_a_results])
    part_a_score = part_a_numerator / part_a_weight_sum
    part_b_weight_sum = sum([r[1] for r in part_b_results])
    part_b_numerator = sum([r[0] * r[1] for r in part_b_results])
    part_b_score = part_b_numerator / part_b_weight_sum
    mers_ranking = (part_a_score + part_b_score) / 2
    cur.execute(
        'update players set mers_ranking = %s where id = %s',
        [mers_ranking, player_id])
    
def get_weight_adjusted_result(result):
    (base_rank, weight, date) = result
    if date.year == 2023:
        return (base_rank, weight / 2, date)
    else:
        return result

if __name__ == '__main__':
    with psycopg.connect(DBCONN) as conn:
        with conn.cursor() as cur:    
            max_player_id = get_max_player_id(cur)
            for player_id in range(1, max_player_id + 1):
                print(f"Calculating MERS ranking for player id {player_id}")
                calculate_mers_ranking(cur, player_id)

