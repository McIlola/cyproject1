## Cyber Security Project 1 website
Premade users:
- alice : redqueen
- bob : squarepants
- admin : salasana1

Using the OWASP 2021 list

### Essay
https://github.com/McIlola/cyproject1 

Instructions on how to use: 
- Download the project and unzip it. 
- Move to the to the project folder in the terminal. 
- Write “python manage.py runserver“. 
- Open the provided link to access the website. 

If you have done the previous exercises on the course, it should work. 

Flaw 1 A01:2021 – Broken Access Control: 

https://github.com/McIlola/cyproject1/blob/fce66ab436cc7e3aac4a54e13470ee5c8da05b1f/polls/views.py#L36  

Broken access control implies that users of an application can access information or do stuff outside their rights. For example, a user performs actions that require admin rights without actually being an administrator or being able to access a page that would require logging in by editing the URL. 

The flaw here is that anyone can vote in the polls and not only verified users. It applies to broken access control because you can perform actions that you necessarily don't have the right to do. It can be fixed by uncommenting the code below the marked row. This code checks that the user is verified and prevents them from voting if they are not and returns a message saying they need to be verified. 

 

Flaw 2 A02:2021 – Cryptographic Failures: 

https://github.com/McIlola/cyproject1/blob/fce66ab436cc7e3aac4a54e13470ee5c8da05b1f/mysite/settings.py#L141  

Cryptographic failures mean weak or missing encryption. There are multiple encryption methods and some of them are weak in today's standards, having simple or hardcoded encryption keys that make decrypting traffic simpler for attackers. Also not having enhanced encryption on sensitive information, such as payment information or medical records. 

The second flaw that that can be found behind the link is a hardcoded encryption key. This allows an attacker to decrypt traffic on the website if they get access to the key since the same key is used by everyone. To fix the issue you should remove the hardcoded key on line 143 and uncomment line 142 that allows the application to use a randomly generated environmental key. This allows the users to have more secure encryption keys and most importantly different encryption keys. 

 

Flaw 3 A03:2021 – Injection: 

https://github.com/McIlola/cyproject1/blob/a7925bc1ca29f593e2b8e3be44a736fc5840ef02/polls/views.py#L40  

Injection means that users can pass unwanted information through the application that can harm the application. For example, delete a table from a database. It works when an application has an insecure way of handling user inputs and through the input allows a user to access information, they should not have access to or just break an application. It can be fixed by validating user inputs and using more secure ways of adding and accessing information. 

In this application the injection flaw can be found behind the link, it uses an insecure way of searching for information in a database. By editing the URL while in the voting part of the application, you can pass through information that can break the application. It can be fixed by uncommenting line 43 and removing line 44. On line 44 the application inputs the users' inputs directly into the SQL command and by doing so allows the user to manipulate the database. The commented part uses parameterized queries to have a more secure way of manipulating the database without allowing the user to break anything. 

Flaw 4 A07:2021 – Identification and Authentication Failures: 

https://github.com/McIlola/cyproject1/blob/a7925bc1ca29f593e2b8e3be44a736fc5840ef02/mysite/settings.py#L89  

Identification and authentication failures mean poor ways of handling security. It includes allowing users to have bad passwords and not using multi-factor authentication. Bad passwords allow malicious actors to access user accounts and possibly get important information from them. To make an application more secure you should use multi-factor authentication, then having a bad password does not give anyone direct access to your account. To prevent automated login attacks, you should implement timeouts for incorrect login. 

The flaw in this application is allowing bad passwords to be used. Django provides automated password checking so that bad passwords don’t get used, but disabling this feature allows any password to be used. Under the row provided in the link, you can find AUTH_PASSWORD_VALIDATORS commented out. By uncommenting the section, you can get access to password validation that does not allow bad passwords. 

Flaw 5 CSRF vulnerability: 

https://github.com/McIlola/cyproject1/blob/a7925bc1ca29f593e2b8e3be44a736fc5840ef02/polls/templates/polls/detail.html#L2  

https://github.com/McIlola/cyproject1/blob/a7925bc1ca29f593e2b8e3be44a736fc5840ef02/mysite/settings.py#L47  

CSRF stands for cross-site request forgery, it entails that someone makes a user submit a request that they did not mean to submit. It requires that the attacker knows how the website handles a request. Then the user needs to be authenticated on the target website and the attack can start. By using a link that executes something on a website the attacker can perform some wanted action on the user's behalf. It does not require the user to click the link, since you can use image tags to automatically execute the URL. 

The flaw in the application is allowing the user to make requests without a CSRF token. This token means to add a layer of security to requests by having the website authenticate the user's token upon requests. If a request is made without the token, it will not go through. To get rid of this flaw in the application you will need to do two things: behind the first link is the HTML document that handles voting, and you will need to uncomment the “csrf_token” part so that you are only left with “{% csrf_token %}”. Behind the second link, you will be in the Django settings part, since Django has additional CSRF protections, you will need to uncomment the “'django.middleware.csrf.CsrfViewMiddleware',” part to enable extra protection. This will allow the website to use CSRF protection while making requests. 
