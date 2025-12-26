def get_max_player_id(cur):
    cur.execute("select max(id) from players")
    return cur.fetchone()[0]