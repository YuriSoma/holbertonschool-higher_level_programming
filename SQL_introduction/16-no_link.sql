-- List all records have a value

SELECT score, name
FROM second_table
ORDER BY score DESC
WHERE name IS NOT NULL;