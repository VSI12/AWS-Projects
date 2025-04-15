import boto3


#Open Management Console

iam_console = boto3.client("iam")
# List IAM users
response = iam_console.list_users()
for user in response['Users']:
    print(user['UserName'])
