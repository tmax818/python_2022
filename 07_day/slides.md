![](../images/coding_dojo_logo_white.png)
<!-- .slide:data-background="#000000" -->
---
# MySQL Queries
---
## SQL
--
### Intro to SQL
<!-- .slide:data-background="#000000" -->
--
![](../images/sql-icon.png)
--
### Database and SQL

---
## Connecting to MySQL
---
## Import
---
## `SELECT`
--
![](../images/twitter_ERD.png)
--
<!-- .slide:data-background="#001100" -->
```sql
SELECT * FROM table_names; 
```
- select everything from table_names <!-- .element: class="fragment" -->
--
<!-- .slide:data-background="#000600" -->
```sql
SELECT column_name FROM table_names; 
```
- select column_name from table_names <!-- .element: class="fragment" -->
--
<!-- .slide:data-background="#000600" -->
```sql
SELECT column_name1, column_name2 FROM table_names; 
```
- select column_name1 and column_name2 from table_names <!-- .element: class="fragment" -->
--
### `SELECT` with Conditionals
--
<!-- .slide:data-background="#000600" -->

```sql
SELECT column_name1 
FROM table_names 
WHERE id = 2;
```

- select the record from column_name1 from table_names with an id of 2 <!-- .element: class="fragment" -->
--


---
## `INSERT`
--
<!-- .slide:data-background="#000600" -->

```sql
INSERT INTO table_name (column_name1, column_name2) 
VALUES('column1_value', 'column2_value');
```

---
## `UPDATE`
--
<!-- .slide:data-background="#000600" -->

```sql
UPDATE table_name 
SET column_name1 = 'some_value', column_name2='another_value' 
WHERE condition(s)
```
--
>IMPORTANT: if WHERE condition is not added to the UPDATE statement, the changes will be applied to every record in the table.
---
## `DELETE`
--
<!-- .slide:data-background="#000600" -->

```sql
DELETE FROM table_name (column_name1, column_name2) 
VALUES('column1_value', 'column2_value');
```
---
## Functions
---
## Joins
---
## Left Joins
---
## Export
---
## Forward Engineer
---
## MySQL Workbench Setup (Practice)
---
## Users (Practice)
---
## Dojo and Ninjas (Core)
---
## Friendships (Practice)
---
## MySQL Countries (Core)







---

---
## data types
--

--

---
## simple blog
---
## likes
---
## yelp
---
