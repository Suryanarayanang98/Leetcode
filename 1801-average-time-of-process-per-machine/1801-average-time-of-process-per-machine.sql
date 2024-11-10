# Write your MySQL query statement below
select a1.machine_id, round(avg(end_time-start_time),3) processing_time from ((select machine_id,process_id,timestamp start_time from Activity where activity_type = "start") a1 
inner join (select machine_id,process_id,timestamp end_time from Activity where activity_type = "end") a2
on a1.machine_id = a2.machine_id and a1.process_id = a2.process_id) group by a1.machine_id;