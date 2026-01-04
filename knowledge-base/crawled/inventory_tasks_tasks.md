# Zoho Inventory Article

**Source:** https://www.zoho.com/de-de/inventory/help/tasks/tasks.html
**Crawled:** 2026-01-04

---

# Tasks

Tasks are the to-dos that you and your users have to complete. In Zoho Inventory, you can create and assign finance-related tasks to your users, mark them by priority, and send reminders.

**Notes:** This feature is available only for certain plans of Zoho Inventory. Visit the [pricing page](/inventory/pricing-comparison/) to check if it’s available in your current plan.

**Scenario:** Patricia, the manager of Zylker wants one of her employees, Brandon, to follow-up on an invoice by calling the customer two days before the due date. So, she creates a task for that particular invoice and assigns it to Brandon, marks the due date as the date on which the invoice is due and sets a reminder two days before the due date. Brandon receives an email notifying him that this task has been assigned to him. He also gets a reminder two days before the due date reminding him to make the follow-up call.

### Benefit of Tasks

With the Tasks feature, you can seamlessly communicate about various to-dos within the organisation. Some of the benefits are:

  * Mark tasks based on priority like high, low, normal, etc.
  * Set reminders to send notification about a task through email, in-app notification, or both.
  * Notify users about the tasks via email.
  * Create custom statuses and mark the tasks based on the status.
  * Create tasks associated with transactions and view them in the transaction details page.



### Enable Tasks

Tasks will not be available in Zoho Inventory by default. You will have to enable it for your organisation. Here’s how:

  * Go to **Settings** > **Preferences**.
  * In the **General** tab check the **Tasks** option.
  * Click **Save**.



### Create Tasks

**Prerequisite:** Ensure that you’ve provided all your users with the required access in the [Users and Roles](/de-de/inventory/help/settings/users.html) section.

Once you have enabled tasks and given your users the required permissions in your organisation, you can start creating tasks and assign them to users.

There are two ways in which you can create a task.

  1. [Top right corner of any page](#top right)
  2. [Menu bar of a specific transaction](/de-de/inventory/help/tasks/tasks.html#menu-bar)



#### Top right corner of any page {#top right}

You can create a task by clicking the Task icon on the top right corner of any page. A task created in this section will not be assigned to any specific transaction.

#### Menu bar of a specific transaction

If you want to associate a task to a particular transaction, you can do it by going to the transaction and clicking the Task icon in that menubar. You can view these tasks on the corresponding transaction page by clicking the Task icon.

You can create tasks contextually from modules such as:

  * Items
  * Customers
  * Sales Orders
  * Invoices
  * Credit Notes
  * Vendors
  * Expenses
  * Purchase Orders
  * Bills
  * Vendor Credits



**To create a task:**

  * Click the **Task** icon and click the **\+ New** button on the top right corner of the page.
  * Enter the necessary details.

Field| Description  
---|---  
Title| Enter the title or name of the task.  
Assign to| Select the user to whom you want to assign the task.  
Notify user via email| Mark this option if you wish to notify the user about the task through email.  
Related Contact| Add the contact you want to associate with this task.  
Due Date| Select the date on which you expect the task to be completed.  
Priority| Choose the priority of the task. You can choose if its very high, high, normal, low or very low priority task.  
Set Reminder| Set reminders and choose to send the reminders via email, in-app notification or both to the assigned user.  
  
  * Click **Save**.



On clicking save, the task will be created and if you had marked the _Notify user via email_ option, the user will receive an email with the task details. You can view the task by clicking the tasks icon in the top right side of the page.

Once you or a user completes the task, it can be marked as **Completed** from the **Change Status** dropdown.

### Task Preferences

#### Custom Status

There are predefined statuses in tasks such as **Yet to Start** , **In Progress** and **Completed**. However, if you wish to create other statuses, you can do it by creating a custom status. These custom statuses will have to be created as a sub-status of a predefined status. Here’s how:

  * Go to **Settings** > **Preferences** > **Tasks**.
  * Click the **\+ New Custom Status** button in the top right corner of the page.
  * Select the status under which you want to create this sub-status and enter the **Status Name**.
  * Click **Save**.



If you create a sub-status under Completed, and if that status is applied on a task, no notifications will be sent for that task as it will be considered as completed.

**Insight:** Only the admins, the assigned user, or the user who created the task will have permission to change the status of a task.

#### Manage Permissions

You can choose the level of permission you wish to give your users. By default, only the admin will have full access. The admins will have to provide access to the other users, only after which they’ll be able to see the tasks assigned to them. To grant access:

  * Go to **Settings** > **Users and Roles**.
  * Under the **Roles** tab, select the role that you want to set the permission for.
  * You can give full access, view, create, delete or edit access.
  * If you wish to give a user access to other users’ tasks, you can click **More Permission** and check the **Manage other users’ tasks** option.



**Insight:** If a user is given a permission, let’s say View permission, then they can only view the task assigned to them. However, if the user is given both View and Manage other users’ tasks, they can view other users tasks. This applies to all permissions such as View, Create, Edit and Delete under the tasks header in the [Users and Roles](/de-de/inventory/help/settings/users.html) section.

### Other Actions

#### Delete Task

**Notes:** Only the Admins, the assigned user, the user who created the task, and anyone with Manage other users’ tasks permission will be able to delete tasks.

**To delete a task:**

  * Go to the **Tasks** module.
  * Click the down arrow next to the task that you want to delete.
  * Click **Delete**.
  * In the following pop-up, click **Delete Task** to confirm.



#### Edit Task

**Notes:** Only the Admins, the assigned user, the user who created the task, and anyone with Manage other users’ tasks permission will be able to edit tasks.

**To edit a task:**

  * Go to the **Tasks** module.
  * Click the down arrow next to the task that you want to edit.
  * Click **Edit**.
  * Make the necessary changes and click **Save**.



#### Manage Filters

If you want to view tasks based on their status, you can filter them. Here’s how:

  * Go to the **Tasks** list page.
  * Click **All Tasks** on the top of the page and select that status based on which you want to filter the tasks. The tasks will be listed based on the filter you’ve applied.



#### Bulk Actions

You can bulk-delete and bulk-update the tasks that you’ve created in Zoho Inventory. Here’s how:

  * Go to the **Tasks List** page.
  * Select the tasks in bulk that you want to update or delete.
  * Click the **Delete** icon and then **OK** if you wish to delete the selected tasks or the Bulk Update icon and then Update to make changes to the selected task.



## IN THIS PAGE

  * [Benefits of Tasks](/de-de/inventory/help/tasks/tasks.html#benefits)
  * [Enable Tasks](/de-de/inventory/help/tasks/tasks.html#enable)
  * [Create Tasks](/de-de/inventory/help/tasks/tasks.html#create)
  * [Task Preferences](/de-de/inventory/help/tasks/tasks.html#preference)
    * [Custom Status](/de-de/inventory/help/tasks/tasks.html#custom-status)
    * [Manage Permissions](/de-de/inventory/help/tasks/tasks.html#manage)
  * [Other Actions](/de-de/inventory/help/tasks/tasks.html#other-actions)
    * [Delete Tasks](/de-de/inventory/help/tasks/tasks.html#delete)
    * [Edit Tasks](/de-de/inventory/help/tasks/tasks.html#edit)
    * [Manage Filters](/de-de/inventory/help/tasks/tasks.html#manage-filter)
    * [Bulk Actions](/de-de/inventory/help/tasks/tasks.html#bulk-actions)



[ Join the Community Forum](https://help.zoho.com/portal/en/community/zoho-inventory)