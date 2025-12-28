SELECT p.first_name, p.last_name, r.ranking_date, r.ranking
FROM public.mers_ranking r
JOIN public.players p on p.id = r.player_id
WHERE p.country = 'gb'
AND NOT EXISTS (
	SELECT 1
	FROM public.mers_ranking r_higher
	WHERE r.player_id = r_higher.player_id
	AND r.ranking < r_higher.ranking
)
AND NOT EXISTS (
	SELECT 1
	FROM public.mers_ranking r_newer
	WHERE r.player_id = r_newer.player_id
	AND r.ranking = r_newer.ranking
	AND r.ranking_date < r_newer.ranking_date
)
ORDER BY r.ranking DESC