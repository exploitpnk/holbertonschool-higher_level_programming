-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT gr.name name FROM tv_genres AS gr JOIN tv_show_genres AS shgr ON gr.id=shgr.genre_id JOIN tv_shows AS sh ON shgr.show_id=sh.id WHERE sh.title = "Dexter" ORDER BY gr.name ASC;
