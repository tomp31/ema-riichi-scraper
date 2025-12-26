def get_player_results(cur, player_id):
    cur.execute("""
                select tr.base_rank, t.date, t.weight, t.days
                from tournament_results tr
                join tournaments t on tr.tournament_id = t.id
                where tr.player_id = %s
                order by t.date
                """,
        [player_id])
    return cur.fetchall()