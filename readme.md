This repository is made for the Meta Back End Developer Course (Capstone Project).


URLs that can be tested with:
(djoser):
auth/* [Any url that djoser added, excluding jwt as it is not implemented for this project] (can obtain token with token/login too)
restaurant/api-token-auth (obtain token - can be via this)
restaurant/menu/
restaurant/menu/<int:pk> (int:pk = id of menu item)
restaurant/booking (booking url)

For unittest test cases:
If you are unable to run the test successfully via python manage.py test , please do add the this configuration behind '--pattern="test*.py"' or '--pattern="test_*.py"' without the single quote.