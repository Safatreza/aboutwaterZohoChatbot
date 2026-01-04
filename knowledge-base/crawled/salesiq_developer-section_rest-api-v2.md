# Zoho Salesiq Article

**Source:** https://www.zoho.com/salesiq/help/developer-section/rest-api-v2.html
**Crawled:** 2026-01-04

---

# Rest APIs

A REST API defines a set of functions using which the developers can perform requests and receive responses via the HTTP protocols such as GET and POST.

## Server URI

SalesIQ offers the following server URI. Choose the server URI based on your data center.

**Data Center**| **ZohoSalesIQ_Server_URI**| **ZohoAccounts_Server_URI**| **Developer Console**  
---|---|---|---  
US  
(United States)| salesiq.zoho.com| accounts.zoho.com| [api-console.zoho.com](https://api-console.zoho.com/)  
EU  
(Europe)| salesiq.zoho.eu| accounts.zoho.eu| [api-console.zoho.eu](https://api-console.zoho.eu/)  
IN  
(India)| salesiq.zoho.in| accounts.zoho.in| [api-console.zoho.in](http://api-console.zoho.in/)  
AU  
(Australia)| salesiq.zoho.com.au| accounts.zoho.com.au| [api-console.zoho.com.au](http://api-console.zoho.com.au/)  
CN  
(China)| salesiq.zoho.com.cn| accounts.zoho.com.cn| [api-console.zoho.com.cn](http://api-console.zoho.com.cn/)  
JP  
(Japan)| salesiq.zoho.jp| accounts.zoho.jp| [api-console.zoho.jp](http://api-console.zoho.jp/)  
  
### What is the Screen name?

The unique name provided to your SalesIQ portal is known as the Screen name.

**Example:** https://salesiq.zoho.com/**zylker** /index

### What is the response format?

The response format is how you get the answer from the respondent. Both the success and the error responses hold the status code as 200.

### Success Response Format

If the request is successful, the response object contains a key "data" that holds the result of the request.

  * **url** : request URL
  * **object** : list or resource object type
  * **data** : String or array or object
  * **sync_time** : request current time (Only to GET Resouce list APIs)



**Example**
    
    
    {
          "data" : <value - string, array or object> ,
          "url":<value - string> ,
          "object": < value - string>
    }

### 

### Error Response Format:

In case of errors, the response object contains a key "error" which contains information about the error. The error object might contain keys such as the "code" (unique error code), and the "message" (description of the error), and you might also get one of these [optional keys](/salesiq/help/developer-section/rest-api-v2.html#keydetails) (json_key or param or header) in your error response. Use them to identify and resolve your error.

**Example**
    
    
    {
      "error" :
      {
        "message":"Invalid URL",
        "code":1006,
        "json_key":<value - string>, // Optional key
        "param":<value - string>, // Optional key
        "header":<value - string> // Optional key
      }
    }​​​

### 

### Basic Authorization Errors

#### 1\. General Error (Code: 1001 )

**Message** : "Unknown authentication error. Contact SalesIQ Team!"

This type of response occurs in case of internal server error (i.e., due to problems in the server while retrieving the data.)

* * *

#### 2\. Invalid Header Error (Code: 1002)

**Message** : "Invalid authorization header."

This error occurs when either the Authorization header is absent or is not set properly.

* * *

#### 3\. Invalid Header Value (Code: 1054)

**Message** : "Invalid header value"  
Header: <header-name>

This error occurs when the request header value is not valid. (For ex, If an API accepts JSON input, the request header "content-type" should be "application/json"). If your error is related to the "content-type" header, you can refer to the following:

**Valid content-type request header values:**

  * For JSON input APIs - application/json
  * For form input APIs - application/x-www-form-urlencoded



* * *

#### 3\. **Invalid Request Type Error (Code: 1004)**

**Message** : "Invalid Request Type."

The invalid request type error occurs when the request method is incorrect (For ex : If you have sent a Post request instead of a Get URL request.)

* * *

#### 4\. **Invalid Portal Error (Code: 1005)**

**Message** : "Invalid portal or wrong screen name."

This type of error occurs when the user portal is invalid (i.e., If the user Portal is not valid or the provided screen name is wrong.)

* * *

#### 5\. **Invalid URL error (Code: 1006)**

**Message** : "Invalid URL"

This kind of error occurs if the requested URL is incorrect. For example, "https://zylker.com/api/" - is the wrong URL because the screen name is missing in the provided URL.

* * *

#### 6\. **Invalid Data Type (Code: 1007)**

**Message** : Invalid datatypes found in params,  
param: <Invalid-param-name>, //Optional key  
json_key: <Invalid-json-key> //Optional key

The error is sent when the data type of a parameter sent does not comply with the mentioned one. You might get one of these [optional keys](/salesiq/help/developer-section/rest-api-v2.html#keydetails) (json_key or param) in your error response. Use them to identify and resolve your error.

* * *

#### 7\. **Invalid OAuthToken (Code 1008)**

**Message** : Invalid OAuthToken.

This kind of error occurs if the OAuthToken is incorrect.

* * *

#### 8\. **Invalid OAuthScope (Code: 1009)**

**Message** : Invalid OAuthScope.

This kind of error occurs if the OAuthScope is invalid.

* * *

#### 9\. **Invalid Method (Code: 1010)**

**Message** : Invalid Method.

This kind of error occurs if the mentioned method is invalid.

* * *

#### 10\. **Invalid Params (Code 1011)**

**Message** : Either the request parameters are invalid or absent,  
param: <Invalid-param-name> //Optional key

This kind of error occurs if the provided param is invalid or not present.

* * *

#### 11\. **Invalid Inputstream (Code: 1015)**

**Message** : Either the input stream is invalid or absent,  
json_key: <Invalid-json-key> //Optional key

This kind of error occurs if the provided input stream is invalid or is not present.

* * *

## General Errors

#### 1\. **Resource Already Exists (Code: 1014)**

**Message** : "Resource already exists"

This type of response occurs in case if the provided resource details already exist.

* * *

#### 2\. **Permission Denied (Code: 1016)**

**Message** : "Operator doesn't have permission to perform the operation"

This type of error occurs when the operator doesn't have access to perform the operation based on their role (Associate, Supervisor, Administrator).

* * *

#### 3\. **Limit Exceeded (Code: 1017)**

**Message** : "Resource limit reached for current plan"

This type of error occurs when the resource limit has been exceeded. This is based on their current Zoho SalesIQ purchase plan.

* * *

#### 4\. **Empty File (Code: 1018)**

**Message** : "File is empty"

This type of error occurs when the file sent doesn't contain any data.

* * *

#### 5\. **Invalid Resource (Code: 1019)**

**Message** : "Invalid Resource"

This kind of error occurs if the requested resource is not valid.

* * *

#### 6\. **Invalid Operator (Code: 1020)**

**Message** : Invalid operator

This type of error occurs when the requested operator does not belong to the portal.

* * *

#### 7\. **Upgrade Needed (Code: 1021)**

**Message** : Operation is not available in the current plan

This kind of error occurs if your current plan does not support the requested action.

* * *

#### 8\. **Remote IP Locked (Code: 1023)**

**Message** : Too many requests, lease try after sometime

This kind of error occurs if too many actions are performed at the same time and the IP is blocked from performing any action for a while.

* * *

#### 9\. **Invalid Operator IDs (Code: 1024)**

**Message** : Invalid Operator id/s

This kind of error occurs if the requested operator ID is not valid.

* * *

#### 10\. **Invalid Department IDs (Code: 1025)**

**Message** : Invalid Department IDs

This kind of error occurs if the requested department ID is not valid or is not present.

* * *

#### **11\. Last Available Resource (Code: 1026)**

**Message** : Last available resource

This kind of error occurs if you are about to delete the last available resource in the portal. (For ex, If your portal has one department and you are about to delete that department, then this error will occur.)

* * *

#### 12\. **File Size Exceeded (Code: 1027)**

**Message** : File size is greater than the allowed size

This kind of error occurs if the file size is greater than the allowed size.

* * *

#### 13\. **Invalid File Type (Code: 1028)**

**Message** : Invalid file type

This kind of error occurs if the file type is not valid.

* * *

#### 14\. **Invalid Filters (Code: 1029)**

**Message** : Invalid Filter

This kind of error occurs if the filter you have applied is not valid.

* * *

#### 15\. **Insufficient Data (Code: 1031)**

**Message** : Insufficient data 

This kind of error occurs if the given data is insufficient to perform the action.

* * *

### **New Key Details**

  * If your input JSON key is invalid, you will get "json_key" in your error response.


    
    
    Example:
     {
     "department":{
        "status":012345
      },
      "app_ids":["app", 123456789],
      "operators":[
        {
          "name":"agent 1"
        },
        {
          "name":"$#!@%^"
        }
      ]
    }

**Note:**

**Scenario**| **Syntax**| **Example**  
---|---|---  
If an invalid value is present inside JSONObject| <parent-key>.<child-key>| department.status  
If an invalid value is present inside JSONArray| <key>[<index>]| app_ids[0]  
If an invalid value is present inside an array of JSONObject| <parent-key>[<index>].<child-key>| operators[1].name  
  
  * If your query param or form input is invalid, you will find the "param" key in your error response.
  * You will find the "header" key in your error response if your request header is invalid.