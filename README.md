# PP5 - Something Sweet

[View the live project here.](https://pp5-2025-ef5b32295a0a.herokuapp.com/)

![](https://github.com/MiaTothova/PP5/blob/main/readme-images/am-i-responsive.png)
The image is from [Am I responsive?](http://ami.responsivedesign.is/)

SomethingSweet is a fun and colorful e-commerce application for premium candy products. Built using Django,The platform features user registration with Allauth, a dynamic shopping bag system, integrates Stripe for secure payments and offers a full-stack, user-friendly solution for browsing, customizing, and purchasing sweet treats online. Admin users can manage products, contact-us message requests, faq's and orders through the Django admin dashboard.

## Business Plan

SomethingSweet is an online candy shop aimed at bringing a fun and personalized shopping experience to sweet lovers of all ages. The goal of the business is to offer high-quality, visually appealing candy products that can be purchased individually or through customizable mix boxes (Future Feature). By targeting customers looking for gifts, party supplies, or personal indulgence, SomethingSweet aims to stand out through convenience, product variety, and user-friendly design.

Revenue is generated through direct product sales and premium pricing on candy. In the future, the business may expand to offer subscription boxes, wholesale bundles, and gift card options. Key features such as secure Stripe payments, account registration, wishlist functionality, and a contact form support both customer satisfaction and long-term growth. With its vibrant design and scalable functionality, SomethingSweet has the potential to grow into a successful niche e-commerce brand.
[Access Facebook Business Page Here](https://www.facebook.com/profile.php?id=61578362021551)

![](https://github.com/MiaTothova/PP5/blob/main/readme-images/facebook/b-page1.png)
![](https://github.com/MiaTothova/PP5/blob/main/readme-images/facebook/b-page2.png)
![](https://github.com/MiaTothova/PP5/blob/main/readme-images/facebook/b-page3.png)


## UX

### The ideal client:
* Candy lovers of all ages who want a fun and easy online shopping experience.
* Gift buyers looking to send sweet treats to loved ones.

### The site will help clients to:
* Browse and purchase a wide range of candy products.
* Easily register, log in, and manage their account.
* Safely pay via Stripe and receive order confirmation.

#### 🔍 Navigation Overview

1. Logo Navigation: On the homepage, clicking the **SomethingSweet** logo at the top left returns the user to the homepage from any page.
2. Search Bar: Next to the logo is the **search functionality**, allowing users to search for candy products by name or keyword.
3. Contact and FAQ: Next to the search bar are the **Contact** and **FAQ** links, where users can fill out a contact form and browse frequently asked questions.
3. Account Access: To the right is the **Account** menu where users can register, log in, log out, and access their profile or order history. 
5. Admin Access: Admin users can run `python3 manage.py createsuperuser` in the terminal to create a superuser. Once logged in, they can access the Django admin panel to add, edit, or delete products, manage orders, and moderate contact messages and faq's.

#### 🛒 Shopping & Checkout

1. Bag Icon: At the top right, the **shopping bag icon** shows how many items are in the user's bag. Clicking it opens the cart summary.
2. Product Detail Page: Clicking on a product opens its detail page where users can:
  - View product description
  - Choose quantity using increment/decrement buttons
  - Click **Add to Bag** to add the product
3. Cart Management: In the **shopping bag**, users can view their selected items, adjust quantities, remove items, and click **Checkout** to proceed.
4. Checkout Flow: At checkout, users provide their shipping details and complete their payment securely using Stripe. An email confirmation is sent after a successful purchase.
 

## The skeleton
### Wireframes

HOME PAGE
![](https://github.com/MiaTothova/PP5/blob/main/readme-images/wireframes/w-home.png)

PRODUCT LIST
![](https://github.com/MiaTothova/PP5/blob/main/readme-images/wireframes/w-product.png)

SHOPPING BAG
![](https://github.com/MiaTothova/PP5/blob/main/readme-images/wireframes/w-bag.png)

database schema

![]()

## The Scope

### Features
1. Full product catalog with filtering by category, price, and rating.
2. Shopping cart with quantity management.
3. Secure Stripe checkout.
4. User registration and authentication (via Django Allauth).
5. Contact form and newsletter signup.
6. Admin dashboard to manage products, orders, and users.
7. FAQ page

### Future features
1. Candy subscription service.
2. Wishlist functionality for logged-in users.
3. Product reviews.


## Testing
### User Stories
HOME PAGE
![](https://github.com/MiaTothova/PP5/blob/main/readme-images/user-story-testing/homepage.png)

PRODUCT LIST
![](https://github.com/MiaTothova/PP5/blob/main/readme-images/user-story-testing/productspage.png)

PRODUCT INFO/ADD TO BAG
![](https://github.com/MiaTothova/PP5/blob/main/readme-images/user-story-testing/addbag.png)

SHOPPING BAG
![](https://github.com/MiaTothova/PP5/blob/main/readme-images/user-story-testing/cart.png)

CHECKOUT
![](https://github.com/MiaTothova/PP5/blob/main/readme-images/user-story-testing/checkout.png)

CHECKOUT SUCCESS
![](https://github.com/MiaTothova/PP5/blob/main/readme-images/user-story-testing/checkout-succes.png)

PRODUCT SEARCH BAR
![](https://github.com/MiaTothova/PP5/blob/main/readme-images/user-story-testing/product-search.png)

FOOTER NEWSLETTER
![](https://github.com/MiaTothova/PP5/blob/main/readme-images/user-story-testing/footer.png)

NEWSLETTER SUBSCRIPTION SUCCESS
![](https://github.com/MiaTothova/PP5/blob/main/readme-images/user-story-testing/newsletter.png)

CONTACT PAGE
![](https://github.com/MiaTothova/PP5/blob/main/readme-images/user-story-testing/contact.png)

FAQ
![](https://github.com/MiaTothova/PP5/blob/main/readme-images/user-story-testing/FAQ.png)

 ### Adicional Testing

![](https://github.com/MiaTothova/PP5/blob/main/readme-images/lighthouse.png)
![](https://github.com/MiaTothova/PP5/blob/main/readme-images/Email-confirmation.png)
![](https://github.com/MiaTothova/PP5/blob/main/readme-images/Email-pss-reset.png)


## Validation

### CSS:

### Base
![](https://github.com/MiaTothova/PP5/blob/main/readme-images/validations/base.css-validation.png)

### Checkout
![](https://github.com/MiaTothova/PP5/blob/main/readme-images/validations/checkout.css-val.png)

### Faq
![](https://github.com/MiaTothova/PP5/blob/main/readme-images/validations/faq.css-val.png)

### Profiles
![](https://github.com/MiaTothova/PP5/blob/main/readme-images/validations/profiles.css-val.png)

### JavaScript:

![](https://github.com/MiaTothova/PP5/blob/main/readme-images/validations/jshint.png)
### Python:

![](https://github.com/MiaTothova/PP5/blob/main/readme-images/validations/no-errors.png)

### HTML: All Pages

![](https://github.com/MiaTothova/PP5/blob/main/readme-images/validations/html-validation.png)


## Technologies Used

* [Github](https://github.com/) Was used to host my repository.
* [Heroku](https://id.heroku.com/login)Used to host my application.
* [pep8online.com](https://pep8ci.herokuapp.com/#)Used to validate my code validate my code and check for errors.
* [Balsamiq](https://balsamiq.com/) I used the low-fidelity wireframing tool to create structure of the website layout.
* [Visual Studio Code](https://code.visualstudio.com/) Was used as my coding enviroment.
* [W3C Markup Validation Service](https://validator.w3.org/#validate_by_input) Was use to check the markup of the web documents in HTLM.
* [W3C jigsaw Validation Service](https://jigsaw.w3.org/css-validator/validator) Was used to chech and validate the CSS in my project.
* [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/)Was used to inspect any issues and inspect the responsiveness of the website.
* [js hint](https://jshint.com/) Was use to check for any errors in the Javascript code.
* [DALL.E](https://chatgpt.com) Was use to generate images for my website.

## Deployment

## Credits
No code has been copied from external sources. This project is based entirely on the Boutique Ado walkthrough, which provided the foundation for the e-commerce functionality.

I did research online for inspiration and guidance on implementing my three custom models, referring to resources such as YouTube and Stack Overflow. However, with the clear guidance and support of my tutor, Rory Patrick Sheridan, I was able to fully understand and implement the models independently. His explanations were incredibly helpful and played a key role in my development process.

I'd also like to thank Roman for his occasional support during development, which was helpful at key moments when I needed a second opinion or quick clarification.

## During Development
* This project is based on the Boutique Ado walkthrough. In the walkthrough, the SECRET KEY is pushed directly to GitHub, which should not happen. It wasn’t until the very end that I realized the key should be set through my env.py file. As a result, I had to change my SECRET KEY, and the exact same issue occurred with the Stripe Webhook Key.
This should not happen and is a very serious mistake.

* After implementing the shopping bag refactoring video, the minus (-) button for decreasing quantity no longer disables when the quantity reaches 1 — particularly in desktop view. This allows users to reduce the quantity below the minimum, which should not happen
- Future fix: To prevent this issue, consider removing the +/- buttons entirely and allowing users to input the quantity directly into the input field with validation. This approach would simplify the logic and avoid button state inconsistencies across different devices.

* In the Boutique Ado walkthrough, there is a critical issue related to order visibility and user assignment:
- If a user completes a purchase, copies the checkout success URL, logs out, and then logs in as a different user — pasting the copied link into the browser will still grant access to the checkout success page of the original order.
- A different user can view another customer’s order details, which is a privacy concern.
- Even more critically, the order gets reassigned to the newly logged-in user in the admin panel, resulting in incorrect order ownership and potential data inconsistency.
- Future fix: Restrict the ability to place and view orders to logged-in users only.



