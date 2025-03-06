Answer the following:
>Does SNS guarantee exactly once delivery to subscribers?
>What is the purpose of the Dead-letter Queue (DLQ)? This is a feature available to SQS/SNS/EventBridge.
>How would you enable a notification to your email when messages are added to the DLQ?

Create a public github repository that has a README.md file, containing the above answers.
Submission is the url to your public github repository.
### Does SNS guarantee exactly once delivery to subscribers?

Amazon SNS (Simple Notification Service) `does not guarantee` exactly-once delivery to subscribers. Instead, it provides `at-least-once delivery`. This means that a message published to an SNS topic will be delivered to subscribers at least once, but there is a possibility of duplicate deliveries. Subscribers must be designed to handle potential duplicates idempotently.

### What is the purpose of the Dead-letter Queue (DLQ)?

A Dead-letter Queue (DLQ) is a feature available in AWS services like SQS (Simple Queue Service), SNS, and EventBridge. Its purpose is to capture and store messages or events that cannot be processed successfully after multiple attempts. This helps in:

1. `Isolating problematic messages`: Messages that fail processing are moved to the DLQ, preventing them from blocking the processing of other messages.
2. `Debugging and analysis`: Developers can analyze the messages in the DLQ to identify and fix issues in the processing logic.
3. `Retry mechanism`: After fixing the issue, messages can be replayed from the DLQ for reprocessing.

### How would you enable a notification to your email when messages are added to the DLQ?

To enable email notifications when messages are added to a DLQ, follow these steps:

1. `Create an SNS Topic`:
   - Go to the AWS SNS console.
   - Create a new topic (e.g., "DLQ-Alerts").
   - Subscribe your email address to this topic.

2. `Configure the DLQ to Trigger Notifications`:
   - For SQS:
     - Enable a `CloudWatch Alarm` on the `ApproximateNumberOfMessagesVisible` metric of the DLQ.
     - Set the alarm to trigger when the number of messages exceeds a threshold (e.g., > 0).
     - Configure the alarm to send a notification to the SNS topic (`DLQ-Alerts`) when the threshold is breached.
   - For SNS or EventBridge:
     - Use EventBridge to monitor the DLQ and create a rule that triggers when a message is sent to the DLQ.
     - Configure the rule to send a notification to the SNS topic (`DLQ-Alerts`).

3. `Test the Setup`:
   - Send a test message to the DLQ and verify that you receive an email notification.

By following these steps, you will receive email notifications whenever messages are added to the DLQ, allowing you to take timely action.