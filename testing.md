# Fitnology - Testing Details

### [README.md](readme.md)
### [Fitnology](https://fitnology.herokuapp.com/)

## Table of Contents
1. [User Stories Testing](#user-stories-testing)
2. [Manual Testing](#manual-testing)
3. [Code Validation](#code-validation)
4. [Bugs Discovered](#bugs-discovered)
5. [Further Testing](#further-testing)
### User Stories 
* First Time Visitor Goals
    * As a first time visitor, I want to be able to understand the purpose of the application;
       * By landing on the home page the user is provided with all information needed to understand the purpose of the website.
    * As a first time visitor, I want to be able to find information about the company;
       * By scrolling on the home page the user can read information about the company. 
    * As a first time visitor, I want to be able to see all products the company has to offer;
       * By navigating with the navigation bar I can find the all products section by pressing products > all products and it takes me to the products page.
    * As a first time visitor, I want to be able to move through the menu pages;
       * I can click on each navigation bar to get to each separate page.
    * As a first time visitor, I want to be able to add products to the virtual bag;
       * If I go to the single product page by pressing for example the image of the product I there find a button that I can add the item to my bag with.
    * As a first time visitor, I want to be able to check the virtual bag;
       * If i press the bag icon I land on the bag page holding all my added products. 
    * As a first time visitor, I want to be able to place an order in Fitnology;
       * In the bag if I have added an item I can press the checkout button leading me to a form I have to fill in to purchase an item.
    * As a first time visitor, I want to be able to pay an order in Fitnology;
       * On the secure chekout page I can add my card details to pay an order.
    * As a first time visitor, I want to be able to see a overview of my placed and payed order;
       * Once an order is successfully created the user lands on a page with all the details.
    * As a first time visitor, I want to be able to create a profile;
       * If I press the profile icon I could choose the option register and land on the register page holding a form I need to fill in to become a member.
    * As a first time visitor, I want to be able to register;
       * Once I have filled in the form for the registration I press register and get a confirmation email I need to confirm to get registered.
    * As a first time visitor, I want to be able to login;
       * Pressing the profile icon I could choose the option login, taking me to the login page where I can enter name and password then the button login to get to my account.
    * As a first time visitor, I want to be able to logout.
       * Once Loged in I could press the profile icon and choose logout.
* Returning Visitor Goals
    * As a returning visitor, I want the same application experience as a first time visitor;
       * Stays the same as for what was mentioned above.
    * As a returning visitor, I want to check my order history at Fitnology;
       * All orders from the user and its history are saved in the users profile page. 
    * As a returning visitor, I want to read blog posts.
       * If the user is logged in they can go to the blog page and scroll to the post they want to read and press the button read more to see the full post.
* Frequent User Goals
    * As a frequent user of this application, I want the same experience as a first time visitor and returning visitor;
       * Stays the same as for what was mentioned above.
    * As the owner of Fitnology I want to easily create, update blog posts or products, and/or remove product items or blog posts from the products and/or blog. 
       * if I am logged in as admin user/ owner user I find edit and delete buttons under the products and in the single posts page. If I want to add a product or blog post I simply press the profile icon and choose Product management or Blog management.

## Manual Testing
Below you find all manual testing that was performed to confirm all things work as expected on the website.

### Testing on different devices 
All these steps were taken on one larger screen and one laptop screen and one mobile screen. All tested in Chrome and Safari.

#### As visitor 
   + Clicked each link in the navbar to confirm that they took me to the right pages.
   + Added a product to the cart making sure the right amount was shown in the bag and that the bag turned blue once I added the product.
   + Removed Item from cart to make sure the amount changed to something less.
   + Clicked on the logo to confirm I landed on the home page.
   + Searched in the search bar to see that the search function worked by giving the correct results.
   + Pressed the products page category buttons to confirm they showed the right products for each category.
   + Clicked on the dropdown button in the navbar and tested the category links took me to the right products.
   + Went to the home page pressing all it's links and making sure they took me to the right places.
   + Clicked on products to see if I landed on single product page.
   + Checked the blog page and pressed the register button to see it took me to the register page
#### As Member 
   + As logged in user I checked to see that they could read the blog post by pressing the read more button.
   + As logged out user I checked to see blog page that read more button was replaced with register button.
   + Confirmed that once logged out the register and login became visible in the profile icon and my profile and logout wasn't visible.
   + Logged into the website and looked so my profile and log out was visible, whilst register and login was removed.
   + Checked my profile to see that my order history was saved correctly.
#### As Admin 
   + Log in as the admin user, confirmed that the Product Management and Blog Management links was added.
   + Confirmed as a logged in admin user I could Add new products from Product Management
   + Confirmed as a logged in admin user I could Add new posts from Blog Management
   + Confirmed as a logged in admin user I could remove a product or blog post.
   + Confirmed as a logged in admin user I could edit a product or blog post.

## Code Validation 

### [CSS Validator](https://jigsaw.w3.org/css-validator/)
No Errors or warnings were found.


### [HTML Validator](https://validator.w3.org/nu/)
One warning shown due to unnecessary for JavaScript resource. Otherwise No errors. 

### [JSHint](https://jshint.com/)
Gave me some smaller warnings and I tried to fix most of them.

### [PEP8 Validator](http://pep8online.com/)
The check resulted in a a few errors. Several of them saying "line too long", as some of them were a bit longer than 79 characters, I reformatted my code as much as I could, still having a couple of them left.
   

## Bugs

#### Solved bugs

1. Creating the blog app
    +  Whilst creating the blog app and giving it its url the terminal gave me this error
“ModuleNotFoundError : no module named : crispy_forms” 
I searched on Stackoverflow to find a helping solution, and whilst this [article](https://stackoverflow.com/questions/59704108/modulenotfounderror-no-module-named-crispy-forms) gave me a bigger understanding regarding what could cause the problem, I later discovered after going back to my code and looking after typos. That I had forgotten to add a comma in installed apps for the settings.py file. This what I understand it as was causing the terminal to not recognize the code and therefore not being able to render my code and start the application. 

2. Main bugs
   + Several of my bugs occured with the error message “Template does not exist” I found throughout the process a routine helping me tackle issues like this, most of them also being solved after following these steps. First was to look at my folders, did they have the correct name in terms of what I for example had been typing in my views.py file. Second, do the links in the navbar hold the right file path and names. Third. is the url patterns added in the fitnology urls.py file. By following this I managed to solve several problems fast and quick without having to get stuck for too long in the process. 

3. Blog add post page
   + In this section of the coding process I had a big error causing me and the owners of the store not to open the add blog post management page and instead giving a 404 error. What I found with the help of tutor Kevin was that I had the wrong url in the add_post.html template, and the changes that had to be made was to remove the url ‘add_post’ and change it to url ‘addpost’ to make it match with the url I put in the urls.py file for the blog. Yet for this to work I also needed to comment out the url leading to the blog posts page and whilst that fixed the issue for the post management a new issue occurred, causing users not being able to open the blog itself. Giving the error “NoReverseMatch at blog/blog/”. The solution was for when one uses SLUG urls they have to be listed last in the urls file, or they will interfere with other urls. So by moving the url path for the blog to the end of the list everything worked as wanted again.

4. Add Fixtures
   + We could follow along in the Boutique ado project whilst they teach us how to deploy our project. I had a lot of struggle understanding how to create my fixtures and then after creating a dumpdata for my code I could not do the command loaddata for each category, post or product. This resulted in me creating three different json files that were empty and what I had to do was to take my saved info regarding each field (such as categories, posts and products) in my db.json file and copy them into the correct json file. After that I could complete the deployment of my website.

5. Adding Images from Amazon AWS
   + I had two issues here, first one was that the media folder I created for the AWS deleted itself after I came back the next morning. I had to create a new media folder and add all images again and the problem was solved at the same time the fourth bug was fixed. Some images remained empty in the website tho, so I had to look in the terminal to see that I had added the correct image with the correct image name. Once adding the images, the missing blog and products images were working as they should. Second was my header image in the blog landing page and home page, these didn’t show up. Once again back to devtools and look at the file path here I found out that I needed to add {{ IMG_URL }} before each image path I had added in the html. Once that was fixed everything was up and running. 

#### Unsolved Bugs

1. When it comes to my register page the form there is too small for my screen and I would like to make it so it looks like all the other forms on my website. Due to time I could not fix this for now but leave it as a known bug for future fix. 

## Further Testing
Asked friends and family to take a look at my website and play with it on different devices and make sure to report any issues they found.