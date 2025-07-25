# WCD_project  Capstone WCD project by K. Thompson 

## How it works 
This Capstone project is based on a typical retail sales data ingestion task. Raw data is being ingested from two different sources, Amazon S3 using a Lambda function and Amazon RDS that we connected to using Airbyte. This batch process data pipeline utilizes modern cloud tools that ingests the data into SnowFlake and DBT, which is a separate staging area that scrubs and transforms the data getting it ready for analytics in Metabase.  

## Phase 1 Installation in several steps 

--set the needed .pem key files for each AWS EC2 instance, the .pem files were saved on the desktop in a ".ssh" folder.  Each instance has specific size requirements. 

--installed using VS CODE, Docker and Docker compose 
-- then used GIT CLONE "https://github.com/airbytehq/airbyte.git"
--started airbyte using  ./run-ab-platform.sh
-- then set up the connection, source and destination using the Airbyte interface

--next was setting up an S3 bucket and using the serveless option to connect to it via a lambda file
--setting the name of bucket (needs to be unique for your region):
	wcd_function_bucket_v1

--lambda file was too large for AWS S3 interface therefore a docker container was deployed containing the lambda file and all its dependencies
--no .toml file was needed because those dependencies were in the main lambda file
-- the .env file contained the secret info for connecting to SnowFlake
--use the AWS UI to set up the event trigger 
-- use Airbyte UI to set up cron job time to 2 am UTC

--CoPilot was utilized to review the code to debug any errors

--doing these steps several times required updating/modifying the config.ssh file with the new host names for each instance

## Phase 2 Data Injestion 

--.yaml file is needed to get dbt UI up and running
	dbt_project.yml
 
--staged tables in dbt came from the tables in raw sources 

-- dbt was opened in local host:
	http://localhost:8080/#!/overview/tpcds 
 
--write SQL code as per business requirements for transforming the staged tables

--create documented files using:
	dbt docs generate  

--to view docs created use:
	dbt docs serve

--lineage graph created in dbt was branched off into multiple lines 

## Phase 3 Metabase results

--sum and aggregation of staged tables to produce charts and graphics for visualization.
--used UI in metabase to generate final analytics report
--needed to go back into EC2 instance for Metabase to make the instance bigger as it would time out too often

## Contributing
- Guidelines for contribution: Coding standards, documentation rules, etc.
- Instructions for how to submit code: here 
- Issue reporting: How to report bugs, suggest features, or ask questions.
- Code of conduct: Expectations for respectful and inclusive behavior (often linked as a separate doc).
- Tooling setup: Details on installing dependencies or running tests locally.
- Acknowledgments or thanks: Some projects shout out frequent contributors Humza and Anna's code were the templates worked on and used in this project.


## License  there is no license for this project
