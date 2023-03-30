<!---`python3 -m http.server`--->
# MUNCH -

I have created a full-stack website [site](website address) that allows my users to manage a common dataset in the form of recipies to cookbook domain.

My project is incomplete please can you provide me with any feedback possible, thank you.

![multi-device](assets/readmeimages/multiscreen.png)

## Live Site

[site](website address)

## Repository

[repository address](repository address)

---

## Contents

+ [Project Requirements](#project-requirements)
+ [UX and UI](#ux-and-ui)
+ [Strategy Plane](#strategy-plane)
  + [Initial Idea](#initial-idea)
  + [User Stories and Goals](#user-stories-and-goals)
+ [Scope Plane](#scope-plane)
+ [Structure Plane](#structure-plane)
+ [Skeleton Plane](#skeleton-plane)
    + [Header](#header)
    + [Footer](#footer)
+ [Site Visuals - Surface Plane](#site-visuals---surface-plane)
    + [Form Confirmation Page](#form-confirmation-page)
    + [Site Structure](#site-structure)
    + [Colour Pallette](#colour-pallette)
    + [Typography](#typography)
    + [Imagery](#imagery)
+ [Features](#features)
  + [Included Features](#included-features)
    
    + [Product Page](#product-page)
        + [Product Information](#product-information)
    + [Contact Page](#contact-page)
      + [Contact Form](#contact-form)
        + [Form Confirmation](#form-confirmation)
    + [Future Features](#future-features)
+ [JavaScript Process](#javascript-game-process)    
+ [Technologies Used](#technologies-used)
+ [Testing](#testing)
+ [Deployment](#deployment)
+ [Sources](#sources)
+ [Credits & Acknowledgements](Credits)
  + [Content](#content)
  + [Media](#media)
  + [Code](#code)

---

## Project Requirements

Main technologies need to be used

+ HTML
+ CSS
+ JavaScript
+ Python+Flask
+ PostgreSQL
+ Additional Libraries and External APIs
  + tech library example

Mandatory Requirements

+ Data handling - To build a relationa Database backed Flask project for a web application that allows users to store and manipulate data records about a particular domain.

+ Database structure - deigning a database structure well-suited for my domain. Showing thought put into relationships between records of different entities.

+ User Functionality - Use CRUD Functionality so users can Create, Read, Update and Delete records. (including locate).

+ Use of technologies - Use HTML and custom CSS for the website's front-end.

+ Structure - Incorporate a main navigation menu and structured layout.

+ Documentation - Write a README.md file for your project that explains what the project does and the value that it provides to its users.

+ Version control - Use Git & GitHub for version control.

+ Attribution - Maintain clear separation between code written by you and code from external sources.

+ Deployment: Deploy the final version of your code to a hosting platform such as Heroku.

---

## UX and UI

Creating products that are useful, useable and provide value using UCD (User Centered Design)

Organisation Goals + User Goals + User Interface + Interaction with Back End System = User Experience

User Centric Design process using 5 planes of UX is what I will focus on to ensure a positive expeirience for the user

---

## Strategy Plane

The Idea, Objectives and Users needs

### Initial Idea

To create a Application that allows people to access many different styles and sources of recipies from many different collaborators, while also advertising high quality kitchen tools and appliances.

### User Stories and Goals

Being the primary user I expect the following -

+ Being able to share my recipies with a larger community.
+ also be able to expand my knowledge from other users submissions.

As the owner I want the following from my site -

+ To create a repository of recipies from the data submitted by many different people.
+ I can add my own recipies to one location and make sure i can refer back to them later.
+ See if recipies submitted can be improved by users suggestions.
+ Promote with the hope to increase sales of a brand of cooking implements and tools.
+ Increase visitors and contributions to the site

As a developer I am looking to provide the following -

+ Clean, efficient and easily intuitive design
+ No bugs or errors throught the site with features responsind correctly to vistors requests
+ User Centered Design process followed to ensure user has a postive expereince whenever they use my application

---

## Scope Plane

How am I going to provide users with what they want

Which features, based on information from strategy plane, do you want to include in your design?

+ The Creation of a web application that stores and allows access to users recipes, while also allowing for editing of the recipie by the recipie creator and suggestions by other users.
+ Fields within the recipes to make them easily understandable and comparable to other recipies on site include, ingredients, preperation time, cook time, tools, cooking steps.
+ Create the backend code and frontend form(s) to allow users to add new recipes to the site, edit them and delete them.
+ Create a search function using the backend and frontend functionality for users to locate recipes based on selected recipe's fields such as ingredients.
+ Easy to read and intuitive design to allow easy navigation of an ever increasing recipe directory
+ With-in the tools section include relevant detail and links to promote sales of the my kitchen tools.
+ Look into incorporating a scoring system for recipies that users can rate and review tried recipies

---

## Structure Plane

Interaction of features

How is the information structured and how is it logically grouped, the features, the elements, the data, the information?

+ Recipes can be searched by using the keyword or title from the recipe such as from the ingredients list and also other keywords included when creating the recipe such as vegetarian, pasta etc.
+ Home Page - introduction to the site
  + Links to the tools used in the recpies
+ Recipes Page
  + Recipes shown within certain categories (vegetraian, Meat, Fish, under 30 mins, etc...)
  + Categories;
    + Vegetarian
    + Meat
    + Fish
    + Under 30 mins
    + Best Rated
    + New Recipes
  + Option to create/add own recipes
  + Search Option
+ Sign in/Add own recipies Page
+ Links to shop or products Page
+ Contact and socials Page
+ With-in the individual recipe's have the following features;
  + Prep Time
  + Cook Time
  + Appliances Required
  + Cooking Temperatures
  + Ingredients
  + Stages
  + Add you own photos of your version of the recipie
  + Suggested Combinations such as drinks, deserts etc
  + Links to socials to share
  + Suggestions that contributors can add to maybe make the recipe better
  + Rating System

---

## Skeleton Plane

Inteface and Navigation Design

### How will our information be represented, and how will the user navigate to the infomration and the features?

Navigation throughout the site will be from the Nav Bar accesible in the header of every page. The Header and Footer will stay consistent on every page to aid navigation.

#### Header

Header & Navbar

![Header](/munch/static/images/munch-header.png)

#### Footer

+ Social Media & Contact Links for Owners and Developer

![Footer](/munch/static/images/munch-footer.png)

### How do you navigate through the information and features?

From within the recipie page you can either click on one of the categories represented or search for a specific recipe

### How will the content relate to each other, what relationships will the content have?

### What has priority and lower priority and based on this where do we position the content?

I focused on a simple priority progression to allow for easy manuverability throughout the site, where you can go from Home, to the main recipe repository to a single recipe.

Priority was also given to help visulaise how a recipe might be followed in reality, for exaple you'll need to know what need preheating and prepared first and the stages that follow that to ensure the recipe is followed correctly and the users desired result is acheived at the end of it.

---

## Site Visuals - Surface Plane

 What Will the finished product look like?

### Wireframes

I created my Wireframes using [Balsamiq](https://balsamiq.com).

#### Home Page

![Home/Game Page Wireframes](/munch/static/images/home-page.png)

#### Recipie Repository Page

![Home/Game Page Wireframes](/munch/static/images/recipes-page.png)

#### Sign In Page

![Home/Game Page Wireframes](/munch/static/images/Sign-in-page.png)
#### Products Page

![Home/Game Page Wireframes](/munch/static/images/shop-page.png)
#### Contact & Socials Page

![Home/Game Page Wireframes](/munch/static/images/contact-page.png)

### Colour Pallete

I wanted my site to represent a bright and lively display so will be going with an orange from materialize.

### Typography

The fonts I selected were not ideal to the finished product i wished to present;

### Imagery

Style and statements I wanted to make are still pending but there will be a minamalist addition of images other than the images submitted in the recipes.

### Design elements

I used design elements such as Materialize which greatly helps with planning and positioning the layout of the pages.

---

### Future Developments

+ integrate a rating system for recipes
+ in depth catergory sytem

+ links to recipe how to videos etc.

---

<!--## Thought Process

### Thought 1-->

---

## Technologies Used

+ [Python](https://www.python.org/)
+ [HTML5](https://html.spec.whatwg.org/)
+ [CSS](https://www.w3.org/Style/CSS/Overview.en.html)
+ [JavaScript](https://www.javascript.com/)
+ [Balsamic](https://balsamiq.com/wireframes/)
+ [Google Fonts](https://fonts.google.com/)
+ [Font Awesome](https://fontawesome.com/)
+ [Chrome Developer Tools](https://developer.chrome.com/docs/devtools/)
+ [GitHub](https://github.com/)
+ [GitPod](https://www.gitpod.io/)
+ [Multi Device Mock Up Generator](https://techsini.com/multi-mockup/)
+ [Bootstrap](https://getbootstrap.com/docs/5.2/getting-started/introduction/)

---

## Testing

Due to the unfinished nature of my site I was unable to test extensivley <!-- [click here](testing.md)-->

## Deployment

The site was deployed to GitHub pages.

+ Go To your Git Hub Repository
+ Under Repository Name, click on "Settings"
![setting image](/munch/static/images/github-settings.png)
+ Click on "Pages" options on the left hand side of the screen
![Page selection](/munch/static/images/github-pages.png)
+ under "build & deployment, & under "source" select "main Branch".![Page selection](/munch/static/images/github-build-deployment.png)
+ and then select publishing source "(root)
+ click Save
+ this will then give you your Git Pages address
![GitHub Pages](/munch/static/images/livesite.png)

 [live site on git hub](https://melanyhowell.github.io/p3-munch/)
## Sources

Codemy on Youtube was very helpful in seeing how the basics of SQL ALchemy came together - [link](https://www.youtube.com/watch?v=Q2QmST-cSwc&t=540s)
### Media

so far no images were sourced other than icons from Font Awesome

### Code

+ with issues I found I used the following references;

[code institute walkthrough](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DIWADRDB+2022_Q3/courseware/c0c31790fcf540539fd2bd3678b12406/6e44128b0b37416ab40c1a87ef2cb32a/)

many-many relationship issues -
[abdelhadi Dyouri tutorial](https://www.digitalocean.com/community/tutorials/how-to-use-many-to-many-database-relationships-with-flask-sqlalchemy)

## Credits & Acknowlegements

+ Thank you to my newly assigned mentor Chris, he has helped me see its not a problem to ask if stuck and the problem is never as big as it seems.

Melany Howell 2023.
