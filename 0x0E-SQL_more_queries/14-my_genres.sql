-- list all genres of the show Dexter
-- each record should display: tv_genres.name
-- results must be sorted in ascending order by the genre name
SELECT tv_genres.name 
FROM tv_show_genres RIGHT JOIN tv_genres 
ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_show_genres.show_id = 8
GROUP BY tv_genres.name
ORDER BY tv_genres.name; 
