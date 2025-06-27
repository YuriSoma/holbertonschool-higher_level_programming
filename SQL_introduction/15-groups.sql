-- List records grouped by some INT

SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;