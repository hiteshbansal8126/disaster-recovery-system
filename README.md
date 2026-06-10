# ☁️ Automated Disaster Recovery System on AWS

An event-driven disaster recovery solution built on AWS that automatically restores services when the primary server fails, reducing downtime and improving availability.

---

## 📌 Overview

This project implements an automated Disaster Recovery (DR) system using AWS services. When the primary EC2 instance becomes unavailable, Amazon EventBridge detects the event and triggers an AWS Lambda function, which launches a recovery server from a backup Amazon Machine Image (AMI). Amazon SNS sends email notifications to administrators after recovery.

The project also supports cross-region backup by maintaining AMI replicas in the Singapore region to enhance resilience against regional failures.

---

## 🚀 Features

* Automated recovery using AWS Lambda
* Event-driven failover with Amazon EventBridge
* AMI-based backup and restoration
* Cross-region backup support
* Email notifications with Amazon SNS
* Reduced Recovery Time Objective (RTO)
* High availability and fault tolerance
* Fully automated recovery workflow

---

## 🏗 Architecture

```text
Users
   │
   ▼
Primary Web Server (EC2 - Mumbai)
   │
   ▼
EC2 State Change Event
   │
   ▼
Amazon EventBridge
   │
   ▼
AWS Lambda (AutoRecoveryFunction)
   │
   ├──────────────► Amazon SNS
   │                    │
   │                    ▼
   │             Email Notification
   │
   ▼
Recovery Server (EC2)

Cross-Region Backup:
Mumbai AMI ─────────► Singapore AMI
```

---

## 🛠 AWS Services Used

* Amazon EC2
* Amazon Machine Image (AMI)
* AWS Lambda
* Amazon EventBridge
* Amazon SNS
* AWS IAM
* AWS CLI

---

## ⚙ Workflow

1. Primary EC2 server hosts the application.
2. EventBridge monitors EC2 state changes.
3. If the primary server stops, EventBridge triggers Lambda.
4. Lambda launches a recovery server from the backup AMI.
5. Amazon SNS sends an email notification.
6. Services are restored automatically.

---

## 📂 Project Structure

```text
Disaster-Recovery-System
│
├── architecture/
├── docs/
├── lambda/
├── report/
├── screenshots/
├── .gitignore
└── README.md
```

---

## 📈 Recovery Time Objective (RTO)

| Stage                  | Approximate Time |
| ---------------------- | ---------------- |
| Failure Detection      | 30–60 seconds    |
| Recovery Server Launch | 1–2 minutes      |
| Total Recovery Time    | ~2 Minutes       |

---

## 🔄 Backup Strategy

**Primary Region**

* Mumbai (ap-south-1)

**Backup Region**

* Singapore (ap-southeast-1)

Cross-region AMI replication provides disaster recovery capability in case of regional failures.

---

## 🧪 Test Scenario

### Failure Simulation

The primary EC2 server was manually stopped.

### Recovery Process

* EventBridge detected the state change.
* AWS Lambda executed automatically.
* Recovery server was launched successfully.
* Email notification was sent using Amazon SNS.

### Result

✅ Automated recovery completed successfully.

---

## 📁 Screenshots

* Primary Server
* Singapore AMI Backup
* Lambda Function
* EventBridge Rule
* Recovery Server
* Recovery Email Notification

---

## 🔮 Future Enhancements

* Multi-region automatic failover
* Intelligent region selection
* CloudWatch health monitoring
* Auto Scaling integration
* Load Balancer integration
* Infrastructure as Code using Terraform

---

## ⭐ Technologies

**Python • AWS • EC2 • Lambda • EventBridge • SNS • Ubuntu • Linux • AWS CLI**
