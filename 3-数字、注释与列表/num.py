# 素素带你学python的第三期示例程序
import decimal as de

# 避免0.2+0.1出现多余小数的问题
value1=de.Decimal("0.2")
value2=de.Decimal("0.1")
print(value1+value2)


age=23
message="Happy "+str(age)+"rd Birthday"
print(message)

color=["red",'green',2]
print(color)