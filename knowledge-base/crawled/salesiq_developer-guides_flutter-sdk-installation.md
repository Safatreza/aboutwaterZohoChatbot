# Zoho Salesiq Article

**Source:** https://www.zoho.com/salesiq/help/developer-guides/flutter-sdk-installation.html
**Crawled:** 2026-01-04

---

# Zoho SalesIQ Mobilisten Flutter Plugin

Mobilisten, the Zoho SalesIQ Flutter SDK, brings live chat and in-app calling directly into your mobile app, helping you connect with customers at every stage of their journey. With Mobilisten, users can reach you from any screen, get instant support, and make faster, more confident purchase decisions, all without leaving your app.

  * **In-app Chat:** Let customers start conversations, get their questions answered in real-time, and stay engaged right inside your app.
  * **[New]****In-app Calls:** Go beyond chat with voice calls, making it easy to resolve complex issues faster and provide a more personal support experience.
  * **Deep Customization:** Mobilisten is highly flexible, from UI customization to behavior control, you can shape the experience to match your app’s design and workflow.
  * **Knowledge Base & Tracking: **Give customers quick access to your knowledge base, track user activity for better insights, and send timely notifications to drive engagement.
  * **Comprehensive APIs:** Every feature, chat, calls, tracking, notifications, KB, and more is available through well-documented APIs under the API Reference.



Download the sample app below to explore how Mobilisten works in action.

Download Sample App

