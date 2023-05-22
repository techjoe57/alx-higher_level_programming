-- list all genres of the show Dexter
-- each record should display: tv_genres.name
-- results must be sorted in ascending order by the genre name
SELECT tv_genres.name 
FROM tv_show_genres 
RIGHT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
RIGHT JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name; 
