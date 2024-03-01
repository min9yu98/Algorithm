-- 코드를 작성해주세요
select sum(score) as score, he.emp_no, he.emp_name, he.position, he.email
from HR_EMPLOYEES as he, HR_GRADE as hg
where he.EMP_NO=hg.EMP_NO
group by hg.year, he.emp_no
having hg.year=2022
order by score desc limit 1