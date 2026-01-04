# Zoho Inventory Article

**Source:** https://www.zoho.com/de-de/inventory/help/integrations/twilio.html
**Crawled:** 2026-01-04

---

# Integrate Zoho Inventory with Twilio

Twilio is a cloud communication platform that allows businesses to communicate via phone calls and SMS using it’s web service APIs. When you integrate Zoho Inventory with Twilio, you can send the in-app notifications to your customers via SMS.

**Benefits**

  * Send SMS notifications to your customers regarding invoices, payments, and payment reminders.
  * Configure SMS notifications at customer and contact person level.



**Prerequisites**

  * An existing Twilio account, if you do not have one, [create a new Twilio account](https://www.twilio.com/login?iss=https%3A%2F%2Flogin.twilio.com%2F).
  * Account SID(Security Identifier) and Auth Token from Twilio.
  * An active phone number that works with Twilio. If you do not have such phone number, you have to [purchase a phone number](https://help.twilio.com/articles/223135367-Twilio-Phone-Number-Types-and-Their-Capabilities) from Twilio.



**Note:** This feature is available only in certain plans of Zoho Inventory. Visit our [pricing page](/inventory/pricing/) to know more about each plan.

## Connect with Twilio

To set up this integration:

  * Go to **Settings**.
  * Select **SMS Notifications** under _Reminders & Notifications_.
  * Click **Configure** near _Twilio_.
  * On the _SMS Integration_ page, click **Connect** next to _Twilio_.
  * In the next page, click **Connect** near _Twilio_.
  * In the pop-up that appears, enter the **Account SID** , **Auth Token** and the **Phone Number** from your Twilio account.
  * Click **Connect with Twilio**.



Twilio is now integrated with your Zoho Inventory organization. You can view the templates for SMS notifications by clicking **Configure** below the integration.

You will be redirected to the SMS Notifications page, where you can configure the SMS templates and also enable or disable the SMS notifications for different notification types.

## Enable or Disable SMS Notifications

All the SMS notifications will be disabled by default. You can enable the required SMS notifications and send SMS to your customers. To enable SMS notifications:

  * Go to **Settings**.
  * Select **SMS Notifications** under _Reminders & Notifications_.
  * Click **Configure** near _Twilio_.
  * In the next page, click **Configure** below the integration.
  * Slide the toggle near the required transaction to enable the SMS notifications.



Similarly, you can slide the toggle to disable the SMS notifications that you’ve enabled.

## Configure SMS Notifications

You can choose a template for the SMS notifications and also configure the message in it.

To configure the SMS templates:

  * Go to **Settings**.
  * Select **SMS Notifications** under _Reminders & Notifications_.
  * Click **Configure** near _Twilio_.
  * In the next page, click **Configure** below the integration.
  * Click **Change Template** near the required SMS Template.
  * In the _Choose a Template_ pop-up, click **Customize Template**.
  * You can select an SMS template and insert placeholders from the respective dropdowns if required.
  * Click **Save**.



## Enable SMS for Primary Contacts

To enable SMS notifications for a primary contact:

  * Go to _Sales_ on the left sidebar and select **Customers**.
  * Click the customer for whom you want to enable SMS Notifications.
  * In the _Overview_ section, click **Enable SMS Notification**.



The SMS Notifications will be enabled for the respective primary contact.

## Enable SMS for Contact Persons

To enable SMS notifications for the contact persons:

  * Go to _Sales_ on the left sidebar and select **Customers**.
  * Click the required customer to enable SMS notifications for their contact persons.
  * Scroll down to the **Contact Persons** section in the _Overview_ tab.
  * Click the _Gear_ icon near the contact person and select **Enable SMS Notification** from the dropdown.



The SMS Notifications will be enabled for the respective contact person.

# Enable SMS Notifications for Customers in Bulk

You can enable SMS notifications for customers and contact persons in bulk in two ways:

  * [All Primary Contact and Contact Persons](/de-de/inventory/help/integrations/twilio.html#all)
  * [Specific Primary Contact and Contact Persons](/de-de/inventory/help/integrations/twilio.html#specific)



### All Primary Contact and Contact Persons

To enable SMS Notifications for all the customers and their contact persons:

  * Go to **Settings**.
  * Select **SMS Notifications** under _Reminders & Notifications_.
  * Click the **Gear** icon in the _Twilio_ section, and select **Update Communication Preference** from the dropdown.
  * In the following pop-up, select the default recipients to whom you want to send the SMS notifications.
  * Click **Save**.



The SMS Notifications will be enabled for all the primary contacts and their contact persons.

### Specific Primary Contact and Contact Persons

To enable SMS Notifications for specific customers and their contact persons:

  * Go to _Sales_ on the left sidebar and select **Customers**.
  * Select the customers for whom you want to disable the SMS Notifications.
  * Click **Configure Communication Preferences** at the top of the page.
  * In the following pop-up, select the default recipients to whom you want to send the SMS notifications.
  * Click **Save**.



The SMS Notifications will be enabled for the selected primary contacts and their contact persons.

## Disable SMS for Primary Contacts

To disable SMS Notification for a primary contact:

  * Go to _Sales_ on the left sidebar and select **Customers**.
  * Click the customer for whom you want to disable SMS Notifications.
  * In the _Overview_ section, click **Disable SMS Notification**.



The SMS Notifications will be disabled for the respective primary contact.

### Disable SMS for Contact Persons

To disable SMS Notifications for the contact persons of a primary contact:

  * Go to _Sales_ on the left sidebar and select **Customers**.
  * Click the customer for whom you want to disable SMS notifications.
  * Scroll down to the **Contact Persons** section in the _Overview_ tab.
  * Click the _Gear_ icon near the contact person and select **Disable SMS Notification** from the dropdown.



SMS Notifications will be disabled for this contact person.

## Disable Notifications in Bulk

To disable SMS Notifications for customers in bulk:

  * Go to _Sales_ on the left sidebar and select **Customers**.
  * Select the customers for whom you want to disable the SMS Notifications.
  * Click **Configure Communication Preferences** at the top of the page.
  * In the pop-up that appears, select **None** from the _Default Recipients_ dropdown.
  * Click **Save**.



When the default recipients for customers are selected as **None** , the SMS notifications will not be sent to any contact persons.

## Send SMS Notifications

Based on your configured SMS preferences, you will be able to send SMS notifications to your customers and their contact persons in the following cases:

  * When you have configured **Create and Send Invoices** , or **Create, Share and Send Invoices** preferences for recurring invoices, an invoice creation message will be sent.
  * When you receive online payments from your customers, a **Payment Thank You SMS** will be sent to that customer.



Apart from sending automated SMS to your customers, you can also send manual messages to them. Here’s how:

  * Go to the left sidebar and select a module (say, **Invoices**).
  * Click the invoice for which you want to send SMS.
  * Click **Send** at the top of the invoice’s _Details_ page and select **Send SMS** from the dropdown.
  * In the pop-up that appears, click **Send SMS**.



The SMS Notification for the invoice will be sent to your customer.

## View sent SMS Notifications

To view the SMS Notifications sent to your customers and their contact persons:

  * Go to the left sidebar and select a module (say, **Invoices**).
  * Click the invoice for which you want to view the sent SMS notifications.
  * Click **Comments and History** in the top right corner of the invoice’s _Details_ page.



You can view the details of the SMS Notifications sent to your customers.

IN THIS PAGE…

  * [Connect With Twilio](/de-de/inventory/help/integrations/twilio.html#connect)
  * [Enable or Disable SMS Notifications](/de-de/inventory/help/integrations/twilio.html#enable-disable)
  * [Configure SMS Notifications](/de-de/inventory/help/integrations/twilio.html#configure)
  * [Enable SMS for Primary Contacts](/de-de/inventory/help/integrations/twilio.html#enable)
  * [Enable SMS for Contact Persons](/de-de/inventory/help/integrations/twilio.html#enable-cp)
  * [Enable SMS Notifications for Customers in Bulk](/de-de/inventory/help/integrations/twilio.html#bulk-enable)
    * [All Primary Contact and Contact Persons](/de-de/inventory/help/integrations/twilio.html#all)
    * [Specific Primary Contact and Contact Persons](/de-de/inventory/help/integrations/twilio.html#specific)
  * [Disable SMS for Primary Contacts](/de-de/inventory/help/integrations/twilio.html#disable)
  * [Disable SMS for Contact Persons](/de-de/inventory/help/integrations/twilio.html#disable-cp)
  * [Disable Notifications in Bulk](/de-de/inventory/help/integrations/twilio.html#bulk-disable)
  * [Send SMS Notifications](/de-de/inventory/help/integrations/twilio.html#send)
  * [View sent SMS Notifications](/de-de/inventory/help/integrations/twilio.html#view)



[ Join the Community Forum](https://help.zoho.com/portal/en/community/zoho-inventory)