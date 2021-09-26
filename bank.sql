create database bank_db;

use bank_db;

CREATE TABLE bank (
    code VARCHAR(10) NOT NULL,
    name VARCHAR(20) NOT NULL,
    address TINYTEXT NOT NULL,
    PRIMARY KEY (code)
);

CREATE TABLE bank_branch (
    branch_no VARCHAR(10) NOT NULL,
    address TINYTEXT NOT NULL,
    bank_code VARCHAR(10),
    PRIMARY KEY (branch_no),
    FOREIGN KEY (bank_code)
        REFERENCES bank (code)
        ON DELETE CASCADE
);

CREATE TABLE loan (
    loan_no VARCHAR(10) NOT NULL,
    amount BIGINT UNSIGNED NOT NULL,
    type VARCHAR(30) NOT NULL,
    branch_no VARCHAR(10),
    PRIMARY KEY (loan_no),
    FOREIGN KEY (branch_no)
        REFERENCES bank_branch (branch_no)
        ON DELETE CASCADE
);

CREATE TABLE account (
    account_no VARCHAR(10) NOT NULL,
    balance BIGINT UNSIGNED NOT NULL,
    type VARCHAR(30) NOT NULL,
    branch_no VARCHAR(10),
    PRIMARY KEY (account_no),
    FOREIGN KEY (branch_no)
        REFERENCES bank_branch (branch_no)
        ON DELETE CASCADE
);


CREATE TABLE customer (
    ssn VARCHAR(10) NOT NULL,
    name VARCHAR(30) NOT NULL,
    address TINYTEXT NOT NULL,
    phone CHAR(10) NOT NULL,
    PRIMARY KEY (ssn)
);

CREATE TABLE ac (
    account_no VARCHAR(10),
    ssn VARCHAR(10),
    FOREIGN KEY (account_no)
        REFERENCES account (account_no)
        ON DELETE CASCADE,
    FOREIGN KEY (ssn)
        REFERENCES customer (ssn)
        ON DELETE CASCADE,
    PRIMARY KEY (account_no , ssn)
);

CREATE TABLE lc (
    loan_no VARCHAR(10),
    ssn VARCHAR(10),
    FOREIGN KEY (loan_no)
        REFERENCES loan (loan_no)
        ON DELETE CASCADE,
    FOREIGN KEY (ssn)
        REFERENCES customer (ssn)
        ON DELETE CASCADE,
    PRIMARY KEY (loan_no , ssn)
);

CREATE TABLE users (
    username VARCHAR(10),
    password VARCHAR(20),
    PRIMARY KEY (username)
);;
