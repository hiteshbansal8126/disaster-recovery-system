# Recovery Time Objective (RTO) Report

## Project Name

Automated Disaster Recovery System on AWS

---

## Objective

To automatically recover services when the primary server becomes unavailable by using AWS EventBridge, Lambda, and EC2.

---

## Failure Scenario

The primary EC2 instance hosting the web application was manually stopped to simulate a disaster.

---

## Recovery Workflow

Primary Server
↓
EC2 State Change Event
↓
EventBridge Rule
↓
AWS Lambda
↓
Recovery Server Launch
↓
SNS Email Notification

---

## Test Results

| Parameter            | Observation                |
| -------------------- | -------------------------- |
| Failure Event        | Primary server stopped     |
| Detection Method     | EC2 State Change Event     |
| Automation Service   | EventBridge                |
| Recovery Service     | AWS Lambda                 |
| Backup Method        | Amazon Machine Image (AMI) |
| Notification Service | Amazon SNS                 |
| Recovery Server      | Successfully launched      |

---

## Recovery Time Objective (RTO)

Detection Time:
30-60 seconds

Recovery Instance Launch Time:
1-2 minutes

Approximate RTO:
2 minutes

---

## Backup Strategy

Primary Region:
Mumbai (ap-south-1)

Backup Region:
Singapore (ap-southeast-1)

Cross-region AMI replication was used to improve disaster recovery capability.

---

## Conclusion

The project successfully demonstrated automated disaster recovery on AWS. EventBridge detected the failure event, Lambda launched a recovery server automatically, and SNS sent notification emails to administrators. The overall recovery time was approximately two minutes.