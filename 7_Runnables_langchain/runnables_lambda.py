
from langchain_core.runnables import RunnableLambda

boil = RunnableLambda(lambda x : x + "water boiled")

teaPower = RunnableLambda(lambda x : x +" added tea powder ")

addSugar = RunnableLambda(lambda x : x+ "Added two spoon sugar")

milk = RunnableLambda(lambda x : x + " added milk and then ")

serve = RunnableLambda(lambda x : x + "severd the tea to relatives and they dont like it")

process = boil | teaPower| addSugar | milk | serve
print(process.invoke('start '))

double = RunnableLambda(lambda x : x *2)
square = RunnableLambda(lambda x : x **2)
maths = double | square
print(maths.invoke(5), " : double gets 5 * 2 = 10 and then we get sqaure of 10 = 100")

a = RunnableLambda(lambda x: x+ 2)
b = RunnableLambda(lambda x: x* 3)
c = RunnableLambda(lambda x: x -4)

chain = a | b | c

print(chain.invoke(5))