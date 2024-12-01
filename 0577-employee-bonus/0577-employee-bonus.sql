# Write your MySQL query statement below
select * from (Select e.name, b.bonus from Employee e
left join
Bonus b
using (empId)
) d
where bonus < 1000 or bonus is null
