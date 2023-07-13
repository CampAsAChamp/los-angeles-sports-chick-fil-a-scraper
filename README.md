# Los Angeles Chick Fil A Scraper
The Los Angeles sports teams have agreements with Chick Fil A for free sandwiches if one of the following criteria is met
- Angeles score 7 or more runs at home
- Ducks score 5 or more goals at home
- LAFC wins at home

This repo/service checks all of these criteria each day at 8 AM PT (3 PM UTC) using Python and Github Actions (for the automatic cron job) and sends me an email as a reminder to check my Chick Fil A app so I can claim my free Chick Fil A sandwich

# Set up for yourself
If you want to set up for yourself to get email alerts here are the steps you need to follow:

**NOTE**: I've only tested this on Gmail accounts

1. Fork this repo
2. Set up an app password in your Google Account
    1. Follow this article to set one up https://support.google.com/accounts/answer/185833?hl=en
    2. Copy the app password somewhere safe as you'll be needing to put it in the Github Actions secrets
3. In your newly forked repo add Github Actions secrets for the needed environment variables: `FROM_EMAIL`, `TO_EMAIL`, `PASSWORD`
    1. Go to repo settings > Security > Secrets and Variables > Actions
    2. Click `New Repository Secret`
    3. Add a separate one for each of the three keys listed above and paste the actual value that belong
    4. For name use the key list above (`FROM_EMAIL`, `TO_EMAIL`, `PASSWORD`)
    5. For the value use the actual value of your email addresses or app password
4. It will now run every day, you can check the runs in the `Actions` tab in Github
    1. If the criteria is met you will receive an email for each one met so you know to check your Chick Fil A app to claim your free sandwich coupon

# TODO:
* Make functions more modular as the 3 score checking functions have a lot of duplicate code
* Use switch statements in the column checking instead of if statements for better readability
