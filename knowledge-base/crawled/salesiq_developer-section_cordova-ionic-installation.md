# Zoho Salesiq Article

**Source:** https://www.zoho.com/salesiq/help/developer-section/cordova-ionic-installation.html
**Crawled:** 2026-01-04

---

# Overview:

Zoho SalesIQ Mobilisten lets you add live chat and visitor tracking to your Cordova or Ionic application with ease. Mobilisten comes with a rich set of APIs that lets you tailor the SDK to fit your needs. Click on the below button to get a sample app. 

Download Sample App

**Note** : Zoho SalesIQ is GDPR Compliant. The configurations for the website and Mobile SDK remains the same. If you have already configured it on your site, it will be automatically reflected in Mobile SDK. If not, then [learn how to configure](/salesiq/help/portal-settings-enable-gdpr.html) now.

# Installation of Zoho SalesIQ SDK:

Please follow the steps mentioned below to install the SalesIQ Mobilisten plugin seamlessly in your Cordova/Ionic application.

## Requirements:

**Android** : 

  * Minimum Android Version: Android 5.0 (Lollipop) (API Level 21)
  * Compile SDK Version: 34 (Android 14)



**iOS** : The iOS SDK is compatible with iOS version 11 and above; Xcode 13.0 and above is required as the development environment.

## How to embed SalesIQ's SDK into your Cordova/Ionic project?

#### **Step 1:**

You can install Mobilisten to your project by using either npm or GitHub. In the root folder of your project, execute the following command in the terminal.

**For Cordova Projects:**
    
    
     Copied 
    
    
    cordova plugin add https://github.com/zoho/SalesIQ-Mobilisten-Cordova.git               

####   
**For Ionic Projects:**
    
    
     Copied 
    
    
    ionic cordova plugin add https://github.com/zoho/SalesIQ-Mobilisten-Cordova.git              

####   
**For Ionic React Projects using Capacitor:**
    
    
     Copied 
    
    
    npm install https://github.com/zoho/SalesIQ-Mobilisten-Cordova.git
    npx cap sync               

**Step 2:**

For iOS, Update the Info.plist file with the below list of permissions. ​Alternatively, to add these entries to the _Info.plist_ file, you can use the config-file tag in the config.xml as shown below for the ios platform.​​
    
    
    Copied<config-file target="*-Info.plist" parent="NSPhotoLibraryAddUsageDescription">
        <string>We would like access to add Images/Videos to your photo library.</string>
    </config-file>
    
    <config-file target="*-Info.plist" parent="NSPhotoLibraryUsageDescription">
        <string>We would like access to the photo library to enable sharing images and videos via chat.</string>
    </config-file>
    
    <config-file target="*-Info.plist" parent="NSCameraUsageDescription">
        <string>We would like access to the camera to enable taking photos and videos for sharing via chat.</string>
    </config-file>
    
    <config-file target="*-Info.plist" parent="NSMicrophoneUsageDescription">
        <string>We would like access to the microphone to allow recording voice messages.</string>
    </config-file>
    
    <config-file target="*-Info.plist" parent="NSLocationWhenInUseUsageDescription">
        <string>We would like access to location services to update your location on the map.</string>
    </config-file>

Run the **cordova prepare ios** command once the above xml is added for the iOS platform.

**Step 3:**

Open the android folder of your Ionic/Cordova project in Android Studio or any other platform for Android development and sync the project with the Gradle files as shown below:

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

**Step 4** :

In the Zoho SalesIQ console, navigate to _Settings > Brands > {Your brand name} > Installation > iOS._ You can then enter your application ID under the Register App section.

Click on **Generate**. Copy the App key and Access key. You can also generate the keys by clicking on the **Create New Access Key** button.

**Step 5** :

  * Similarly, generate the app key and access key for Android to initialize SalesIQ. This will allow your Android app to connect with SalesIQ.



  * In the Zoho SalesIQ console, go to _Settings > Brands > {Your brand name}​ > Installation > Android_. Then, enter your application ID in the input field under the Resiter App section



****

Click on**Generate**. Copy the App key and Access key. You can also generate the keys by clicking on the **Create New Access Key** button.

## Initializing the Plugin

Now, initialize the SDK by adding the following code to your application, depending on the platform. The app and access keys generated for both iOS and Android must be provided separately, as shown below. 

#### For Cordova Projects
    
    
    Copied    let appKey;
        let accessKey;
        if (device.platform === 'iOS') {
            appKey = "ios_app_key";
            accessKey = "ios_access_key";
        } else {
            appKey = "android_app_key";
            accessKey = "android_access_key";
        }
      
        ZohoSalesIQ.init(appKey, accessKey, (success) => {
            //Use the ZohoSalesIQ.Launcher.show API if you wish to show the launcher by default.
            ZohoSalesIQ.Launcher.show(VisibilityMode.ALWAYS);
        });   

#### For Ionic Projects
    
    
    Copieddeclare var ZohoSalesIQ: any;
    
        let appKey;
        let accessKey;
        if (device.platform === 'iOS') {
            appKey = "ios_app_key";
            accessKey = "ios_access_key";
        } else {
            appKey = "android_app_key";
            accessKey = "android_access_key";
        }
      
        ZohoSalesIQ.init(appKey, accessKey, (success) => {
            //Use the ZohoSalesIQ.Launcher.show API if you wish to show the launcher by default.
            ZohoSalesIQ.Launcher.show(VisibilityMode.ALWAYS);
        });       

**Step 6: Permissions:**

  * android.permission.INTERNET: Required for network-related operations (mandatory)
  * android.permission.SCHEDULE_EXACT_ALARM: If you want your chatbot to be proactively triggered for your mobile app users after a specified duration (more than a second), add [SCHEDULE_EXACT_ALARM](https://developer.android.com/reference/android/Manifest.permission#SCHEDULE_EXACT_ALARM) permission in your AndroidManifest.xml. This ensures scheduling the bot trigger after the designated time. Even if your app is inactive, SalesIQ will post the trigger message as a notification for your app users. 



**Note:** To use the bot triggers in Android 12 & above, the SCHEDULE_EXACT_ALARM permission is mandatory.

**Step 7:****Proguard Configuration (Minifying App)**

In some versions of the Android Gradle plugin, the R8 compiler exhibits aggressive behavior that removes some essential classes necessary for the SDK to function as expected. To handle this, we have added specific pro-guard rules within our Mobilisten SDK to preserve these crucial classes during the build process. If you have enabled ProGuard(minifyEnabled) R8, then please add the following rules in your **proguard-rules.pro** file in your **project/android** folder.
    
    
    Copied 
    
    
    -dontwarn kotlinx.parcelize.Parcelize

  
If you encounter any instances where these pro-guard rules do not suffice, kindly reach us at ([support@zohosalesiq.com](mailto:support@zohosalesiq.com)).

**Step 8: Backup Codes**

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
    android:fullBackupContent="@xml/merged_backup_rules" 
    tools:replace="android:fullBackupContent,android:dataExtractionRules,android:allowBackup"