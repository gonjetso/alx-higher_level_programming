-- List all record where name value is not null
-- Display score and name

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
