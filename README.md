# auto-cht-backup
Automatic CHT (Cultuurhistorische Thesaurus) backup from the Poolparty server. Backup is executed daily at 5 am. An updated TriG is only pushed if there are changes to the current CHT file. 

If you want to set up a similar workflow, copy the yaml file in the workflow folder and change the project number to your Poolparty project number. Be sure to also set the Poolparty api user login and password credentials in your repo secrets, under settings.
