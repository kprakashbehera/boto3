import boto3

aws_mgmt_console = boto3.session.Session(profile_name="kpb.devops")
s3_console = aws_mgmt_console.resource("s3")

for each_bucket in s3_console.buckets.all():
    print(each_bucket)