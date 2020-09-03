# 0x14. MySQL

## Resources:books:
Read or watch:
* What is a primary-replica cluster
* MySQL primary replica setup
* Build a robust database backup strategy
* man or help - mysqldump
---
## Learning Objectives:bulb:
* What you should learn from this project:
* General

* What is the main role of a database
* What is a database replica
* What is the purpose of a database replica
* Why database backups need to be stored in different physical locations
* What operation should you regularly perform to make sure that your database backup strategy actually works
---

### [0. Install MySQL]

### [1. Let us in!]

* Create a user and password for both MySQL databases which will allow the checker access to them.



### [2. If only you could see what I've seen with your eyes ]
* you’ll need to have a database with at least one table and one row in your primary MySQL server (web-01) to * replicate from.


### [3. Quite an experience to live in fear, isn't it?]
* On your primary MySQL server (web-01), create a new user for the replica server.


### [4. Setup a Primary-Replica infrastructure using MySQL]
* Once MySQL replication is setup, add a new record in your table via MySQL on web-01 
* and check if the record has been replicated in MySQL web-02. If you see it, 
* it means your replication is working!


### [5. MySQL backup]
* Write a Bash script that generates a MySQL dump and creates a compressed archive out of it.

---

## Author
* **Sandra Macias** - [s-macias](https://github.com/s-macias)