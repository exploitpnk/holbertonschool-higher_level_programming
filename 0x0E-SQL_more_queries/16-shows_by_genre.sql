--  lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
SELECT sh.title, gr.name FROM tv_shows AS sh LEFT JOIN tv_show_genres AS shgr ON sh.id=shgr.show_id LEFT JOIN tv_genres AS gr ON shgr.genre_id=gr.id ORDER BY sh.title, gr.name ASC;
