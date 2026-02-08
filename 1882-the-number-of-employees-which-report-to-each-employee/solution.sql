# Write your MySQL query statement below
SELECT m.employee_id, m.name, COUNT(*) AS reports_count, ROUND(AVG(e.age)) AS average_age
FROM Employees e
LEFT JOIN Employees m
    ON e.reports_to = m.employee_id
WHERE m.employee_id IS NOT NULL
GROUP BY employee_id
ORDER BY employee_id ASC
