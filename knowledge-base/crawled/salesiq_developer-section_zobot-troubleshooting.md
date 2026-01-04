# Zoho Salesiq Article

**Source:** https://www.zoho.com/salesiq/help/developer-section/zobot-troubleshooting.html
**Crawled:** 2026-01-04

---

​

## **Zobot Troubleshooting**

**Table of Contents**

  * **SalesIQ Scripts**
  * Save Error​
  * Runtime Error



### **Save Errors**

Save error is a type of error that prevents the user from saving their script. This type of error mostly occurs due to incorrect syntax and variable declaration. The following table lists the save errors in Deluge.

**Error Message**| **Description**  
---|---  
Message : <Handler name> : (Line no: 2) Variable '<variable>' is not defined| This error message is displayed if a variable is used before it is defined. One common way to define a variable is to use set variable task.  
**Example** :  
a=10;  
c= a+b;**Solution** :  
The variable b is defined with a number value.  
a=10;  
b=5;  
c=a+b;  
Message : <Handler name> : (Line no: 5) Syntax error. Expecting '}' or statement. Found '<EOF>'.| This error message is displayed if an opening parenthesis is not perfectly matched with a closing parenthesis. The closing parenthesis marks the end of a block of statements.  
**Example** :  
a=10;  
if(a>0)  
{  
info "True";**Solution** :  
The opening parenthesis is correctly matched with a closing parenthesis.  
a=10;  
if(a>0)  
{  
info "True";  
}  
Message : <Handler name> : (Line No : 3) Syntax error. Expecting '}' or statement. Found '/'.| This error message is displayed if an opening comment symbol (/*) is not correctly paired with a closing comment symbol (*/). Anything between these two comment symbols is skipped from execution.  
**Example** :  
/*a=10;  
b=5;  
c=a+b**Solution** :  
The opening comment symbol is perfectly paired with a closing comment symbol.  
/*a=10;  
b=5;  
c=a+b;*/  
Message : <Handler name> : (Line no: 5) Improper Statement Error might be due to missing ';' at   
end of the line or incomplete expressionorMessage : <Handler name> : (Line no: 5) Syntax error. Expecting ';'. Found 'question2'.| In Scripts, every line must be terminated by a semicolon to call it a statement. The mentioned error message is displayed if a statement is not properly terminated with a semicolon.  
**Example** :  
response.put("action","context");  
response.put("context_id","enquiry");  
//No semicolon in question1  
question1 = {"name":"name","replies":{"May I have your name please?"}}   
question2 = {"name":"email","replies":{{"text":"Can you provide your email address?","validate":{"format":"email"}}}};**Solution** :  
The variable definition statement is terminated with a semicolon.  
response.put("action","context");  
response.put("context_id","enquiry");  
question1 = {"name":"name","replies":{"May I have your name please?"}};  
question2 = {"name":"email","replies":{{"text":"Can you provide your email address?","validate":{"format":"email"}}}};  
Message : <Handler name> : (Line no: 4) Unexpected token found '"'(Or)Message : <Handler name> : (Line no: 4) Improper Statement Error might be due to missing ';' at   
end of the line or incomplete expression| A text must always be enclosed in double-quotes. If it is not properly enclosed, the improper statement error is thrown.  
**Example** :  
response.put("action","context");  
response.put("context_id","enquiry");  
//No double quotes on question1 (name)   
question1 = {"name":"name","replies":{"May I have your name please?}};  
question2 = {"name":"email","replies":{{"text":"Can you provide your email address?","validate":{"format":"email"}}}};**Solution** :  
The value "May I have your name please?" is correctly enclosed in double-quotes.  
response.put("action","context");  
response.put("context_id","enquiry");  
question1 = {"name":"name","replies":{"May I have your name please?"}};  
question2 = {"name":"email","replies":{{"text":"Can you provide your email address?","validate":{"format":"email"}}}};  
Message : <Handler name> : (Line no: 4) Syntax error. Expecting '}' or ','. Found ';'.| This error message is displayed if an opening parenthesis is not perfectly matched with a closing parenthesis. The closing parenthesis marks the end of a line on statements.  
**Example** :  
response.put("action","context");  
response.put("context_id","enquiry");  
//No closing parenthesis at the end of "question1"  
question1 = {"name":"name","replies":{"May I have your name please?"};  
question2 = {"name":"email","replies":{{"text":"Can you provide your email address?","validate":{"format":"email"}}}};**Solution:**  
The opening parenthesis is correctly matched with a closing parenthesis.  
response.put("action","context");  
response.put("context_id","enquiry");  
question1 = {"name":"name","replies":{"May I have your name please?"}};  
question2 = {"name":"email","replies":{{"text":"Can you provide your email address?","validate":{"format":"email"}}}};  
Message : <Handler name> : (Line No : 1) Missing return statement: Provide MAP expression to return| This error message is displayed if a return statement is defined but no value is returned.  
**Example** :  
response = Map();  
{  
Block of statements  
}**Solution** :  
The return statement is provided here.  
response = Map();  
{  
Block of statements  
}  
return response;  
  
### **Runtime Errors**

Runtime error occurs during script execution. This type of error mostly occurs due to inappropriate action, done by the user. The following table lists the runtime errors in Deluge.

**Error Message**| **Description**  
---|---  
Logs : Insufficient data| 1\. This error message is displayed, if the block response is "context" and the context_id is not defined.  
**Example** :  
response.put("action","context");  
question1 = {"name":"name","replies":{"May I have your name please?"}};  
question2 = {"name":"email","replies":{{"text":"Can you provide your email address?","validate":{"format":"email"}}}};  
questions = Collection();  
questions.insert(question1);  
questions.insert(question2);  
response.put("questions",questions);**Solution** :  
The context_id is defined for the context.  
response.put("action","context");  
question1 = {"name":"name","replies":{"May I have your name please?"}};  
question2 = {"name":"email","replies":{{"text":"Can you provide your email address?","validate":{"format":"email"}}}};  
questions = Collection();  
questions.insert(question1);  
questions.insert(question2);  
response.put("questions",questions);2\. This error message is displayed, if the block has no output response defined in it.  
**Example** :  
question1 = {"name":"name","replies":{"May I have your name please?"}};  
question2 = {"name":"email","replies":{{"text":"Can you provide your email address?","validate":{"format":"email"}}}};  
questions = Collection();  
questions.insert(question1);  
questions.insert(question2);  
response.put("questions",questions); **Solution** :  
The output response is defined here "action"  
response.put("action","context");  
response.put("context_id","enquiry");  
question1 = {"name":"name","replies":{"May I have your name please?"}};  
question2 = {"name":"email","replies":{{"text":"Can you provide your email address?","validate":{"format":"email"}}}};  
questions = Collection();  
questions.insert(question1);  
questions.insert(question2);  
response.put("questions",questions);