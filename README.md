1. Clone the repo and run install_packages.sh
2. go to utilities/initialize_db.py and add the pincodes and email ids

3. cd src/
4. run: python3 utilities/initialize_db.py (your pwd should be at src/)

Step 2 & 3 will initialize the db

5. go to services/email_service.py
6. add sender_email (Less secure apps should be allowed for this email id for more info visit: https://myaccount.google.com/lesssecureapps)
7. add password

Step 5 to 7 are needed to send emails once the vaccine is available

