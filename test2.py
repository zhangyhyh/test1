# import re
# a = 'adfhxxhaoxxhfhxxdexxjfojf'
# b = re.sub('xx(.*?)xx', 'xx%dxx'%222, a)
# print(b)

import re
a = 'adfhxx123xxhfhxx456xxjfojf'
b = re.findall('\d+', a)
print(b)