import boto3

aws_mgmt_console = boto3.session.Session(profile_name="kpb.devops")
iam_session = aws_mgmt_console.client('iam')

print("list of iam users in json format. It is a dictionary")
# print(iam_session.list_users)
# prints a dictionary
print(iam_session.list_users())
print("-------------")

print('list of user details')
# prints a list
print(iam_session.list_users()['Users'])

# print only the first user details
# print(iam_session.list_users()['Users'][1])

# print only the first user name
# print(iam_session.list_users()['Users'][1]['UserName'])

print("-----------")

print('list of iam user names only')
# print all the iam users
for user in iam_session.list_users()['Users']:
    print(user['UserName'])
