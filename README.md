# Los Angeles Angels Chick Fil A Sandwich Scraper
Checks each day at 8 AM PST (3 PM UTC) using Github Actions if the Angels scored at least 7 runs while playing at home (Anaheim) the previous day and sends me an email as a reminder to check my Chick Fil A app so I can claim my free Chick Fil A sandwich

# Set up for yourself
If you want to set up for yourself to get email alerts here are the steps you need to follow:

**NOTE**: I've only tested this on Gmail accounts

1. Set up an app password in your Google Account
    1. Follow this article to set one up https://support.google.com/accounts/answer/185833?hl=en
    2. Copy the app password somewhere safe as you'll be needing to put it in the Github Actions secrets
3. Fork this repo
4. In your newly forked repo add Github Actions secrets for the needed environment variables: `FROM_EMAIL`, `TO_EMAIL`, `PASSWORD`
    1. Go to repo settings > Security > Secrets and Variables > Actions
    2. Click `New Repository Secret`
    3. Add a separate one for each of the three keys listed above and paste the actual value that belong
    4. For name use the key list above (`FROM_EMAIL`, `TO_EMAIL`, `PASSWORD`)
    5. For the value use the actual value of your email addresses or app password
5. It will now run every day from March - October at 8 AM PST, you can check the runs in the `Actions` tab in Github
    1. If the criteria for a free Chick Fil A sandwich is met you will receive an email
