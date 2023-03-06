-- list score and name 
-- where name is not null
-- score in descending order
SELECT score, name FROM second_table
WHERE name IS NOT 'NULL'
ORDER BY score[DESC];
