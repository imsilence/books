title: finance模块
date: 2015-11-11 11:00:28
tags: [mysql]
categories: [db]
---


CREATE USER 'cloud'@'%' IDENTIFIED BY 'cloud!@#123'; 
GRANT ALL ON *.* TO 'cloud'@'10.18.24.%' WITH GRANT OPTION;
GRANT ALL ON *.* TO 'cloud'@'10.18.213.%' WITH GRANT OPTION;
SET PASSWORD FOR 'cloud'@'10.18.24.%' = PASSWORD('cloud!@#123');
SET PASSWORD FOR 'cloud'@'10.18.213.%' = PASSWORD('cloud!@#123');

REVOKE ALL ON databasename.tablename FROM 'cloud'@'%';
DROP USER 'cloud'@'%'

权限:
ALTER   Allows use of ALTER TABLE.
ALTER ROUTINE   Alters or drops stored routines.
CREATE  Allows use of CREATE TABLE.
CREATE ROUTINE  Creates stored routines.
CREATE TEMPORARY TABLE  Allows use of CREATE TEMPORARY TABLE.
CREATE USER Allows use of CREATE USER, DROP USER, RENAME USER, and REVOKE ALL PRIVILEGES.
CREATE VIEW Allows use of CREATE VIEW.
DELETE  Allows use of DELETE.
DROP    Allows use of DROP TABLE.
EXECUTE Allows the user to run stored routines.
FILE    Allows use of SELECT... INTO OUTFILE and LOAD DATA INFILE.
INDEX   Allows use of CREATE INDEX and DROP INDEX.
INSERT  Allows use of INSERT.
LOCK TABLES Allows use of LOCK TABLES on tables for which the user also has SELECT privileges.
PROCESS Allows use of SHOW FULL PROCESSLIST.
RELOAD  Allows use of FLUSH.
REPLICATION Allows the user to ask where slave or master
CLIENT  servers are.
REPLICATION SLAVE   Needed for replication slaves.
SELECT  Allows use of SELECT.
SHOW DATABASES  Allows use of SHOW DATABASES.
SHOW VIEW   Allows use of SHOW CREATE VIEW.
SHUTDOWN    Allows use of mysqladmin shutdown.
SUPER   Allows use of CHANGE MASTER, KILL, PURGE MASTER LOGS, and SET GLOBAL SQL statements. Allows mysqladmin debug command. Allows one extra connection to be made if maximum connections are reached.
UPDATE  Allows use of UPDATE.
USAGE   Allows connection without any specific privileges.