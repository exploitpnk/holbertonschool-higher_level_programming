-- lists all shows from hbtn_0d_tvshows_rate by their rating
SELECT sh.title, SUM(shrt.rate) AS rating FROM tv_shows AS sh JOIN tv_show_ratings AS shrt ON sh.id=shrt.show_id GROUP BY sh.title ORDER BY rating DESC;
