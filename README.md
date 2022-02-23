# Milestone Project 4: Fitnology

The website that is created for those with an interest in sports and technology. It offers products that are made for activity and to make the art of working for your body more efficient. In addition to this, the user can go to the website's blog which is there to inspire, motivate and inform those who are curious about how their products collected from different companies can be used to simplify everyday life and become healthier. In addition, there is the ability to create a profile, which allows the user to add comments to blog posts and evaluations for the products. All to offer the best possible experience to the user.

## Showcase 
![showcase-screenshot](media...)

[view the live project here.](#http)<br>

## Navigation

* [Features]
* [UX](#ux)
  + [User-stories](#user-stories)
* [Structure](#structure)
* [Wireframes](#wireframes)
* [Features](#features)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

## Features
The website follows UX and UI design as well as CRUD to create the best experience for the user, below shows what was created to contribute to this.

### Existing Features

- __Navigation Bar__

  - Featured on all pages, consist with a fully responsive navigation bar that includes links to the home page both on the logo and Home button, link to all the products featuring the products categories within it’s dropdown menu, third dropdown menu on the left standing for motivation and holding the link for the blog, membership page and for companies page. The the right side of the navigation bar the user find the profile link with dropdown menu to login, logout or signup. Lastly on the right there is the cart that will get all products added to it and send messages in case something goes with success or with an error. 
  - The Navigation Bar continues to be identical on all pages to remain as easy navigation.
  - Giving the user easy navigation through out the website, moving from page to page. It is responsive and functional as well as simple and aesthetically pleasing on all devices.   
 
![Nav Bar](media...)

- __Landing Page Image, Heading and Button__
  - Once landing on the home page there is a image holding a heading and button to give the user a first glance at what this website is and give them the chance to directly jump to the all products page.
  - This section is an inspiring and fun solution to interest the user and let them continue to explore the overall website and homepage itself.

  ![Landing Page Image](media...)

 - __Navbar Cart__
  - On the Navbar a cart is provided, this cart once a product is added to it turns to the color blue, letting the user know when something is added to it. 
  - Once you press the add to cart button, a smaller screen pops up showing a success message, the image of the product you just added, quantity, size if any, the total price for everything in your cart and go to the secure checkout button.
  - If the user presses the cart they land on the cart page.
  - If the user presses the go to secure checkout page they land on the checkout page.

  ![Nav Bar Cart](media...)

- __Introduction Section__
  - This section will provide the user with an inspiring introduction of the company, allowing the user to get a better understanding of what this company is. 
  - With its built in carousel showcasing three different images and small sections of introduction for each image. The user gets a visually appealing and quick understanding of what the website provides.

![Introduction Section](media...)

- __Introduction Post Section__
  - These three sections will allow the user to read exactly what the company are, does, and provide. 
  - Each section is separated by three images holding inspiring text that is clickable and leading to the blog page holding all different and inspiring posts.
  - Lastly there is a button on the bottom of the three introduction post sections leading the user to the create account page 

  ![Introduction Post Section](media...)

- __Contact Us__
  - Almost at the bottom of the homepage there is a form letting the user send the company a message in case of questions. 
  - This form is ended with a button that the user must click to send their message.

  ![Contact Us](media...)

- __Fotter__
  - At the end of each page for the website there is a responsive footer with the companies featured, links to products page, blog and homepage as well as the address for the company itself to continue provide the user with navigation and information about the company

  ![Fotter](media...)

- __Products Page__
  - The user if clicked on all products page, will here find everything the website has to offer in a row of four and down.
  - On the top there is a header telling the user they are on the products page following with clickable category buttons leading the user to specific categories holding specific products. Under the products heading after choosing the category a subheading appears with the category name they picked.
  - Under the category options a search bar is available, giving the option to search a specific product to find what one is looking for more quickly. 
  - Each Product section holds the Name, price, category and likes.
  - If the user is a member and logged in they get underneath the category name of the product options to like or dislike the product.
  - If the user is one of the logged in owners they get underneath the category name of the product an edit or delete button leading to the edit product page, or giving the user "product deleted" message if they choose to delete it. 

  ![Products Page](media...)

- __Single Products Page__
  - If the user chooses to click on a product they come to the single products page. This page shows a bigger image of the product itself, holding the product name, price, category, likes and description.
  - Underneath the description there is a quantity option that the user adds more quantity by pressing the plus button or less by pressing the minus button. The minus button only lets the user go to one then one cant press less. 
  - Lastly Two buttons are provided, one leading back to the products page and second putting the product in the cart. 

  ![Single Products Page](media...)

- __Cart Page__
  - Here the user gets an overview of everything they added to their cart, each individual product showing the name, quantity, price, size if any, SKU and image. 
  - On the right bottom a cart total amount is shown for every product, the delivery cost and total cost for everything.
  - Underneath the quantity the user has two options to choose from, update and or delete. If the user deletes a product a new message appears telling the product was successfully deleted from your bag. If you press the update button and you choose to add more quantity of that product you will get a new message telling your product was successfully updated and a new total price will be shown. 
  - Lastly two buttons are provided on the bottom right side of the page right above the footer. One leading back to the all products page and one leading to the checkout page. 

  ![Cart Page](media...)

- __Checkout Page__

![Checkout Page](media...)

# UX

## Strategy 

This project is a shopping system where users and/or guests can purchase technology products related to exercise and fitness as well as if they create an account and become a member of the website, they can purchase extra events provided only for members. The purpose of the application is to make it easy to anywhere in the world by mobile, computer or tablet find tech related products for fitness and also a platform to share their fitness journey on. 

### Site Goals

* Display Fitnology information;
* Allow Fitnology guests to create a account;
* Allow Fitnology users to easily delete their account;
* Allow Fitnology users to add, edit and/or delete a comment; 
* Allow Fitnology users to add, edit and/or delete their own blog post; 
* Allow Fitnology users special deals & offers;
* Display to guests & users Fitnology products;
* Allow Fitnology guests & users to place an order;
* Allow Fitnology guests & users to pay an order;
* Allow Fitnology guests & users to check their order history;
* Allow Fitnology owners to easily add, edit and delete products, special deals & offers.

#### User Stories: 

* First Time Visitor Goals
    * As a first time visitor, I want to be able to understand the purpose of the application;
    * As a first time visitor, I want to be able to find information about the company;
    * As a first time visitor, I want to be able to see all products the company has to offer;
    * As a first time visitor, I want to be able to move through the menu pages;
    * As a first time visitor, I want to be able to add products to the virtual cart;
    * As a first time visitor, I want to be able to check the virtual cart;
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
    * As a returning visitor, I want to add a review on products I purchased;
    * As a returning visitor, I want to add a comment to blog posts;
    * As a returning visitor, I want to add a blog post.

* Frequent User Goals
    * As a frequent user of this application, I want the same experience as a returning visitor;
    * As the owner of Fitnology I want to easily create, update, add deals, add events, blog posts and remove items or blog posts from the product and blog section. 

### My strategy 

I started the whole project by finding knowledge and inspiration from the code institute follow along project named Boutique Ado to get a brief understanding of how to make a project like this. You will find a link to this project in the credits section. I also had another website in mind whilst doing this application, this named Fitbit, in which I have found most of my inspiration regarding the layout of the website and it’s system. In case anything has been copied from another code all information about that will be found under the credits section. Yet in terms of my process all in which was created by inspiration from already working platforms. (maybe edit this)

## Scope 

Planned Features:<br>
* Responsive design;
* Navigation menu;
* tab;
* Menu with categories;
* Search bar;
* CRUD functionality;
* Product and blog management for the Fitnology owners;
* Profile page;
* Blog page;
* Comment sections for blog & products;
* Login functionality;
* Logout functionality.


# Technologies

Google fonts 
https://fonts.google.com/specimen/Dosis?query=dosis

Logo maker
https://www.freelogodesign.org/manager/signin?r=https%3A%2F%2Fwww.freelogodesign.org%2Fmanager

Images found 
Here https://wallpapersafari.com/w/eRjNCp

# Libraries 

jQuery https://releases.jquery.com/