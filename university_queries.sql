
-- ex 3.1a Find the titles of courses in the CS dpeartment 
-- that are 3 credits.
SELECT
    title 
FROM
    course
WHERE   
    -- dept_name LIKE  'Comp% Sci%' AND
	dept_name ~ 'Comp.* Sci.*' AND   -- postgres specific 
	credits = 3;
	
-- Listing the names of all students who have taken Calculus
SELECT
    student.name, student.id, takes.semester, takes.year
FROM
    takes, 
	student, 
	(select course_id from course where title = 'Calculus') as t
WHERE
    t.course_id = takes.course_id AND
	student.id = takes.id
ORDER BY
    year, semester;
	
-- Rewrite the above query using a WITH
WITH 
    t as (select course_id from course where title = 'Calculus'),
	-- have as many subqueries here as needed
SELECT 
    student.name, student.id, takes.semester, takes.year
FROM
    takes, student, t
WHERE
    t.course_id = takes.course_id AND
	student.id = takes.id
ORDER BY
    year, semester;
	
-- List the course titles that are prereq for 
-- 692 Cat Herding
SELECT
    title 
FROM 
    course
WHERE
    course_id in (SELECT prereq_id FROM prereq WHERE course_id = 
	              (SELECT course_id from course where title = 'Computability Theory'));
				  

-- Names of prereqs version 2
WITH
    -- table of preqs
    t as (SELECT prereq_id FROM prereq WHERE course_id = '692')
SELECT
    title
FROM
    course,t
WHERE
    t.prereq_id = course_id;
	
-- What course is 130 a prereq for.
WITH
    t as (SELECT * FROM prereq WHERE prereq_id = '130')
SELECT
    course.course_id, title
FROM
    course, t
WHERE
    t.course_id = course.course_id; 