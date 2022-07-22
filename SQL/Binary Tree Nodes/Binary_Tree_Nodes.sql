/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
with
r as (select 'Root' as t, n, p from bst where p is null),
l as (
    select 'Leaf' as t, n, p
    from bst l
    where not exists (
        select 1
        from bst chk
        where chk.p = l.n
    )
)
select
    b.n,
    coalesce(r.t, l.t, 'Inner')
from bst b
left join l
    on b.n = l.n
left join r
    on b.n = r.n
order by
    b.n
;