# Zoho Inventory Article

**Source:** https://www.zoho.com/de-de/inventory/help/picklist/
**Crawled:** 2026-01-04

---

# Picklists

A picklist is a document assigned to a warehouse picker communicating the list of items and its quantities to pick from a specific warehouse to fulfil orders.

Why do you need a picklist?

  * It contains only the information essential for a warehouse picker.
  * It helps organize stock picking for large volumes of orders.
  * Assigning a set of picklists to each warehouse picker helps minimize errors during fulfilment.



### Enable Picklists

Picklist is an optional module you can enable if your business process requires it. However, you must have the [Multi-warehouse](/de-de/inventory/help/warehouses/warehouses-overview.html#enable-multiwarehouse) feature enabled in your organization to access picklists.

To enable picklists:

  1. Go to _Settings_ , then _Preferences_.
  2. Click _General_.
  3. Select **Picklists** under _‘Which modules you’d like to enable?’_.
  4. Scroll down and click **Save** for the changes to take effect.



**Note:** It is not mandatory to generate picklists before packaging. You can skip this step and create packages directly.

### Create Picklist

There are three ways in which you can generate picklists for the sales orders in Zoho Inventory:

**Method 1:**

  1. Click the ‘**+** ’ button next to the _Picklist_ module on the left side bar.

  2. Select the warehouse for which you want to create the picklist and click **Add Items**.

  3. Select one or more parameters based on which you want to search for the sales order items.

  4. Click **Search**.

  5. Select the items to add to the picklist.

  6. Click **Add Items**.

  7. Enter the quantity to pick for each item. If you’ve already picked some quantity, enter the value under the respective _Quantity Picked_ field.

  8. Click **Generate Picklist** to save the picklist.




**Method 2:**

  1. Open a sales order.

  2. Click **Create** > **Picklist**.

  3. Choose the warehouse for which you want to generate a pick list. This prompt appears only when you’ve chosen a different warehouse for each item in your order. Otherwise, you’ll be directed to a new pick list page automatically.

  4. Select an assignee for this picklist. You can also do this later.

  5. Enter the quantity to pick for each item. If you’ve already picked some quantity, enter the value under the respective Quantity Picked field.

  6. Click **Generate Picklist**.




**Method 3:**

  1. Go to the sales orders module in the left navigation pane.

  2. Select the sales orders by clicking the checkbox next to them.

  3. Click the **Bulk Actions** button on the top.

  4. Click **Generate Picklist**.

  5. Choose the warehouse for which you want to generate a picklist.

  6. Select an assignee for this picklist. You can also do this later.

  7. Enter the _quantity to pick_ for each item. If you’ve already picked some quantity, enter the value under the respective Quantity Picked field.

  8. Click Generate Picklist.




**Insight:** Quantity to Pick = Quantity Ordered - Quantity already picked - Quantity packed directly without picking

### Update Item Status in the Picklist

Once the picklist is generated, you or the assignee can update the status of the items. To do so:

  1. Go to the _Picklist_ module on the left sidebar.

  2. Open a picklist.

  3. Click the **Update Picklist** button on the top.

  4. Enter the quantity picked against each item and select a status. If an item’s been fully picked (quantity to pick = quantity picked), you can directly mark its as _Completed_.

  5. Click **Save**.




Note: The Update Status button only allows you to update the current status of the items in the picklist. To add more items to the picklist or to change the quantity to pick, you must _edit_ the picklist.

### Update Picklist Status

If all the items in the picklist have been picked, then instead of updating each item, you can directly mark the picklist as Completed. The resultant action also marks all the items within the list as Completed. If you want to put the picklist on hold for the time being, you can change its status to On Hold.

To change the status of a picklist:

  1. Go to the _Picklist_ module on the left sidebar.

  2. Open a picklist.

  3. Click the **Set Status** button on the top.

  4. Select a status from the dropdown.




Once you mark a picklist as Completed, you cannot change its overall status from the details page as the Completed status holds the highest priority. However, you can change the status of the picklist if you update the Quantity to Pick or Quantity Picked field for an item.

### Packages for Picklists

When you create packages for a sales order, the stock associated with picklists are indicated by the picklist number, and the items whose stock is not associated with picklists are listed separately.

### View Associated Sales Orders and Packages from Picklists

You can now view associated Sales Orders and Packages directly from the Picklist details page. To do this:

  * Go to the **Picklists** under Inventory.
  * Click a specific Picklist to view its details page.
  * On the Picklist details page, you will see:
    * Associated Sales Orders tab
    * Packages tab



## IN THIS PAGE…

  * [Enable Picklists](/de-de/inventory/help/picklist/#enable)
  * [Create Picklist](/de-de/inventory/help/picklist/#create)
  * [Update Item Status in the Picklist](/de-de/inventory/help/picklist/#item-status)
  * [Update Picklist Status](/de-de/inventory/help/picklist/#picklist-status)
  * [Packages for Picklists](/de-de/inventory/help/picklist/#packages)



[ Join the Community Forum](https://help.zoho.com/portal/en/community/zoho-inventory)