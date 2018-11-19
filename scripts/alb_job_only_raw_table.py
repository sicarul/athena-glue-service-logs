from athena_glue_service_logs.job import JobRunner

job_run = JobRunner(service_name='alb')
job_run.raw_create_tables_if_needed()
job_run.add_new_raw_partitions()
job_run.finish()
