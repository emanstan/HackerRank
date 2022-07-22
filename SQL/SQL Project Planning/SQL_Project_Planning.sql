/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
with ord as (
    select row_number() over (order by end_date) as r, task_id, start_date, end_date from Projects
),
bnd as (
    select
        row_number() over (order by n_end_date) as boundary,
        c_r,
        c_start_date, c_end_date,
        n_r,
        n_start_date, n_end_date,
        diff
    from (
        select
            cur.r as c_r,
            cur.start_date as c_start_date, cur.end_date as c_end_date,
            nxt.r as n_r,
            nxt.start_date as n_start_date, nxt.end_date as n_end_date,
            datediff(day, cur.end_date, nxt.end_date) as diff
        from ord cur
        left join ord nxt
            on cur.r-1 = nxt.r
        where nxt.end_date is null or datediff(day, nxt.end_date, cur.end_date) > 1
    ) tmp
)
select
    e.c_start_date, coalesce(s.n_end_date, e.c_end_date)
from bnd e
left join bnd s
    on e.boundary = s.boundary-1
order by datediff(day, e.c_start_date, coalesce(s.n_end_date, e.c_end_date)), e.c_start_date
;