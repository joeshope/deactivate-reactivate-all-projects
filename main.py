import argparse
import sys, getopt, os
import snyk
from yaspin import yaspin

parser = argparse.ArgumentParser(description='orgs: input the org(s) for which you would like to reactivate projects to generate webhooks.')
parser.add_argument("--orgs")
args = parser.parse_args()
inputOrgs = args.orgs.split()

# Collect Snyk token if not in environment
if "SNYK_TOKEN" in os.environ:
    snyk_token = os.environ['SNYK_TOKEN']
else:
    print("Enter your Snyk API Token") 
    snyk_token = input()

# Set Snyk token, verify API token and get orgs
userOrgs = []
client = snyk.SnykClient(f'{snyk_token}')
try:
    userOrgs = client.organizations.all()
except snyk.errors.SnykHTTPError as err:
    print("💥 Ran into an error while fetching account details, please check your API token")
    print( helpString)

# Collect Orgs if not provided during script call
if inputOrgs == '':
    print("Input the org(s) for which you would like to reactivate projects to generate webhooks.")
    inputOrgs = input().split()

# Run through Orgs and deactivate projects
for currOrg in userOrgs:
    if currOrg.slug in inputOrgs:
        #remove currorg for org proccesing list and print proccesing message
        inputOrgs.remove(currOrg.slug)
        print("Processing" + """ \033[1;32m"{}" """.format(currOrg.name) + "\u001b[0morganization")

        #cycle through all projects in current org and deactivate
        for currProject in currOrg.projects.all():
            currProjectDetails = f"Origin: {currProject.origin}, Type: {currProject.type}"
            action =  "Deactivating"
            spinner = yaspin(text=f"{action}\033[1;33m {currProject.name}", color="yellow")
            spinner.write(f"\u001b[0m    Processing project: \u001b[34m{currProjectDetails}\u001b[0m, Status Below👇")
            spinner.start()
            try:
                currProject.deactivate()
                spinner.ok("🆗 ")
            except exception as e:
                spinner.fail("💥 ")

        #cycle through all projects in current org and activate     
        for currProject in currOrg.projects.all():
            currProjectDetails = f"Origin: {currProject.origin}, Type: {currProject.type}"
            action =  "Activating"
            spinner = yaspin(text=f"{action}\033[1;32m {currProject.name}", color="yellow")
            spinner.write(f"\u001b[0m    Processing project: \u001b[34m{currProjectDetails}\u001b[0m, Status Below👇")
            spinner.start()
            try:
                currProject.activate()
                spinner.ok("🆗 ")
            except exception as e:
                spinner.fail("💥 ")

#process input orgs which didnt have a match
if len(inputOrgs) != 0:
    print("\033[1;32m{}\u001b[0m are organizations which do not exist or you don't have access to them, please check your spelling, insure that spaces are replaced with dashes, and that you are using org slugs rather then display names".format(inputOrgs))