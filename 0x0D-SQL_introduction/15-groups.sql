-- list count of students with the same score
SELECT score, count(score) AS number FROM second_table GROUP BY score ORDER BY number DESC;
