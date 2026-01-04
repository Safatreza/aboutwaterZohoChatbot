# Zoho Salesiq Article

**Source:** https://www.zoho.com/salesiq/help/developer-section/form-controllers.html
**Crawled:** 2026-01-04

---

## **Form Controllers**  
  
  * Introduction to Form Controllers
  * To create a form controller
  * To edit/delete a form
  * Platforms to build Forms



### **Introduction to Form Controllers**

A form controller is triggered either upon the [form's](/salesiq/help/developer-section/widgets-return-type-form.html) submission or on adding or updating input in a form field. When an operator adds or updates an input value in a form field or clicks the submit or cancel button in the form, the form function associated with this function is triggered to execute the intended action.

**Benefits of Form Controllers:**

  * In general, form controllers are used to collecting multiple structured data as inputs to perform a particular action. 
  * Forms can be used as a part of a widget's action response to collect data from your operator and push the data to any application. 
  * For example, in an e-commerce business, every customer may have a membership. The operator can upgrade or downgrade the membership based on the visitor/customer's requirement. 



### **To create a form controller:**

  * To build a form controller for your widget, follow the below instructions.
  * In your Zoho SalesIQ dashboard, navigate to **_Settings_** > **_Developers_** > **_Form Controller_**. 
  * Click on **Add**
  * Give your form a **name**. 
  * Next, select the **brand** on which you would like to deploy the form. Only the department associated with the brand will be able to view this form. 



​**Note:** Form can be associated with more than one brand.

  * Then, choose the **modules** that the form should display. 
  * Choose the platform to build your form, it can either be
    * [Scripts](/salesiq/help/developer-section/widgets-detail-handler.html)
    * [Webhooks](/salesiq/help/developer-section/widgets-webhook-authentication.html)
  * Finally, click on "**Create Form Controller** ", and you will be directed to the form platform you choose. 



  * After building your form, click on Save. For testing, click on **Preview,** and select the widget you would like to associate this form and its **module.**



****​****

  * Finally, click on **Publish** to deploy the form on the widget and so on the operators' dashboard. 



### **To edit/delete a form:**

  * To edit the form, navigate to **Settings** > **Developers** > **Form Controllers** , all your existing widgets will be listed here. 
  * Click on the form you would like to edit.
  * Then, click on Configure profile to edit the form's name and description. 
  * To edit the code/script or the webhook URL of the widget, click on Edit code/URL, and you will be directed to the platform you choose.



  * ​Next, make the required changes and click on **Publish** to reflect the changes made.
  * To **delete** a form, navigate to **Settings** > **Developers** > **Form Controllers** , all your existing forms will be listed here. 
  * Hover over the form you would wish to delete, then the delete icon will appear.
  * Click on it and the form will be deleted.
  * Toggle on the form at the right to disable it. 



### **Platforms to build Forms:**

​Currently, SalesIQ supports two platforms to build your custom widgets. 

[**SalesIQ Scripts**](/salesiq/help/developer-section/form-controller-submit-handler.html)

SalesIQ Scripts is a form-building platform that uses [Deluge](/deluge/) or Data Enriched Language for Universal Grid Environment as its online scripting language. Deluge is deemed to be robust and easy to use because of its user-friendly syntax. The deluge script builder offers a drag-drop user interface, thus leaving out the task of remembering deluge syntax and functions for the user. Furthermore, deluge offers a connection interface to make third-party integration easy. 

[**Webhooks**](/salesiq/help/developer-section/form-controllers-webhooks.html)

​Webhooks are useful and an easy way to implement event reactions. Webhooks provide a mechanism whereby a server-side application can notify a client-side application when a new event (that the client-side application might be interested in) has occurred on the server. ​When you have widgets in an external service, you can hook them up using webhooks. 

**Related Link:**

  * [How to create/build a widget?](/salesiq/help/developer-section/salesiq-widgets.html)