-- 코드를 입력하세요
SELECT ugu.USER_ID, ugu.NICKNAME, sum(ugb.PRICE) as TOTAL_SALES
from USED_GOODS_USER ugu
join USED_GOODS_BOARD ugb on ugu.USER_ID=ugb.WRITER_ID and ugb.STATUS='DONE'
group by ugu.USER_ID
having TOTAL_SALES >= 700000
order by TOTAL_SALES asc
