# 使用import导入整个模块
import sayhello
from sayhello import sayh2,sayh3
# 别名
import saybye as sb
from saybye import sayb as s
# 导入所有函数
from sayhello import *

# 使用模块中的函数
# sayhello.sayh()

sayh()
sayh3()

# 不使用句点
sayh2()

# 别名的效果和函数名或模块名相同
sb.sayb()
s()