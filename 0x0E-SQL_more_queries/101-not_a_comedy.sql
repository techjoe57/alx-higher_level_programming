-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows
-- The database name will be passed as an argument of the mysql command
SELECT title
FROM tv_shows
WHERE title NOT IN
(SELECT tv_shows.title
FROM tv_show_genres
RIGHT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
RIGHT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy')
ORDER BY title ASC;
