# Zoho Salesiq Article

**Source:** https://www.zoho.com/salesiq/help/developer-section/workflows.html
**Crawled:** 2026-01-04

---

# Introduction to Workflows

Workflows in **Zoho SalesIQ** let you automate follow-up actions based on specific events that happen inside your portal, such as when a chat ends, a visitor replies, an operator is added, or a lead is updated.

Here's how it works:

  * **Events** : These are specific activities or changes happens in SalesIQ, like a conversation being rated, a tag being created, or a department being updated.
  * **Rules** : For each event, you can define rule conditions using available parameters. For example, for a "conversation.rated" event, you might create a rule that only triggers when the rating is exactly 5 stars.
  * **Actions** : Once an event occurs and its rules are satisfied, an action is triggered. You can choose between:
    * **Webhooks** \- Sends data to external applications via an HTTP request.
    * **Deluge scripts** \- Perform custom logic or third-party integration to perform tasks using Deluge scripts. 



This setup allows you to automate repetitive tasks, trigger real-time integrations with other tools, and implement logic-based workflows that respond instantly to customer activity or internal updates, all without manual effort.

**Workflow types and actions:**

  * Types of Workflows
  * Modules, Events & Rule Parameters
    * Data Workflow
    * Admin Workflow
  * Action Types
    * Webhooks
    * Deluge Scripts



## Types of Workflows

SalesIQ offers two types of workflows: **Admin Workflow** and **Data Workflow**. Each serves a different purpose and supports specific modules. The table below outlines what each type covers:

Workflow Type| Modules Supported| Description  
---|---|---  
**Admin Workflow**| 

  * Operators
  * Departments
  * Brands
  * Tags

| Handles backend or portal-level changes. Use this to trigger actions when configuration settings are added, updated, or deleted.  
**Data Workflow**| 

  * Conversations
  * Visitors
  * Contacts
  * Leads

| Tracks visitor/user and system activity. Use this to automate responses or actions based on customers and their interactions.  
  
**Note:**

  * Each module supports its own set of events, each with specific parameters that can be used to set up rules.
  * For example, if you want to trigger an action when a conversation receives 5 stars, select "**Data Workflow" > "conversation.rated" **event > Set the rule as "**Rating is 5".**
  * Only when this event occurs and the rule matches, the configured action (webhook or Deluge script) will be triggered.



## Modules, Events & Rule Parameters

The modules are categorized based on the workflow types. 

### Data Workflow

**1\. Operator Module**

Event| Rule Parameters  
---|---  
conversation.created| Visitor Email, Chat Department, Country/Region, City, State, Question, Campaign Name, Campaign Content, Campaign Medium, Campaign Source, Current Page URL, Current Page Title, Landing Page URL, Landing Page Title, First Visit Source, Current Visit Source, Previous Page URL, Number of Past Visits, Referrer, Channels, Search Engine, Time of the Day, Day of the Week, Zoho CRM Contact, Deal, Account, Visitor Stage, Visitor Name, Visitor Phone, Brand, Browser, Operating System, Lead Score, IP Address, Number of Past Chats, Language, Timezone  
conversation.attender.updated| All parameters from conversation.created + Attender Name, Attender Email, Attended Time  
conversation.missed| All parameters from conversation.created + Missed By, Missed By Count, Is Abandoned Chat?, Ringing Time  
conversation.completed| All parameters from conversation.attender.updated + Chat Owned By, Chat Ended By, Chat Duration  
conversation.rated| All parameters from conversation.completed + Rating, Feedback  
conversation.visitor.replied| All parameters from conversation.attender.updated + Visitor Message (Text), Visitor Message (Contains Attachment)  
conversation.operator.replied| All parameters from conversation.attender.updated + Operator Message (Text), Operator Message (Contains Attachment)  
conversation.transfer.initiated| All parameters from conversation.attender.updated + Transfer Attempt Count  
conversation.transfer.accepted| All parameters from conversation.transfer.initiated + Accepted By  
conversation.transfer.rejected| All parameters from conversation.transfer.initiated + Rejected By  
conversation.participants.added| All parameters from visitor.replied and operator.replied + Participant Added, Participant Added By  
conversation.participants.deleted| All parameters from visitor.replied and operator.replied + Participant Deleted, Name of the Participant Deleted, Participant Deleted By  
conversation.supervisor.added| All parameters from visitor.replied and operator.replied + Supervisor Added, Name of the Supervisor Added  
conversation.message.edited| All parameters from visitor.replied and operator.replied + Edited By, Current Message  
conversation.message.deleted| All parameters from visitor.replied and operator.replied + Deleted By  
conversation.metrics| All parameters from conversation.created, missed, completed, rated + Conversation Status, Metric, Current Metric Value  
conversation.reopened| All parameters from conversation.created, missed, completed, rated + Reopened By Visitor, Reopened Operator, Time Since Closure, Time Since the Chat Was Closed  
  
