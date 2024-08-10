import boto3
# import json

aws_session = boto3.session.Session(profile_name="kpb.devops")
ec2_rsrc = aws_session.resource("ec2")

running_instances = ec2_rsrc.instances.filter(Filters=[{"Name": "instance-state-name", "Values": ["running"]}])
# ec2_instance = ec2_console.describe_instances()

for instance in running_instances:
    print('running instance id ' + instance.id + ' is of type ' + instance.instance_type)
    print("Stopping instance...")
    instance.stop()
    print("Stopped instance...")
