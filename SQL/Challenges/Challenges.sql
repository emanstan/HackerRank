/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
with
grp as (
    select
        c.hacker_id, h.name, count(*) as n
    from challenges c
    inner join hackers h
        on c.hacker_id = h.hacker_id
    group by 
        c.hacker_id, h.name
),
stats as (
    select max(n) as mx from grp
),
uniq as (
    select n
    from grp
    group by n
    having count(*) = 1
)
select grp.hacker_id, grp.name, grp.n
from grp
where exists (
    select 1
    from uniq chk
    where grp.n = chk.n
)
or grp.n = (
    select mx from stats
)
order by grp.n desc, grp.hacker_id
;