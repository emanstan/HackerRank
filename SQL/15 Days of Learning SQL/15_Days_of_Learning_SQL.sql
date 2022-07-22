/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
with
dt as (
    select
        dense_rank() over (order by submission_date) as d_r,
        dense_rank() over (partition by hacker_id order by submission_date) as h_r,
        submission_date,
        hacker_id
    from submissions
),
stats as (
    select
        submission_date, count(distinct hacker_id) as c
    from dt
    where d_r = h_r
    group by
        submission_date
),
grp as (
    select
        submission_date, hacker_id, count(*) as n
    from submissions
    group by
        submission_date, hacker_id
),
rnk as (
    select
        row_number() over (
            partition by grp.submission_date
            order by grp.n desc, grp.hacker_id
        ) as r,
        grp.submission_date,
        grp.hacker_id
    from grp
)
select
    stats.submission_date,
    stats.c,
    rnk.hacker_id,
    h.name
from stats
inner join rnk
    on stats.submission_date = rnk.submission_date
    and rnk.r = 1
inner join hackers h
    on rnk.hacker_id = h.hacker_id
order by
    rnk.submission_date
;