from robot.api import logger
from SeleniumLibrary import SeleniumLibrary
from SeleniumLibrary.base import keyword
from selenium.webdriver.support.expected_conditions import _find_element


class ExtendedSeleniumLib(SeleniumLibrary):

    def run_keyword(self, name, args, kwargs):
        # list of keyword which need to be highlighted
        commandsTohighlight = ['element_should_be_enabled','element_should_be_focused','element_should_be_visible','get_text','click_button','click_image',
                               'click_link','click_element','double_click_element','scroll_element_into_view','get_list_items','get_selected_list_value','select_from_list_by_value','select_from_list_by_label',
                               'select_checkbox','select_radio_button','input_password','input_text'
                               ]
        if name in commandsTohighlight:
             element1=_find_element(self, args[:1])
             self.highlight(element1)
        return SeleniumLibrary.run_keyword(self, name, args, kwargs)
    
    @keyword
    #  Example from robot framework doc 
    def title_should_start_with(self, expected):
        title = self.get_title()
        if not title.startswith(expected):
            raise AssertionError("Title '%s' did not start with '%s'"
                                 % (title, expected))
    
    # code to highlight the element
    # copied from https://gist.github.com/marciomazza/3086536.js  
    def highlight(self,element):
        """Highlights web elements
        """
        driver = element._parent
        driver.execute_script("""
            element = arguments[0];
            original_style = element.getAttribute('style');
           
            if(original_style == null){
                element.setAttribute('style', "background: yellow; border: 2px solid red;");
            } else{
                element.setAttribute('style', original_style + "; background: yellow; border: 2px solid red;");
            }
            
            setTimeout(function(){
                if(original_style == null){
                    element.removeAttribute('style');
                } else{
                    element.setAttribute('style', original_style);
                }          
            }, 300);
        """, element)
        
