import boto3

aws_mgmt_con = boto3.session.Session(profile_name='kpb.devops')
ec2_con_cli = aws_mgmt_con.client('ec2')

# list all ec2 instances ids.

response = ec2_con_cli.describe_instances()
# print(response['Reservations'][0]['Instances'][0]['InstanceId'])

# print(response['Reservations'])
for each_item in response['Reservations']:
    for each_instance in each_item['Instances']:
        print(each_instance['InstanceId'])
