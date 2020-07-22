-- lists all genres in the database hbtn_0d_tvshows_rate by their rating
SELECT gr.name,
       SUM(shrt.rate) AS rating FROM tv_show_ratings AS shrt
       JOIN tv_show_genres AS shgr
       	    ON shrt.show_id=shgr.show_id
       JOIN tv_genres AS gr
       	    ON gr.id=shgr.genre_id
       GROUP BY gr.name ORDER BY rating DESC;
