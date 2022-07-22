/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
with
grp as (
    select
        s.hacker_id, s.challenge_id, max(s.score) as max_score
    from submissions s
    group by 
        s.hacker_id, s.challenge_id
)
select
    grp.hacker_id, h.name, sum(grp.max_score) as total_score
from grp
inner join hackers h
    on grp.hacker_id = h.hacker_id
group by
    grp.hacker_id, h.name
having
    sum(grp.max_score) > 0
order by
    sum(grp.max_score) desc, grp.hacker_id
;