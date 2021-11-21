*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input New Command
    Input Credentials  matti  salasana123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input New Command
    Input Credentials  kalle  kalle123456
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input New Command
    Input Credentials  ma  salasana123
    Output Should Contain  Username too short

Register With Valid Username And Too Short Password
    Input New Command
    Input Credentials  matti  sala
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Input Credentials  matti  salasana
    Output Should Contain  Password must contain special characters

*** Keywords ***
Input New Command And Create User
    Input New Command
    Input Credentials  kalle  kalle123
