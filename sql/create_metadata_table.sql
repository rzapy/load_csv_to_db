CREATE TABLE metadata.etl_metadata (
    run_id SERIAL PRIMARY KEY,
    job_name VARCHAR(100) NOT NULL,
    source_file VARCHAR(255),
    rows_extracted INTEGER,
    rows_validated INTEGER,
    rows_loaded_staging INTEGER,
    rows_loaded_final INTEGER,
    status VARCHAR(20) CHECK (status IN ('RUNNING', 'SUCCESS', 'FAILED', 'PARTIAL')),
    started_at TIMESTAMP NOT NULL,
    completed_at TIMESTAMP,
    duration_seconds NUMERIC(10,2),
    error_message TEXT,
    run_by VARCHAR(50),
    pipeline_version VARCHAR(20)
);