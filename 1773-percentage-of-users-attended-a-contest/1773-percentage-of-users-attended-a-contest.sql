with table_1 as (select count(*) as total_users from users)
Select contest_id, round(sum1/total_users*100,2) as percentage from (
select contest_id, count(user_id) as sum1
from register
group by contest_id
) f
cross join table_1
order by percentage desc, contest_id
