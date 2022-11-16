# RossAnthonyDesigns

## Recipe Sharing app
------------------------------------

![alt text](./docs/landingpage.png)

Live site available [here](https://rossanthonydesigns.herokuapp.com/). 


-----

## Table of Contents
--------------------------------------

- [Description](#description)
- [Design](#design)
- [UX](#ux)
- [Agile Development](#agile-development)
- [Features](#features)
- [Testing](#testing)
- [Technologies](#technologies)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)
- [Author Info](#author-info)

------

## Description
---------------------------------------

Taste of India is a website built in Django using Python, JavaScript, CSS/Bootstrap and HTML. It centers around the very popular Indian cuisine. It enables users to create and share recipes with other users from around the world. It is targetted towards users who enjoy their food and would like to share their recipes with others. Users have the ability to create recipes, and their own profile. They can upload images for use on their recipe or on their profile, link their personal accounts and websites, leave comments on recipes and private message other users.

This is the fourth project for the Code Institute Diploma in Software Development.

The site provides role based permissions for users to interact with a central dataset. It includes user authentication and Full CRUD functionality for Recipes and User Profiles.

-------
## Design
-------

#### Wireframe mock-ups
---
Home page: 

The home page provides the user with a clear understanding as to the purpose of the site. The welcome message is clearly visable to the user when they first arrive at the site regardless of the device they are using.

![Home Page Wireframe](./docs/landingpage-wireframe.jpg)


Recipes Page:

Users have the ability to create recipes to share with other users. The emphasis of the design is to provide a clear recipe layout that can adapt to any size device. Clearly seperating general information, ingredients and steps.
Users will have the ability to search for recipes based on a search query of their choice. To aid in the discovery of different recipes, each recipe will be displayed in the form of a summary card from which the user can access the full recipe details.

![Recipes Wireframe](./docs/recipes-wireframe.jpg)


Profile Page:

Users also have the ability to create a personal profile. From this profile users can access the recipes they have created. They can also control the information they share with other users.

![User Profile Wireframe](./docs/user-profile-wireframe.jpg)


Wireframes were also produced for each major page for both mobile and tablet devices. With the intention of the site being fully responsive so that no matter the device size the user is viewing the site on, it will display accordingly.


* [Single-Recipe page wireframe](./docs/single-recipe-wireframe.jpg)
* [Profiles page wireframe](./docs/profiles-wireframe.jpg)
* [Inbox page wireframe](./docs/inbox-wireframe.jpg)
* [Message page wireframe](./docs/message-wireframe.jpg)
* [Form page wireframe](./docs/formpage-wireframe.jpg)
* [Delete page wireframe](./docs/delete-object-wireframe.jpg)


[Back to the Top](#table-of-contents)
#### Database Schema

Several custom models were predicted to be required when building the site. A Profile Model was included. In order for the users to create Recipes a custom recipe model was required, which would be linked to the User Profile through using the profile as a foreign key. The database schema was drawn out by hand.

![Database Schema Diagram](./docs/database-schema.jpg)

Once I was happy with the overall structure of the site, and the layout of the wireframes, I selected the colour scheme. The colour schemes were checked for colour contrast to ensure that the appropriate colours were used for a high level of colour contrast to maximise accessibility for users.

These colours were:

Light Mustard/Yellow: #e1a052

Light Green: #6e9d6c


[Back to the Top](#table-of-contents)

## UX
*  Taste of India is intended to be a friendly community site for users to create and share their own recipes with others. Users will also be able to find recipes created by other users from around the world. The graphical elements and overall design of the site provide the user with a fun and enjoyable environment.

### The Sites Ideal User
* Food lover looking to share their favourite recipes with others
* Someone looking to expand their recipe knowledge
* Someone looking for inspiration for new things to try

### Site Goals

* To provide users with a place to find recipes
* To provide users with a place to share their own recipes
* To provide users with a place to discover new meals

[Back to the Top](#table-of-contents)

## Agile Development

The plan for this project was carried out using the Agile Methodology in Github. User Stories were created using issues on git hub. Each user story explicitly explains the purpose of the issues. Each user story is segmented into acceptance criteria and tasks. It was prioritised using GitHub labels with different colors.

8 Epics were created which were then further developed into 29 User Stories. The details on each epic, along with the user stories linked to each one can be found in the project kanban board [here](https://github.com/users/KSheridan86/projects/4)

From the Epics, 29 User stories were developed. Each story was assigned a classification of Must-Have, Should-Have, Could-Have or Won't Have. Each story was also assigned user story points, based on my best estimation for the time/difficulty of completing each story. In practice some of these tasks were completed much quicker than anticipated and others took a little longer but overall the development went smoother than anticipated and the project was completed ahead of schedule. A number of these stories were chosen to be left out of the project as it was already quite big (I.E password reset or social media login) I was aware that as I approached the next project, PP5 - ECommerce these would be explained in more detail and I would get a chance to implement them properly.

### Epics

1. User Profile [#1](https://github.com/KSheridan86/project-4-TasteOfIndia/issues/1)
2. Sign in/out [#2](https://github.com/KSheridan86/project-4-TasteOfIndia/issues/2)
3. Recipes [#3](https://github.com/KSheridan86/project-4-TasteOfIndia/issues/3)
4. Recipe Interaction [#4](https://github.com/KSheridan86/project-4-TasteOfIndia/issues/4)
5. Search Recipes [#5](https://github.com/KSheridan86/project-4-TasteOfIndia/issues/5)
6. Landing page [#6](https://github.com/KSheridan86/project-4-TasteOfIndia/issues/6)
7. Messaging [#7](https://github.com/KSheridan86/project-4-TasteOfIndia/issues/7)
8. Authorisation [#8](https://github.com/KSheridan86/project-4-TasteOfIndia/issues/8)

### User Stories

These are the user stories that were completed within the projects first release, by Epic.

- User Profile
	*  Create a User Account - As a User, I would like to be able to create an account, so that I can create and save recipes
	*  Users can view their profile - As a User, I would like to be able to see the details in my user profile, so that I can see what  information other users can see about me
	*  Users can edit their profile - As a User, I would like to be able to edit my profile, so that I can keep the information upto date
	*  Users can delete their account - As a User, I can delete my account, so that I can remove my details and recipes at my request

- User sign in or sign out
	*  User Account Login / Logout - As a User, I would like to be able to login or logout of my account, so that I can keep my account secure
	*  Features restricted to signed in users - As a Site Owner, I would like to restrict some features of the site to registered users, so that it encourages people to sign up to the site

- User recipes
	*  Create a Recipe - As a User, I would like to be able to share my own recipes, with family and friends so they can teach them to their own children and have fun experiences together baking
	*  View Recipes - As a User, I can access the recipes on the site.
	*  Update a recipe - As a user, I can update a recipe that I have created, so that I can correct any mistakes I may have made
	*  Delete a recipe - As a user, I can delete a recipe that I have created, so that I can remove it from the site

- Recipe Interaction
	*  Leave Comments - As a User I can leave comments/feedback on Recipes I like/don't like
	*  Respond to Comments - as a user I can respond to comments left on my or others Users Recipes

- Recipe searching
	*  Recipe Searching - As a User, I would like to be able to find Recipes, so that I can increase the variety of meals we consume.
	*  Recipe Search - Advanced - As a User, I would like to be able to search the Recipes by title, ingredients or author, so that I can find the ones that match my fancy at that point in time

- Landing page
	*  As a User I would like to be brought to the landing page upon first visiting the site so that I can see what options are available to me
    *  As a User from the landing page I should have the option to view the Recipes or the Users
    *  As a User on the landing page I should be easily able to Log in or Register for an account

- Messaging
    *  As a User I would like to be able to send private messages to other Users
    *  As a User I would like to be able to reply to received private messages
    *  As a User I should be able to delete received private messages
    *  As a User access to my inbox should be easy and straight forward

- Authorisation
	*  As the site developer I would like to restrict Recipe CRUD functionality to logged in Users
    *  As the site developer I would like to restrict User Crud functionality to logged in Users 


[Back to the Top](#table-of-contents)


## Features

**Features planned:**
* User Profile - Create, Read, Update and Delete.
* Recipes - Users can create, read, update and delete their own recipes.
* Other Users Recipes - Users can read and comment on other users recipes.
* Profiles - Users can read other users profiles.
* Users can login to their account.
* Users can logout of their account.
* Users need to be registered and logged in to access recipe creation and account editing.
* Users can send each other private messages.
* Responsive Design - the site needs to be fully responsive to cover the wide variety of devices users may use to access a recipe site.


#### Home page
A welcoming homepage was built to welcome the user to the site and clearly convey the sites purpose. The call to action for the user to search for recipes is at the top of the main page, with a large, hero like welcome message appearing just below. At the bottom of the page a clear comparison showing users the benefits of signing up to the site is displayed.

![Home Page](./docs/landingpage.png)

#### Navigation Bar
The main navigation bar appears at the top of the page, clearly displaying the main navigational links users would require.

![Nav Bar](./docs/loggedout-navbar.png)

A secondary user menu is available to users who are logged into the site.

![logged in user nav bar](./docs/loggedin-navbar.png)


#### Footer
A common footer is utilised throughout the site.
The name is tongue in cheek and a reference to the working Burros I witnessed on a road trip across the American South-West.
This is a domain owned by myself and one day will host all of my projects.

![footer](./docs/footer.png)

#### Recipe/User Search
Users have the ability to search the database of recipes against the recipe title, ingredients and the author of the recipes username and the Users by their username/name.

![Recipe search](./docs/search-bar.png)

#### Recipe Cards
Search results appear in the form of recipe summary cards. The cards show the user the title of the recipe, the featured image of the recipe, and the author of the recipe. This allows the users to quickly identify the recipes they would like to look at in more detail.

##### Standard Recipe Card
![Standard Recipe Card](./docs/recipe-card.png)

#### User Profile
Users have the ability to create a profile. The user profile page provides the profile owner with quick access to edit and delete functionality.

![Owner Profile Page](./docs/user-profile.png)

Users can also access their own recipes easily.

![Easy Access to view/edit own recipes](./docs/recipe-crud.png)

#### Edit Profile Page
Users have the ability to edit their profiles on the site. The edit profile page is clearly laid out.

![Edit profile page](./docs/edit-profile.png)


## Future Enhancements
There are several items of functionality that I would like to add in the future. I have left the original user stories that were developed in the project kanban board as future enhancement opportunities.
The key areas I would like to add to the site in the future are:

* The ability for users to login via social networks such as google or facebook
* Forgot/reset password functionality
* Welcome emails


[Back to the Top](#table-of-contents)

## Testing

### Testing Strategy
I utilised a manual testing strategy for the development of the site.
Seperate to the functionality testing of the site, and the testing of the code, User Story tests were implemented to ensure that the criteria of the user stories listed above were met.


#### Testing Overview

Testing was divided into different sections to ensure everything was tested individually with test cases developed for each area.


#### Validator Testing
All code files were validated using suitable validators for the specific language.
HTML & CSS code passed the validation.
JavaScript code produced one warning about the use of an anonymous function within a loop.
When this function was named and moved outside the loop but referenced inside the loop, it broke functionality.
After attempting a few fixes I decided that an anonymous function inside a for loop was an acceptable JavaScript practice.
All validation screenshots are included below.

All HTML validation returned the same result so I have included only 1 screenshot here.
![HTML Validation](./docs/html-validation.png)
![CSS Validation](./docs/css%20validation.png)
![JS Validation](./docs/jshint.png)


#### Lighthouse Testing
Below you can see the results of Googles Lighthouse Testing.

![Lighthouse Testing](./docs/lighthouse-testing.png)


#### Python/JavaScript Testing
All Custom Python & JavaScript code was manually tested multiple times during and after development.
This is reflected in the fact that all of the user stories below are working and have produced no errors in the terminal or the console.

## Testing User Stories

------
User Story:

> Create a User Account - As a User, I would like to be able to create an account, so that I can create and save recipes

Acceptance Criteria:
* Given that I am an unregistered user, When I am on the homepage, Then I can see a button to sign up, And, When I click on the button, Then I am taken to the user registration page.
* Given that I am an unregistered user, And, I am on the user registration page, When I enter my username, email address and password, And, I click on the register button, Then The system creates me an account, And, signs me in.
* Given that I have an account, And, I am signed into the account, When I have an option to create a recipe, And, when I click on that option, Then I am taken to a page where I can provide the details of my recipe.

Implementation of tests:
* Check for clearly accessible call to action on homepage to register for an account and that it works as expected.
* Clearly accessible link to login or register within main navigation bar and that it functions correctly.
* Easy to use User registration process, user account and profile is created upon submission.
* Clear UX design, prevent unnecessary links to register as a user, if user is already logged in.

All Tests Passed &#x2611;
---

-----

User Story:

> Users can view their profile - As a User, I would like to be able to see the details in my user profile, so that I can see what information other users can see about me.

Acceptance Criteria:
* Given that I am logged into my user account I can access an option to view my profile.

Implementation of tests:
* Once a user is registered a button giving them access to their account appears in the menu.

All Tests Passed &#x2611;
---

-----

User Story:

> Users can edit their profile - As a User, I would like to be able to edit my profile, so that I can keep the information upto date.

Acceptance Criteria:
* Given that I am logged into my account when I am viewing my profile then I should be able to edit the details.
* Given that I am logged into my account when I click on the edit button on my profile page then I should be taken to a page to edit the details.
* Given that I am not logged into my account when I view my profile page, or anyone elses then I should not be able to see the edit button.
* Given that I am not logged into my account when I type in the address to edit my profile, or anyone elses then I should be redirected to the log in page.

Implementation of tests:
* Provide a clearly accessible button on a user's profile for the profile owner only, so they can edit their profile.
* Provide a simple and clear edit profile form, linked from the edit profile button.

All Tests Passed &#x2611;
---

-----

User Story:

Users can delete their account - As a User, I can delete my account, so that I can remove my details and recipes at my request.

Acceptance Criteria:
* Given that I am a registered user when I navigate to my account then I have an option to delete my account.
* Given that I am a registered user viewing my account details when I click on the option to delete my account then I am requested to confirm the request.
* Given that I am a registered user viewing my account details when I click on the option to delete my account
And, When I confirm the request then My account and the recipes that I have created are deleted.
* Given that I am a registered user when I delete my account then I should receive confirmation of the account deletion.

Implementation of tests:
* Provide users with an easily accessible option to delete their account.
* Provide users with a secure confirmation process to confirm account deletion requests to prevent accidents.
* Link all user created elements so that when a user deletes their account, all associated records are deleted.
* Provide the user with confirmation that their account has been deleted.

All Tests Passed &#x2611;
---

-----

User Story:

> User Account Login / Logout - As a User, I would like to be able to login or logout of my account, so that I can keep my account secure.

Acceptance Criteria:
* Given that I am a registered user, who is not logged in when I navigate to the sign in page and I enter my credentials correctly and press sign in then I am signed into my account.
* Given that I am a registered user, who is currently logged in when I click on the sign out link then I am signed out of my account.
* Given that I am a registered user, who has signed out of my account when I use the browser navigation buttons such as back button then I can not access information which requires me to be signed in.

Implementation of tests:
* Provide login and logout functionality.
* Secure restricted pages from access when a user is not signed in.

All Tests Passed &#x2611;
---

-----

User Story:

> Features restricted to signed in users - As a Site Owner, I would like to restrict some features of the site to registered users, so that it encourages people to sign up to the site.

Acceptance Criteria:
* Given that a user is not registered or signed in, when they look at a recipe then they do not have the ability to create a recipe.
* Given that a user is not registered or signed in, when they look at a recipe then they are unable to leave a comment.
* Given that a user is not registered or signed in, when they encounter functionality that requires them to be signed in then they are redirected to the login or register page.

Implementation of tests:
* Restrict the ability to create a recipe to authenticated users.
* Restrict the ability to comment on recipes to authenticated users.
* Redirect users who make a request for functionality that requires them to be authenticated users to the login page

All Tests Passed &#x2611;
---

-----

User Story:

> Create a Recipe - As a User, I would like to be able to share my own recipes, with family and friends.

Acceptance Criteria:
* Given that I am a logged in user when I navigate to the recipe section of my account then I have the option to create a recipe.
* Given that I have created a recipe as a logged in user when I save the completed recipe then it is available to other users to view.

Implementation of tests:
* Provide authenticated users with a clear option to create a recipe.
* Make saved recipes available to other users to view.

All Tests Passed &#x2611;
---

-----

User Story:

> View Recipes - As a User, I can access the recipes on the site, so that I can follow them at home.

Acceptance Criteria:
* Given that I am a user on the site when I navigate to the recipes page then I am presented with a list of the recipes available.
* Given that I am a user on the site when I navigate to the recipes page And When I click on a recipe then I am presented with the full recipe details.

Implementation of tests:
* Provide users of the site with the ability to access all recipes.
* Provide users of the site with the ability to access the full recipe details from the recipe summary card.

All Tests Passed &#x2611;
---

-----

User Story:

>  Update a recipe - As a user, I can update a recipe that I have created, so that I can correct any mistakes I may have made.

Acceptance Criteria:
* Given that I am a registered user who has created a recipe when I navigate to my profile page then I have the option to edit the details of my recipes.
* Given that I am a registered user when I navigate to someone else's recipe then I do not get the edit option.

Implementation of tests:
* Provide easy access to recipe owners to edit recipes.
* Prevent other users from editing a recipe they did not create.
* Provide a method for recipe owners to edit the recipe details.
* Ensure recipe edits are saved to the database and users are informed of changes.

All Tests Passed &#x2611;
---

-----

User Story:

> Delete a recipe - As a user, I can delete a recipe that I have created, so that I can remove it from the site.

Acceptance Criteria:
* Given that I am a registered user who is logged in, and has created a recipe when I navigate to my profile page then I have the option to delete my recipes.
* Given that I am a registered user who is logged in and wishes to delete a recipe, when I click the delete recipe button then I receive a confirmation window to confirm that I really want to delete the recipe.
* Given that I am a registered user who is logged in, has created a recipe, navigated to that recipe and clicked on the delete recipe button when the confirmation window appears and I confirm the deletion then the recipe is deleted from the system.
* Given that I am a registered user, or a non registered user when I navigate to a recipe page that I did not create then I do not have the option to delete the recipe.

Implementation of tests:
* Provide recipe owners with the option to delete their recipe.
* Provide recipe deletion requests with a confirmation window to prevent mistakes.
* Ensure confirmed deletion requests are processed on the database correctly.
* Prevent unauthorised access to recipe deletion functionality.

All Tests Passed &#x2611;
---

-----

User Story:

> Recipe Searching - As a User, I would like to be able to find recipes.

Acceptance Criteria:
* Given that I am a user of the website when I navigate to the homepage then I can access a link to all the recipes.
* Given that I am a user of the website when I want to view a specific recipe then I can access the full recipe details by clicking on the recipe.

Implementation of tests:
* Provide ease of access to full recipe list.
* Provide users with the ability to access full recipe details from the summary card.

All Tests Passed &#x2611;
---

-----

User Story:

> Recipe Search - Advanced - As a User, I would like to be able to search the recipes, so that I can find the ones that match my fancy at that point in time.

Acceptance Criteria:
* Given that I am a user of the website when I navigate to the site then I can access a search function to access related recipes.
* Given that I am a user of the website when I search the recipes then the search results show relevant recipes.

Implementation of tests:
* Provide all users the ability to search the recipes.
* Enable search query to match with recipe title, ingredients and author.

All Tests Passed &#x2611;
---

-----

User Story:

> Clear Recipe Layout - As a User, I would like clear instructions on how to make each recipe, so that I am able to follow along as an inexperienced cook.


Acceptance Criteria:
* Given that I am a user when I click on a recipe to view the details then The instructions on how to make the recipe are clearly accessible.
* Given that I am a user accessing the recipe details when I access a recipe instructions then they should be easy to follow.

Implementation of tests:
* Provide users with a clean and simple recipe detail page layout.
* Provide users with a easy to follow instruction list.

All Tests Passed &#x2611;
---

-----

User Story:

> Responsive Templates - As a Site Owner, I would like my site to be fully responsive, so that Users accessing the site from different devices have an enjoyable experience.

Acceptance Criteria:
* Given that I am a user accessing the site on my smartphone when I navigate through the site then all pages should be formatted to my device.
* Given that I am a user accessing the site on my tablet when I navigate through the site then all pages should be formatted to my device.
* Given that I am a user accessing the site on my laptop when I navigate through the site then all pages should be formatted to my device.
* Given that I am a user accessing the site on my desktop computer when I navigate the site then all pages should be formatted to suit my screen size.

Implementation of tests:
* Provide users with a fully responsive site that responds to mobile, tablet, laptop and desktop sized devices.


All Tests Passed &#x2611;
---

-----

User Story:

> Comment on Recipes - As a User, I would like to be able to comment on Recipes, so that all users can give and receive feedback on Recipes.

Acceptance Criteria:
* Given that I am logged in I should be able to post comments and read other users comments.
* Given that I am logged in I should be able to reply to comments left on Recipes .

Implementation of tests:
* Provide users with the ability to leave/view/reply to comments on Recipes.


All Tests Passed &#x2611;
---

-----

User Story:

> Visit Inbox - As a logged in user, I should be able to navigate to my Inbox easily.

Acceptance Criteria:
* Given that I am a logged in user, it should be easy for me to navigate to my inbox.
* Given that I am not logged in I should have no access to an inbox.

Implementation of tests:
* Provide users with a link to their inbox in the menu aswell as a clickable message icon in the navbar.
* Ensure that users who are not logged in have no acces to an inbox.


All Tests Passed &#x2611;
---

-----

User Story:

> Send Private Messages - As a User I should be able to send other users private messages.

Acceptance Criteria:
* Given that I am a user visiting another users profile page I should easily see a button to send a private message.

Implementation of tests:
* On all users account pages their is a button to send private messages.


All Tests Passed &#x2611;
---

-----

User Story:

> Reply to private messages - As a logged in user I should be easily able to reply to private messages I have received through my inbox.

Acceptance Criteria:
* Given that I am a logged in user I can see a Reply button inside any private message I have received from another logged in user.
* Given that I am a logged in user I can see an email address with which to respond to private messages from users who do not have an account.

Implementation of tests:
* Inside each private message received from a registered user there is a button to reply to that message.
* Inside each private message received from a non-registered user their email address is clearly marked for responding to their message.


All Tests Passed &#x2611;
---

-----

User Story:

> Delete private messages - As a logged in user I should be easily able to delete to private messages.

Acceptance Criteria:
* Given that I am a logged in user I can see a Delete button inside any private message I have received.
* Given that I am a logged in user I can see a Delete button beside any message I have received in my inbox.
* Given that I am a logged in user and I click the Delete message button I am shown a warning and asked to confirm that I wish to Delete this message.

Implementation of tests:
* Inside each private message received from a registered user there is a button to reply to that message.
* Inside each private message received from a non-registered user their email address is clearly marked for responding to their message.
* After the Delete button has been clicked a warning message appears to clarify that the message will be deleted.


All Tests Passed &#x2611;
---

-----

User Story:

> Pagination, As a user only a limited number of recipes/profile should be visible on any given page and I should be provided with easy navigation links to move to next/previous page.

Acceptance Criteria:
* Given that I am a User I can see buttons to navigate through the page results.
* Given that I am a User when I click on these buttons I am taken to the correct page.
* Given that I am a User and I use the search functionality, the page navigation buttons should reflect the current search results

Implementation of tests:
* Pagination buttons are clearly visible at the bottom of the recipes/profiles pages.
* When Clicked these buttons take the user to the desired page.
* When a user user the search functionality the pagination shown is directly linked to the results of the user search.
* 6 items are shown per page, this number works well across different devices, I.E Mobile = 1 column with 6 Items, Tablet = 2 columns with 3 items each, Desktop = 3 columns with 2 items each.


All Tests Passed &#x2611;
---

[Back to the Top](#table-of-contents)

-----

## Bugs

Tags issue:

To add Tags to the Recipes I had implemented a check box for users to select which tags were appropriate, this worked in the admin panel but unfortunately would not save the tags when used in the front end by the user.
When no fix could be found for this I used a different approach.
The checkbox was replaced with a text box for users to input their chosen tags.
In the view that handles this functionality I processed the input box so that each tag was separated, capitalized and added to the recipe.
But the user then had no ability to delete tags.
I insured that the tags added to the input box would override previous tags and prompted the user to include all relevant tags for the recipe in the input box.
This resolved most of the problem but I noticed that if the form was submitted with an empty tag input box it would delete all current tags.
To resolve this I insured that if an empty input box was submitted then the current tags would be prepopulated into the field upon submission therefore giving the user full crud functionality on the tags.


[Back to the Top](#table-of-contents)

-----

## Technologies

* Python
* Django
    * Django was used as the main python framework in the development of this project.
* Heroku
    * Was used as the cloud based platform to deploy the site on.
* Heroku PostgreSQL
    * Heroku PostgreSQL was used as the database for this project during development and in production.
* JavaScript
    * Custom JavaScript was utilised to allow Users to close site messages.
* Bootstrap 5
    * Bootstrap was used for general layout and spacing requirements for the site.
* Font Awesome
    * Was used for access to several icons for different sections where icons were appropriate.
* CSS
    * Custom css was written for a large number of areas on the site to implement custom styling and escape a bootstrap look and feel to the site.
* Jinja/Django Templating
    * Jinja/Django templating language was utilised to insert data from the database into the sites pages. It was also utilised to perform queries on different datasets.
* HTML
    * HTML was used as the base language for the templates created for the site.

#### Packages Used

* VS Code & Gitpod was used to develop the site
* Git was utilised for version control and transferring files between the code editor and the repository
* GitHub was utilised for storing the files for this project

#### Resources Used

* The Django documentation was used extensively during development of this project
* The Cloudinary documentation was used.
* The Code Institute reference material was used as a general reference for things that I had previously done during the course.
* All other resources used are referenced where appropriate.


[Back to the Top](#table-of-contents)

----

## Deployment

The site was deployed via Heroku, and the live link can be found here - [TasteOfIndia](https://pp4tasteofindia.herokuapp.com/)

### Project Deployment

To deploy the project through Heroku I followed these steps:
* Sign up / Log in to [Heroku](https://www.heroku.com/)
* From the main Heroku Dashboard page select 'New' and then 'Create New App'
* Give the project a name - I entered The-Pantry and select a suitable region, then select create app. The name for the app must be unique.
* This will create the app within Heroku and bring you to the deploy tab. From the submenu at the top, navigate to the resources tab.
* Add the database to the app, in the add-ons section search for 'Heroku Postgres', select the package that appears and add 'Heroku Postgres' as the database
* Navigate to the setting tab, within the config vars section copy the DATABASE_URL to the clipboard for use in the Django configuration.
* Within the django app repository create a new file called env.py - within this file import the os library and set the environment variable for the DATABASE_URL pasting in the address copied from Heroku. The line should appear as os.environ["DATABASE_URL"]= "Paste the link in here"
* Add a secret key to the app using os.environ["SECRET_KEY"] = "your secret key goes here"
* Add the secret key just created to the Heroku Config Vars as SECRET_KEY for the KEY value and the secret key value you created as the VALUE
* In the settings.py file within the django app, import Path from pathlib, import os and import dj_database_url
* insert the line if os.path.isfile("env.py"): import env
* remove the insecure secret key that django has in the settings file by default and replace it with SECRET_KEY = os.environ.get('SECRET_KEY')
* replace the databases section with DATABASES = { 'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))} ensure the correct indentation for python is used.
* In the terminal migrate the models over to the new database connection
* Navigate in a browser to cloudinary, log in, or create an account and log in. 
* From the dashboard - copy the CLOUDINARY_URL to the clipboard
* in the env.py file created earlier - add os.environ["CLOUDINARY_URL"] = "paste in the Url copied to the clipboard here"
* In Heroku, add the CLOUDINARY_URL and value copied to the clipboard to the config vars
* Also add the KEY - DISABLE_COLLECTSTATIC with the Value - 1 to the config vars
* this key value pair must be removed prior to final deployment
* Add the cloudinary libraries to the list of installed apps, the order they are inserted is important, 'cloudinary_storage' goes above 'django.contrib.staitcfiles' and 'cloudinary' goes below it.
* in the Settings.py file - add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
* Link the file to the templates directory in Heroku TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
* Change the templates directory to TEMPLATES_DIR - 'DIRS': [TEMPLATES_DIR]
* Add Heroku to the ALLOWED_HOSTS list the format will be the app name given in Heroku when creating the app followed by .herokuapp.com
* In your code editor, create three new top level folders, media, static, templates
* Create a new file on the top level directory - Procfile
* Within the Procfile add the code - web: guincorn PROJECT_NAME.wsgi
* In the terminal, add the changed files, commit and push to GitHub
* In Heroku, navigate to the deployment tab and deploy the branch manually - watch the build logs for any errors.
* Heroku will now build the app for you. Once it has completed the build process you will see a 'Your App Was Successfully Deployed' message and a link to the app to visit the live site.

#### Forking the repository
By forking the GitHub Repository you can make a copy of the original repository to view or change without it effecting the original repository
This can be done by
    * Log into GitHub or create an account.
    * Locate the repository at https://github.com/KSheridan86/project-4-TasteOfIndia .
    * At the top of the repository, on the right side of the page, select "Fork" from the buttons available.
    * A copy of the repository should now be created in your own repository.

#### Create a clone of this repository
Creating a clone enables you to make a copy of the repository at that point in time - this lets you run a copy of the project locally:
This can be done by:
* Navigate to https://github.com/KSheridan86/project-4-TasteOfIndia
* click on the arrow on the green code button at the top of the list of files
* select the clone by https option and copy the URL it provides to the clipboard
* navigate to your code editor of choice and within the terminal change the directory to the location you want to clone the repository to.
* type 'git clone' and paste the https link you copied from github
* press enter and git will clone the repository to your local machine


[Back to the Top](#table-of-contents)

-----

## Credits

All Images used across the site were sourced from either pexels.com, bbcgoodfood.com or (in the case of the user profiles created) freely available images of the subjects.
The Black Icons used across the site were sourced from a number of locations, attributions below.
- The map of India, (<a href="https://www.flaticon.com/free-icons/india" title="india icons">India icons created by Anditii Creative - Flaticon</a>) 
- Picture of a Donkey, (<a href="https://www.flaticon.com/free-icons/donkey" title="donkey icons">Donkey icons created by PLANBSTUDIO - Flaticon</a>)
- Taj-Mahal (<a href="https://www.flaticon.com/free-icons/taj-mahal" title="taj mahal icons">Taj mahal icons created by Freepik - Flaticon</a>)
- Envelope, This was sourced from Font awesome.
- Social media links were all sourced from Font Awesome.

I relied heavily on the Code institute course work, particularly the Django walk through projects.
Further research was done by building walk through projects available freely on youtube and Dennis Ivy's Django/Python course on Udemy.

-----

## Acknowledgements

I would like to acknowledge the help and support given by my mentor Chris Quinn, he is never short of good ideas. 
All of the students in my own study group aswell as all the students in the wider Code Institute Slack channels. My cohort Facilitator [Kasia](https://github.com/bezebee) and all of the staff at Code Institute. The sense of comraderie among all of these individuals has helped me to feel at home on my journey to a new career in programming.

On top of all these wonderful people I can't forget to thank my wife Rebecca for her help and understanding, without which none of this would be possible.

-----


## Author Info

Ken Sheridan, Junior Full Stack Software Developer.
- [GitHub](https://github.com/KSheridan86)
- [Linkedin](https://www.linkedin.com/in/kensheridan86/)


[Back to the Top](#table-of-contents)