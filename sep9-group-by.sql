select
    max(salary)  -- aggregate function
from
    instructor;

select
    avg(salary)  -- aggregate function
from
    instructor;

-- Find all of the instructors earning the maximum salary
select
    id,name
from
    instructor
where
    salary = (select max(salary) from instructor);

-- Find all of the instructors who make less
-- than the average salary
select
    id,name
from
    instructor
where
    salary < (select avg(salary) from instructor);

-- How many faculty are teaching in Spring 2010
select distinct
    *
from
    teaches
where
    semester = 'Spring' and year = 2010;

select
    count(*)
from
    (select distinct
    id
from
    teaches
where
    semester = 'Spring' and year = 2010) as t;

select
    count(distinct id)
from
    teaches
where
    semester = 'Spring' and year = 2010;

-- Table of Instructors teaching 3 classes in 2006
select
    id,count(id)   -- applies to the groups
from
    teaches
where
    year = 2006
group by
    id
having      -- conditions on a group by
    count(id) = 3;

-- Get the average salary of each department
select
    dept_name, avg(salary)
from
    instructor
group by
    dept_name;

