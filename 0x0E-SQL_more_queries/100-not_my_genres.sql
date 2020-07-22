-- uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT gr.name FROM tv_genres AS gr
LEFT JOIN
(
       SELECT gr.id FROM tv_genres AS gr
       JOIN tv_show_genres AS shgr
       	    ON gr.id=shgr.genre_id
       JOIN tv_shows AS sh
       	    ON shgr.show_id=sh.id
       WHERE sh.title = "Dexter"
       ORDER BY gr.name ASC
) AS subdx ON subdx.id = gr.id WHERE subdx.id IS NULL ORDER BY gr.name ASC;
