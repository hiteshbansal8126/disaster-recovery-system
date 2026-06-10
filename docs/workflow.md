# Workflow

1. Primary Web Server runs in Mumbai region.
2. EventBridge continuously monitors EC2 state changes.
3. If the primary server stops, EventBridge triggers Lambda.
4. Lambda launches a recovery server from a backup AMI.
5. SNS sends an email notification to the administrator.
6. Services are restored automatically.

Backup Strategy:
Mumbai AMI → Singapore AMI