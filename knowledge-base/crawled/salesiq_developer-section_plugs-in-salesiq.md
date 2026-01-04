# Zoho Salesiq Article

**Source:** https://www.zoho.com/salesiq/help/developer-section/plugs-in-salesiq.html
**Crawled:** 2026-01-04

---

## What are Plugs?

Plugs are exclusive to the Codeless bot builder. Generally, the Codeless bot builder offers many functions/actions as blocks to build your bot. However, if you want other actions that are not present in the block gallery, such as OTP verification or external third-party integration, or the user's own logic, they can be achieved via Plugs. 

Plugs help to create any customized action and add it as a block on the codeless bot builder like the other blocks to use in the bot's flow.

## What can Plugs do?

  * Plugs perform the actions/functions with inputs from the codeless bot builder and provide outputs to the codeless bot. For example, visitor data like name, email, date & time, etc., can be set as the plug's input. That data can be pushed to any third-party services to s,c, schedule an appointment/booking, and the data from the third-party service can be given as the plug's output (booking ID, etc.). 
  * With plugs, you can save yourself from the trouble of writing or building logic more than once. These plugs can be created once and used in multiple places in the bot.
  * Plugs are implemented using the Deluge scripts or webhooks. 



## Platforms to build Plugs

​Currently, SalesIQ supports two platforms to build your Plugs. 

**SalesIQ Scripts**

SalesIQ Scripts is a platform that uses Deluge or Data Enriched Language for Universal Grid Environment as its online scripting language. Deluge is deemed to be robust and easy to use because of its user-friendly syntax. The deluge script builder offers a drag-drop user interface, thus leaving out the task of remembering deluge syntax and functions for the user. Furthermore, deluge offers a connection interface to make third-party integration easy. 

**Webhooks**

​Webhooks are an easy way to implement event reactions. Webhooks provide a mechanism whereby a server-side application can notify a client-side application when a new event (that the client-side application might be interested in) has occurred on the server. ​When you have actions in an external service, you can hook them up using webhooks. 

​