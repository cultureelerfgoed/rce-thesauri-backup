# Automatic scheduled backup of the Cultural Heritage Thesaurus

Repo to store and set the workflow for the automatic CHT (Cultuurhistorische Thesaurus) backup from the Poolparty server. Backup is executed daily at 5 am. An updated TriG is only pushed if there are changes to the current CHT file. 

If you want to set up a similar workflow, copy [cht-backup-poolparty.yml](.github/workflows/cht-backup-poolparty.yml) and change the [project name](https://github.com/cultureelerfgoed/auto-cht-backup/blob/bc7617cd855041cc21cf758ceef087c750b2c556/.github/workflows/cht-backup-poolparty.yml#L5) to your Poolparty project number. You will also need an API account from Poolparty, and store that in the repo:

**Secret variables**

This action requires two secrets to be added to the repository:

`POOLPARTY_USERNAME`

`POOLPARTY_PASSWORD`

These are credentials of a PoolParty API user and can be added via the repository's `Settings --> Secrets and Variables --> Actions --> Repository secrets section`.
