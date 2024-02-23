-- 코드를 입력하세요
SELECT fh.FLAVOR from FIRST_HALF fh 
join ICECREAM_INFO ii on ii.FLAVOR=fh.FLAVOR 
where fh.TOTAL_ORDER >= 3000 and ii.INGREDIENT_TYPE='fruit_based'