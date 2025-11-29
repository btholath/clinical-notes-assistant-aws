

SaaS Gen AI and Agentic AI in production

Services used by the app
- Docker
- AWS IAM
- AWS CloudWatch
- AWS ECR
- AWS AppRunner

=============================================================
Setup AWS user account
=============================================================
Step 4: Create an IAM User for Daily Work
Never use your root account for daily work. Let's create a limited user:

Search for IAM in the AWS Console
Click Users → Create user
Username: aiengineer
Check ✅ Provide user access to the AWS Management Console
Select I want to create an IAM user
Choose Custom password and set a strong password
Uncheck ⬜ Users must create a new password at next sign-in
Click Next
Step 5: Create a User Group with Permissions
We'll create a reusable permission group first, then add our user to it:

On the permissions page, select Add user to group
Click Create group
Group name: BroadAIEngineerAccess
In the permissions policies search, find and check these policies:
AWSAppRunnerFullAccess - to deploy applications
AmazonEC2ContainerRegistryFullAccess - to store Docker images
CloudWatchLogsFullAccess - to view logs
IAMUserChangePassword - to manage own credentials
IMPORTANT: also IAMFullAccess - I don't think I mention this in the video, but it must be included or you will get errors later! Thank you Anthony W and Jake C for pointing this out.
Click Create user group
Back on the permissions page, select the BroadAIEngineerAccess group (it should be checked)
Click Next → Create user
Important: Click Download .csv file and save it securely!
It's worth keeping in mind that you might get permissions errors thoughout the course, when AWS complains that your user doesn't have permission to do something. The solution is usually to come back to this screen (as the root user) and attach another policy! This is a very common chore working with AWS...

Step 6: Sign In as IAM User
Sign out from root account
Go to your AWS sign-in URL (in the CSV file, looks like: https://123456789012.signin.aws.amazon.com/console)
Sign in with:
Username: aiengineer
Password: (the one you created)
✅ Checkpoint: You should see "aiengineer @ Account-ID" in the top right corner




bijut@b:~/aws_apps/saas$ git remote set-url origin git@github.com:btholath/clinical-notes-assistant-aws.git

bijut@b:~/aws_apps/saas$ git push -u origin main --force
Enumerating objects: 59, done.
Counting objects: 100% (59/59), done.
Delta compression using up to 14 threads
Compressing objects: 100% (52/52), done.
Writing objects: 100% (59/59), 93.37 KiB | 1.17 MiB/s, done.
Total 59 (delta 15), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (15/15), done.
To github.com:btholath/clinical-notes-assistant.git
 + c9f1357...7b087ac main -> main (forced update)
branch 'main' set up to track 'origin/main'.

-- Deploy to Vercel
bijut@b:~/aws_apps/saas$ vercel .
Vercel CLI 48.12.0
🔍  Inspect: https://vercel.com/bijus-projects-71507ffb/saas/BpkpHMRCohX2W5272sAgu6ZwXzVb [2s]
✅  Preview: https://saas-omy9397q4-bijus-projects-71507ffb.vercel.app [46s]
📝  To deploy to production (saas-lilac-alpha.vercel.app), run `vercel --prod`
bijut@b:~/aws_apps/saas$


-- Unit Testing (Manual testing)
In Consultation Notes
Patient Name: Biju Tholath
Date of Visit: 2025-11-28
Consultation Notes: Biju complains of a headache. I told him to take 2 Tylenol and come back in 2 days if it hasn't gone away.