#Import modules and libraries
import boto3
import boto3.session

aws_management_console = boto3.session.Session(profile_name='default')

ec2_client = aws_management_console.client('ec2')

# List all EC2 instances in the account 
describe_instances = ec2_client.describe_instances()

for each_instance in describe_instances['Reservations']:
    for instance in each_instance['Instances']:
       print(instance['InstanceId'])