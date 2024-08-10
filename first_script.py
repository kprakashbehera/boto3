import boto3

aws_mgmt_console = boto3.session.Session(profile_name="kpb.devops")
iam_console = aws_mgmt_console.resource("iam")

# print all the users in your aws account
for each_user in iam_console.users.all():
    print("User Name: ", each_user.name)

