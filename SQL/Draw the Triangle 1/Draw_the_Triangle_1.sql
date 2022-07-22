/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
declare @start int, @end int;
select @start = 20, @end = 1;
with lst as (
    select @start as n
    union all
    select n - 1
    from lst
    where n > @end
)
select replicate('* ', n)
from lst
;