import datetime
from math import ceil

def calculate_mers_ranking(player_results, ranking_date):
    results = [get_weight_adjusted_result(result, ranking_date) for result in player_results]
    results = [result for result in results if result is not None] # filter
    
    result_count = len(results)
    
    if result_count == 0:
        return 0
    
    results.sort(key = lambda r: r[0], reverse = True) # sort on base rank
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
    return (part_a_score + part_b_score) / 2
    
def get_weight_adjusted_result(result, ranking_date):
    (base_rank, result_date, weight, _) = result
    if (get_dropoff_date(result_date) <= ranking_date) | (result_date > ranking_date) :
        return None
    elif get_weight_halved_date(result_date) <= ranking_date:
        return (base_rank, weight / 2)
    else:
        return (base_rank, weight)
    
def get_dropoff_date(result_date):
    return add_years_to_mers_result(result_date, 2)

def get_weight_halved_date(result_date):
    return add_years_to_mers_result(result_date, 1)

def add_years_to_mers_result(result_date, years_to_add):
    year = result_date.year
    month = result_date.month
    day = result_date.day
    modified_date = datetime.date(year + years_to_add, month, day)
    if (is_in_covid_freeze(modified_date)): # decay delayed by 2 years during COVID freeze
        modified_date = datetime.date(year + years_to_add + 2, month, day)
    return modified_date

def is_in_covid_freeze(date):
    return ((date >= datetime.date(2020, 4, 1)) & (date < datetime.date(2022, 4, 1)))

