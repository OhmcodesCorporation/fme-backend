from django import template
import ast,datetime
from datetime import datetime,date

register = template.Library()


@register.filter(name='formatDecimal')
def testTag(value):
	return value
# 	if value < 1000:
# 		value = round(value,2)
# 		value = format(value, '.2f')
# 	else:
# 		value = round(value)
	
# 	return value

