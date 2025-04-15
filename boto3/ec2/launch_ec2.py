import boto3

# Create an EC2 client
ec2_client = boto3.client('ec2')

Instance1 = ec2_client.run_instances(
    ImageId='ami-00a929b66ed6e0de6',
    InstanceType='t2.micro',
    KeyName='test',  
    MinCount=1,
    MaxCount=1,
)