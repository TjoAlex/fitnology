# Milestone Project 4: Fitnology

This project is made for the store owner(admin), potential businesses wanting to sell products and customers of the store. It shall be used by users who want to know more about technology products related to fitness and users who want one single place that provides a focused selection of technology products related to fitness. This is designed for business and informative purposes for the owner who wants to increase customers and provide a bigger selection of products as well as provide the users a good understanding of how these products can help one improve their health by reading the blog members of the website have access to.

## Showcase 
![showcase-screenshot](media...)

[view the live project here.](#http)<br>

## Navigation

* [UX](#ux)
* [Features](#features)
* [Information Architecture](#information-architecture)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

## UX
### Goals 
#### Visitor Goals 
The central targeted audience for Fitnology are:
+ People who want to find simple ways to start exercising.
+ People who value a simple shopping experience.
+ People who want to find exercise products related to technology.
#### User Goals 
+ Find products to suit my needs.
+ Enjoy browsing technology products related to fitness.
+ Enjoy learning more about fitness and how technology can help with that.
+ Be able to navigate the shop easily, find what I need and make safe and secure purchases.
+ Buy from a trustworthy online shop. 
#### Website Goals
+ Display Fitnology information;
+ Allow Fitnology guests to create an account.
+ Display to guests & users Fitnology products and blog posts.
+ Allow Fitnology guests & users to place an order;
+ Allow Fitnology guests & users to pay an order;
+ Allow Fitnology guests & users to check their order history;
+ Allow Fitnology owners to easily add, edit and delete products and blog posts.
### User Stories 
* First Time Visitor Goals
    * As a first time visitor, I want to be able to understand the purpose of the application;
    * As a first time visitor, I want to be able to find information about the company;
    * As a first time visitor, I want to be able to see all products the company has to offer;
    * As a first time visitor, I want to be able to move through the menu pages;
    * As a first time visitor, I want to be able to add products to the virtual bag;
    * As a first time visitor, I want to be able to check the virtual bag;
    * As a first time visitor, I want to be able to place an order in Fitnology;
    * As a first time visitor, I want to be able to pay an order in Fitnology;
    * As a first time visitor, I want to be able to see a overview of my placed and payed order;
    * As a first time visitor, I want to be able to create a profile;
    * As a first time visitor, I want to be able to register;
    * As a first time visitor, I want to be able to login;
    * As a first time visitor, I want to be able to logout.
* Returning Visitor Goals
    * As a returning visitor, I want the same application experience as a first time visitor;
    * As a returning visitor, I want to check my order history at Fitnology;
    * As a returning visitor, I want to read blog posts.
* Frequent User Goals
    * As a frequent user of this application, I want the same experience as a first time visitor and returning visitor;
    * As the owner of Fitnology I want to easily create, update blog posts or products, and/or remove product items or blog posts from the products and/or blog. 
## Design 
### Font
+ Primary font 'Dosis' for the overall text of the website because of its clear readability, size and spacing of letters with a simple and minimal look well suited for the theme of the website helping maintain visual comfort.
### Icons
+ In order to keep an uncluttered site only a few icons were utilized when needed to keep things simple for the user. 
### Color Schema 
![](media/readme-images/.png)
   - The main colors used in this site are black(#111), white(#ffff), gray(#777), and teal(#0c343d).
   - Main text color is Black #111
   - Intro sections for home page have text color gray #777
   - Buttons, logo and navbar text carries this teal color #0c343d, for some contrast and theme color.
   - Image for the top of the home page and blog page have some orange in it to get some fun contrast whilst still maintaining the theme of the website.
### Styling
+ The overall style was to keep everything simple, clean and fresh letting things as the products or blog posts be the main part making the website get some color and visual appeal. 
## Wireframes
#### These wireframes were made using [Balsamiq](https://balsamiq.com/) during the Scope Plane part of the design and planning process for this project.
+ [Home](media/readme-images/.png)
+ [Products](media/readme-images/.png)
+ [Product Details](media/readme-images/.png)
+ [Blog](media/readme-images/.png)
+ [Blog Detail Post](media/readme-images/.png)
+ [Shopping Bag](media/readme-images/.png)
+ [Checkout](media/readme-images/.png)
+ [Checkout Success](media/readme-images/.png)
+ [profile](media/readme-images/.png)
## Database Shema
## Features
The website follows UX and UI design as well as CRUD to create the best experience for the user, below shows what was created to contribute to this.
### Existing Features

- __Navigation Bar__

  - Featured on all pages, consist with a fully responsive navigation bar that includes links to the home page both on the logo and Home button, link to all the products featuring the products categories within it’s dropdown menu, third button on the left standing for motivation and holding the link for the blog page. To the right side of the navigation bar the user finds the profile link with a dropdown menu to login, logout or sign up and/or if logged in as owner it contains product management and blog management. Lastly on the right there is the cart that will get all products added to it and send messages in case something goes with success or with an error.
  - The Navigation Bar continues to be identical on all pages to remain as easy navigation.
  - Giving the user easy navigation throughout the website, moving from page to page. It is responsive and functional as well as simple and aesthetically pleasing on all devices.   
 
![Nav Bar](media...)

- __Landing Page Image, Heading, Button and introduction section__
  - Once landing on the home page there is an image holding a heading and button to give the user a first glance at what this website is and give them the chance to directly jump to the all products page.
  - It continues to hold three sections one introducing the user to what is about to come, sendond is what the company is, third what the company offers and fourth how everything works.
  - Each introduction section is divided with an image holding a link to the blog page and the last image holding a link to the register page.

  ![Landing Page Image](media...)

 - __Navbar Cart__
  - On the Navbar a cart is provided, this cart once a product is added to it turns to the color blue, letting the user know when something is added to it. 
  - Once you press the add to cart button, a smaller screen pops up showing a success message, the image of the product you just added, quantity, size if any, the total price for everything in your cart and go to the secure checkout button.
  - If the user presses the cart they land on the cart page.
  - If the user presses the go to secure checkout page they land on the checkout page.

  ![Nav Bar Cart](media...)

- __Products Page__
  - The user, if clicked on all products page, will here find everything the website has to offer in a row of four and down.
  - On the top there is a header telling the user they are on the products page following with clickable category buttons leading the user to specific categories holding specific products. 
  - Under the category options a search bar is available, giving the option to search a specific product to find what one is looking for more quickly. 
  - Each Product section holds the Name, price, category, size (if any), and ratings(if any).
  - If the user is one of the logged in owners they get underneath the category name of the product an edit or delete button leading to the edit product page, or giving the user "product deleted" message if they choose to delete it. 

  ![Products Page](media...)

- __Single Product Page__
  - If the user chooses to click on a product they come to the single products page. This page shows a bigger image of the product itself, holding the product name, price, category, description, size and ratings(if any).
  - Underneath the description there is a quantity option that the user adds more quantity by pressing the plus button or less by pressing the minus button. The minus button only lets the user go to one then one cant press less more. 
  - Lastly Two buttons are provided, one leading back to the products page and second putting the product in the cart leaving the user with a successfully added product message from the bag. 

  [Single Products Page](media...)

- __Add Products Page__ 
  - If the owner of the stor press the profile icon and then product management they land on a page holding a form.
  - The owner can here add everything necessary for each product and later press the button on the bottom to add the product.
  - If everything went correct the user gets a message from the bag successfully added product and lands on the products page again. Otherwise the user gets an error message telling the user to look at the form so everything is filled in correctly.
  - If the user pressed the edit button they landed on the same page, yet then everything is already filled in an the user need only to fix what was needed to fix.
  - This form looks mostly the same for the blog management and blog edit button. Only difference is the information required.

  [Add Products Page](media...)

- __Bag Page__
  - Here if clicked on the bag icon the user gets an overview of everything they added to their cart, each individual product showing the name, quantity, price, size if any, SKU and image. 
  - On the right bottom a cart total amount is shown for every product, the delivery cost and total cost for everything.
  - Underneath the quantity the user has two options to choose from,  update and or delete. If the user deletes a product a new message appears telling the product was successfully deleted from your bag. If you press the update button and you choose to add more quantity of that product you will get a new message telling your product was successfully updated and a new total price will be shown. 
  - Lastly two buttons are provided on the bottom right side of the page. One leading back to the all products page and one leading to the checkout page. 

  [Cart Page](media...)

- __Checkout Page__
  - On the Checkout page the user is provided with a form, A form required for the user to fill in to make sure they can purchase their products.
  - If the form is incorrect when the user presses the secure payment an error message from the bag will appear telling the user to look at the form and make sure it is correct.
  - This page also shows a last overview of the products the user chooses to purchase containing all the product details as well.

[Checkout Page](media...)

- __Profile Page__
  - In the profile page the user finds their full order history with all information attached regarding their purchase.

[Profile Page](media...)

- __Blog__
  - When the user goes to the blog they land on a page holding a new header with a small introduction telling them where they are.
  - Under this image all the blog posts are presented one by one. This with a heading, then image and lastly a short part from the blog text itself.
  - Under the line of text for the blog post a button is provided for the user if logged in to read more and if not logged in to register.

[Blog](media...)

- __Single Blog Post__ 
  - If the user is a logged in member and press the button read more they land on the single blog post page.
  - This page shows the image for the specific post, author and when it was made as well as the full text for the post.
  - If the user is an owner for the website it will also appear edit and delete buttons. These work exactly the same as for the products edit or delete buttons.
  - Lastly the user finds a button leading back to the all blog posts page.

[Single Blog Post](media...)

- __Sign In__
  - The user is not already signed in can click on the profile icon and find the sign in page.
  - This contains a form for the user to fill in holding the username and password.
  - Once all information is in the form the user can press the signin button and land on the homepage again.

  [Sign In](media...)

- __Sign Out__ 
 - Once logged in users can press the profile icon in the navigation and find the logout option. If that is pressed the user lands on a page confirming they have been logged out.

 [Sign Out](media...)

- __Register__ 
  - By choosing the register option either from the navigation bar, blog link or home page link the user lands on a page holding a form.
  - This form shows the user everything that is necessary to fill in to become a member of the website.

  [Register](media...)

### Future Features 

   - Create a like button for each product that the user can press and the product will be saved in a liked products page. 

   - Add a comment section on the blog so the user can interact more.

   - Add a review section for each product that the user could leave a review on. 

   - Add a save information form to the user profile to save shipping information and make the checkout more easy.

   - Add a for companies page, promoting business to reach out to the website to get their products sold on this platform. 

## Data Models 

##### Profiles
Inside the profiles app you find the userprofile model.

Name | Key in DB | Validation | Field Type
------------ | ------------- | ------------- | -------------
User | user | User, on_delete=models.CASCADE | OneToOneField
Default Phone Number | default_phone_number | max_length=20, null=True, blank=True | CharField
Default Street Address 1 | default_street_address1 | max_length=80, null=True, blank=True | CharField
Default Street Address 2 | default_street_address2 | max_length=80, null=True, blank=True | CharField
Default City | default_city | max_length=40, null=True, blank=True | CharField
Default County | default_county | max_length=80, null=True, blank=True | CharField
Default Postcode | default_postcode | max_length=20, null=True, blank=True | CharField
Default Country | default_country | blank_label='Country', null=True, blank=True | CountryField

##### Category
Inside the products app the Category model holds all the data needed for the categories.

Name | Key in DB | Validation | Field Type
------------ | ------------- | ------------- | -------------
Name | name | max_length=254 | CharField
Friendly Name | friendly_name | max_length=254, null=True, blank=True | CharField 

##### product 
In the products app is the model that holds all data for the products in fitnology.

Name | Key in DB | Validation | Field Type
------------ | ------------- | ------------- | -------------
Category | category | 'Category', null=True, blank=True, on_delete=models.SET_NULL | ForeignKey
SKU | sku | max_length=254, null=True, blank=True | CharField
Name | name | max_length=254 | CharField
Description | description |  | TextField
Sizes | has_sizes | default=False, null=True, blank=True | BooleanField
Price | price | max_digits=6, decimal_places=2 | DecimalField
Rating | rating | max_digits=6, decimal_places=2, null=True, blank=True | DecimalField
Image URL | image_url | max_length=1024, null=True, blank=True | URLField
Image | image | null=True, blank=True | ImageField

##### Blog Posts Model
Inside the blog app is the model holding all data for the blog posts.  

Name | Key in DB | Validation | Field Type
------------ | ------------- | ------------- | -------------
Title | title | max_length=200, unique=True | CharField
Slug | slug | max_length=200, unique=True | SlugField
Author | author | User, on_delete=models.CASCADE, related_name="blog_posts" | ForeignKey
Updated On | updated_on | auto_now=True | DateTimeField
Content | content |  | TextField
Created On | created_on | auto_now_add=True | DateTimeField
Created On | image_url | max_length=1024, null=True, blank=True | URLField
Image | image | null=True, blank=True | ImageField
Status | status | choices=STATUS, default=0 | IntegerField

##### Checkout app Models
In the checkout app there are the Order and Orderlineitem models holding data so that users can create and pay for their orders.

##### Order
Name | Key in DB | Validation | Field Type
------------ | ------------- | ------------- | -------------
Order Number | order_number | max_length=32, null=False, editable=False | CharField
User Profile | user_profile | UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders' | ForeignKey
Full Name | full_name | max_length=50, null=False, blank=False | CharField
Email | email | max_length=254, null=False, blank=False | EmailField
Phone Number | phone_number | max_length=20, null=False, blank=False | CharField
Country | country | blank_label='Country *', null=False, blank=False | CountryField
Postcode | postcode | max_length=20, null=True, blank=True | CharField
City | city | max_length=40, null=False, blank=False | CharField
Street Address 1 | street_address1 | max_length=80, null=False, blank=False | CharField
Street Address 2 | street_address2 | max_length=80, null=True, blank=True | CharField
County | county | max_length=80, null=True, blank=True | CharField
Date | date | auto_now_add=True | DateTimeField
Order Total | order_total | max_digits=10, decimal_places=2, null=False, default=0 | DecimalField
Original Cart | original_cart | null=False, blank=False, default='' | TextField
Stripe PID | stripe_pid | max_length=254, null=False, blank=False, default='' | CharField

##### OrderLineItem

Name | Key in DB | Validation | Field Type
------------ | ------------- | ------------- | -------------
Order | order | Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems' | ForeignKey
Product | product | Product, null=False, blank=False, on_delete=models.CASCADE | ForeignKey
Product Size | product_size | max_length=2, null=True, blank=True | CharField
Quantity | quantity | null=False, blank=False, default=0 | IntegerField
Line Item Total | lineitem_total | max_digits=6, decimal_places=2, null=False, blank=False, editable=False | DecimalField

## Technologies Used

#### Languages Used
  - [HTML5](https://en.wikipedia.org/wiki/HTML5)
  - [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
  - [JavaScript](https://en.wikipedia.org/wiki/Javascript)
  - [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

#### Tools
  - [Gitpod](https://www.gitpod.io/) Used as online IDE for developing this project.
  - [Django](https://www.djangoproject.com/) Used as python web framework.
  - [Stripe](https://stripe.com/en-ie) Used as payment platform to validate and accept credit card payments securely.
  - [AWS S3 Bucket](https://aws.amazon.com/) Used to store images added into the database.
  - [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) Used to enable creation, configuration and management of AWS S3.
  - [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) Used to style the django forms.
  - [Django Storages](https://django-storages.readthedocs.io/en/latest/) This is a collection of custom storage backends with django to work with boto3 and AWS S3.
  - [Django Allauth](https://django-allauth.readthedocs.io/en/latest/) Used to handle register, log in, log out actions.
  - [Django Countries](https://pypi.org/project/django-countries/2.0/) For handling the country selection.
  - [Gunicorn](https://pypi.org/project/gunicorn/) Used for deployment of the Django project to heroku.
  - [Pillow](https://pillow.readthedocs.io/en/stable/) USed as python imaging library to aid in processing image files to store in database.
  - [Psycopg2](https://pypi.org/project/psycopg2/) Used as PostgreSQL database adapter for Python.
  - [PIP3](https://pip.pypa.io/en/stable/) for installation of tools in this project.
  - [Git](https://git-scm.com/) Used to handle the version control.
  - [GitHub](https://github.com/) Used to store all project code.
  - [Balsamiq](https://balsamiq.com/) Used to create the wireframes.
  - [Mockup Generator](https://techsini.com/multi-mockup/index.php) USed to create a mockup of this project.
#### Databases
  - [PostgreSQL](https://www.postgresql.org/) for production database, provided by heroku.
  - [SQlite3](https://www.sqlite.org/index.html) for development database, provided by django.
#### Libraries
  - [FontAwesome](https://fontawesome.com/) Used to add all icons.
  - [JQuery](https://jquery.com/) to simplify DOM manipulation.
  - [Google Fonts](https://fonts.google.com/) Used to get the 'Dosis' font.
  - [Bootstrap](https://getbootstrap.com/) to make the website responsive and more visually appealing.

## Testing

Information about the testing proccess can be found in a separate [TESTING.md](testing.md) file. 

## Deployment

### Heroku Deployment
1. Start by creating a `requirements.txt` file using the terminal command `pip freeze > requirements.txt`.
2. Create a `Procfile` and add this line of code: web: gunicorn fitnology.wsgi:application
3. `git add`, `git commit` and push to Github what you just added. 
4. Go to [Heroku website](https://dashboard.heroku.com/apps/) and create a new app starting in the dashboard and clicking the "New" button select "Create new app". Give it a name and region.
5. On the newly created application dashboard, click "Deploy" > "Deployment method" and select GitHub.
6. Find and Confirm the correct github repository link of the heroku app.
7. On the project dashboard for the application, click on "Settings" and "Reveal Config Vars".
8. Then add the following config vars:

Key | Value 
------------ | ------------- 
AWS_ACCESS_KEY_ID | `Your Value`
AWS_SECRET_ACCESS_KEY | `Your Value` 
DATABASE_URL | `Your Value` 
EMAIL_HOST_PASS | `Your Value` 
EMAIL_HOST_USER | `Your Value` 
SECRET_KEY | `Your Value` 
STRIPE_PUBLIC_KEY | `Your Value` 
STRIPE_SECRET_KEY | `Your Value` 
STRIPE_WH_SECRET | `Your Value`  
USE_AWS | `True` 

9. Now from the command line of your local IDE:
    + Enter the heroku postgres shell
    + Migrate the database models
    + Create your superuser account in your new database

10. Back in the heroku dashboard, click "Deploy". Scroll down to "Manual Deploy", select the master branch then click "Deploy Branch".
11. Lastly click the "View app" button and the website should be ready to go. 


## Credits

### Code
- [Boutique Ado](https://github.com/Code-Institute-Org/boutique_ado_v1) - The Code institute Boutique Ado demonstration has been a huge inspirational source for me in this project. This was what was first introducing me to django and this was the best guide way for me to follow to create the fitnology website. Any code copied from Boutique Ado has been mentioned in the project code itself.
- [Codemy.com](https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi) - These are the youtube videos that helped me understand how I could build a blog for the website. Any code copied from Codemy.com has been mentioned in the project code itself.
- Other helpful websites was [w3schools.com](https://www.w3schools.com/) and [Stack Overflow](https://stackoverflow.com/)

### Content 

- [Code Institute README](https://github.com/Code-Institute-Solutions/readme-template) - This template was used to guide me in the right direction for making my own README.
- [Article about exercise](https://dietsinreview.com/diet_column/11/exercise-makes-you-less-anxious-and-reduces-stress/) - The text from this article was borrowed in the blog of the fitnology website.
- [Article about working out at home](https://us.humankinetics.com/blogs/excerpt/advantages-of-working-out-at-home) - The text from this article was borrowed in the blog of the fitnology website.
- [Article about heart](http://www.mankatoclinic.com/the-importance-of-living-a-heart-healthy-lifestyle) - The text from this article was borrowed in the blog of the fitnology website.
- [Article about biking](https://www.betterhealth.vic.gov.au/health/healthyliving/cycling-health-benefits) - The text from this article was borrowed in the blog of the fitnology website.

### Media

- [Freelogodesign](https://www.freelogodesign.org/manager/signin?r=https%3A%2F%2Fwww.freelogodesign.org%2Fmanager) - Platform to create your own logo. 
- [Unsplash](https://unsplash.com/) - Many of my images for the home page and blog is taken from this website. 
- [Amazon](https://www.amazon.se/) - Most of my products images was found on amazon. 
- [Fitbit](https://www.fitbit.com/global/se/products) - Where I found images for smartwatches.
- [Apple](https://www.apple.com/se/) - Image for airpods. 
- [Vaha](https://uk.vaha.com/) - Smart Mirror Image. 

### Acknowledgements
A big thanks to the tutor team of Code Institute for taking their time helping me whilst I struggled to get my website deployed. 

## Disclaimer
#### Please note that content on this website is for educational purpose only.