-- list all genres not linked to the show Dexter
-- The tv_shows table contains only one record where title = Dexter
-- Each record should display: tv_genres.name
SELECT name 
FROM tv_genres WHERE name NOT IN 
(SELECT tv_genres.name 
FROM tv_show_genres 
RIGHT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
RIGHT JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter')
ORDER BY name ASC;

