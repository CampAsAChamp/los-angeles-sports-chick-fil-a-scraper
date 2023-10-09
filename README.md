<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="imgs/Chick Fil A Logo.svg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Los Angeles Chick Fil A Scrapper</h3>

  <p align="center">
    Checks all of the Los Angeles sports teams scores each morning to see if any of them qualify for free Chick Fil A sandwiches and sends me an email as a reminder to check my app to claim the coupon
    <br />
    <br />
    <a href="https://github.com/CampAsAChamp/los-angeles-chick-fil-a-scraper">View Demo</a>
    ·
    <a href="https://github.com/CampAsAChamp/los-angeles-chick-fil-a-scraper/issues">Report Bug</a>
    ·
    <a href="https://github.com/CampAsAChamp/los-angeles-chick-fil-a-scraper/issues">Request Feature</a>
  </p>
</div>





<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]]()

The Los Angeles sports teams have agreements with Chick Fil A for free sandwiches if one of the following criteria is met
- Angels score 7 or more runs at home
- Ducks score 5 or more goals at home
- LAFC wins at home

This repo/service checks all of these criteria each day at 8 AM PT (3 PM UTC) using Python and Github Actions (for the automatic cron job) and sends me an email as a reminder to check my Chick Fil A app so I can claim my free Chick Fil A sandwich

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python 3](https://python.org)
* [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/)
* [GitHub Actions](https://github.com/features/actions)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* **Python 3**

### Running Locally

1. Clone the repo
    ```sh
    git clone https://github.com/CampAsAChamp/los-angeles-chick-fil-a-scraper.git
    ```
2. Create virtual environment
    ```sh
    python -m venv .venv 
    ```
3. Activate virtual environment
    ```sh
    source ./venv/Scripts/Activate
    ```
4. Download dependencies
    ```sh
    pip install -r requirements.txt
    ```
5. Create .env file for secrets
    ```sh
    mkdir env
    touch env/app.env
    nano env/app.env
    ```

    Paste in the following content
    ```
    FROM_EMAIL"<from_email_here>"
    TO_EMAIL="<to_emails_here>"
    PASSWORD="<gmail_app_password_here>"
    SHOULD_SEND_EMAIL=True
    USE_LOCAL=False
    ```
    1. The `USE_LOCAL` environment variable is if you want to use the local HTML pages inside the repo (in the `/sample_pages/` directory), instead of fetching the actual live page.
6. Run in VS Code by going to the "Run and Debug" tab on the side bar and clicking the green plus ▶️

# Set up to run automatically for yourself
If you want to set up for yourself to get email alerts here are the steps you need to follow:

**NOTE**: I've only tested this on Gmail accounts

1. Fork this repo
2. Set up an app password in your Google Account
    1. Follow this article to set one up https://support.google.com/accounts/answer/185833?hl=en
    2. Copy the app password somewhere safe as you'll be needing to put it in the Github Actions secrets
3. In your newly forked repo add Github Actions secrets for the needed environment variables: `FROM_EMAIL`, `TO_EMAIL`, `PASSWORD`, `SHOULD_SEND_EMAIL`, and `USE_LOCAL`
    1. Go to repo settings > Security > Secrets and Variables > Actions
    2. Click `New Repository Secret`
    3. Add a separate one for each of the three keys listed above and paste the actual value that belong
    4. For name use the key list above (`FROM_EMAIL`, `TO_EMAIL`, `PASSWORD`)
        1. `TO_EMAIL` is a comma separated list of emails, so you can send email alerts to multiple people, or just keep it to one. 
           
                TO_EMAIL = "person1@gmail.com"
                OR
                TO_EMAIL = "person1@gmail.com, person2@gmail.com"
       
           
    5. For the value use the actual value of your email addresses or app password
4. For `SHOULD_SEND_EMAIL` use the value -- **True**
5. For `USE_LOCAL` use the value -- **False**
6. It will now run every day, you can check the runs in the `Actions` tab in Github
    1. If the criteria is met you will receive an email for each one met so you know to check your Chick Fil A app to claim your free sandwich coupon


<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>


## TODO
- Change logic to use numerical for loop to be able to get previous game easier (current_index - 1)

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[product-screenshot]: imgs/Banner.png
