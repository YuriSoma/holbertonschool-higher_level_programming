-- Lists all records of a table

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.genre_id=tv_show_genres.id
ORDER BY tv_shows.title and tv_show_genres.genre_id;