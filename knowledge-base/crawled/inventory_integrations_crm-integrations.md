# Zoho Inventory Article

**Source:** https://www.zoho.com/de-de/inventory/help/integrations/crm-integrations.html
**Crawled:** 2026-01-04

---

# Integrate Zoho Inventory with Zoho CRM

When you integrate Zoho Inventory with Zoho CRM, you can view and manage customer and order management information in one place. This integration improves collaboration between sales and inventory teams in your business, allowing them to track deals, create sales orders, and invoices without switching between applications.

**Prerequisites:**

  * Must have an active Zoho CRM account.
  * Must have a live Zoho Inventory organization.
  * Your CRM account should not be integrated to another Zoho Inventory or Zoho Inventory organization. If that is the case, then you need to disable that integration before you start integrating with your current organization.



## Benefits of the Integration

  * Capture all customer information in one place, so you can work on the same information at hand in both the apps.
  * View customer’s key accounting metrics like sales information and outstanding receivables directly from Zoho CRM.
  * Sync transactions between both apps.
  * Automate workflows, like creating an invoice when a deal is won.



* * *

## Set up the Integration

**Prerequisites:**

  * You can integrate with a Zoho CRM organization only if it’s in the **Professional** plan or higher.
  * If multi-currency is enabled in Zoho CRM, ensure that the base currency in Zoho CRM matches the one set in Zoho Inventory.



**Insight:** When you integrate, the following data from Zoho Inventory will be shared with Zoho CRM:

  * Your organization name, email address, and your country.
  * All your users’ details.



To set up the CRM integration from Zoho Inventory:

  * Go to **Settings** on the top right corner of the page.

  * Select **Zoho Apps** under _Integrations & Marketplace_.

  * In the _Zoho Apps_ page, click **Connect** next to _Zoho CRM_.

  * In the _Connect to Zoho CRM_ page, click **Select Organization** in the _Zoho CRM Organization_ section.

  * In the _Connect Zoho CRM_ pop-up, select the required **Organization** , and click **Save**.




A two-way sync will be set up, which means that data will be fetched from Zoho CRM into Zoho Inventory and vice-versa.

**Note:** If you want to integrate multiple Zoho Inventory organizations with a Zoho CRM organization, email us at [support@zohoinventory.com](mailto:support@zohoinventory.com), and we’ll assist you with the set up. However, this will be a one-way sync, which means that data will be fetched only from Zoho CRM into Zoho Inventory and transaction modules will not be synced during this process.

* * *

## Configure the Modules to be Synced

Once you set up the integration, you can configure the modules to sync between Zoho Inventory and Zoho CRM. To do this:

  * Go to **Settings**.
  * Select **Zoho Apps** under _Integrations & Marketplace_.
  * In the _Zoho Apps_ page, click **Show Details** next to _Zoho CRM_.
  * In the _Configure Module to be Synced_ section, click **Configure Now** next to the required module you want to sync from Zoho CRM into Zoho Inventory.



