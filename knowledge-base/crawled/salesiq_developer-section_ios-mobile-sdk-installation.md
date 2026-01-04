# Zoho Salesiq Article

**Source:** https://www.zoho.com/salesiq/help/developer-section/ios-mobile-sdk-installation.html
**Crawled:** 2026-01-04

---

# Overview

ZohoSalesIQ Mobile SDK lets you embed live chats, calls, and user tracking into your existing mobile application. This enables your users to converse with your support team quickly in case help is needed and helps you make the support experience seamless. The SalesIQ Mobile SDK comes with a feature-rich set of APIs that allow you to integrate seamlessly with your application. You may check the **API Reference** section for more information on the available APIs and click the button below to get a sample app.

Download Sample APK

Download Sample App

**Note:** Zoho SalesIQ is GDPR Compliant. The website and Mobile SDK configurations remain the same. If you have already configured it on your site, it will be automatically reflected in the Mobile SDK as well. If it's not reflected, [learn how to configure](/salesiq/help/portal-settings-enable-gdpr.html) it.

# Integrating SalesIQ live chat into iOS app

  * Install the SalesIQ live chat SDK (Mobilisten) using one of the supported methods:
    * Swift Package Manager (SPM) (Recommended)
    * CocoaPods
  * Update Info.plist with the required configurations
  * Initialise Mobilisten SDK in your app’s startup flow



Once these steps are completed, SalesIQ live chat will be successfully integrated and ready to use in your iOS app.

**Requirements:** The iOS SDK is compatible with **iOS version 13** and above.

## Install the SalesIQ live chat SDK (Mobilisten) 

### Install with Swift Package Manager

Follow the steps below to add the Mobilisten SDK using SPM:

  1. Open your project in Xcode.
  2. In the **Project Navigator** , click your**project name**.
  3. Select the **Package Dependencies** tab.
  4. Click the **+** (Add Package) button.



  5. In the prompt, paste the following URL.


    
    
    Copied 
    
    
    https://github.com/zoho/SalesIQ-Mobilisten-iOS-SP

  6. Set Dependency Rule to: **Up to Next Major Version (recommended for automatic updates)**
  7. Click **Add Package**.



  8. After the package is downloaded, there will be two options: **Mobilisten** and **MobilistenCalls**.
     * To enable both **Chat** and **Call** , add targets for**both packages**.
     * For only **Chat** , select just **Mobilisten**.



**Note:** MobilistenCalls alone will not work without Mobilisten.

  9. Once your selections are made, click the **Add Package** button to complete the integration.



### Install with Cocoapods

Follow the steps below to add the Mobilisten SDK using Cocoapods:

  1. Open your project folder in Terminal.
  2. If you don’t have a Podfile, create one by running:


    
    
    Copied 
    
    
    pod init

#### Open the Podfile and add
    
    
    Copiedplatform :ios, '13.0'
    use_frameworks!
    
    target 'YourAppTarget' do
      pod 'Mobilisten' 
      pod 'MobilistenCalls' // use only for audio calls
    end
    //Replace 'YourAppTarget' with your actual app target name.

  3. Save the file and run:


    
    
    Copied 
    
    
    pod repo update && pod install

  4. Once the pod is successfully downloaded, open the generated .xcworkspace file to continue development.



**Note** : When using "pod MobilistenCalls", it is mandatory to add " pod Mobilisten". 

## Update Info.plist

  * Update your app’s Info.plist file to include the necessary permission keys for the SDK options. These keys help your app access system features correctly.



## Initialize Mobilisten SDK

Once the SDK is integrated and necessary permissions are configured, initialize it in your app's launch flow.

**Recommended location:** Inside AppDelegate.swift > didFinishLaunchingWithOptions.

**Note:** Before calling ZohoSalesIQ.initWithAppKey, ensure the following:

  * You're using the correct **appKey** and **accessKey** generated from the SalesIQ portal. To get the appKey and accessKey, from your SalesIQ dashboard, navigate to _**Settings > Brands > Select the brand > Installation > iOS.**_
  * Your app's Bundle ID matches the one configured in the portal.



#### Swift

SwiftObjective C
    
    
    Copiedimport Mobilisten
    import MobilistenCalls // Only if using audio call support
    
    // Initialize MobilistenCalls (only if you're using it)
    ZohoSalesIQCalls.initialise() 
    
    // Initialize Mobilisten SDK
    ZohoSalesIQ.initWithAppKey("YOUR_APP_KEY", accessKey: "YOUR_ACCESS_KEY") { error in
        if error == nil {
            print("Mobilisten initialized successfully.")
        } else {
            print("Initialization failed: \(error?.message)")
        }
    }
    
    
    
    Copied#import <Mobilisten/Mobilisten.h>
    #import <MobilistenCalls/MobilistenCalls.h> // Only if using audio call support
    
    // Initialize MobilistenCalls (only if you're using it)
    [ZohoSalesIQCalls initialise];
    
    // Initialize Mobilisten SDK
    [ZohoSalesIQ initWithAppKey:@"YOUR_APP_KEY"
                      accessKey:@"YOUR_ACCESS_KEY"
                     completion:^(NSError * _Nullable error) {
        if (!error) {
            NSLog(@"Mobilisten initialized successfully.");
        } else {
            NSLog(@"Initialization failed: %@", error.message);
        }
    }];
    

**Note:**

  * To use the calls functionality (MobilistenCalls), calling **ZohoSalesIQCalls.initialise()** inside **didFinishLaunchingWithOptions** is mandatory.
  * To display the chat launcher (floating button) by default in your app UI, use [ZohoSalesIQ.Launcher.show(.always)](/salesiq/help/developer-guides/ios-sdk-launcher-show.html).