**Note:**  
Zoho SalesIQ is GDPR Compliant. The configurations for the website and Mobile SDK remain the same. So, if you have already configured on your site, it will be automatically reflected in the Mobile SDK. If not, then learn [how to configure](https://help.zoho.com/portal/en/kb/salesiq-2-0/admin-guide/global-settings/articles/global-settings#How_to_enable_GDPR_for_the_portal) now.

## Installation:

Please follow the steps mentioned below to install the Mobilisten plugin in your Flutter mobile application.

### Requirements:

**Android:**

  * Minimum Android Version: Android 6.0 (Marshmallow) (API Level 23)
  * Compile SDK Version: 35 (Android 15)



**Note:** Click here to view the required permissions for the Mobilisten SDK.

**iOS** : 

The iOS SDK is compatible with iOS version 13 and above; Xcode 13.0 and above is required as the development environment.

### Installation steps:

1\. Add Mobilisten as a dependency within the **pubspec.yaml** file as shown below
    
    
    Copied 
    
    
    dependencies:
      flutter:
         sdk: flutter
    salesiq_mobilisten: ^6.5.1
    // Add this only if you require Mobilisten Calls functionality
    salesiq_mobilisten_calls: ^0.0.2

  
2\. Run **flutter pub get** to fetch dependencies for the project.

3\. Navigate to the **ios** directory and run the **pod install** command.

4\. Add the following permissions in the **Info.plist** file for the iOS Runner project.

5\. Open the **android** directory in Android Studio or any IDE used for Android development. Open the project **build.gradle** file and add the following maven repository.

  * Add the following maven repository in the project root **settings.gradle**(project/android/settings.gradle) or **build.gradle file**(project/android/build.gradle).



#### For Gradle version 6.7 and below
    
    
    Copied// Add the following to your project's root build.gradle file.
    
    allprojects {
       repositories {
          google()
          mavenCentral()
          // ...
          maven { url 'https://maven.zohodl.com' }
       }
    }

#### For Gradle version 6.8 and above

KotlinGroovy
    
    
    Copied// Add the following to your settings.gradle file.
    
    dependencyResolutionManagement {
        repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
        repositories {
            google()
            mavenCentral()
            // Add the Zoho Maven URL here
            maven { url = uri("https://maven.zohodl.com") }
        }
    }
    
    
    Copied// Add the following to your settings.gradle file.
    
    dependencyResolutionManagement {
        repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
        repositories {
            google()
            mavenCentral()
            // Add the Zoho Maven URL here
            maven { url 'https://maven.zohodl.com' }
        }
    }

[](/sites/zweb/images/salesiq/and1.png)

Now, click on **Sync Now** or use the **Sync Project with Gradle Files** option under the File menu.

6\. To initialize Mobilisten, generate the App and Access keys for iOS. In the Zoho SalesIQ console, navigate to  _Settings → Brands → Installation → iOS_. Enter the bundle ID for the application, as shown in the example below, and click on **Generate**.

**Note:** The App and Access keys generated for iOS are to be used in further steps.

7\. Generate the App and Access keys for Android to initialize Mobilisten. In the Zoho SalesIQ console, navigate to _Settings → Brands → Installation → Android_. Enter the application ID for the application as shown in the below example and Click on **Generate**.

8\. Setup the Lifecycle Callback: Add the android:name property to the <application> tag in your AndroidManifest.xml:
    
    
    Copied 
    
    
    <application
        android:label="@string/app_name"
        android:icon="@drawable/ic_launcher"
        android:name="<package_name>.MyFlutterApplication">    
    
    
    Copiedimport io.flutter.app.FlutterApplication;
    import com.zoho.salesiq.mobilisten.calls.plugin.MobilistenCallsPlugin;
    import com.zohosalesiq.plugin.MobilistenPlugin;
    
    public class MyFlutterApplication extends FlutterApplication {
    
            //...
     
           @Override
            public void onCreate() {
                    MobilistenPlugin.registerCallbacks(this);
                    MobilistenCallsPlugin.registerCallbacks(this);
                    super.onCreate();
            }
    }

This is essential as it enables Mobilisten to track activity's lifecycles and other listener callbacks on the app's startup to show the launcher and other important user behaviors.

**Note:** If you already have a custom Application class, ensure to "**import com.zohosalesiq.plugin.MobilistenPlugin;** " and call "**MobilistenPlugin.registerCallbacks(this);** " before invoking "**super.onCreate()** ".

9\. Open the **main.dart file** inside the lib directory and import Mobilisten as shown below. With this, additionally import **dart:io** to check the current platform which will be used at a later stage.
    
    
    Copied 
    
    
    import 'dart:io' as io;
    import 'package:salesiq_mobilisten/salesiq_mobilisten.dart';

  
10\. Initialize Mobilisten using the**init API** within the[ initState()](https://www.zoho.com/salesiq/help/developer-guides/flutter-sdk-init.html) method in the **main.dart file.**
    
    
     Copiedif (io.Platform.isIOS || io.Platform.isAndroid) {
      String appKey;
      String accessKey;
    
      if (io.Platform.isIOS) {
        appKey = "INSERT_IOS_APP_KEY";
        accessKey = "INSERT_IOS_ACCESS_KEY";
      } else {
        appKey = "INSERT_ANDROID_APP_KEY";
        accessKey = "INSERT_ANDROID_ACCESS_KEY";
      }
    
      ZohoSalesIQ.eventChannel.listen((event) {
        switch (event["eventName"]) {
          case SIQEvent.visitorRegistrationFailure:
            {
              // event("code") - Gives the error code
              // event("message") - Gives the error message
              if (isLoggedInUser) {
                ZohoSalesIQ.sendEvent(
                  SIQSendEvent.visitorRegistrationFailure,
                  [SalesIQUser(userId: "test")],
                );
              } else {
                ZohoSalesIQ.sendEvent(
                  SIQSendEvent.visitorRegistrationFailure,
                  [SalesIQGuestUser()],
                );
              }
              break;
            }
        }
      });
    
    SalesIQConfiguration configuration = SalesIQConfiguration(
        appKey: appKey,
        accessKey: accessKey);
    
    ZohoSalesIQ.initialize(configuration).then((_) {
      // initialization successful
      ZohoSalesIQ.launcher.show(VisibilityMode.always);
    }).catchError((error) {
      // initialization failed
      print(error);
    });
    

**11\. Permissions**

Mobilisten requires a set of permissions for chat, bot triggers, and call features to function properly.

**Base permissions:**

  * android.permission.INTERNET: Required for network-related operations (mandatory)
  * android.permission.SCHEDULE_EXACT_ALARM: If you want your chatbot to be proactively triggered for your mobile app users after a specified duration (more than a second), add [SCHEDULE_EXACT_ALARM](https://developer.android.com/reference/android/Manifest.permission#SCHEDULE_EXACT_ALARM) permission in your AndroidManifest.xml. This ensures scheduling the bot trigger after the designated time. Even if your app is inactive, SalesIQ will post the trigger message as a notification for your app users.



**Note:** To use the bot triggers in Android 12 & above, the SCHEDULE_EXACT_ALARM permission is mandatory.

**Call permissions:**

  * android.permission.POST_NOTIFICATIONS
  * android.permission.FOREGROUND_SERVICE_SPECIAL_USE
  * android.permission.FOREGROUND_SERVICE_PHONE_CALL
  * android.permission.FOREGROUND_SERVICE_MICROPHONE
  * android.permission.MANAGE_OWN_CALLS
  * android.hardware.sensor.proximity
  * android.permission.BLUETOOTH_CONNECT
  * android.permission.USE_FULL_SCREEN_INTENT
  * android.permission.MODIFY_AUDIO_SETTINGS
  * android.permission.SYSTEM_ALERT_WINDOW
  * android.permission.RECORD_AUDIO
  * android.permission.VIBRATE



**Step 11: Backup Codes**

If your app has enabled backup and you have your own backup rules or some of your other dependencies have them, then all these steps below are mandatory for App data backup to Google. Since Android doesn’t support manifest merging, all backup rules must be combined into a single file, which you’ll need to reference in your app’s **AndroidManifest.xml.**

To complete this setup,

  1. Create XML files called **merged_backup_rules.xml** and**merged_data_extraction_rules.xml** in the **res/xml/** directory. Example: **android/app/src/main/res/xml.**
  2. Add your rules with our Mobilisten rules to your app and verify that everything is functioning as expected.


    
    
    Copied<?xml version="1.0" encoding="utf-8"?>
    <full-backup-content>
        <!-- Your own/other library's rules --> 
        <exclude domain="sharedpref" path="sample-data"/>
        <exclude domain="database" path="sample.db"/>
    
        <!-- Mobilisten rules -->
        <exclude
            domain="sharedpref"
            path="siq_encrypted_shared_preference_entries.xml" />
        <exclude
            domain="sharedpref"
            path="siq_session.xml" />
        <exclude
            domain="sharedpref"
            path="siq_permission.xml" />
        <exclude
            domain="database"
            path="siq_mobilisten.db" />
         <exclude
            domain="database"
            path="mobilisten_zoho_salesiq.db" />
    </full-backup-content>

#### merged_data_extraction_rules.xml
    
    
    Copied<?xml version="1.0" encoding="utf-8"?>
    <data-extraction-rules>
    
        <cloud-backup>      
            <!-- Your own/other library's rules -->
            <exclude domain="sharedpref" path="sample-data"/>
            <exclude domain="database" path="sample.db"/>
    
            <!-- Mobilisten rules -->
            <exclude
                domain="sharedpref"
                path="siq_encrypted_shared_preference_entries.xml" />
            <exclude
                domain="sharedpref"
                path="siq_session.xml" />
            <exclude
                domain="sharedpref"
                path="siq_permission.xml" />
            <exclude
                domain="database"
                path="siq_mobilisten.db" />
            <exclude
                domain="database"
                path="mobilisten_zoho_salesiq.db" />
        </cloud-backup>
    
        <device-transfer>
            <!-- Your own/other library's rules -->
            <exclude domain="sharedpref" path="sample-data"/>
            <exclude domain="database" path="sample.db"/>         
        </device-transfer>
    </data-extraction-rules>

Also, ensure to map it in your **AndroidManifest.xml.**
    
    
     Copied 
    
    
    android:dataExtractionRules="@xml/merged_data_extraction_rules" 
    android:fullBackupContent="@xml/merged_backup_rules"'
    tools:replace="android:fullBackupContent,android:dataExtractionRules,android:allowBackup"

**12\. Proguard Configuration (Minifying App)**

In some versions of the Android Gradle plugin, the R8 compiler exhibits aggressive behavior that removes some essential classes necessary for the SDK to function as expected. To handle this, we have added specific pro-guard rules within our Mobilisten SDK to preserve these crucial classes during the build process. If you have enabled ProGuard(minifyEnabled) R8, then please add the following rules in your **proguard-rules.pro** file in your **project/android** folder.
    
    
    Copied 
    
    
    -dontwarn kotlinx.parcelize.Parcelize

If you encounter any instances where these pro-guard rules do not suffice, kindly reach out to us at ([support@zohosalesiq.com](mailto:support@zohosalesiq.com)).