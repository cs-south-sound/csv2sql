-- A Script for creating the table that the pipeline will load data into
CREATE TABLE holdings (
	ID INT NOT NULL AUTO_INCREMENT,
    date DATETIME,
    fund VARCHAR(255),
    company VARCHAR(255),
    ticker VARCHAR(255),
    cusip VARCHAR(255),
    shares BIGINT,
    total_value NUMERIC,
    portfolio_percentage NUMERIC,
    PRIMARY KEY (ID)
);