**2\. Visitor Module**

Event| Rule Parameters  
---|---  
visitor.updated| Visitor Info: Current Value, Updated By  
  
**3\. Contact Module**

Event| Rule Parameters  
---|---  
contact.tag.action| All parameters from conversation.created, missed, completed, rated + Tag Action, Added Tag, Deleted Tag, Updated By  
  
**4\. Lead Module**

Event| Rule Parameters  
---|---  
lead.tag.action| All parameters from conversation.created, missed, completed, rated + Tag Action, Added Tag, Deleted Tag, Updated By  
  
### Admin Workflow

**1\. Operator Module**

Event| Rule Parameters  
---|---  
operator.created| Operator First Name, Last Name, Known As, Email, Departments, Language, Timezone  
operator.updated| All parameters from operator.created + Operator Status, Is Operator Verified?  
operator.deleted| All parameters from operator.created  
operator.departments.associated| All parameters from operator.created  
operator.departments.dissociated| All parameters from operator.created  
  
**2\. Department Module**

Event| Rule Parameters  
---|---  
department.created| Department Name, Created By, Department Type, Department Email, Associated Operators  
department.updated| All parameters from department.created + Updated By  
department.deleted| All parameters from department.created + Deleted By  
  
**3\. Brands Module**

Event| Rule Parameters  
---|---  
brands.enabled| Brand Name, Enabled By  
brands.disabled| Brand Name, Disabled By  
  
**4\. Tags Module**

Event| Rule Parameters  
---|---  
tag.created| Tag Name, Created By, Tag Module  
tag.updated| Tag Name, Created By, Updated By, Tag Module  
tag.deleted| Created By, Deleted By, Tag Module  
  
## Action Types

Once an event occurs and its rule conditions are met, you can define what happens next, this is an action. In SalesIQ, you can choose from two types of actions: Webhooks and Deluge Scripts. These allow you to integrate with external systems or run custom logic, without manual intervention.

### Webhooks

Webhooks let you send real-time data from SalesIQ to any external application or service when a rule-matched event occurs.

  * Provide a request URL (the endpoint of your external system).
  * When the event is triggered and rules are satisfied, SalesIQ sends a POST request to that URL with a structured payload containing event data (like visitor info, chat rating, operator details, etc.).



**Example use case:** If a chat is rated 1 star, use a webhook to automatically alert your support lead on Cliq/Slack or create a follow-up task in your helpdesk system.

### Deluge Scripts

Deluge is Zoho’s scripting language that allows you to define and run custom logic when a rule-matched event occurs.

  * This script can perform internal actions (e.g., update a CRM field, send an email) or make REST API calls to third-party platforms for more complex integrations.
  * Deluge offers more flexibility and logic handling compared to webhooks, including loops, conditions, and multiple actions.



**Example use case:** If a lead is actively engaging and the tag “Priority Lead” is added in SalesIQ, use a Deluge script to automatically add the tag “Priority” to the corresponding lead in Zoho CRM.