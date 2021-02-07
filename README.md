# www_resume_backend
- Website: https://resume.lhtran.com/
- API URL: https://api.lhtran.com/wwwresume/get_view_count

This project contains source code and supporting files for a serverless application of personal resume website to display view count. The serverless architecture utilizes AWS API Gateway, Lambda Function and DynamoDB for the backend. The project is deployed with the SAM template and Github Actions. It includes the following files and folders.

- app - Code for the application's Lambda function.
- tests - Unit tests and integration test for the application code. 
- template.yaml - SAM template to deploy AWS API Gateway, Lambda Function, and DynamoDB
- .github/workflows/workflow.yml - Github workflow for CI/CD

Architecture:
![Architecture Diagram](https://i.imgur.com/uXJ6Qrx.jpg)

Visit https://github.com/longhtran91/www_resume_frontend for the Front End
