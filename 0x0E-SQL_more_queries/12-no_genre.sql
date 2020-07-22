-- lists all shows contained in hbtn_0d_tvshows without a genre linked
SELECT sh.title, shgr.genre_id FROM tv_shows sh LEFT JOIN tv_show_genres shgr ON sh.id=shgr.show_id WHERE shgr.genre_id IS NULL ORDER BY sh.title, shgr.genre_id ASC;
