use sakila;
-- 1
-- 1a. Display the first and last names of all actors from the table actor. 
select first_name, last_name from actor;

-- 1b. Display the first and last name of each actor in a single column in upper case letters. 
-- Name the column Actor Name. 
select concat(First_Name, ' ', Last_Name) AS 'Full Name' from actor;

-- 2
-- 2a. You need to find the ID number, first name, and last name of an actor, of whom you know only the first name, 
-- "Joe." What is one query would you use to obtain this information?

select *
from actor
where first_name in
(
select first_name
from actor
where first_name = 'Joe'
);

-- 2b. Find all actors whose last name contain the letters GEN:
select *
from actor
where last_name in
(
select last_name
from actor
where last_name LIKE '%Gen%'
);

-- 2c. Find all actors whose last names contain the letters LI. 
-- This time, order the rows by last name and first name, in that order:
select *
from actor
where last_name in
	(
	select last_name
	from actor
	where last_name LIKE '%li%'
	)
order by last_name, first_name ASC;

-- 2d. Using IN, display the country_id and country columns of the following countries: Afghanistan, Bangladesh, and China:
select country_id, country
from country
where country in
(
select country
from country
where country = 'Afghanistan' OR country = 'Bangladesh' OR country = 'China'
);

-- 3
-- 3a. Add a middle_name column to the table actor. Position it between first_name and last_name. 
alter table actor
add middle_name varchar(25) after first_name; 

-- 3b. You realize that some of these actors have tremendously long last names. 
-- Change the data type of the middle_name column to blobs.
alter table actor
modify middle_name blob;

-- 3c. Now delete the middle_name column.
alter table actor
drop middle_name;

-- 4
-- 4a. List the last names of actors, as well as how many actors have that last name.
select count(last_name), last_name
from actor 
GROUP BY last_name
ORDER BY last_name ASC;

-- 4b. List last names of actors and the number of actors who have that last name, 
-- but only for names that are shared by at least two actors
select count(last_name), last_name
from actor 
GROUP BY last_name
having count(last_name) >= 2
ORDER BY last_name ASC;

-- 4c. Oh, no! The actor HARPO WILLIAMS was accidentally entered in the actor table as GROUCHO WILLIAMS, 
-- the name of Harpo's second cousin's husband's yoga teacher. Write a query to fix the record.

Select first_name, last_name, actor_id from actor where first_name = 'Groucho' and last_name = 'Williams';

update actor set first_name = 'Harpo'  where actor_id = 172;

-- 4d if the first name of the actor is currently HARPO, change it to GROUCHO. 
-- Otherwise, change the first name to MUCHO GROUCHO
update actor set first_name = 
case when first_name = 'Harpo' then 'Groucho' else 'Mucho Groucho' end 
where actor_id = 172;

-- 5
SHOW CREATE TABLE address;

-- 6
-- 6a. Use JOIN to display the first and last names, as well as the address, of each staff member. 
-- Use the tables staff and address: 
select s.last_name, s.first_name, a.address 
from staff s
inner join address a 
on s.address_id = a.address_id;

-- 6b. Use JOIN to display the total amount rung up by each staff member in August of 2005. 
-- Use tables staff and payment. 
select s.last_name, s.first_name, sum(p.amount)
from staff s
inner join payment p 
on s.staff_id = p.staff_id
where month(p.payment_date) = 08 AND year(p.payment_date) = 2005
group by s.staff_id;

-- 6c. List each film and the number of actors who are listed for that film. Use tables film_actor and film. 
-- Use inner join.
select count(fa.actor_id) as 'Actor Count', f.title 
from film_actor fa 
inner join film f 
on f.film_id = fa.film_id
group by f.title
order by `Actor Count` DESC;

-- 6d
select f.title, count(i.inventory_id) 
from film f 
inner join inventory i
on f.film_id = i.film_id
where f.title = 'Hunchback Impossible'
group by f.title;


