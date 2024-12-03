# Write your MySQL query statement below
Select s.student_id,s.student_name,sub.subject_name,coalesce(attended_exams,0) as attended_exams from Students s 
cross join 
Subjects sub
left join 
(select student_id, subject_name, count(*) as attended_exams from Examinations e group by student_id, subject_name) ex
on s.student_id = ex.student_id and sub.subject_name = ex.subject_name
order by 1,3