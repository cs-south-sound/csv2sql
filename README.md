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

Once MySQL Server is setup, a database needs to be created. This can be done from the terminal by 
executing the following steps.

Access MySQL (replace 'root' with your username)
``` Bash
sudo mysql -u root -p
```
Enter your password

Create database for fund holdings
``` SQL
CREATE DATABASE fund_holdings;
```
