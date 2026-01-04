# Zoho Inventory Article

**Source:** https://www.zoho.com/de-de/inventory/help/items/items-overview.html
**Crawled:** 2026-01-04

---

# Items

Items are either goods that you purchase from your vendors and sell to your customers, or, services that you provide for which you get paid. In Zoho Inventory, you can add these items with ease and manage their inventory such that, every time you create a purchase request to your vendor, its stock increases and when you sell the items, its stock decreases automatically.

The upcoming sections will guide you in detail on the various ways in which you can add your items and manage them in Zoho Inventory.

* * *

### Create New Item

To create a new item in Zoho Inventory:

  1. Go to the **Items** module under _Items_ from the left sidebar.

  2. Click the **New Item** button or the **\+ New** button on the top.




You can also create an item from a transaction on the fly. Here’s how:

  1. Open a new sales or purchase transaction.

  2. Go to the **Item Details** section and click the empty space under it.

  3. Click the **\+ Add New Item** option from the dropdown.




In the New Item page, fill in the following details:

  * [Add Primary Details](/de-de/inventory/help/items/items-overview.html#primary-details)
  * [Add Sales & Purchase Details](/de-de/inventory/help/items/items-overview.html#sales-purchase-info)
  * [Add Inventory Tracking Details](/de-de/inventory/help/items/items-overview.html#inventory-info)



#### Primary details

  1. Choose whether your item should be classified under **Goods** or **Service**.

**Pro Tip:** Service items can be used for adding packing costs, labor costs and other services. These items will not be displayed in while creating packages and shipments. You cannot track inventory for these items.

  2. Enter the **Name** of the item.

  3. Record the **SKU** (Stock Keeping Unit) for the item.

**Insight:** The SKU field will serve as one of the unique identifiers for an item. Here, you can store your item’s barcode information, so that you can scan and retrieve the item while creating transactions.

  4. Choose from or enter a unit of measurement (**E.g.** Kgs, Pieces, Liters etc.) for the item in the **Unit** field.

  5. Choose a category or add a new category for your item. Learn more about [item categories](/de-de/inventory/help/items/item-categories.html) in Zoho Inventory.

  6. Click the **Returnable Item** checkbox if you accept sales returns for this item. [Sales returns](/de-de/inventory/help/sales-returns/sales-returns-overview.html) can be created only for those items you qualify as returnable.

  7. Upload different images of your item. You can upload up to fifteen images for an item.(**File format:** .gif, .png, ,jpeg, .jpg, .bmp; **Max File Size:** 5 MB each). Choose one picture as the primary image.

  8. Record the dimensions of the item. This will be helpful if you want to calculate the [package geometry](/de-de/inventory/help/sales-orders/package-geometry.html) for an order.

  9. If applicable, you can record other product codes associated with the item in the **UPC** , **EAN** , **MPN** and **ISBN** fields.

**Insight:** The UPC and EAN fields are numeric fields. The MPN and ISBN are alphanumeric fields that support alphabets, numbers, spaces and even hyphens.




#### Sales & Purchase Details

  1. Enter the **Selling Price** and **Purchase Price** for the item.

  2. Associate a sales account (The default account will be _Sales_) and a purchase account (The default account will be _Cost of Goods Sold_).

**Pro Tip:** You can also add a new account under _‘Cost of Goods Sold’_ by clicking the **\+ New Account** option from the **Account** dropdown. You can then associate the new account to the item to keep track of the purchases.

  3. Add a brief sales and purchase description for your item which will be displayed on all the respective transactions.

  4. Choose a tax preference for your item.




#### Inventory Tracking Details

  1. Select the **Track Bin Location for this item** option if you wish to track the bin locations for this item. You cannot disable this option once you have recorded transactions for this item.



**Insight:** If you do not want to keep stock for this item, disable this item and create a non-inventory tracked item.

  2. If you have enabled Advanced Inventory Tracking in Settings for your organisation, choose whether you want to track your items by serial numbers or by batch. If you want neither, choose **None** and proceed.

  3. Select an account to track the inventory for your items.

  4. Select an Inventory Valuation Method:

     * **FIFO (First In, First Out):** In this method, the inventory gets tracked based on the First In, First Out system, which lets you assess the value of your inventory. This simply means the oldest inventory items recorded are sold first. Learn more about [FIFO](/inventory/kb/reports/inventory-fifo-report.html).
     * **WAC (Weighted Average Costing):** In this method, the average cost of all the inventory items will be calculated. The average cost is then used to determine the Cost of Goods Sold (COGS) and the value of your remaining inventory. Learn more about [WAC](/inventory/kb/items/inventory-wac-report.html).



**Insight:** Weighted Average Costing (WAC) is recalculated whenever new stock is added to your inventory.

  5. Select the Reorder Point. A notification will be sent out to you, which will help you keep tabs on the stock levels of your items so you never run out of stock.
  6. Enter the **Opening Stock** (if any) and **Opening Stock Value** , which is the average purchase price of the item. If you have enabled multi-warehouse, enter the Opening Stock and Opening Stock Value for each warehouse.



* * *

### Advance Inventory Tracking

Zoho Inventory provides two advance features to track your stock flow accurately. But first, make sure to enable Advance Inventory Tracking in your item preferences and check the **Track Inventory** option in the New Item page to access the advanced inventory tracking options for your item.

  * [Serial Number Tracking](/de-de/inventory/help/items/items-overview.html#track-serial-numbers)
  * [Batch Number Tracking](/de-de/inventory/help/items/items-overview.html#track-batch-numbers)



**Insight:**

  * Your current subscription plan in Zoho Inventory must allow you to access the advanced inventory tracking features.
  * Each item can be tracked either by serial numbers or by batch numbers, but not both.



#### Track Serial Numbers

To track your item by serial numbers:

  1. Open the new item page and fill in the [necessary details](/de-de/inventory/help/items/items-overview.html#primary-details).

  2. Choose the **Track Serial Number** option under **Advanced Inventory Tracking**.

  3. If you’ve entered an opening stock, you can add serial numbers for the given opening stock in the field below.

  4. If you have enabled multi-warehouse in your organization, click the ellipsis icon at the end of each warehouse row and click **Add Serial Numbers**.

  5. Enter the serial number for the opening stock given in each warehouse.

**Insight:**

     * You can enter up to 200 serial numbers for an opening stock.
     * You can either enter the serial numbers manually or scan the barcode of the item.

  6. Click **Save**. The serial numbers will now be available for your sales transactions. You can also choose to save the item and enter the serial numbers at a later point while creating a bill.




**Pro Tip:** You can also [add serial numbers to composite items](/de-de/inventory/help/items/composite-items.html#serialized-composite-item).

* * *

#### Track Batch Numbers

  1. Open the new item page and fill in the [necessary details](/de-de/inventory/help/items/items-overview.html#primary-details).

  2. Choose **Track Batches** under **Advanced Inventory Tracking**.

  3. If you’ve entered an opening stock, you can add batch details for the given opening stock in the fields below.

  4. If you have enabled multi-warehouse in your organization, click the ellipsis icon at the end of each warehouse row and click **Add Batches**.

  5. Enter the batch details for the opening stock given in each warehouse.

**Insight:** You can enter up to 100 batch numbers for an opening stock.


Field Name| Description  
---|---  
**Batch Reference#**|  A unique number which will serve as a reference for you to save and track your batches in Zoho Inventory. This is **not** the manufacturer batch number.  
**Manufacturer Batch#**|  Batch number provided by your manufacturer.  
**Manufactured Date**|  The date on which the item was manufactured.  
**Expiry Date**|  The date until which the item is consumable.  
**Quantity in**|  Quantity of the item that you wish to add in each batch.  
  
**Insight:** You can enter decimal quantity (up to 6 decimal places) for batches. For instance, a certain quantity of milk has to be divided into batches. In Zoho Inventory, you will be able to add 1.91L in batch 1 and 3.560L in batch 2 and so on.

  * You’ll also be able to enter batch numbers for items while recording a new bill.



* * *

### Import Items

To import items into your Zoho Inventory account:

  1. Go to the **Items** module under _Items_ from the left sidebar.

  2. Click on the  icon.

  3. Select the **Import Items** option.

  4. Click **Upload File** to browse and select the file to upload from your device.

  5. To update the details of all your items at one go, you can choose the **overwrite** option while importing. [Learn how.](/inventory/kb/items/item-overwrite.html)

  6. Choose the character encoding involved from the dropdown. By default, the character encoding is **UTF-8(Unicode)**.

  7. Choose the **File Delimiter**(comma or semicolon). By default it will be comma for a .csv type file.

  8. Click **Next** to proceed to mapping the fields.

  9. To overwrite duplicate records, you must choose a unique field (Item Name, Item ID or SKU) which will be mapped with the equivalent field from the import file. If the values match, then its corresponding records will be overwritten with the data in the import file. For example, if you want to update item names, you can choose Item ID or SKU as the unique field. If the SKU/Item ID that you’re trying to import exists, then its corresponding item name and other details will get updated.

  10. Zoho Inventory finds similar fields and maps them automatically. You can make changes, if needed.

  11. Check the box near the **Save these selections for use during future imports** option to automate mapping for future imports.

  12. Click **Next** to proceed to the Preview window.

  13. View a summary of the number of invoices ready for import, number of skipped records and unmapped fields will be shown.

  14. Click **Previous** to make any changes. If everything is ready, click **Import**.




* * *

### Import Items from Zoho Books

Zoho Books is an in-house accounting platform that is built to seamlessly integrate with Zoho Inventory. This means that all your customer information, item information, transactions etc., entered in one of these platforms will automatically be available in the other, thus, preventing double entry.

If you already have an organization in Zoho Books, learn how you can [integrate it](/de-de/inventory/help/getting-started/sign-up.html#join-with-existing-zoho-account) with Zoho Inventory.

* * *

### Import Products from Zoho CRM

You can pull the items into Zoho Inventory from Zoho CRM. Learn more about:

  * [Integrating Zoho Inventory with Zoho CRM](/de-de/inventory/help/integrations/crm-integrations.html).
  * [Configuring your product sync](/de-de/inventory/help/integrations/crm-integrations.html#products).
  * [Triggering an instant sync](/de-de/inventory/help/integrations/crm-integrations.html#instant-sync) between Zoho Inventory and Zoho CRM.



**Pro Tip:** The items synced from Zoho CRM will only have sales information. To enable inventory tracking for these items, you must first [edit](/de-de/inventory/help/items/items-overview.html#edit-item) them and enable purchase information.

* * *

Curate your own kits and sell them in special prices with [item grouping](/inventory/item-grouping-bundling/?utm_source=HelpDocRedirection&utm_medium=Website)

## IN THIS PAGE…

  * [Create New Item](/de-de/inventory/help/items/items-overview.html#create-item)
  * [Advanced Inventory Tracking](/de-de/inventory/help/items/items-overview.html#advanced-inventory-tracking)
    * [Track Serial Numbers](/de-de/inventory/help/items/items-overview.html#track-serial-numbers)
    * [Track Batch Numbers](/de-de/inventory/help/items/items-overview.html#track-batch-numbers)
  * [Import Items from Other System](/de-de/inventory/help/items/items-overview.html#import-items)
  * [Import Items from Zoho Books](/de-de/inventory/help/items/items-overview.html#books-items)
  * [Import Products from Zoho CRM](/de-de/inventory/help/items/items-overview.html#crm-products)



[ Join the Community Forum](https://help.zoho.com/portal/en/community/zoho-inventory)