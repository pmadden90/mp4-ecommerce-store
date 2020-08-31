# Shannon Gaels 

The Shannon Gaels Django app 
 
## UX
 
Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

"**_As a user, I would like to_** _______________"

Y - *successfully implemented*

N - *not yet implemented*

- View the site from **any device** *(mobile, tablet, desktop)*. Y
- View all products for sale in the shop as a **Guest**. Y
- Create* my own **profile** to see news and fixtures relating to the club. Y
- Save details such as address and card number to my **profile** to make checkout more convenient. Y
- Shop securely with a widely recognised card payment facilitator. Y
- Search for products for sale in shop via a search bar. Y
- Sort items for sale by price, rating, name or category. Y
- Access the Google Maps locations from the website. N
- See images on the news posts. N 
- As an admin, add items to the shop easily. Y 
- As an admin, add fixtures or news to the website easily. Y



## Features
 
### Existing Features
- REGISTRATION - allows users create profiles, by having them fill out a registration form
-- By registering, logged-in users can access news and fixtures relating to the club
- LOGIN - allows previously registered users to log back in
- SHOP - allows users to view and purchase club gear securely through Stripe
- CLUBNEWS - a news section for match reports and club related news
- GEARBAG - the shopping bag application - allows users to add multiple items to the bag before purchasing
- CHECKOUT - Application that facilitates payment for orders through Stripe



### Features Left to Implement
- Images on fixtures and news posts - currently not loading and due to time constraints, not implemented yet. 
The website is going to be used by the local GAA club so thisfeature will be added shortly. 
- Google Maps location data for club facilities to be added and a hyperlink to Google Maps app. 
- Link the existing fundraising activities to the Django app. Particularly the 404020.ie draw but also future endeavours
- Adding and editing products through the browser. Currently this is done through the Django admin - time constraints prevented
this being implemented

## Technologies Used


- [Gitpod](https://gitpod.io) - Used as the IDE for developing projects
- [Github] (https://github.com) - Used for remote storage of projects
- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
- [Bootstrap]  (https://getbootstrap.com/)
    - The project uses **Bootstrap** for styling and layout.
- [Django](https://www.djangoproject.com/)
    
- [MongoDB] https://www.mongodb.com/)
    - The project uses **MongoDB** for creating, reading, updating and deleting data from a database.
- [Heroku]  (https://Heroku.com/)
    - The project uses **Heroku** for deploying and hosting the app.
- [Python] (https://python.org)
- [AWS] (https://aws.amazon.com/s3/)
    - **AWS S3 Buckets** used for storing of media and static files




## Deployment

Project has been deployed via Heroku and is accessible here - https://ci-mp4-shannongaels.herokuapp.com/
 The process for deployment was as follows: Project pushed to GitHub repository Navigated to Settings in relevant GitHub repository Under GitHub Pages, selected relevant branch (master branch) and saved

Local Deployment
Go to directory you would like to clone this project to. Download or clone this link https://github.com/pmadden90/mp4-ecommerce-store and open in your chosen directory.

git clone https://github.com/pmadden90/mp4-ecommerce-store.git

This site is currently deployed on [Heroku](https://www.heroku.com/) using the **master** branch on GitHub. When the project has been setup locally, you can proceed to deploy it remotely with the following steps:

- Create a **requirements.txt** file so Heroku can install the required dependencies to run the app:
    - pip3 freeze --local > requirements.txt`
    - The *requirements.txt* file for this project can be found here: [requirements.txt](project/requirements.txt)
- Create a **Procfile** to tell Heroku what type of application is being deployed using *gunicorn*, and how to run it:
    - web: gunicorn main.wsgi:application > Procfile`
    - The *Procfile* for this project can be found here: [Procfile](project/Procfile)
- Sign up for a free Heroku account, create your project app, and click the **Deploy** tab, at which point you can *Connect GitHub* as the Deployment Method, and select *Enable Automatic Deployment*.
- In the Heroku **Resources** tab, navigate to the *Add-Ons* section and search for **Heroku Postgres**. Make sure to select the free *Hobby* level. This will allow you to have a remote database instead of using the local sqlite3 database, and can be found in the Settings tab. You'll need to update your *.env* file with your new *database-url* details.
- In the Heroku **Settings** tab, click on the *Reveal Config Vars* button to configure environmental variables. You will need to copy/paste all of the *.env* key value pairs into the config variables, but please omit the *development=1* variable; this is only for local deployment.
- Your app should be successfully deployed to Heroku at this point, but you're not quite finished yet!
- Update the *settings.py* file to connect the remote database using this Python package: `dj_database_url`
- Re-build the migrations and create a superuser to your new remote database using the instructions in the *local deployment* section above.
- Sign up for a free [Amazon AWS](https://aws.amazon.com/) account in order to host your *staticfiles* and *media* files. From the **S3 buckets** section, you'll need to create a new unique bucket. Follow these next steps to complete the setup:

**Permissions** > **CORS configuration**:

```
<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
<CORSRule>
    <AllowedOrigin>*</AllowedOrigin>
    <AllowedMethod>GET</AllowedMethod>
    <AllowedMethod>HEAD</AllowedMethod>
    <MaxAgeSeconds>3000</MaxAgeSeconds>
    <AllowedHeader>Authorization</AllowedHeader>
</CORSRule>
</CORSConfiguration>
```

**Permissions** > **Bucket Policy**:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::<x>/*"
        }
    ]
}
```

*! IMPORTANT ! - on the **Resource** line above, be sure to replace `<x>` with your **AWS bucket arn** details, but retain the `/*` at the end.* It should look similar to this:
    - `"Resource": "arn:aws:s3:::my-bucket-name/*"`

- From here, you'll need to navigate to the **IAM** section of AWS.
    - Create a *New Group* and be sure to select your existing S3 Bucket details to attach.
    - Create a *New Policy* and a *New User* in the IAM section as well, then attach these to the Group you just built.
- In your CLI-terminal, you should now be able to push the static files to AWS if everything is configured properly using this command:
    - `python manage.py collectstatic`
- Sign up for a free [Stripe](https://stripe.com) account. Navigate to the **Developers** section, and click on **API Keys**. You should have two confidential keys which need to be added to your *.env* file, as well as your Heroku config vars. These keys are:
    - `Publishable Key`: **pk_test_key**
    - `Secret Key`: **sk_test_key**


## Credits
Base template based on Bootstrap template - ('https://getbootstrap.com/docs/4.5/getting-started/introduction/')
News & fixtures app - based on Codemy - Create A Simple Blog Youtube Playlist

TravelTim - credited as I have used some of his readme file (from here - https://raw.githubusercontent.com/TravelTimN/ci-milestone05-fsfw/master/README.md) to help write the deployment section of this readme.

### Content
- The text for the about page was copied from the old Shannon Gaels website - https://shannongaelsgaa.com/club-history/

### Media
- The photos used in this site were obtained from oneills.ie
- Canva was used for some of the designs featured on the page

### Acknowledgements

- I received inspiration for this project from the existing Shannon Gaels page while the blue camoflauge overlay was inspired by 
the Brushed Nevis range of O'Neills clubwear - https://www.oneills.com/shannon-gaels-roscommon-nevis-brushed-crew-neck-meltmrn-bot-amb.html