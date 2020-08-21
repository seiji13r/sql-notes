# psql Command Line NOTES <!-- omit in toc-->

- [psql Command Line NOTES ](#psql-command-line-notes)
  - [Launch from Ubuntu Command Line](#launch-from-ubuntu-command-line)
  - [Get Help](#get-help)
  - [Quit](#quit)
  - [List Users](#list-users)
  - [Check Current Connection Info](#check-current-connection-info)
  - [Change Password](#change-password)
  - [List Databases](#list-databases)
  - [Connect to Database](#connect-to-database)

## Launch from Ubuntu Command Line

```
sudo -u postgres psql postgres

psql -h [host] -p 5432 -U [User] [Database]
```

## Get Help
```
help
\h -> SQL help
\? -> psql help
```

## Quit

```
\q
```

## List Users

```
\du
```

## Check Current Connection Info

```
\conninfo
```

## Change Password

```
\password [USERNAME]
```

## List Databases

```
\l
```

## Connect to Database

```
\c [DATABASE]
```

## Check Users Privileges in the Database

```
\c [DATABASE]
## Connect to Database

```sql
SELECT DISTINCT grantee FROM information_schema.table_privileges;
 SELECT * FROM information_schema.table_privileges WHERE grantee = '[USERNAME]';

```
```
