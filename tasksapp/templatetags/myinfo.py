from django import template
import os

####  CUSTOM TAGs HERE
register = template.Library()


@register.simple_tag
def localsystem_info():
    system_info = dict()
    infolist = ['username', 'userdomain', 'computername', 'os']
    for _ in infolist:
        if os.getenv(_):
            system_info[_] = (os.getenv(_))
    return system_info
