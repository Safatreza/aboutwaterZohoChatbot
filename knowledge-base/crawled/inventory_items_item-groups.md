# Zoho Inventory Article

**Source:** https://www.zoho.com/de-de/inventory/help/items/item-groups.html
**Crawled:** 2026-01-04

---

# Item Groups

An Item Group in Zoho Inventory, contains variations of the same base item. It’s similar items, except in the time of creating one item you can easily create multiple items.

**Scenario:** Jason runs a textile showroom where he sells a variety of T-Shirts. Let’s say the T-Shirts available in the colors Blue, White, Red and in sizes S, M and L. So the variants would be T-Shirt/Blue/S, T-Shirt/Blue/M and T-Shirt/Blue/L. Likewise, there can be six more variants. To add these items one at a time into Zoho Inventory would be a tedious and repetitive task. However, using the Item Groups feature, he can add any number of such items in the time of adding just one.

#### How To Video

### Create Item Group

To create an item group in Zoho Inventory:

  1. Go to the **Item Groups** module under _Items_ from the left sidebar.

  2. Click the **New Item Group** button or the **\+ New** button on the top right corner to open the New Item Group page.

  3. Select whether your item group is of the type ‘Goods’ or ‘Services’.

  4. Enter the name of the item group.

  5. If the items in this group qualifies for [return](/de-de/inventory/help/sales-returns/sales-returns-overview.html), select the **‘Returnable Item’** option.

  6. Select or add a Unit of Measurement (Unit) for the item group.

  7. If you have enabled [item categories](/de-de/inventory/help/items/item-categories.html), then assign a category to the item group. You can add a new category or choose from an existing category.

