/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
with
d as (select row_number() over (order by name) as r, occupation, name from occupations where occupation = 'Doctor'),
p as (select row_number() over (order by name) as r, occupation, name from occupations where occupation = 'Professor'),
s as (select row_number() over (order by name) as r, occupation, name from occupations where occupation = 'Singer'),
a as (select row_number() over (order by name) as r, occupation, name from occupations where occupation = 'Actor'),
mx as (
    select max(c) as c
    from (
        select count(*) as c from d union all
        select count(*) as c from p union all
        select count(*) as c from s union all
        select count(*) as c from a
    ) tmp
)
select d.name, p.name, s.name, a.name
from (
    select r
    from (
        select row_number() over (order by (select 1)) as r
        from occupations
    ) tmp2
    where r <= (select mx.c from mx)
) tmp
left join d
    on tmp.r = d.r
left join p
    on tmp.r = p.r
left join s
    on tmp.r = s.r
left join a
    on tmp.r = a.r
;