# Zoho Salesiq Article

**Source:** https://www.zoho.com/salesiq/help/developer-section/rest-api-new.html
**Crawled:** 2026-01-04

---

# Rest APIs

A REST API defines a set of functions which developers can perform requests and receive responses via HTTP protocols such as GET and POST.

## What is Rest API?

A REST API defines a set of functions which developers can perform requests and receive responses via HTTP protocols such as GET and POST.

## What is Screen name?

The unique name provided to your SalesIQ portal is known as the screen name. 

**Example:**  
https://salesiq.zoho.com/**zylker** /index;

## What is response format?

The response format is how you get the answer from the respondent. Both the success and error responses hold the status code as 200.

## Success Response Format

If the request is successful, the response object contains a key "data" which holds the result of the request.

**Example:**  
{  
"data" : <value - string, array or object>  
}

## Error Response Format:

In case of errors, the response object contains a key "error" which contains info about the error. Error object contains 2 keys namely the "code" ( unique error code") and the "message" (message describing the error")

**Example:**  
{  
"error" :  
{   
"message":"Invalid URL",  
"code":1006  
}  
}

## Basic Authorization Errors

1\. **General Error:**

This type of response occurs in case of the internal server error (i.e., due to some problem in the server while retrieving the data.)

code: 1001 ,  
message: "Unknown authentication error, Contact SalesIQ Team!"

2\. **Invalid Header Error:**

This error occurs when either the Authorization header is absent or not set properly.

Code: 1002,  
Message: "Invalid authorization header."

3\. **Invalid Request Type Error:**

The invalid request type error occurs when the request method is incorrect (For ex : If you have sent a Post request instead of a Get URL request.)

Code: 1004 ,  
Message: "Invalid Request Type."

4.**Invalid Portal Error:**

This type of error occurs when the user portal is invalid (i.e., If the user Portal is not valid or the provided screen name is wrong.)

Code: 1005 ,  
Message: "Invalid portal or wrong screen name."

5\. **Invalid URL error:**

This kind of error occurs if the requested URL is incorrect.

For example: https://zylker.com/api/ - is a wrong URL because the screen name is missing in the provided URL.

Code: 1006 ,  
Message: "Invalid URL"

6\. **Invalid Data Type:**

Error sent when the data type of a param sent does not comply with the mentioned one.

Code: 1007 ,  
Message: Invalid datatype found in params

7\. **Invalid OAuthToken:**

This kind of error occurs if the OAuthToken is incorrect.

Code: 1008 ,  
Message: Invalid OAuthToken.

8\. **Invalid OAuthScope:**

This kind of error occurs if the OAuthScope is invalid.

Code: 1009 ,  
Message: Invalid OAuthScope.