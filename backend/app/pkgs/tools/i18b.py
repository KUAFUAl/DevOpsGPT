import gettext
from app.pkgs.tools import storage

from config import LANGUAGE, SITE_NAME

def getCurrentLanguageName():
    try:
        language = storage.get("language")
    except Exception as e:
        language = LANGUAGE

    if language == "en":
        return "English"
    else:
        return "Chinese"

def getI18n(domain):
    try:
        language = storage.get("language")
    except Exception as e:
        language = LANGUAGE

    if language is None:
        language = LANGUAGE

    translate = gettext.translation(domain=domain, localedir="./i18n", languages=[language])
    translate.install()
    i18n = translate.gettext
    return i18n

def getFrontendText():
    _ = getI18n("frontend")
    return {
        "title": SITE_NAME,
        "change_language": _("切换为中文"),
        "start": _("Start"),
        "more_operations": _("More"),
        "hello": _("Hello"),
        "login": _("Login"),
        "logout": _("Logout"),
        "error":_("ERROR"),
        "service_modification_item_empty":_("The services involved are not analyzed. Check whether the application architecture information is accurate"),
        "ai_think": _("Thinking..."),
        "ai_start_1": _("Hello, I am the AI-assisted code development assistant, please select the"),
        "ai_start_2": _("to start the development task!"),
        "ai_select_app": _("I need to develop requirements in the"),
        "ai_selected_app_1": _("Task APP"),
        "ai_selected_app_2": _("Task ID"),
        "ai_selected_app_3": _("Task repo"),
        "ai_selected_app_4": _("Task branch: Based on"),
        "ai_selected_app_5": _("to development"),
        "ai_selected_app_6": _("Now, please tell me the requirements that need to be completed, describing them in as much detail as possible."),
        "ai_requirement_clarify_1": _("Development requirements overview: "),
        "ai_requirement_clarify_2": _("Development requirements details: "),
        "ai_requirement_clarify_3": _("The requirements document has been generated, and the interface document will be generated after confirmation: "),
        "ai_requirement_clarify_4": _("In order to better understand the requirements, I also need to confirm the following questions: "),
        "ai_api_clarify_1": _("The interface documentation has been generated, and once confirmed, the analysis of how to modify the program code will begin: "), 
        "ai_api_clarify_confirm": _("Confirm interface document."),    
        "ai_api_subtask_1": _("Analyzing how to modify the"),    
        "ai_api_subtask_2": _("code according to the requirement description, it is expected to take 1-6 minutes, please wait..."),  
        "ai_api_subtask": _("According to the above development tasks and the product database, I analyze that the following contents need to be modified:"), 
        "start_ci": _("Start CI"),  
        "submit_code": _("Submit code"),  
        "auto_check": _("Auto check"),  
        "modify_file": _("Modify file"),  
        "reasonfor_for_modification": _("Reason for modification"),  
        "adjust_code": _("Adjust code"),  
        "review_code": _("Review code"),  
        "status": _("Status"),  
        "app": _("APP"),
        "select_app": _("Select APP"),
        "requirement_description": _("Requirement description"),
        "operation": _("Operation"),
        "submit": _("Submit"),
        "ok": _("Ok"),
        "edit": _("Edit"),
        "close": _("Close"),
        "cancel": _("Cancel"),
        "retry": _("Retry"),
        "restart": _("Restart"),
        "question": _("Question"),
        "answer": _("Answer"),
        "initial_code": _("Initial code"),
        "self_check": _("Self check"),
        "compile_check": _("Compile check"),
        "fix_compile_check": _("Fix Compile check"),
        "static_scan": _("Static scan"),
        "fix_static_scan": _("Fix Static scan"),
        "no_problem_this_file": _("No problem found in the current file, refer to other solutions:"),
        "backend_return_error": _("The back-end service returns an exception. Contact the administrator to check the terminal service logs and browser consol."),
        "start_cd": _("Start deployment"), 
        "start_task": _("Start task"), 
        "requirement_list": _("Requirement List"), 
        "app_list": _("APP List"), 
        "setting": _("Setting"), 
        "create_new": _("Create new"), 
        "back_to_list": _("Back to list page"),
        "app_name": _("APP name"), 
        "app_intro": _("APP introduction"), 
        "app_base_branch": _("Base branch"), 
        "app_feat_branch": _("Feature branch"), 
        "service_name": _("Service name"), 
        "service_role": _("Service role"), 
        "service_language": _("Language"), 
        "service_framework": _("Framework"),
        "service_libs": _("Dependency library"),
        "app_sub_service": _("APP sub service"),
        "git_path": _("Git path"),
        "ai_code_analysis": _("AI code analysis"),
        "service_api_type": _("API type"),
        "service_api_path": _("API path"),
        "service_database": _("Service database"),
        "service_code_struct": _("Service code struct"),
        "requirement_id": _("Requirement ID"),
        "requirement_origin": _("Requirement name"),
        "requirement_status": _("Requirement status"),
        "requirement_user": _("Requirement owner"),
        "requirement_completion": _("Requirement completion rating"),
        "requirement_satisfaction": _("Requirement satisfaction_rating"),
        "opensource_version_1": _("Historical requirement recovery is not supported at this time, please visit workspace to obtain the code results"),
        "notice": _("Notice"),
        "username": _("Username"),
        "password": _("Password"),
        "register": _("Register"),
        "email": _("Email"),
        "tenant_name": _("Company Name"),
        "tenant_status": _("Company Status"),
        "tenant_description": _("Company Description"),
        "tenant_billing_type": _("Billing type"),
        "tenant_billing_quota": _("Billing quota"),
        "tenant_created_at": _("Created"),
        "tenant_billing_end": _("Plus expiry"),
        "employee_count": _("Employee count"),
        "industry_type": _("Industry type"),
        "change_tenant": _("Switch Tenant"),
        "tenant_member_count": _("Member Count"),
        "create_tenant_notice": _("Please ensure that the information is accurate and we will review it within 24 hours to activate your account."),
        "create_user_notice": _("In order to protect your rights, please ensure that the information is accurate."),
        "enter": _("Enter"),
        "show_tenant": _("Details"),
        "members": _("Members"),
        "country": _("Country"),
        "role": _("Role"),
        "phone": _("Phone Number"),
        "add_member": _("Add member"),
        "invite": _("Invite"),
        "billing": _("Billing"),
        "bill_type": _("Bill type"),
        "bill_user": _("Operating user"),
        "bill_date": _("Billing date"),
        "remarks": _("Remarks"),
        "operate": _("Operate"),
        "git_provider": _("Git provider"),
        "git_url": _("Git URL"),
        "git_token": _("Git token"),
        "git_username": _("Git username"),
        "git_email": _("Git email"),
        "ci_token": _("CI Token"),
        "ci_api_url": _("CI API URL"),
        "ci_provider": _("CI provider"),
        "cd_provider": _("CD provider"),
        "ACCESS_KEY": _("ACCESS_KEY"),
        "SECRET_KEY": _("SECRET_KEY"),
        "configuration": _("Configuration"),
        "config_name": _("Config name"),
        "app_cd_config": _("Associated CD Config"),
        "app_ci_config": _("Associated CI Config"),
        "app_git_config": _("Associated Git Config"),
        "my_role": _("My Role"),
        "others_1": _("The tenant does not exist or is abnormal"),
        "others_2": _("Insufficient authority."),
        "renewal": _("Renewal Plus"),
        "recharge": _("Recharge CodePower"),
        "renewal_PayPal": _("PayPal"),
        "renewal_Alipay": _("Alipay"),
        "invite_notice": _("Note: Renewal will take effect immediately. If you switch plus types, the previous plus duration will be reset and start counting anew."),
        "recharge_notice": _("Note: The CodePower is valid for 12 months, please recharge it reasonably."),
        "code_power": _("CodePower"),
        "task_limit_msg": _("Weekly development task limit: "),
        "expired_at": _("Expired: "),
        "others_3": _("The number of tasks for today has exceeded the limit. Please upgrade your membership or try again tomorrow."),
        "others_4": _("CodePower has been depleted. Please check your bill and recharge before using it again."),
        "others_5": _("Billing system error, please check your bill."),
        "reset_workspace": _("Sync from Git"),
        "create_from_tpl": _("Way 2: Create APP via template. Templates are stored on GitHub by default, and you can clone them into your own repository."),
        "create_from_gitpath": _("Way 1: Create APP via AI, give git path, AI automatically analyzes the code base to create APP, Make sure Git token has code pull permission."),
        "ai_code_analysis_wait": _("AI code analysis... It will take a few minutes. Please wait"),
        "launch_code": _("Launch code"),
        "others_6": _("Your KUAFUAI launch code"),
        "others_7": _("The username cannot be smaller than 4 characters."),
        "others_8":  _("The username format you entered is incorrect(Only letters a-Z and _ - are allowed)."),
        "others_9":  _("The password cannot be smaller than 6 characters."),
        "others_10":  _("The phone_number cannot be smaller than 9 characters."),
        "others_11": _("The email format you entered is incorrect."),
        "others_12": _("The email launch code is incorrect."),
        "invitation_code": _("invitation code (Thank you for your interest. We will open registration after the beta testing phase.)"),
        "version_status": _("Alpha(internal testing)"),
        "intro_short_introduction": _("Welcome to KuafuAI, Multi agent system for AI-driven software development."),
        "intro_short_introduction2": _("Natural language requirements into working software."),
        "intro_short_introduction3": _("Multi agent system for AI-driven software development. Combine LLM with DevOps tools to convert natural language requirements into working software. Supports any development language and extends the existing code."),
        "intro_feature_title_1": _("Full Process"),
        "intro_feature_title_2": _("Multi-Agent"),
        "intro_feature_title_3": _("Domain Models"),
        "intro_feature_intro_1": _("An AI-driven development platform that covers the entire software lifecycle management, combined with various DevOps tools, achieves end-to-end delivery of software from natural language requirements."),
        "intro_feature_intro_2": _("AI intelligently adjusts workflow orchestration based on user feedback and continuously performs autonomous self-correction and optimization of generated results, enabling flexible and high-quality software development."),
        "intro_feature_intro_3": _("Multiple domain models are trained for the software production process. These domain models collaborate to complete software development tasks and can support private deployment. Extension development based on existing software code is achieved through proprietary models."),
        "intro_support_curd_title": _("CURD Requirements"),
        "intro_support_curd_intro": _("In software development, CRUD (Create, Read, Update, Delete) represents essential operations for managing data. It involves creating new records, retrieving existing data, updating information, and deleting records. These CRUD operations are fundamental in various applications, from database management systems to web and mobile applications, as they enable users to interact with and manipulate data effectively."),
        "intro_support_chatbot_title": _("ChatBot Requirements"),
        "intro_support_chatbot_intro": _("In software development, chatbot requirements for applications like Enterprise WeChat typically encompass functionalities such as real-time messaging, automated responses, integration with enterprise systems, user management, and multi-platform compatibility, ensuring efficient communication and task automation within corporate environments."),
        "intro_support_more_title": _("More"),
        "intro_support_more_intro": _("As our foundational and product capabilities continue to improve, we will gradually expand our development to encompass more complex application scenarios, bringing universal benefits to every user with software development needs. Please stay tuned and follow us for updates."),
        "intro_sign_up_msg": _("Now, you can experience our products with minimal cost. We look forward to bringing a whole new experience to your software development!"),
        "intro_pricing_free": _("Opensource"),
        "intro_pricing_basic": _("Basic"),
        "intro_pricing_pro": _("Pro"),
        "intro_private_deployment": _("Private Deployment"),
        "intro_private_deployment_intro": _("Utilize our fine-tuned model and deploy it within your private environment to ensure data security. We welcome further communication with you."),
        "intro_contact_us": _("Contact Us"),
        "intro_links": _("Links"),
        "get_launch_code": _("Get Launch code"),
        "service_type": _("Service Type"),
        "others_13": _("The email address has been registered."),
        "change_password":  _("Change password"),
        "newpassword":  _("New password"),
        "help":  _("Help center"),
        "ai_tecDoc_clarify_1": _("Technical document has been generated. You can confirm the document, or manually modify the document."),
        "ai_pm":  _("Assist in clarifying product requirements and produce requirement documents."),
        "ai_tl":  _("Design system architecture, break down development tasks, and produce technical documentation for development."),
        "ai_qa":  _("Assess product quality, identify and report defects."),
        "ai_rd":  _("Write, review, test, and maintain software code."),
        "ai_op":  _("Responsible for application deployment, as well as managing servers, networks, and systems to ensure system availability and stability."),
        "ai_intro": _("The following AI roles will assist you in completing the entire development process for requirement tasks."),
        "try_it": _("Try it!"),
        "goodcase_title_1": _("Web application"),
        "goodcase_content_1": _("Asset Registration Function: Supports adding new fixed asset information, including asset number, name, specifications, purchase date, and purchase price."),
        "goodcase_title_2": _("Office collaboration application expansion"),
        "goodcase_content_2": _("Input meeting notes, invoke ChatGPT to organize the meeting notes into meeting minutes, and send them to the group via the enterprise WeChat bot."),
        "goodcase_title_3": _("Integration between services via API"),
        "goodcase_content_3": _("Integrate with the GitLab server using GitLab's OpenAPI. The system will query the recent one-hour continuous integration failure records every hour."),
        "goodcase_title_4": _("mini-games"),
        "goodcase_content_4": _("Snake Game: Players control the direction of the snake, collect food, and the snake grows in length when it eats food."),
        "goodcase_chose": _("Try this requirement"),
        "ai_goodcase_intro": _("Please note that different types of applications are suitable for different types of needs. Please provide a detailed description of your requirements. Below are some reference cases."),
        "trigger_code_review": _("Trigger code review"),  
        "update_status": _("Update status"),
        "view_detail": _("View details"),
        "index_view_url": _("index_view_url"),
        "msg_empty_task": _("You haven't created an app yet. <a href='/app.html?action=create_new' target='_blank'>You can quickly create one.</a>"),
        "others_14": _("The verify code is incorrect."),
        "others_15": _("The phone number has been registered."),
        "others_16": _("You have obtained the verify code too many times."),
        "select_existing_application": _("Select existing applications"),
        "select_existing_application_intro": _("Select from already created applications."),
        "ai_imports": _("AI import existing code project"),
        "ai_imports_intro": _("Use AI to automatically import existing code items to create new applications."),
        "tpl_imports": _("Create application using templates"),
        "tpl_imports_intro": _("Use templates to quickly create new application."),
        "repair_workspace": _("Repair workspace"),
    }
