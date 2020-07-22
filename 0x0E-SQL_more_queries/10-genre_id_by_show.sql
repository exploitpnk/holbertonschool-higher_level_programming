-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT sh.title, shgr.genre_id FROM tv_shows AS sh JOIN tv_show_genres AS shgr ON sh.id=shgr.show_id ORDER BY sh.title, shgr.genre_id ASC;
