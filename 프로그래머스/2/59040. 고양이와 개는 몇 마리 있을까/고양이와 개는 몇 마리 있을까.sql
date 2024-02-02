-- 코드를 입력하세요
SELECT ANIMAL_TYPE, count(ANIMAL_ID) as count
FROM ANIMAL_INS
group by ANIMAL_TYPE
having ANIMAL_TYPE='Dog' or ANIMAL_TYPE='Cat'
order by ANIMAL_TYPE