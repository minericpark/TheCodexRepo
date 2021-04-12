from FbAutomator import FbAutomator
from FbGender import FbGender
from FbMonth import FbMonth

newAutomator = FbAutomator()
newAutomator.create_fb_account("Test", "Last", "testemail@gmail.com", "testpassword", FbMonth.December, "28", "1999", FbGender.female)
