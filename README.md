# Auto backups of key thesauri of the Dutch Cultural Heritage Agency

Repo to store and set the workflow for automatic backup of key RCE thesauri from the Poolparty server. Backup is executed daily. A new TriG of a thesaurus is only pushed if there are changes to the current repo file. 

## Current thesauri that are automatically backed up:
- [Cultural Heritage Thesaurus (CHT)](https://data.cultureelerfgoed.nl/term/id/cht.html)
- [Archeologisch Basis Register (ABR)](https://data.cultureelerfgoed.nl/term/id/abr.html) 
- [Referentie Netwerk RCE](https://data.cultureelerfgoed.nl/term/id/rn.html) 

## How to make backups of a Poolparty project yourself
If you want to set up a similar workflow, copy e.g. [cht-backup-poolparty.yml](.github/workflows/cht-backup-poolparty.yml), change the [project name](https://github.com/cultureelerfgoed/auto-cht-backup/blob/bc7617cd855041cc21cf758ceef087c750b2c556/.github/workflows/cht-backup-poolparty.yml#L5) to your Poolparty project number, and adapt the [file name](https://github.com/cultureelerfgoed/rce-thesauri-backup/blob/bc7617cd855041cc21cf758ceef087c750b2c556/.github/workflows/cht-backup-poolparty.yml#L6). The workflow expects that a TriG file with the specified filename already exists in your repo.

You will also need an API account from Poolparty, and store your credentials in the repo:

**Secret variables**

This action requires two secrets to be added to the repository:

`POOLPARTY_USERNAME`

`POOLPARTY_PASSWORD`

These are credentials of a PoolParty API user and can be added via the repository's `Settings --> Secrets and Variables --> Actions --> Repository secrets section`.
