
HEADER_MENU_LOCATOR = "//div[contains(@class, 'header__menu')]"
LOGOUT_BUTTON_LOCATOR = "//button[contains(@class, 'footer-exit')]"
CHOICE_ORGANISATION_BUTTON_LOCATOR = "xpath=//div[contains(@class, 'school-select-widget__btn-title') and text()='Выберите организацию']"
ORGANISATION_SELECTOR_LOCATOR = "xpath=//div[contains(@class, 'plex-field-trigger')]"
ORGANISATION_SELECTOR_SAVE_BUTTON = "xpath=//button[@class='plex-btn plex-btn-ui-primary plex-btn-l']"
ADMIN_PAGE_BUTTON_LOCATOR = "//div[contains(@class, 'header__helpers')]"
SCHOOL_DROPDOWN_INPUT = "//div[contains(@class, 'plex-panel__body')]//input[contains(@class, 'plex-field-input')]"



class MainPageLocators:
    @staticmethod
    def SCHOOL_SELECTOR_LOCATOR(text: str) -> str:
        return f"xpath=//div[contains(@class, 'plex-popup')]//div[contains(@class, 'plex-typography') and text()='{text}']"

    @staticmethod
    def OPEN_REGISTRY_LOCATOR(text: str) -> str:
        return f"xpath=//div[contains(@class, 'plex-typography plex-typography-heading-xs') and text()='{text}']"
