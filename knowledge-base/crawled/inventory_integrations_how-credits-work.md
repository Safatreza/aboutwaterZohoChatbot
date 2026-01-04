# Zoho Inventory Article

**Source:** https://www.zoho.com/de-de/inventory/help/integrations/how-credits-work.html
**Crawled:** 2026-01-04

---

# How WhatsApp Credits Work

To understand how WhatsApp credits works, it’s important to be familiar with concepts such as conversation categories and customer service window. This help document provides an overview of these concepts and includes simple examples to illustrate how credits work.

## Conversation Categories

You can send three types of messages to your recipients through your WhatsApp Business Account:

  1. **Utility Messages** \- These messages allow you to follow up with your recipients through requests or confirmation messages. This includes sending reminders for invoices and payment thank-you messages. To categorise such messages, create a template and select **Utility** as the _Template Category_. The charges for utility messages are determined by the [volume tier](/de-de/inventory/help/integrations/how-credits-work.html#Volume-Tier) assigned to the WhatsApp Business Account based on the recipient’s country, as defined by Meta.

  2. **Marketing Messages** \- You can send marketing messages to promote your products, services, or provide offers to increase sales. This includes recipients notifications sent from Zoho Inventory about various discounts. To categorise such messages, create a template and select **Marketing** as the _Template Category_. Marketing messages are charged on a per-message basis. That is, regardless of how many marketing messages are sent to a contact person, a fixed cost is charged per message based on the recipient’s country.

  3. **Service Messages** \- These are messages you can send to your contacts from the service window without using predefined templates. These messages can be sent only after the contact initiates the conversation. Service messages are free of cost.




* * *

## Customer Service Window

When a contact person sends you a message on WhatsApp, a new customer service window opens for 24 hours. During this time, you can chat with your contact person and send utility message templates without any charges.

You can send service messages only when the customer service window is active. Otherwise, you can only send predefined template messages. Each time the customer or vendor sends a new message, the 24-hour window resets from that point.

The following table explains how cost deduction works when a WhatsApp notification is sent to a contact person.

Date| Notification Time| Message Type| Cost Deduction  
---|---|---|---  
10th of July| 10 a.m.| Utility Message| Cost deducted based on the volume tier.  
10th of July| 11 a.m.| Marketing Message| Cost deducted per-message.  
10th of July| 12.30 p.m.| Service Message  
  
(Customer has sent you a message at 12 p.m., so the customer service window is open)| No cost deducted.  
10th of July| 1 p.m.| Utility Message| No cost deducted.  
10th of July| 3 p.m.| Service message  
  
(Customer has sent you a message at 2 p.m., so the the customer service window is open)| No cost deducted.  
10th of July| 4 p.m.| Marketing Message| Cost deducted per-message.  
11th of July| 1 p.m.| Utility Message| No cost deducted.  
11th of July| 3 p.m.| Utility Message| Cost is deducted based on the volume tier, as the customer service window closed at 2 p.m.  
  
## Cost Deduction Factors

### 1\. Currency Associated with the WhatsApp Business Account

The cost deducted for your messages depends on the currency associated with your WhatsApp Business Account. To view the currency:

  * Log in to [facebook.business.com](https://www.facebook.com/business/tools/meta-business-suite?content_id=RSnQo4HygrPVv5N&ref=sem_smb&utm_term=business%20manager%20page%20facebook&gclid=CjwKCAjwr7ayBhAPEiwA6EIGxOXHicVeK254-Scoz1EMUXTZ_DRirAJ-f-P4mfe3wm7g6UoDU3rNzRoCrNgQAvD_BwE&gad_source=1).

  * Go to **Settings**.

  * Navigate to _Accounts_ and click **WhatsApp Accounts**.

  * Select the WhatsApp account that you’ve connected with Zoho Inventory.

  * You can view the currency in the _Business Information_ section.

  * Meta provides different rate cards based on the WhatsApp Business Account’s base currency. You can also [check the recent pricing updates](https://developers.facebook.com/docs/whatsapp/pricing/updates-to-pricing#pricing-updates-on-the-whatsapp-business-platform) and [download the volume tier with the rate card](https://developers.facebook.com/docs/whatsapp/pricing/updates-to-pricing/#rate-cards) for your WhatsApp Business Account’s currency.




### 2\. Message Category

The cost deducted also varies based on the _Message Category_.

In the rate card that you’ve downloaded, the _Marketing column_ consists of the rate that is charged for a single message sent to a contact person from your WhatsApp Business account. The _Utility column_ consists of the list rate, which is the standard rate applied for the first range of utility messages. 

**Note:** If the customer or vendor initiates the conversation, you can send utility messages for free of charge within the 24-hour customer service window.

### 3\. Recipient’s Country

The rate also depends on the country of the contact person’s phone number to whom the message is sent.

Example: If you are sending a marketing message to a contact person with an Indian phone number, the cost deducted is 0.0107 USD per-message.

In Zoho Inventory, your credits will be reduced based on the rate charged. For example, if one credit costs $2.06, and sending a WhatsApp marketing message to an Indian customer costs $0.0107, you can send approximately 192 messages to that contact person using just one credit. (Number of messages that can be sent = Cost per credit / Message cost).

## Volume Tier

A Volume Tier is a pricing structure defined by Meta for WhatsApp Business accounts. It determines the cost per-message based on the total number of utility messages sent in a month, excluding those sent during the customer service window. Based on this count, we determine the applicable volume range.

**Note:** At the beginning of every month, the utility message count for each country is reset to 0.

## Example for Credit Calculation

**Note:** Credits are deducted instantly whenever a message is sent, based on the message category and recipient’s country.

Here’s a sample scenario to illustrate the WhatsApp credits usage:

Patricia runs a textile business and wants to stay connected with her customers. Her WhatsApp Business Account currency is set to USD, and one credit is valued at $2.06. She had purchased 45,000 credits for her WhatsApp Business Account. On July 1, she sends a utility and a marketing message to her customer in Argentina.

Since the first utility message falls under Tier 1, the list rate 0.0289 USD (standard rate applied for the first range of utility messages) is applied. As soon as the message is delivered, credits are reduced based on that cost. Later, the marketing message is sent and the credits will be deducted based on rate per-message. Here is how we calculate the deduction of credits:
    
    
    
    

The above image depicts the volume tier chart for calculating the utility messages sent to a recipient in Argentina. The first 100,000 messages falls under the first tier, known as the list rate. As the message volume increases the messages move through different tiers with decreasing rates. This tiered pricing helps reduce costs as the total message volume increases. 

As shown in the image above, the cost of each marketing message sent to a recipient in Argentina is $0.0618.

The table below shows how credits are deducted on July 1 based on the message category:

Recipient’s Country| Message Category| Message Count| Rate per Message| Cost| Credits Used (Cost ÷ 2.06)| Remaining Credits (from 45,000)  
---|---|---|---|---|---|---  
Argentina| Utility Message| 1| 0.0289 (List rate)| 1 × 0.0289 = 0.0289| 0.0140| 44,999.9524  
Argentina| Marketing Message| 1| 0.0618| 1 × 0.0618 = 0.0618| 0.0300| 44,999.9224  
  
On July 31, Patricia sends a utility message and a marketing message to her customer in Argentina. By this time, a large number of messages have already been sent throughout the month, including 2,000,000 utility messages and 25 marketing messages. As a result, the 2,000,001st utility message falls under Tier 3, and the marketing message is charged based on the per-message rate.

Since credits are deducted instantly for each message sent, Patricia’s WhatsApp Business Account had only 576 credits remaining by July 30. The table below shows how credits will be deducted on July 31:

Recipient’s Country| Message Category| Message Count| Rate per Message| Cost| Credits Used (Cost ÷ 2.06)| Remaining Credits (from 45,000)  
---|---|---|---|---|---|---  
Argentina| Utility Message| 2,000,001| 0.0260 (Tier-3)| 1 × 0.0260 = 0.0260| 0.0126| 576 − 0.0126 = 575.9874  
Argentina| Marketing Message| 26| 0.0618| 1 × 0.0618 = 0.0618| 0.0300| 575.9874 − 0.0300 = 575.9574  
  
By the end of July, Patricia had spent around 44,424 credits and had a balance of approximately 575 credits left in her WhatsApp Business Account.

## WABA and Shared Volume Tier Usage

A Meta Business Account can have multiple WhatsApp Business Accounts (WABAs). When utility messages are sent from different WABAs to recipients in the same country, the total message count is collectively measured across all WABAs for utility billing purposes.

Let’s say, Patricia has a Meta Business Account registered in the US, where she manages two different WhatsApp Business Accounts (WABAs). WABA-1 is connected to Zoho Inventory (with Zoho as the Business Service Provider), and she sends 100,010 utility messages in a month to her customers in Argentina. WABA-2 is linked to a custom application with a different Business Service Provider, and she sends 2,000 utility messages to customers in the same country during the same month. Since both WABAs are part of the same Meta Business Account and the messages are sent in the same _market-category_ (Argentina-Utility), Meta combines the total message volume and counts 102,010 utility messages for tier calculation.

So, the first 100,000 messages fall under the list rate (0–100,000), which costs $0.0289 per message. The remaining 2,010 messages fall under Tier 2 (100,001–1,000,000), billed at $0.0275 per message.

**WABA-1 is billed as follows:**  
Total utility messages sent: 100,010  
The cost for first 100,000 as per the list rate: 100,000 × $0.0289 = $2,890.00  
The cost for next 10 messages as per Tier 2: 10 × $0.0275 = $0.275  
Total cost: $2,890.00 + $0.275 = $2,890.28  
Hence, WABA-1 is billed $2,890.28 for utility messages

**WABA-2 is billed as follows:**  
Total utility messages sent: 2,000  
These 2,000 messages fall under Tier 2  
The cost as per Tier 2 rate: 2,000 × $0.0275 = $55.00  
Total cost: $55.0000  
Hence, WABA-2 is billed $55.00 for utility messages.

Since Patricia manages two WABAs under the same Meta Business Account, the charges are applied separately based on the tier applicable to each WABA’s message volume. WABA-1 is billed $2,890.28, while WABA-2 is billed $55.00, with all its messages falling under Tier 2 pricing.

* * *

##### ON THIS PAGE

  * [Conversation Categories](/de-de/inventory/help/integrations/how-credits-work.html#Conversation-Categories)
  * [Customer Service Window](/de-de/inventory/help/integrations/how-credits-work.html#Customer-Service-Window)
  * [Cost Deduction Factors](/de-de/inventory/help/integrations/how-credits-work.html#cost-deduction-factor)
  * [Volume Tier](/de-de/inventory/help/integrations/how-credits-work.html#Volume-Tier)
  * [Example for Credit Calculation](/de-de/inventory/help/integrations/how-credits-work.html#Example-for-Credit-Calculation)
  * [WABA and Shared Volume Tier Usage](/de-de/inventory/help/integrations/how-credits-work.html#WABA-and-Shared-Volume-Tier-Usage)



[ Join the Community Forum](https://help.zoho.com/portal/en/community/zoho-inventory)