**Insight:** The category assigned will be applied to all items in the group. Likewise, a category assigned to one of the items in a group will apply to all the other items in the same group.

  8. Select a Tax Preference. This will be applied to all the items in the group.

  9. Add the [attributes and options](/de-de/inventory/help/items/item-groups.html#attributes) for this item group. Based on the item group name and attributes, a combination of variant names will be generated automatically. You can modify them as you see fit.

  10. Choose whether you want the items in this group to be of inventory or non-inventory type.

  11. Enter the SKU for all the items, or click [**Generate SKU**](/de-de/inventory/help/items/item-groups.html#generate-sku) to generate them automatically using our in-built tool.

  12. Specify the Cost Price and Selling Price for the items. If the value remains the same for all items, click **Copy To All** to save time.

  13. If available, you can add product codes like **UPC**(Universal Product Code), **EAN**(International Article Number) and **ISBN**(International Standard Book Number) in the respective fields.

**Insight:** The UPC and EAN fields are numeric fields. The MPN and ISBN are alphanumeric fields that support alphabets, numbers, spaces and even hyphens.

  14. Configure the Sales, Purchase and Inventory accounts for the item group.

  15. Click **Save and Next** to proceed.

  16. For every variant, enter the Opening Stock and Opening Stock Value available in each warehouse.

**Insight:** Opening Stock refers to the stock you have on hand at the time of creating an item. The Opening Stock Value refers to the average purchase price of your opening stock. This will be used for FIFO Cost Lot Tracking.

  17. Click **Save** to create the item group.




**Insight:** The variants in the item group can be treated as independent items.

* * *

### Add Attributes and Options

Attributes are properties used to describe an item. For example, a T-Shirt can be described by its color, size and brand. Likewise, there may be many such variants. Zoho Inventory generates all combination of variants based on the given attributes and options.

  1. The **Add Attributes and Options** checkbox will be enabled by default.

  2. If you wish to create an individual item and not a group, deselect the **Add Attributes and Options** option and proceed.

  3. In the following pop-up, choose the **To create a single item, proceed to the Items section** option. The primary information that you’ve entered in the item groups page will be carried over to the New Item page.

  4. Otherwise, if you choose to continue creating an item group,

     * Enter an attribute and provide relevant options for the given attribute each separated by a comma.
     * Likewise, to add another attribute, click the **\+ New Attribute** option. You can add up to three attributes per item group.
  5. Based on the given item group name and attributes, a combination of variant names will be generated automatically. You can edit or remove them as you see fit.




* * *

### Generating SKUs for an Item Group

Some item groups can have many variants and entering the SKU for each is likely to be time-consuming. Instead, you can create a pattern for SKU with your choice of given attributes and apply it across all variants in the group. This will help you save time from manual entry and also create meaningful SKUs for your items.

To generate SKUs for your item group:

  1. Open a **New Item Group** page and enter the primary information and attributes.

  2. Click the **Generate SKU** option under the **SKU** column.

  3. Go to the **Configure SKU Pattern** section.

  4. Choose the **attributes** from the dropdown and the **number of letters** that should be displayed for each attribute. These form the parts of the SKU.

  5. You can also add custom texts to the SKU. Click the Sample Value drop down and select the **Custom Text** option. Enter the text in the field below.

**Pro Tip:** You can select the attributes in any order. For the purpose of demonstration, we have selected **Item Group Name** followed by **Color** and **Size**.

  6. View the changes you make to the SKU structure in the **SKU Preview** field. This is a read-only field. You cannot directly edit this text.

  7. Choose the appropriate delimiter with which you want to separate the SKU texts and select the case used.

  8. Click the **Generate SKU** button to generate the SKU for all items in the group. If there are any duplicates, the SKU will be generated with a number sequence.

  9. Click **Clear** to erase all values from the SKU field.




* * *

### Edit Item Group

To edit an item group:

  1. Go to the **Item Groups** module under _Items_ from the left sidebar.

  2. Click to open the item group whose details you want to edit.

  3. Click the **Pencil** icon on the top.

  4. Make the necessary changes.

  5. Click **Save**.




* * *

### Remove Items from Group

To remove an item from an existing group:

  1. Go to the **Item Groups** module under _Items_ from the left sidebar.

  2. Click to open the item group from which you want to remove an item.

  3. Click the item that you wish to remove from the group.

  4. Click **More** and select **Remove from Item Group** option.

  5. Confirm your action and the item will be removed from the existing group.




* * *

### Move Item to Another Group

To move an item to another group:

  1. Go to the **Item Groups** module under _Items_ from the left sidebar.

  2. Click to open an item group of your choice.

  3. Go to the Item Details section.

  4. Click to open the item that you wish to move to another group.

  5. Click **More** and select the **Move to another Group** option.

  6. Select a **Destination Group**.

  7. Select the attributes for the item.

  8. Click the **Move** button and the item will be removed from the current group and added to the destination group.




* * *

### Clone Item from a Group

Cloning helps you create an item quickly without having to enter all the details from scratch. This feature comes in handy when you want to:

  * deactivate an item and create a new one in its place.
  * create a new item with properties that are similar to the existing one.



An item group as a whole cannot be cloned, but you can clone the variants in the group.

To clone an item from a group:

  1. Go to the **Item Groups** module under _Items_ from the left sidebar.

  2. Click to open an item group of your choice.

  3. Go to the **Item Details** section.

  4. Click to open the item that you wish to clone.

  5. Click on **More** and select **Clone Item**.

  6. The item details will be pre-filled. Make the necessary changes.

  7. Click **Save** at the bottom to create the item by cloning.




**Pro Tip:** When you clone an item from a group, it’ll be created as an individual item and not as part of the group. Learn how you can [move an item into a group](/de-de/inventory/help/items/item-groups.html#move).

* * *

### Add New Item to Group

To create and add a new item to a group:

  1. Go to the **Item Groups** module under _Items_ from the left sidebar.

  2. Click to open the item group to which you want to add a new item.

  3. Click the **Add Item** button at the top of the page.

  4. Enter the new item details and select the attributes. Make sure that the selected attributes are not identical to any of the existing items in the group.

  5. Click **Save** at the bottom of the page. The item will be created and added to the same group.




* * *

### Mark Item Group as Inactive

  1. Go to the **Item Groups** module under _Items_ from the left sidebar.

  2. Click to open the item group you want to deactivate.

  3. Click the **More** button and select the **Mark as Inactive** option from the dropdown. All the items in the item group will be marked as Inactive and will not be available while creating transactions.

  4. To reactivate the item group, click **More** > **Mark as Active**. The items in the group will be available for transactions.

  5. Similarly, you can also deactivate a single item in the item group. Doing so will not affect the status of the other items in the group.




* * *

### Delete Item Group

To delete an item group in Zoho Inventory:

  1. Go to the **Item Groups** module under _Items_ from the left sidebar.

  2. Click to open the item group you want to delete.

  3. Click the **More** button and select the **Delete** option from the dropdown.

  4. Confirm your action in the following pop-up to delete the item group permanently from Zoho Inventory.




**Pro Tip:** You will not be able to delete an item group if one or more items in it are associated with existing transactions in Zoho Inventory. However, you can either [remove those items from the group](/de-de/inventory/help/items/item-groups.html#remove) and then try deleting the item group, or [mark the item group as inactive](/de-de/inventory/help/items/item-groups.html#inactive).

* * *

### Create an Item Group for Ungrouped Items

In Zoho Inventory, we normally have all our items neatly classified under different item groups. But in some cases, we also have to deal with items that are not a part of any item group.

The most common case of ungrouped items is because of the integration between Zoho Books and Zoho Inventory where, the items(Zoho Books does not support Item groups) created in Zoho Books are reflected in Zoho Inventory.

This may add clutter to your inventory. Hence, to resolve this case, we have introduced a feature that allows you to group all the ungrouped items in your inventory by defining new item groups or adding them to the existing ones.

Before we begin please note that only your inventory tracked items can be grouped together.

  1. Go to the **Items** module under _Items_ from the left sidebar.

  2. Click on the Filter dropdown on top-left corner and select the **Ungrouped Items** filter.

  3. Select the items that you wish to group by checking the box near the item name.

  4. Click on the **Add to Group** button on the top.

  5. Choose whether you want create a new item group or add them to an existing group.

  6. If you’re creating a new item group, enter the item group name, unit, SKUs and click **Save**.

  7. If you’re adding the items to an existing group,

     1. Choose the item group to which you want to add the items.
     2. Enter the SKUs and choose the attributes pertaining to the item group. Make sure the attributes are not identical to any item already present in the group.
     3. Click **Save**.
  8. The items will be successfully grouped and classified under an item group.




* * *

## IN THIS PAGE…

  * [Create Item Group](/de-de/inventory/help/items/item-groups.html#create-item-group)
    * [Add Attributes](/de-de/inventory/help/items/item-groups.html#attributes)
    * [Generate SKUs](/de-de/inventory/help/items/item-groups.html#generate-sku)
  * [Edit Item Group](/de-de/inventory/help/items/item-groups.html#edit)
  * [Add New Item to a Group](/de-de/inventory/help/items/item-groups.html#add-new-item)
  * [Clone Item from a Group](/de-de/inventory/help/items/item-groups.html#clone)
  * [Remove Item from Group](/de-de/inventory/help/items/item-groups.html#remove)
  * [Move Item to Another Group](/de-de/inventory/help/items/item-groups.html#move)
  * [Mark Item Group as Inactive](/de-de/inventory/help/items/item-groups.html#inactive)
  * [Delete Item Group](/de-de/inventory/help/items/item-groups.html#delete)
  * [Import Item Groups](/de-de/inventory/help/items/item-groups.html#importing-item-group)
  * [Create Item Group for Ungrouped Items](/de-de/inventory/help/items/item-groups.html#grouping-of-ungrouped-items)



[ Join the Community Forum](https://help.zoho.com/portal/en/community/zoho-inventory)