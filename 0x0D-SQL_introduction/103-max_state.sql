-- script that displays the max temperature of each state
SELECT `state`, AVG(`score`) AS `avg_temp`
FROM `temperatures`
GROUP BY `state`
ORDER BY `state`;
