bijut@b:~/aws_apps/saas$ git remote set-url origin git@github.com:btholath/clinical-notes-assistant.git

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