You can sync data for the following modules from Zoho CRM into Zoho Inventory:

  * [Customers](/de-de/inventory/help/integrations/crm-integrations.html#customers)
  * [Vendors](/de-de/inventory/help/integrations/crm-integrations.html#vendors)
  * [Items](/de-de/inventory/help/integrations/crm-integrations.html#items)



### Sync Customers

To sync customer data from Zoho CRM into Zoho Inventory:

  * Go to **Settings**.

  * Select **Zoho Apps** under _Integrations & Marketplace_.

  * In the _Zoho Apps_ page, click **Show Details** next to _Zoho CRM_.

  * In the _Configure Module to be Synced_ section, click **Configure Now** next to _Customers_.

  * In the next page, configure the following preferences:

    * **Select Module in Zoho CRM:** Select the module you want to sync between Zoho CRM and Zoho Inventory.

      * **Accounts:** The **Accounts** in Zoho CRM will be fetched as **Customers** in Zoho Inventory with the _Customer Type_ set as **Business**.
      * **Contacts:** The **Contacts** in Zoho CRM will be fetched as **Customers** in Zoho Inventory with the _Customer Type_ set as **Individual**.
      * **Accounts & their Contacts:** The **Accounts** and associated **Contacts** in Zoho CRM will be fetched as **Customers** and **Contact Persons** in Zoho Inventory. Check **Include contacts that are not associated to any accounts in Zoho CRM** to sync contacts that are not associated with an account in Zoho CRM. These contacts will be fetched as **Customers** in Zoho Inventory with the _Customer Type_ set as **Individual**.
    * **Select the extent of sync:** Choose how you want to sync records between both the apps.

      * **Fetch from CRM:** The records in Zoho CRM will only be fetched into Zoho Inventory. No Zoho Inventory records will be fetched into Zoho CRM. However, any records already pushed to Zoho CRM will remain unaffected.
      * **Sync both ways:** The records will be synced from Zoho CRM to Zoho Inventory and vice-versa, in which Zoho CRM records will be fetched first.



**Insight:** If you choose two-way sync, a **Customer** with _Customer Type_ set as **Business** in Zoho Inventory will sync with the **Accounts** module in Zoho CRM, and a **Customer** with _Customer Type_ set as **Individual** in Zoho Inventory will sync with the **Contacts** module in Zoho CRM.

  * **Choose how to handle duplicate customers:** When you sync records between Zoho CRM and Zoho Inventory, there might be a record in Zoho CRM that is already present in Zoho Inventory. To resolve this, duplicate records are identified by comparing **Account Name** in Zoho CRM and **Customer Display Name** in Zoho Inventory. Choose how you want to handle duplicate records during the sync:

    * **Clone:** The duplicate record will be cloned, and will be available along with the existing record.
    * **Overwrite:** The duplicate record will replace the existing record in Zoho Inventory.
    * **Skip:** The duplicate record will not be synced, and the existing record will remain unchanged.
  * **Select the view to be synced:** To sync specific records from Zoho CRM, you can create a view and sync that view into Zoho Inventory. If you choose to sync **Accounts & their Contacts**, you can select both the **Account** view and the **Contact** view to sync records.




  * **Map Fields** : Match the fields in Zoho Inventory with the corresponding fields in Zoho CRM. Some fields are mapped automatically, while you must map the remaining fields manually. If certain fields from Zoho CRM can’t be mapped to the default Zoho Inventory fields, [create custom fields](/de-de/inventory/help/settings/preferences.html#custom-fields) in Zoho Inventory. These fields will appear during the mapping process.



**Prerequisite:** If you’ve enabled multi-currency in Zoho CRM, ensure that the base currency in Zoho CRM matches the base currency in Zoho Inventory before mapping the fields.

  * Click **Save and Sync** to start the sync process, or click **Save and Sync Later** if you want to save the preferences now and sync the records later.



The customers will be synced in a while, based on chosen preferences. To check the status of the sync, click **Check Status** under the _Customers_ section.

### Sync Vendors

You can sync vendors into Zoho Inventory similar to how you’ve synced your customers.

  * **Select the extent of sync:** Choose whether you want to sync vendors only from Zoho CRM into Zoho Inventory or both ways.
  * **Choose how to handle duplicate vendors:** Choose whether you want to clone, overwrite, or skip duplicate records during the sync.
  * **Select the view to be synced:** To sync specific vendors, select the view in Zoho CRM you want to sync with Zoho Inventory.
  * **Map Fields:** Match the fields in Zoho Inventory with the corresponding fields in Zoho CRM. You can also [create custom fields](/de-de/inventory/help/settings/preferences.html#custom-fields) in Zoho Inventory to match the fields in Zoho CRM, if required.



Once done, click **Save and Sync** to start the sync process, or click **Save and Sync Later** if you want to save the preferences now and sync the records later.

The vendors will be synced in a while, based on chosen preferences. To check the status of the sync, click **Check Status** under the _Vendors_ section.

### Sync Items

You can sync the **Items** in Zoho Inventory with the **Products** in Zoho CRM, similar to customers and vendors. To sync items:

  * Go to **Settings**.

  * Select **Zoho Apps** under _Integrations & Marketplace_.

  * In the _Zoho Apps_ page, click **Show Details** next to _Zoho CRM_.

  * In the _Configure Module to be Synced_ section, click **Configure Now** next to _Items_.

  * In the next page, configure the following preferences:

    * **Select the extent of sync:** Choose how information flows between the two apps.
      * **Fetch from CRM:** The products in Zoho CRM will only be fetched as Items into Zoho Inventory. No Zoho Inventory records will be fetched into Zoho CRM. However, any records already pushed to Zoho CRM will remain unaffected.
      * **Sync both ways:** The Items from Zoho Inventory will be synced as Products into Zoho CRM, and vice-versa, in which records from Zoho Inventory will be fetched first.
    * **Choose how to handle duplicate items:** When you sync data between Zoho CRM and Zoho Inventory, there might be a record in Zoho CRM that is already present in Zoho Inventory. To resolve this, duplicate records are identified by comparing **Product Name** in Zoho CRM and **Item Name** in Zoho Inventory, and the product’s **SKU** in both the apps. Choose how you want to handle duplicate records during the sync.

      * **Clone:** The duplicate record will be cloned, and will be available along with the existing record.
      * **Overwrite:** The duplicate record will replace the existing record in Zoho Inventory.
      * **Skip:** The duplicate record will not be synced, and the existing record will remain unchanged.



**Insight:** If you selected **Sync both ways** in the previous step, Zoho Inventory items will be pushed to Zoho CRM first, which may result in duplicate records in Zoho CRM. For one-way sync, duplicate records will appear in Zoho Inventory.

  * **Select the view to be synced:** To sync specific records from Zoho CRM into Zoho Inventory, you can create a view in Zoho CRM, add products, and sync the view. During the sync, click the **click here to select a view** option and select the required view in the Select a view dropdown.



  * **Map Fields:** Match the fields in Zoho Inventory with the corresponding fields in Zoho CRM. You can also [create custom fields](/de-de/inventory/help/settings/preferences.html#custom-fields) in Zoho Inventory to match the fields in Zoho CRM, if required.



**Insight:** If you want to classify the products in Zoho CRM as goods or services, create a custom field with **Goods** and **Services**. Then, map this custom field for the _Product Type_ field in Zoho Inventory.

  * Click **Save and Sync** to start the sync process, or click **Save and Sync Later** if you want to save the preferences now and sync the records later.



The items will be synced in a while, based on chosen preferences. To check the status of the sync, click **Check Status** under the _Items_ section.

## Sync Transaction Modules

Once you’ve synced customers, vendors, and items, you can sync transaction modules between Zoho Inventory and Zoho CRM. With this, **Invoices** , **Sales Orders** , and **Purchase Orders** in Zoho Inventory can be accessed from Zoho CRM. Here’s how:

  * Go to **Settings**.

  * Select **Zoho Apps** under _Integrations & Marketplace_.

  * In the _Zoho Apps_ page, click **Show Details** next to _Zoho CRM_.

  * In the _Sync Transaction Modules_ section, click **Enable**.




Now, you can access these modules in the **Zoho Finance** module of Zoho CRM. Only the transactions created in this module in Zoho CRM will be synced to Zoho Inventory.

**Insight:** If you’ve created any custom fields for these transactions in Zoho Inventory, they’ll also appear in Zoho CRM.

### Manage Users and Roles

**Prerequisite:** This section will be enabled only if you’ve synced all the transaction modules.

Once you’ve synced the transaction modules, you can grant permissions to Zoho CRM users to create quotes and sales orders, as well as view invoices and purchase orders in the Zoho Inventory section of Zoho CRM. To do this:

  * Go to **Settings**.
  * Select **Zoho Apps** under _Integrations & Marketplace_.
  * In the _Zoho Apps_ page, click **Show Details** next to _Zoho CRM_.
  * In the _Manage Users and Roles_ section, click **Manage Users**.
  * In the _Manage Users from Zoho CRM_ pop-up, select the users and roles you want to grant permissions, and click **Save**.



## Automate Based on Deal/Potential’s Stage

While setting up the integration, you can configure triggers to automate tasks in Zoho Inventory based on the deal or potential’s stage in Zoho CRM. For example, you can set up a trigger to automatically create a quote in Zoho Inventory whenever a potential is created in Zoho CRM.

**Prerequisite:** While syncing customers from Zoho CRM into Zoho Inventory, if you chose to sync **Accounts & their Contacts**, the deal in Zoho CRM must be associated with an account for the trigger to be automated. If you choose to sync **Contacts** , the deal must be associated with a contact.

To set up the triggers:

  * Go to **Settings**.

  * Select **Zoho Apps** under _Integrations & Marketplace_.

  * In the _Zoho Apps_ page, click **Show Details** next to _Zoho CRM_.

  * In the _Automate Based on Deal/Potential’s Stage_ section, click **Change Preference**.

  * In the pop-up that appears, select the required preference, and click **Save**.




The trigger will be set up. To view the status of this trigger:

  * Go to **Reports** on the left sidebar.
  * Select **Activity Logs & Audit Trail** under _Activity_.



The report for the workflows executed during the integration will be displayed.

### Invoices

You can also automate invoice creation in Zoho Inventory based on the deal’s stage in Zoho CRM. When enabled, an invoice will be created in Zoho Inventory when a deal is won in Zoho CRM, and the corresponding invoice will be voided when the deal is lost.

When setting up a trigger, the invoice or quote created in Zoho Inventory will contain the following details from Zoho CRM:

**Fields in Zoho Inventory**| **Fields in Zoho CRM**  
---|---  
Customer Name| Account’s or Contact’s Name  
Customer Address| Account’s or Contact’s Address  
Sales Person| Deal Owner  
Item Name| Deal Name  
Item Description| Deal Description  
Item Rate| Deal Amount  
  
The created invoice or quote will also be available under the Zoho Finance module of the corresponding deal in Zoho CRM.

**Insight:** A deal being won or lost in Zoho CRM depends on the deal’s stage-probability mapping. For example, let’s assume that a trigger is set up to create invoices automatically. Now, if the deal’s stage is marked as closed won in Zoho CRM, the probability changes to 100 and an invoice is created in Zoho Inventory. If the deal is then edited to change the stage to closed lost, the probability changes to 0 and the invoice is voided in Zoho Inventory.

**Warning:** Once an invoice is marked as **Sent** in Zoho Inventory, any changes made to the potential in Zoho CRM will no longer trigger any actions for the invoice.

## Sync Options

Once you’ve configured the integration, any new account, contact, vendor, or product you add in Zoho CRM will sync into Zoho Inventory every two hours after the initial sync. If you choose to sync transaction modules, they will sync instantly. To do this:

  * Go to **Settings**.
  * Select **Zoho Apps** under _Integrations & Marketplace_.
  * In the _Zoho Apps_ page, click **Show Details** next to _Zoho CRM_.
  * In the _Configure Module to be Synced_ section, select the preferred sync option. They include:
    * **Instant Sync:** If you’ve added new records and want to update them immediately in the other app, click **Instant Sync**.



**Insight:** To update changes for a specific customer or vendor synced from Zoho CRM instead of a full sync, select the required customer or vendor in Zoho Inventory, click the _More_ dropdown in the _Details_ page, and select **Re-sync Contact from Zoho CRM**.

  * **Show Sync History:** You can view a detailed sync history, including the number of records added, updated, or deleted, along with the date and time of sync in Zoho Inventory. It also displays if a sync has failed, along with the failure reason.
  * **Pause/Resume Sync:** If you want to temporarily stop syncing records between Zoho Inventory and Zoho CRM, click **Pause Sync**. To start syncing records between the apps again, click **Resume Sync**.
  * **Edit:** You can modify the sync preferences, if required. The updated preferences will apply to the next automatic or manual sync.



**Note:** If you have created a record in Zoho Inventory, synced it to Zoho CRM, and then deleted the record in Zoho CRM, the respective record will not be deleted in Zoho Inventory.

## Working With the Integration in Zoho Inventory

Once you set up the integration, you can perform the following actions in Zoho Inventory:

  * [Access Zoho CRM Customers and Vendors](/de-de/inventory/help/integrations/crm-integrations.html#access)
  * [Associate Potentials with Transactions](/de-de/inventory/help/integrations/crm-integrations.html#associate-potential)



### Access Zoho CRM Customers and Vendors

Depending on how you choose to sync records, the accounts, contacts, and vendors from Zoho CRM will be available as **Customers** and **Vendors** in Zoho Inventory.

#### Filter by CRM Customers and Vendors

You can view all the accounts and contacts synced from Zoho CRM into Zoho Inventory as **Customers**. Here’s how:

  * Go to _Sales_ on the left sidebar and select **Customers**.
  * Click the _All Customers_ filter at the top of the page and select **CRM Customers** from the dropdown.



The respective CRM accounts and contacts will be displayed. Similarly, you can filter the CRM vendors in the **Vendors** module.

#### Search CRM Customers and Vendors

The customers and vendors fetched from Zoho CRM will be available in Zoho Inventory, and you can create transactions for them. However, you can also create transactions for customers and vendors not yet imported. Here’s how:

  * Select a transaction you want to create (for example, **Invoices**).
  * Click **\+ New** in the top right corner of the page.
  * In the _New Invoice_ page, click the **Advanced Customer Search** icon in the _Customer Name_ field.
  * In the _Advanced Customer Search_ pop-up, the list of customers from Zoho Inventory and Zoho CRM will be displayed. Select **Zoho CRM** at the top of the pop-up.
  * Enter the **Account Name** and click **Search**.



A list of contacts and accounts associated with the entered account name will be displayed. Select the required contact or account from the list.

Once done, the selected account or contact will be fetched as a customer in Zoho Inventory. Now, you can create sales transactions for them.

**Insight:** If you want to search contacts, the available _Search Criteria_ are **First Name** and **Last Name**. If you want to search for accounts, enter the account name from Zoho CRM. The contacts associated with the respective account will be displayed.

Similarly, you can create purchase transactions for vendors that haven’t been fetched from Zoho CRM yet.

### Associate Potentials With Transactions

**Prerequisites:**

  * Ensure that the Zoho Finance modules (**Invoices**) is enabled in your Zoho CRM account.
  * Verify that the deal is associated with the correct account or customer in Zoho CRM.



Once you integrate Zoho Inventory with Zoho CRM, you can associate potentials in Zoho CRM with quotes, sales orders, invoices, and expenses in Zoho Inventory.

To associate a potential with an invoice:

  * Go to _Sales_ on the left sidebar and select **Invoices**.
  * Click **\+ New** in the top right corner of the page.
    * If you want to associate a potential with an existing invoice, select the required invoice, and click **Edit** at the top of the customer’s _Details_ page.
  * In the next page, click the **Associate Potential** field.
  * In the _Potentials_ pop-up, select the required potential you wish to associate with the transaction.



The potential will be associated with the respective invoice, and you can create and record it in Zoho Inventory. e

**Pro Tip:** To view this transaction in your Zoho CRM account, select the potential and scroll down to the _Zoho Finance_ section.

**Insight:** If there are multiple potentials associated with a customer or if you can’t find the required potential, you can search for them. However, deleted potentials in Zoho CRM will not appear in the search results.

### Dissociate Potentials

To dissociate a potential:

  * Go to the respective transaction, and click **Edit** at the top of the transaction’s _Details_ page.
  * In the next page, remove the potential from the _Associate Potential_ field.



The potential will be dissociated.

**Warning:** Potentials that were associated using triggers cannot be dissociated.

## Disable Integration

If you do not want to sync records between Zoho Inventory and Zoho CRM, you can disable it temporarily.

**Warning:** If you’ve enabled syncing of transaction modules, disabling the integration will delete any custom reports, comments, and attachments associated with transactions in the **Zoho Finance** module of Zoho CRM. However, your existing transactions in Zoho Inventory will remain unaffected.

To disable the integration:

  * Go to **Settings**.
  * Select **Zoho Apps** under _Integrations & Marketplace_.
  * In the _Zoho Apps_ page, click **Show Details** next to _Zoho CRM_.
  * Click **Disable Integration** in the _Zoho CRM Organization_ section.
  * In the pop-up that appears, click **Confirm**.



The integration between Zoho CRM and Zoho Inventory will be temporarily disabled. To re-enable the integration:

  * Go to **Settings**.
  * Select **Zoho Apps** under _Integrations & Marketplace_.
  * In the _Zoho Apps_ page, click **Show Details** next to _Zoho CRM_.
  * Click **Enable Integration** in the _Zoho CRM Organization_ section.
  * In the pop-up that appears, click **Confirm**.
  * In the _Connect Zoho CRM_ pop-up, check the **Organization** you want to sync, and click **Save**.



The integration will be enabled again, and data will be synced from Zoho CRM into Zoho Inventory.

## Delete Integration

If you’ve disabled the integration between Zoho Inventory and Zoho CRM and no longer want to sync records, you can delete the integration. Once deleted, the mapping between the records will be permanently removed. This action cannot be undone. If you’ve integrated your Zoho Inventory organization with other Zoho Finance apps, the integration will be removed from those apps as well.

**Prerequisite:** You can delete the integration only if it is disabled.

To delete the integration:

  * Go to **Settings**.
  * Select **Zoho Apps** under _Integrations and Marketplace_.
  * Click **Show Details** next to _Zoho CRM_.
  * Click **Delete Integration** in the _Zoho CRM Organization_ section.
  * In the pop-up, select if you want to convert all synced Zoho CRM records to Zoho Inventory records, or convert only the records with transactions and delete the remaining records.
  * Click **Delete** to confirm.



The integration will be deleted. You’ll also receive an in-app notification when the deletion is complete.

##### ON THIS PAGE

  * [Set up the Integration](/de-de/inventory/help/integrations/crm-integrations.html#set-up)
  * [Configure the Modules to be Synced](/de-de/inventory/help/integrations/crm-integrations.html#configure)
  * [Sync Customers](/de-de/inventory/help/integrations/crm-integrations.html#customers)
  * [Sync Vendors](/de-de/inventory/help/integrations/crm-integrations.html#vendors)
  * [Sync Items](/de-de/inventory/help/integrations/crm-integrations.html#items)
  * [Sync Transaction Modules](/de-de/inventory/help/integrations/crm-integrations.html#transaction-modules)
    * [Manage Users and Roles](/de-de/inventory/help/integrations/crm-integrations.html#manage-user-role)
  * [Automate Based on the Potential’s Stage](/de-de/inventory/help/integrations/crm-integrations.html#automate)
  * [Sync Options](/de-de/inventory/help/integrations/crm-integrations.html#sync)
  * [Working with the Integration in Zoho Inventory](/de-de/inventory/help/integrations/crm-integrations.html#inventory-int)
    * [Access Zoho CRM Contacts](/de-de/inventory/help/integrations/crm-integrations.html#access)
    * [Associate Potentials With Transactions](/de-de/inventory/help/integrations/crm-integrations.html#associate)
    * [Dissociate a Potential](/de-de/inventory/help/integrations/crm-integrations.html#dissociate)
  * [Working with the Integration in Zoho CRM](/de-de/inventory/help/integrations/crm-inventory-integration.html)
  * [Disable Integration](/de-de/inventory/help/integrations/crm-integrations.html#disable)
  * [Delete Integration](/de-de/inventory/help/integrations/crm-integrations.html#delete)



[ Join the Community Forum](https://help.zoho.com/portal/en/community/zoho-inventory)