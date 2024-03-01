-- 코드를 입력하세요
SELECT ao.ANIMAL_ID, ao.NAME
from ANIMAL_INS as ai, ANIMAL_OUTS as ao
where ai.ANIMAL_ID=ao.ANIMAL_ID and timediff(ai.DATETIME, ao.DATETIME) > 0
order by ai.DATETIME asc