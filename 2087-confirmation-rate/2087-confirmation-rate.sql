# Write your MySQL query statement below
SELECT s.user_id, ROUND(AVG(CASE WHEN c.action = 'confirmed' THEN 1 ELSE 0 END),2) as confirmation_rate 
FROM Signups s
LEFT JOIN
Confirmations c
on s.user_id = c.user_id
Group by s.user_id
