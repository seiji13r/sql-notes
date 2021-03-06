# My Personal SQL Notes <!-- omit in toc -->
- [Overview](#overview)
- [Resources](#resources)
  - [Tools](#tools)
- [PostgreSQL Installation Notes](#postgresql-installation-notes)
  - [Ubuntu Linux Virtual Machine Notes](#ubuntu-linux-virtual-machine-notes)
    - [Enable Remote Connections](#enable-remote-connections)
    - [Create Super User as postgres USER](#create-super-user-as-postgres-user)
    - [Create USER and ASSOCIATED DATABASE](#create-user-and-associated-database)
    - [RESTORE backup or tar](#restore-backup-or-tar)
- [MySQL Installation Notes](#mysql-installation-notes)
    - [Edit `/etc/mysql/mysql.conf.d/mysqld.cnf`](#edit-etcmysqlmysqlconfdmysqldcnf)
    - [Create A Remote User](#create-a-remote-user)
    - [Restart MySQL Service](#restart-mysql-service)

# Overview

The Following Notes are created as I'm studing and following along the next courses:

[Udemy' SQL Bootcamp with PostgreSQL](https://www.udemy.com/the-complete-sql-bootcamp/)
[PostgreSQL Tutorial](http://www.postgresqltutorial.com/)

# Resources

[PostgreSQL Documentation](https://www.postgresql.org/docs/)

[PostgreSQL DVD Rental Sample Database](https://wiki.postgresql.org/wiki/Sample_Databases)

[PostgreSQL Tutorial](http://www.postgresqltutorial.com/)

[PostgreSQL Wiki](https://wiki.postgresql.org/wiki/Main_Page)

[PostreSQL Sample Databases](https://community.embarcadero.com/article/articles-database/1076-top-3-sample-databases-for-postgresql)

[MySQL Documentation]()
[MySQL Sakila Sample Database "DVD Rental"]()

## Tools

[DBeaver](https://dbeaver.io/download/)

# PostgreSQL Installation Notes

## Ubuntu Linux Virtual Machine Notes

```bash
sudo apt-get update
sudo apt-get upgrade

sudo apt-get install postresql

# Check if PostrgreSQL is listening
sudo netstat -tulpn

# Check if listed in Services
sudo service --status-all

# Test Connection from Consol for the first time
sudo -u postgres psql postgres
# Quit
\q
```

### Enable Remote Connections

[Reference](https://blog.bigbinary.com/2016/01/23/configure-postgresql-to-allow-remote-connection.html)
[Change Password](https://serverfault.com/questions/110154/whats-the-default-superuser-username-password-for-postgres-after-a-new-install)

**Checklist**

* [ ] Install PostgreSQL
* [ ] Check that service is listening on its default\q port 5432
* [ ] Edit `postgresql.conf` to accept connections from outside.
* [ ] Edit `pg_hba.conf` to accept user connections from outside via password authentication.
* [ ] Create a Remote Super User.
* [ ] Restart the Service
* [ ] Test the Connection

```bash
# Edit pstgresql.conf file usually found in /etc.
sudo vim /etc/postgresql/10/main/postgresql.conf 
# vim command -> : set number
# change line 59 
# listen_addresses = 'localhost' -> listen_addresses = '*'

sudo vim /etc/postgresql/10/main/pg_hba.conf
# Add At the end
# # Allow Remote Connections
# host    all             all             0.0.0.0/0               md5
# host    all             all             ::/0                    md5


sudo service postgresql restart
```

### Create Super User as postgres USER

[Reference1](https://tableplus.io/blog/2018/10/how-to-create-superuser-in-postgresql.html)
[Reference2](https://support.chartio.com/knowledgebase/creating-a-user-with-p)

```console
sudo -u postgres psql
```

```sql
CREATE ROLE pgremote SUPERUSER LOGIN CREATEROLE CREATEUSER REPLICATION BYPASSRLS;
ALTER ROLE pgremote WITH PASSWORD '[password]';
```

### Create USER and ASSOCIATED DATABASE

```sql
CREATE ROLE [USER-NAME] LOGIN PASSWORD '[password]';
CREATE DATABASE [DB-NAME] WITH OWNER=[USER-NAME];

-- Example
CREATE ROLE test LOGIN PASSWORD '1234';
CREATE DATABASE mytest WITH OWNER=test;

```

### RESTORE backup or tar

The following example is done with dvdrental.tar database example.

```bash
# Create the database in psql
sudo -u postgres psql
# or
psql -h localhost -U [USER] [DATABASE]

CREATE DATABASE [DATABASE];
\q

# Database
pg_restore -h localhost -U [USER] -d [DATABASE] -v [FILE_PATH]
# Example
pg_restore -h localhost -U pgremote -d dvdrental -v "/home/ubuntu/dvdrental.tar"

```

# MySQL Installation Notes
[Reference](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-18-04)
```bash
sudo apt-get update
sudo apt-get install mysql-server
sudo mysql_secure_installation
# Enable / Disable VALIDATE PASSWORD PLUGIN
# SET root Password
# Default all other options
```

### Edit `/etc/mysql/mysql.conf.d/mysqld.cnf`

```console
sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf
```

```bash
# Change line 43
# From
bind-address            = 127.0.0.1
# To
bind-address            = 0.0.0.0
```

### Create A Remote User
```console
sudo mysql -u root -p
```

```sql
CREATE USER 'myroot'@'%' IDENTIFIED BY 'myroot';

GRANT ALL PRIVILEGES ON *.* TO 'myroot'@'%' WITH GRANT OPTION;

-- ALTER USER 'root'@'%' IDENTIFIED BY 'MyNewPass';

```

[Reference for Problem Access Denied](https://stackoverflow.com/questions/39281594/error-1698-28000-access-denied-for-user-rootlocalhost)
[Reference to Create a Remote User](https://stackoverflow.com/questions/16287559/mysql-adding-user-for-remote-access)

### Restart MySQL Service

```bash
# Check MySql status
sudo service mysql status
# restart MySql Service
sudo service mysql restart
```