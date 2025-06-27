# IT Ticket Support System

## User Guide

### How to Login

To access the IT Ticket Support System, navigate to the login page. Use one of the following credentials:

- **Admin User**
  - **Username:** admin
  - **Password:** admin

- **Regular User**
  - **Username:** user1 (or user2, user3, ..., user10)
  - **Password:** password

Enter your username and password, then click the **Login** button. Admin users have full access to all tickets and user management features, while regular users can only view and manage their own tickets.

---

### How to Create an Account

If you do not have an account, click on the **Sign Up** link on the login page. Fill in the registration form with the following fields:

- **Username:** Must be at least 3 characters and unique.
- **First Name:** Required.
- **Password:** Must be at least 3 characters.
- **Confirm Password:** Must match the password.

**Validation Controls:**
- Usernames must be unique and at least 3 characters long.
- Passwords must be at least 3 characters and both password fields must match.
- All fields are required.

If your registration is successful, you will be automatically logged in and redirected to the home page. If there are any errors (such as username already exists or passwords do not match), an error message will be displayed and you can correct your input.

---

### Additional Notes

- If you forget your password, please contact an admin user for assistance.
- Admin users can create, view, update, and delete any ticket or user account.
- Regular users can only create, view, and update their own tickets; they cannot delete tickets or view other users' tickets.

## Problem & Scope Statements

Organisations frequently encounter inefficiencies in managing their IT Supprt estates, often leading to reduced productivy, delayed resolutions and employee disatisfaction. Traditional methods for IT support, generally consisting of email chains and excel spreadsheets, present a range of limitations for organisations, lacking transparency, scalability and automation. According to Serrano et al. (2021), many organisation continue to struggle and fail in the adoption of mondernised IT service management practices, highlihting challenges such as inconsitent processes, minimal automation and poor visibility to IT processes. 

This application aims to address these issues through providing a centralised platorm for submiting, resolving and monitoring the progress of IT support tickets. The system is tailored to be a lightweight and intuative solution for automating ticket resolution workflows without the need for a traditional suite of office tools. As such, the scope of this project focusses on secure user authenication, role-based access controls, ticket creation and management, and finally ticket status tracking. Beyond this, Admin users can perform full Create, Read, Update and Delete (CRUD) operations on Tickets and User Accounts, while regular users cannot delete tickets nor see other user data. 

Finally, the system adheres to SOLID principles and leverages database design featues such as soft delete to maxamise the robustness of the system. 


# Refrences

Serrano, J., Faustino, J., Adriano, D., Pereira, R. and da Silva, M.M. (2021). An IT Service Management Literature Review: Challenges, Benefits, Opportunities and Implementation Practices. Information, [online] 12(3), p.111. doi:https://doi.org/10.3390/info12030111.