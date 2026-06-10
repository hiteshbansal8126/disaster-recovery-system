# Architecture

Users
↓
Primary Web Server (EC2)
↓
EC2 State Change Event
↓
EventBridge Rule
↓
AWS Lambda
↓
Recovery Server (EC2)
↓
SNS Email Notification

Cross-Region Backup:
Mumbai AMI → Singapore AMI