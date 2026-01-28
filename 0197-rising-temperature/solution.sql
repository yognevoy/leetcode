# Write your MySQL query statement below
SELECT wt.id
FROM Weather wt
JOIN Weather wy
    ON DATEDIFF(wt.recordDate, wy.recordDate) = 1
    AND wt.temperature > wy.temperature
