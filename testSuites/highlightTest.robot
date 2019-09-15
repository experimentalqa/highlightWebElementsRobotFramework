*** Settings ***
Resource    ../keywords/highlightTestKeywords.robot
Resource    ../testdata/testdata.robot

Suite Setup    Set Selenium Speed    0.5s  # set for better viewing
Suite Teardown    Close Browser

*** Test Cases ***
Highlight Element Test
    Open ${BROWSER} With ${URL}
    Input Text    name=q     test
    Click Element    (//span[text()='test'])[1]    
    Wait Until Element Is Visible    id=logo    
    Element Should Be Visible    name=q    
       
        
