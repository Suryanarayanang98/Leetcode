select p.product_id, ROUND(COALESCE(sum(COALESCE(p.price * u.units,0))/NULLIF(sum(COALESCE(u.units,0)),0),0),2) as average_price from prices p
left join unitssold u
on p.product_id = u.product_id and p.start_date<=u.purchase_date and p.end_date >= u.purchase_date
group by p.product_id
