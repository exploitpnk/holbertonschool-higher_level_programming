-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows
SELECT sh.title FROM tv_shows AS sh
LEFT JOIN
(
       SELECT sh.id FROM tv_shows AS sh
       JOIN tv_show_genres AS shgr
       ON sh.id=shgr.show_id
       JOIN tv_genres AS gr
       ON shgr.genre_id=gr.id
       WHERE gr.name = "Comedy"
) AS subcomd ON subcomd.id = sh.id WHERE subcomd.id IS NULL ORDER BY sh.title ASC;
