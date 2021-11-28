*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  Matti
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Register Credentials
    Welcome Page Sgould Be Open

Register With Too Short Username And Valid Password
    Set Username  Ma
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Register Credentials
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  Matti
    Set Password  salis
    Set Password Confirmation  salis
    Submit Register Credentials
    Register Should Fail With Message  Password too short

Register With Nonmatching Password And Password Confirmation
    Set Username  Matti
    Set Password  salasana123
    Set Password confirmation  salasana1
    Submit Register Credentials
    Register Should Fail With Message  Passowrds doesn't match

Login After Successful Registration
    Go To Register Page
    Set Username  Matti
    Set Password  salasana123
    Set Password confirmation  salasana123
    Submit Register Credentials

    Go To Login Page
    Input Text  username  Matti
    Input Password  password  salasana123
    Submit Login Credentials
    Main Page Should Be Open

Login After failed Registration
    Go To Register Page
    Set Username  Matti
    Set Password  salis
    Set Password confirmation  salis
    Submit Register Credentials

    Go To Login Page
    Input Text  username  Matti
    Input Password  password  salis
    Submit Login Credentials
    Login Page Should Be Open

*** Keywords ***

Submit Register Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open
