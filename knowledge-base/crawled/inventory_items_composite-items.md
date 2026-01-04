# Zoho Inventory Article

**Source:** https://www.zoho.com/de-de/inventory/help/items/composite-items.html
**Crawled:** 2026-01-04

---

# Composite Items

A Composite item in Zoho Inventory is a single commodity that is made up of two or more items and/or services. Whether you’re physically assembling an item or selling curated item sets, Zoho Inventory has you covered with two distinct types:

  * [Assemblies](/de-de/inventory/help/items/composite-items.html#Assemblies)
  * [Kits](/de-de/inventory/help/items/composite-items.html#Kit-Items)



##### Assemblies

Assemblies (formerly known as Bundles) is used when you physically assemble a single item from individual components. This is ideal for manufacturers and businesses that produce finished goods. You’ll now find a dedicated Assemblies module under the Inventory tab, offering better control. Learn [more](/de-de/inventory/help/items/assemblies.html).

**Scenario:** Brandon runs a furniture business that manufactures tables. He purchases the components (items) such as legs, screws, and a tabletop and assembles them to make the final product. To track this process, he uses the assemblies feature in Zoho Inventory where he assembles the component together resulting in the reduction of the component’s stock levels and a new finished good (assembly) is created with it’s own stock. He then uses the Assemblies module to keep track of the assemblies created and manages them all in one place.

##### Kit Items

Kit Items are for grouping existing items for sale without any physical assembly. Great for promotional bundles, gift sets, or product combos where each component remains independent but is sold as a single unit. You can also set custom pricing for kits, making it easier to create compelling offers for your customers.

**Scenario:** Patrcia has a cosmetic store where during the holidays season she offers a gift box at a discounted price that includes moisturiser, lipstick, and perfume. Hence, she uses Zoho Inventory to create kits in composite items that saves time. She does not have to worry about creating a new combo item in Zoho Inventory with its own dedicated stock, instead, the stock of the associated components will be tracked individually and not as a new item.

* * *

### Enabling Composite Items

**Note:** The subscription plan chosen by you must allow you to use this feature. To know about the subscription plans in Zoho Inventory, click [here](/inventory/pricing/).

To enable the Composite Items feature in Zoho Inventory,

To enable Composite Items in Zoho Inventory:

  * Go to **Settings** in the top right corner.
  * Scroll down to the _Module Settings_.
  * Click **Items** under _General_.
  * Click the **Enable Composite Items** option.
  * Click the **Save** button at the bottom to apply the configured settings.
  * Under the **Items** module, you will now be able to access the Composite Items feature.



* * *

### Creating a Composite Item

To create a composite item:

  * Go to the **Composite Items** module under _Items_ from the left sidebar.
  * Click the **’+’** button beside the Composite Items module or **\+ New** button on the top right corner.
  * Enter the **Name** of the composite item.
  * Select the Item Type:
    * **Assembly Item:** A group of items that are physically assembled and managed as a single finished product with inventory tracking.
    * **Kit Item:** A group of separate items packed and sold together as one unit, without requiring physical assembly.
  * Record the **SKU** (Stock Keeping Unit) for the composite item.



**Insight:** _The SKU field will serve as one of the unique identifiers for an item. Here, you can store your item’s barcode information so that you can scan and retrieve the item while creating transactions._

  * Choose or enter a unit of measurement (**E.g.** Kgs, Pieces, Liters etc.) for the item in the **Unit** field.
  * Choose a category or add a new category for your composite item. Learn more about [item categories](/de-de/inventory/help/items/item-categories.html) in Zoho Inventory.
  * Click the **Returnable Item** checkbox if you accept sales returns for this composite item. [Sales returns](/de-de/inventory/help/sales-returns/sales-returns-overview.html) can be created only for those items you set as returnable.
  * Enter a _HSN code_ * for the item.
  * Choose a tax preference for the item.
  * Upload different images of the item. You can upload up to fifteen images for an item. **File format:** .gif, .png, ,jpeg, .jpg, .bmp; **Max File Size:** 5 MB each. Choose one image as the primary image.
  * Associate the items and services that you want to configure as acomposite item and enter its quantity. You can also add an existing composite item as part of this composite item.
  * Enter the **Selling Price** and **Cost Price** for the item.
  * Select a sales and a purchase account in which you want to track the item.
  * Add a brief sales and purchase description for the item, which will be displayed on all the respective transactions.
  * Select the default Interstate and Intrastate tax rates for the item. This will be applied to the item automatically when it’s added to a transaction.
  * Record the dimensions of the item. This will be helpful in calculating the [package geometry](/de-de/inventory/help/sales-orders/package-geometry.html) for an order.
  * If applicable, you can add the product codes associated with the item in the **UPC** , **EAN** , **MPN** and **ISBN** fields.



**Insight:** _The UPC and EAN fields are numeric fields. The MPN and ISBN are alphanumeric fields that support alphabets, numbers, spaces and even hyphens._

  * Select the **Track Bin Location for this item** option if you wish to track the bin locations. You cannot disable this option once you have recorded transactions for the item.



**Insight:** _If you do not want to keep stock for this item, mark this item as inactive and create a non-inventory tracked item._

  * If you have enabled Advance Inventory Tracking option in your organization, choose whether you want to track your composite item by [serial number](/in/de-de/inventory/help/items/composite-items.html#track-serial-numbers) or by [batch number](/in/de-de/inventory/help/items/composite-items.html#track-batch-numbers). If you don’t want to track either, choose ‘None’ and proceed.
  * Select an account to track the inventory for your items.
  * Select an Inventory Valuation Method:
    * **FIFO (First In, First Out):** In this method, the inventory gets tracked based on the First In, First Out system, which lets you assess the value of your inventory. This simply means the oldest inventory items recorded are sold first. Learn more about [FIFO](/inventory/kb/reports/inventory-fifo-report.html).
    * **WAC (Weighted Average Costing):** In this method, the average cost of all the inventory items will be calculated. The average cost is then used to determine the Cost of Goods Sold (COGS) and the value of your remaining inventory. Learn more about [WAC](/inventory/kb/items/inventory-wac-report.html).



**Insight:** _Weighted Average Costing (WAC) is recalculated whenever new stock is added to your inventory._

  * Select the Reorder Point. A notification will be sent out to you, which will help you keep tabs on the stock levels of your items so you never run out of stock.



**Insight:** _Setting a reorder level helps you restock items before they run out._

  * Enter the **Opening Stock** (if any) and **Opening Stock Value** , which is the average purchase price of the item. If you have enabled multi-warehouse, enter the Opening Stock and Opening Stock Value for each warehouse by clicking **\+ Add Warehouses**.



**Insight:** _Opening Stock refers to the quantity you have on hand before you start tracking inventory for the item._

**Insight:** *When you create a composite item, you are only defining the skeleton of the composite item. If you have not added any opening stock, the creation process will not have any effect on the stock level of the composite item. To add stock or increase the stock level of a composite item, you can create assemblies, adjust the stock of the composite item or create purchase receives/bills for the composite item.

  * The Composite Item created will by default be considered as Goods as you cannot create a service type composite item or associate only service items to your composite item in Zoho Inventory.



* * *

### Advance Inventory Tracking

Zoho Inventory provides two advanced features to track the stock flow of your composite items accurately.

  * [Serial Number Tracking](/de-de/inventory/help/items/composite-items.html#track-serial-numbers)
  * [Batch Number Tracking](/de-de/inventory/help/items/composite-items.html#track-batch-numbers)



**Insight:**

  * Your current subscription plan in Zoho Inventory must allow you to access the advanced inventory tracking features.
  * Each item can be tracked either by serial numbers or by batch numbers, but not both.



#### Track Serial Numbers

To track your item by serial numbers:

  * Choose the **Track Serial Number** option under **Advanced Inventory Tracking**.
  * If you’ve entered an opening stock, you can add serial numbers for the given opening stock in the field below.
  * If you have enabled multi-warehouse in your organization, click the ellipsis icon at the end of each warehouse row and click **Add Serial Numbers**.
  * Enter the serial number for the opening stock given in each warehouse.



**Insight:**

  * You can enter up to 200 serial numbers for an opening stock.
  * You can either enter the serial numbers manually or scan the barcode of the item.



  * Click **Save**. The serial numbers will now be available for your sales transactions. You can also choose to save the item and enter the serial numbers at a later point while creating a bill.



**Pro Tip:** You can also [add serial numbers to composite items](/de-de/inventory/help/items/composite-items.html#serialized-composite-item).

* * *

#### Track Batch Numbers

  * Choose **Track Batches** under **Advanced Inventory Tracking**.
  * If you’ve entered an opening stock, you can add batch details for the given opening stock in the fields below.
  * If you have enabled multi-warehouse in your organization, click the ellipsis icon at the end of each warehouse row and click **Add Batches**.
  * Enter the batch details for the opening stock given in each warehouse.



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

### Create an Assembly

Assemblies is the process of putting together different components (items) to produce new finished goods.These components could be items and services of your choice. You can create assemblies to increase the stock level of your composite item in Zoho Inventory. Learn how to [create assemblies from composite items or assemblies module.](/de-de/inventory/help/items/assemblies.html#Create-an-Assembly).

**Note:** _You cannot create an assembly with service items alone. You have to include at least one inventory item as part of it._

* * *

### More Actions

#### Edit Composite Item

If at any point, you wish to change the associated items and services that comprise the composite item, you can do so by editing it.

  * Go to the **Composite Items** module under _Items_ from the left sidebar.
  * Open the preferred composite item.
  * Click the **Edit** button on the item details page.
  * Make the desired changes.
  * Click **Save** to apply the changes.



* * *

#### Deleting a composite item

Before deleting a composite item, make sure that it has no transactions associated with it. Alternatively, you can mark it as inactive.

To delete a composite item:

  * Go to the **Composite Items** module under _Items_ from the left sidebar.
  * Open the preferred composite item.
  * Click **More** and then click **Delete**.
  * Confirm your action to delete the composite item permanently.



**Insight:** Only the composite item gets deleted, its constituent items will remain active and available for use.

* * *

#### Mark as Active/Inactive

When you want to disable a composite item temporarily, then you can mark it as inactive in Zoho Inventory. Once you do, it’ll no longer be available to add in new transactions.

To mark a composite item as inactive:

  * Go to the **Composite Items** module under _Items_ from the left sidebar.
  * Open the preferred composite item.
  * Click **More** and **Mark as Inactive**.
  * To make it active again, click **More** and **Mark as Active**.



**Insight:** Only the composite item becomes inactive, its constituent items will remain active and available for use.

* * *

### Import Composite Items

Instead of adding the items one by one to your inventory, you can use this short-cut to bulk load the items in one sweep and save a lot of time. To import composite items into your Zoho Inventory account:

  * Go to the **Composite Items** module under _Items_ from the left sidebar.
  * Click the **Three dot icon** in the top right corner.
  * Select the **Import Composite Items** option from the dropdown.
  * Browse and upload either a CSV or TSV type file. You can download the sample file from this page to get an idea on how to create the files you need to import.
  * Choose the Character Encoding involved from the dropdown. By default, the character encoding is UTF-8(Unicode).
  * Click **Next** to proceed to the mapping fields window.
  * Zoho Inventory will automatically map similar fields and match them together. You can manually match the unmapped ones or alter the mapped ones.
  * Click the checkbox beside the option **‘Save these selections for use during future imports’** to automate mapping for future item imports.
  * Click the **Next** button.
  * Here, an overview of the number of variants ready for import, number of skipped records and unmapped fields will be shown.
  * Click the **Previous** button if you need to make any changes to the operation.
  * If everything is ready, click the **Next** button to import.



* * *

### Export Composite Items

To export composite items from your Zoho Inventory account:

  * Go to the **Composite Items** module under _Items_ from the left sidebar.
  * Click the **Three dot icon** in the top right corner.
  * Select the **Export Items** option in the dropdown.
  * Choose one of the following options:
    * **All Composite Items:** Export all composite items from your organization.
    * **Specific Period:** Select a custom date range and export the items created within this date range.
  * Select the format in which you want to download your export file.
  * Enter a password to secure your export file if needed.
  * Click the **Export** button in the bottom. The file will be downloaded to your device.



* * *

### Filter Composite Items

You can apply the filters to narrow down your search to the preferred composite items. To apply a filter,

  * Go to the **Composite Items** module under _Items_ from the left sidebar.
  * Click the composite item filter tab on the left top of the page.
  * Choose the desired filter from the dropdown.



* * *

### Adjust Stock for Composite Items

To adjust stock for a composite item:

  * Go to the **Composite Items** module under _Items_ from the left sidebar.
  * Open the preferred composite item.
  * Click **More** and **Adjust Stock**.
  * Select whether you want to make a quantity or a value adjustment.
  * To make a quantity adjustment:
    * Select the Date and Account for the adjustment.
    * Select the warehouse in which this stock adjustment should be reflected.
    * Enter either the New Quantity in Hand directly or enter the Quantity Adjusted.
    * Select the reason for making this adjustment.
    * Save it as draft or adjust it immediately.
  * To make a value adjustment:
    * Select the Date and Account for the adjustment.
    * Enter either the Changed Value or the Adjusted Value.
    * Select the reason for making this adjustment.
    * Save it as draft or adjust it immediately.



* * *

## IN THIS PAGE…

  * [Enabling the Composite Items module](/de-de/inventory/help/items/composite-items.html#enable)
  * [Creating a Composite Item](/de-de/inventory/help/items/composite-items.html#creating-composite-item)
  * [Track Serial & Batch Numbers](/de-de/inventory/help/items/composite-items.html#advanced-inventory-tracking)
  * [Assemblies](/de-de/inventory/help/items/composite-items.html#create-assemblies)
  * [More Actions](/de-de/inventory/help/items/composite-items.html#more)
    * [Edit Composite Item](/de-de/inventory/help/items/composite-items.html#editing-composite-items)
    * [Delete Composite Item](/de-de/inventory/help/items/composite-items.html#deleting-composite-items)
    * [Mark as Active/Inactive](/de-de/inventory/help/items/composite-items.html#inactive-active-composite-item)
    * [Adjust Stock](/de-de/inventory/help/items/composite-items.html#adjustments)
    * [Filter Composite Items](/de-de/inventory/help/items/composite-items.html#filtering-composite-items)
  * [Import Composite Items](/de-de/inventory/help/items/composite-items.html#import)
  * [Export Composite Items](/de-de/inventory/help/items/composite-items.html#export)



[ Join the Community Forum](https://help.zoho.com/portal/en/community/zoho-inventory)