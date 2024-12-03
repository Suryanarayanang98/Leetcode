# Write your MySQL query statement below
SELECT e1.name FROM (
SELECT managerID,count(id) as cnt
FROM Employee e
WHERE managerID is not null
GROUP BY managerID
) m
INNER JOIN
Employee e1
on e1.id = m.managerID
where cnt>=5