# Testing

Test Scenario:
Primary server stopped manually.

Expected Behavior:

* EventBridge detects state change.
* Lambda function executes.
* Recovery server launches automatically.
* SNS email notification is sent.

Recovery Time Objective (RTO):
Approximately 1-2 minutes.