-- 6e Using the tables payment and customer and the JOIN command, list the total paid by each customer. 
-- List the customers alphabetically by last name:
select c.customer_id, c.last_name, c.first_name, count(p.amount) as 'Total Paid' 
from customer c 
inner join payment p
on c.customer_id = p.customer_id
group by c.customer_id
order by c.last_name ASC;

-- 7 
-- 7a Use subqueries to display the titles of movies starting with the letters K and Q whose language is English.
select title
from film 
where title LIKE 'K%' OR title like 'Q%' AND language_id in 
(
	select language_id 
	from language 
    where name = 'English'
);

-- 7b. Use subqueries to display all actors who appear in the film Alone Trip.
select first_name, last_name  
from actor 
where actor_id in 
(
	select actor_id
	from film_actor 
    where film_id in 
    (
		select film_id 
        from film
        where title = 'Alone Trip'
	)
);

-- 7c need the names and email addresses of all Canadian customer
SELECT c.first_name, c.last_name, c.email, co.country
FROM customer c
    INNER JOIN address a 
        ON a.address_id = c.address_id
    INNER JOIN city ci
        ON ci.city_id = a.address_id
	INNER JOIN country co
		ON co.country_id = ci.country_id
        where co.country like 'Canada';


-- 7d Sales have been lagging among young families, and you wish to target all family movies for a promotion. 
-- Identify all movies categorized as famiy films.
select title 
    from film
    where film_id in
	(
		select film_id
		from film_category
		where category_id in 
		(
			select category_id
			from category
			where name like 'Family%'
		));


-- 7e Display the most frequently rented movies in descending order.
SELECT count(r.inventory_id) as 'Rentals', f.title
FROM film f
    INNER JOIN inventory i 
        ON f.film_id = i.film_id
	INNER JOIN rental r
		ON r.inventory_id = i.inventory_id
	GROUP BY f.title
	ORDER BY count(r.inventory_id) DESC;


-- 7f Write a query to display how much business, in dollars, each store brought in.
SELECT s.store_id, sum(p.amount) AS 'Total In Dollars'
FROM payment p
    INNER JOIN staff st 
        ON p.staff_id = st.staff_id
	INNER JOIN store s
		ON st.store_id = s.store_id
	GROUP BY s.store_id;

-- 7g. Write a query to display for each store its store ID, city, and country.

SELECT s.store_id, ci.city, co.country
FROM store s
	JOIN address a
		ON a.address_id = s.address_id
	JOIN city ci 
        ON a.city_id = ci.city_id
	JOIN country co 
        ON ci.country_id = co.country_id
	GROUP BY s.store_id;

-- 7h. List the top five genres in gross revenue in descending order. 
-- (Hint: you may need to use the following tables: category, film_category, inventory, payment, and rental.)

SELECT c.name, sum(p.amount) AS 'Gross Rental ($)'
FROM payment p
	JOIN  rental r
		ON p.customer_id = r.customer_id
	JOIN inventory i 
        ON i.inventory_id = r.inventory_id
	JOIN film f
		ON f.film_id = i.film_id
	JOIN film_category fc 
        ON f.film_id = fc.film_id
	JOIN category c
		on fc.category_id = c.category_id
	GROUP BY c.name
    ORDER BY sum(p.amount) DESC LIMIT 5;
    
-- 8
-- 8a Use the solution from the problem above to create a view.

CREATE VIEW Top_5_Genres AS
SELECT c.name, sum(p.amount) AS 'Gross Rental ($)'
FROM payment p
	JOIN  rental r
		ON p.customer_id = r.customer_id
	JOIN inventory i 
        ON i.inventory_id = r.inventory_id
	JOIN film f
		ON f.film_id = i.film_id
	JOIN film_category fc 
        ON f.film_id = fc.film_id
	JOIN category c
		on fc.category_id = c.category_id
	GROUP BY c.name
    ORDER BY sum(p.amount) DESC LIMIT 5;
    
-- 8b. How would you display the view that you created in 8a?
SELECT * FROM Top_5_Genres;

-- 8c delete view
DROP VIEW Top_5_Genres;

