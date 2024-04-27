-- script that displays the average temperature
SELECT `city`, AVG(`score`) AS `average`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
