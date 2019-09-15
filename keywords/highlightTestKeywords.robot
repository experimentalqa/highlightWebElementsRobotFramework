*** Settings ***
Resource    ../base/keywordImports.robot


*** Keywords ***
Open ${browserVendor} With ${urlToOpen}
    [Documentation]    Launch your website
    Open Browser    ${urlToOpen}  ${browserVendor}    
    Maximize Browser Window
         
    