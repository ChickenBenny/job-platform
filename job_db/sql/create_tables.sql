-- create table to init the database
-- we wil have 5 table such as backend engineer, data engineer, data scientist, machine learning engineer and QA engineer
-- Each table will have 8 columns
CREATE TABLE IF NOT EXISTS backend_engineer (
    url_link TEXT NOT NULL,
    company TEXT NOT NULL,
    skill TEXT[],
    job_type TEXT,
    loc TEXT,
    salary TEXT,
);

CREATE TABLE IF NOT EXISTS data_engineer (
    url_link TEXT NOT NULL,
    company TEXT NOT NULL,
    skill TEXT[],
    job_type TEXT,
    loc TEXT,
    salary TEXT,
);

CREATE TABLE IF NOT EXISTS data_scientist (
    url_link TEXT NOT NULL,
    company TEXT NOT NULL,
    skill TEXT[],
    job_type TEXT,
    loc TEXT,
    salary TEXT,
);

CREATE TABLE IF NOT EXISTS ml_engineer (
    url_link TEXT NOT NULL,
    company TEXT NOT NULL,
    skill TEXT[],
    job_type TEXT,
    loc TEXT,
    salary TEXT,
);

CREATE TABLE IF NOT EXISTS qa_engineer (
    url_link TEXT NOT NULL,
    company TEXT NOT NULL,
    skill TEXT[],
    job_type TEXT,
    loc TEXT,
    salary TEXT,
);