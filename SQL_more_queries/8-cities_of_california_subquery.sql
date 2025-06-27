-- Lists all records of a table

USE hbtn_0d_usa;

SELECT * cities
FROM cities
WHERE state_id = (
    SELECT id FROM states
      WHERE name = "California")
ORDER BY id;