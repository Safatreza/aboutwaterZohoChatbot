# Zoho Salesiq Article

**Source:** https://www.zoho.com/salesiq/help/developer-section/salesiq-widgets.html
**Crawled:** 2026-01-04

---

# Widgets

  * Introduction to widgets
  * How to create a widgets
  * How to edit/delete the widgets
  * Platforms to build widgets



## **Introduction to Widgets**

Widgets are user interfaces that can be built as a part of SalesIQ's platform to display information from third-party applications related to a conversation or bring apps inside the SalesIQ.

### **Benefits of Widgets:**

  * Usually, to know everything about the customer, operators have to navigate through multiple applications. This leads to consuming more time and leaving the customer frustrated. To eliminate this and save time for operators and website visitors, we have custom widgets.
  * Widgets are interfaces where you can bring data from external sources to your chat window. 
  * You can either pull data from any application and display them or push data from SalesIQ to any application with actionable elements present in widgets.
  * For example, suppose you have an organization with 100 operators, and all these operators require access to customer details. In that case, you don't have to give access to all complete visitor data collection necessarily. With SalesIQ's Widgets, you can pull out and display only the information that your operators require to help them answer the visitors' questions. 
  * Widgets are used inside SalesIQ to display different categories of information right inside the live chat window to make your operators' jobs easier.
  * Widgets are highly customizable and support a wide range of textual and visual elements to make the data displayed more actionable. ​



**Example:**

In an e-commerce store, a lot of customers might have issues with their recent orders. You can ease the support operators' work by displaying visitors' recent orders, membership with your store, loyalty points, and other membership details like the last payment date, the next payment date, login ID, payment interval, and so much more. You can also upgrade/downgrade the visitor's plan using custom buttons in the widget. 

**Note:** This is different from integration widgets (Zoho CRM, Desk, and more), click [here](https://help.zoho.com/portal/en/community/topic/tips-to-build-a-powerful-custom-widget-using-salesiq-scripts) to learn the difference between them. 

## **How to create a widget?**

  * To build a widget for your operators, follow the below instructions.
  * In your Zoho SalesIQ dashboard, navigate to **_Settings_** > **_Developers_** > **_Widgets_**. 
  * Click on **Add**
  * Give your widget a **name**. 
  * Next, select the **brand** on which you would like to deploy the widget. Only the department associated with the brand will be able to view this widget. 



​**Note:** Widget can be associated with more than one brand.

  * Then, choose the **modules** that the widget should display. 
  * Choose the platform to build your widget, it can either be
    * [Scripts](/salesiq/help/developer-section/widgets-detail-handler.html)
    * [Webhooks](/salesiq/help/developer-section/widgets-webhook-authentication.html)
  * Finally, click on "**Create Widget** " and you will be directed to the widget platform you choose. 



  * After building your widgets, click on **Save**.
  * For testing the widget, click on **Preview**. 



  * Finally, click on **Publish** to deploy the widget on the operators' dashboard. 



## **How to edit/delete the widget:**

  * To **edit** the widget, navigate to **_Settings_** > **_Developers_** > **_Widgets_** , all your existing widgets will be listed here. 
  * Click on the widget you would like to edit.
  * Then, click on **Configure profile** to edit the widgets' name, brand, and modules. 
  * To edit the widget's code/script or webhook URL, click on **Edit code/URL** , and you will be directed to the platform you choose.



  * Next, make the required changes and click on **Publish** to reflect the changes made.
  * To **delete** the widget, navigate to ** _Settings_** > ** _Developers_** > ** _Widgets_** , all your existing widgets will be listed here. 
  * Hover over the widget you would wish to delete, then the delete icon will appear.
  * Click on it, and the widget will be deleted.
  * Toggle on the widget at the right to disable it. 



### Platform to build Widgets:

​Currently, SalesIQ supports two platforms to build your custom widgets. 

[**SalesIQ Scripts**](/salesiq/help/developer-section/widgets-siq-script-handlers.html)

SalesIQ Scripts is a widget-building platform that uses [Deluge](/deluge/) or Data Enriched Language for Universal Grid Environment as its online scripting language. Deluge is deemed to be robust and easy to use because of its user-friendly syntax. The deluge script builder offers a drag-drop user interface, thus leaving out the task of remembering deluge syntax and functions for the user. Furthermore, deluge offers a connection interface to make third-party integration easy. 

**[Webhooks](/salesiq/help/developer-section/widgets-webhook-authentication.html)**

**​** Webhooks are useful and an easy way to implement event reactions. Webhooks provide a mechanism whereby a server-side application can notify a client-side application when a new event (that the client-side application might be interested in) has occurred on the server. ​When you have widgets in an external service, you can hook them up using webhooks. 

**Related Links:**

  * [Four easy steps to build widgets using Zoho Commerce](https://help.zoho.com/portal/en/community/topic/bring-all-your-apps-to-one-place-using-custom-widgets)
  * [Tips to create effective widgets for operators](https://help.zoho.com/portal/en/community/topic/tips-to-build-a-powerful-custom-widget-using-salesiq-scripts)
  * [Third-party integration - Connection interface](/salesiq/help/developer-guides/bot-siq-scripts-connections-2.0.html)