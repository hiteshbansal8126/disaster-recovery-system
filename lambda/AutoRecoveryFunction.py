import boto3

def lambda_handler(event, context):
    # SNS Client
    sns = boto3.client("sns")

    # Select recovery region
    recover_region = "mumbai"

    if recover_region == "mumbai":
        ec2 = boto3.client("ec2", region_name="PRIMARY_REGION")
        response = ec2.run_instances(
            ImageId="PRIMARY_AMI_ID",
            InstanceType="INSTANCE_TYPE",
            MinCount=1,
            MaxCount=1,
            KeyName="KEY_PAIR_NAME",
            SecurityGroupIds=["PRIMARY_SECURITY_GROUP_ID"],
            SubnetId="PRIMARY_SUBNET_ID",
            TagSpecifications=[
                {
                    "ResourceType": "instance",
                    "Tags": [{"Key": "Name", "Value": "Recovered-Server-Mumbai"}]
                }
            ]
        )
        launched_region = "PRIMARY_REGION"
    else:
        ec2 = boto3.client("ec2", region_name="BACKUP_REGION")
        response = ec2.run_instances(
            ImageId="BACKUP_AMI_ID",
            InstanceType="INSTANCE_TYPE",
            MinCount=1,
            MaxCount=1,
            KeyName="KEY_PAIR_NAME", # Add this if you need SSH in backup too
            SecurityGroupIds=["BACKUP_SECURITY_GROUP_ID"],
            SubnetId="BACKUP_SUBNET_ID",
            TagSpecifications=[
                {
                    "ResourceType": "instance",
                    "Tags": [{"Key": "Name", "Value": "Recovered-Server-Singapore"}]
                }
            ]
        )
        launched_region = "BACKUP_REGION"

    # Send Email Notification
    instance_id = response['Instances'][0]['InstanceId']
    sns.publish(
        TopicArn="SNS_TOPIC_ARN",
        Subject="Disaster Recovery Activated",
        Message=f"""
Primary server failure detected.

Recovery server launched successfully.

Instance ID: {instance_id}
Launched In: {launched_region}

Status: Recovery Completed
"""
    )

    return {
        "statusCode": 200,
        "body": f"Recovery Server {instance_id} launched successfully. Notification sent."
    }