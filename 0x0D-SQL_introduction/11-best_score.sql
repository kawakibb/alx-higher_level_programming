-- Lists all records in the table with a score( >= 10 )in my MySQL server.
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
