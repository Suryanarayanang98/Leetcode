select name, bonus from employee e left join bonus b on e.empid = b.empid where coalesce(bonus,0)<1000