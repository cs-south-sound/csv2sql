# ETL Multiple CSVs Into MySQL Database
This repository provides an example of using Python3 to take a directory of multiple CSVs and
Extract, Transform, and Load (ETL) the data into a local MySQL database. The ETL scripts are 
set up for working with a directory of CSVs for [Ark Invest Funds](https://ark-funds.com/our-etfs/) 
daily breakdowns. CSVs detailing the full holdings in each of their funds are updated each open day 
of the NYSE and can be downloaded from their pages on the website.

## Initial Setup
`pipeline.sh` is a bash script designed for running the complete workflow of the repository. Some 
initial setup is required and listed below.
* MySQL Server installed and setup
* Python3 installed
* Ark Invest CSVs downloaded and saved in a directory locally

### Setting Up The Database
Once MySQL Server is setup, a database needs to be created. This can be done from the terminal by 
executing the following steps.

**Access MySQL from terminal (replace 'root' with your username)**
``` bash
sudo mysql -u root -p
```
Enter your sudo Linux password, followed by your database user (root) password.

**Create database for fund holdings**
``` sql
CREATE DATABASE fund_holdings;
```

**Create table in MySQL database**
Utilizing the `create_table.sql` script, create a table for inserting data with an auto increment
primary key column.

### Create A Config File
The Python scripts utilize a `config.py` file for accessing the following information that is unique 
to the local host.

* file path to directory of Ark CSVs
* MySQL database name, username, password, host

## ETL Scripts
There are three python scripts (`extract()`, `transform()`, `load()`) each designed to perform the 
pipeline task they are named after.

## Scheduling A Job
Using the `pipeline.sh` script, a job can be to run `load.py` which calls on `extract.py` and 
`transform.py` to ETL the data on a scheduled basis. 
