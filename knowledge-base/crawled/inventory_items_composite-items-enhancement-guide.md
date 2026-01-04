# Zoho Inventory Article

**Source:** https://www.zoho.com/de-de/inventory/help/items/composite-items-enhancement-guide.html
**Crawled:** 2026-01-04

---

# Enhanced Composite Items

The Composite Item feature within Zoho Inventory has undergone a few necessary enhancements to adapt to the needs of different businesses. In this document, we have captured all those changes for you to effectively utilize this improved feature.

As a significant part of this upgrade, **Bundling** operation has been introduced in place of Box/ Unbox. Read on to know more about bundling and the changes that accompanies it.

  1. [What is bundling and how does it work?](/de-de/inventory/help/items/composite-items-enhancement-guide.html#bundling-about)
  2. [What does bundling achieve over boxing?](/de-de/inventory/help/items/composite-items-enhancement-guide.html#bundling-over-boxing)
  3. [What are the visible changes post the upgrade?](/de-de/inventory/help/items/composite-items-enhancement-guide.html#bundling-changes)
  4. [What will happen to the composite items that were boxed before the update?](/de-de/inventory/help/items/composite-items-enhancement-guide.html#impact-on-boxed-items)
  5. [How do I discard a bundle that is no longer needed?](/de-de/inventory/help/items/composite-items-enhancement-guide.html#bundle-delete)
  6. [I bought kits from my vendor. How do I unpack it to resell the individual items?](/de-de/inventory/help/items/composite-items-enhancement-guide.html#comp-items-adjustment)
  7. [Is there anything new in store with this enhancement?](/de-de/inventory/help/items/composite-items-enhancement-guide.html#more-features)



* * *

### What is bundling and how does it work?

**Bundling** is the technique of putting together different components in desired quantities to produce a single commodity. These components could be goods, services and other non-inventory items of your choice.

For the most part, bundling works just like boxing except when it comes to its constitution. You can now edit the contents of a bundle as you see fit at any given time (which was not the case before). 

The bundling process will increase the stock of the composite item while the stock of the individual items will drop as per the quantity used by this process.

In simple steps, find out how you can perform [bundling](/de-de/inventory/help/items/composite-items.html#bundling) in Zoho Inventory.

* * *

### What does bundling achieve over boxing?

There were a couple of challenges posed by the boxing/unboxing method, which has been overcome with bundling.

  * Earlier, the COGS(Cost of Goods Sold) entry was posted during the boxing process instead of an actual sale. With bundling, this will be avoided and COGS will only be posted during sales (invoicing). In short, bundling of composite items will have all its items tracked under your Inventory Asset account.

  * Previously, you were allowed to box composite items even when the quantity of the associated items were insufficient. This is however, practically not possible. Now, you need to have sufficient stock for each item to bundle them up.

  * It is now possible to flexibly modify the components at the instant of bundling which was not possible with boxing.




* * *

### What are the visible changes post the upgrade?

The general outlook of the Composite Items has been retained with a few noticeable tweaks.

In the composite item details page,

  * **Box/Unbox** button has been replaced with the **Create Bundle** button.
  * **Boxing/Unboxing History** section has been replaced with the **Bundling History** section.
  * If your composite item has boxed units, then you can view the boxing history under the **Boxes** tab within the **Bundling History** section.



  * In the composite item creation page, you can find the **Add Services** button which was not available before.



* * *

### What will happen to the composite items that were boxed before the update?

If you have composite items with boxing history, you can still view them under the **Boxes** tab within the Bundling History section. Here is how the composite items with boxing history will be affected:

  * You cannot edit the composition of a composite item with boxing history. However, while bundling, you will be able to alter the items and services of your choice.

  * Since you don’t have an unbox option anymore, as a work around, you can simply delete the boxing entry. This works the same as unboxing and the stock level of the associated items increases.




  * When you create an invoice for items with boxing history, the stock will be consumed on a FIFO basis. Say, you have a composite item with boxes as well as bundles. When you add this item to your invoice, the boxed stock will be exhausted first followed by the bundled stock.



* * *

### How do I discard the bundles that are no longer needed?

You can simply delete the bundle by clicking the **trash** icon beside each bundle under the **Bundling History** section. This will raise the stock level of the constituents of that bundle.

* * *

### I bought kits from my vendor. How do I unpack it to resell the individual items?

Item Adjustment serves as another work around in place of the unbox button for unpacking (or unbundling) the items.

Once you purchase kits from your vendor, you can bulk adjust the quantity of the composite item and its constituents accordingly in Zoho Inventory. 

  * Record the purchase of the kits. [Learn how](/de-de/inventory/help/items/composite-items.html#reselling).
  * Go to the Item Adjustment tab under the Items module.
  * Open a new item adjustment page.
  * Fill up the mandatory fields.
  * Add the composite item as a line item and enter its quantity in a negative value (representing the number of kits you are unpacking).
  * Now, add all the components that comprise the kit and enter the quantity to be increased for each item (**Tip:** Quantity to enter = Quantity of the item used in the kit * Number of kits unpacked). 
  * Hit Save to create an item adjustment.



This increases the stock level of the individual components and decreases the number of kits indicating that the kits have been unpacked and its components restored.

* * *

### Is there anything else new in store?

Why, of course! Aside from bundling, the following upgrades have been made to the composite items feature:

  * You can add serial numbers to composite items. [Learn how](/de-de/inventory/help/items/composite-items.html#serialized-composite-item).
  * You can associate non-inventory items (purchase items as well as services) as constituents. This will help you track real time bundling i.e assembling, which you can do by adding the list of items and labour work(service) spent to complete it.



* * *

Curate your own kits and sell them in special prices with [item grouping](/inventory/item-grouping-bundling/?utm_source=HelpDocRedirection&utm_medium=Website)

[ Join the Community Forum](https://help.zoho.com/portal/en/community/zoho-inventory)