-- All cities in hbtn_0d_usa
-- Each record should display: cities.id - cities.name - states.name

SELECT cities.id, cities.name, states.name
FROM cities
LEFT JOIN states ON states.id = cities.state_id
ORDER BY cities.id ASC;
