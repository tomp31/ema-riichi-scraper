from math import ceil

def calculate_rukrs_ranking(player_results, ranking_date, min_date):
    tournament_results = [
        (base_rank, date, days) \
        for (base_rank, date, _, days) \
        in player_results \
        if (date > min_date) & (date <= ranking_date)]
    
    if tournament_results.count == 0:
        return 0

    results = []

    for (base_rank, days) in tournament_results:
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
    return (part_a_score + part_b_score) / 2