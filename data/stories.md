## happy path
* greet
  - utter_greet
  - utter_bot_function
* mood_great
  - utter_bot_function
* ask_kerala_total
   - action_kerala_total_cases
   - utter_back_to_coronasafe_menu
   
## ask about coronasafe network
* ask_about_coronasafenetwork
    - utter_about_coronasafe
    - utter_tools_coronasafe
* ask_about_care
    - utter_about_care
    - utter_back_to_coronasafe_menu
   

## ask return main menu 
* ask_return_main_menu
   - utter_bot_function
 
## ask return coronasafe menu
* ask_return_coronasafe_menu  
   - utter_about_coronasafe
   - utter_tools_coronasafe
 
## ask cases district wise
* ask_district_wise
    - action_district_select_button_dispatch
* inform_district
    - action_district_wise_cases
    - utter_back_to_coronasafe_menu
    
    
## ask hotspots district wise
* ask_hotspots_districtwise
    - action_district_select_button_dispatch
* inform_district
    - action_hotspots_districtwise
    - utter_back_to_coronasafe_menu

## ask about guides
* ask_about_guides
   - utter_about_guides
   - utter_back_to_coronasafe_menu

## ask about share bot
* ask_about_share_bot
   - utter_about_share_bot
   - utter_back_to_coronasafe_menu  
    
    
##ask about kerala community response network
* ask_about_kerala_community_response_network
    - utter_about_kerala_community_response_network
    - utter_back_to_coronasafe_menu
    
## ask about dashboards
* ask_about_dashboards
  - utter_about_dashboards
  - utter_back_to_coronasafe_menu
  
 
## ask about delivery networks
* ask_about_delivery_networks
   - utter_about_delivery_networks
   - utter_back_to_coronasafe_menu
   

## ask take quiz
* ask_take_quiz
  - utter_about_take_quiz
  - utter_back_to_coronasafe_menu
  
  
## ask Edu Courses
* ask_about_Edu_Courses
  - utter_about_Edu_Courses
  - utter_back_to_coronasafe_menu
 
 
 ## ask contact us
* ask_contact_us
  - utter_about_contact_us
  - utter_back_to_coronasafe_menu
  
 
## say thank you
* thank_bot
    - utter_welcome
    - utter_bot_function
    
## say goodbye
* goodbye
  - utter_goodbye
  - utter_back_to_coronasafe_menu

## bot challenge
* bot_challenge
  - utter_iamabot
  - utter_bot_function
  
## out of scope messages
* out_of_scope
  - action_default_fallback
