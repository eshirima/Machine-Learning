import numpy as np

first = np.array([[.6], [.8]])
second = np.array([[.8, .6]])

print first
print second

product = first * second

numpy_product = np.multiply(second, first)

columU = np.array([[-.6], [-.8]])
print 'COLUMN SHAPE', columU.shape #(2,1)
# rowV = np.array([[-.8, .6]])
rowV = np.array([[-.8, -.6]])
print 'ROW SHAPE', rowV.shape#(1,2)

producBeforeConstant = np.multiply(rowV, columU)
afterConst = 3 * producBeforeConstant

secondColumU = np.array([[-.8], [.6]])
# secondRowV = np.array([[-.6, -.8]])
secondRowV = np.array([[.6, -.8]])

secondProducBeforeConstant = np.multiply(secondRowV, secondColumU)

final_answer = afterConst + secondProducBeforeConstant

print 'Column U', columU
print 'Row V', rowV
print 'Product', producBeforeConstant
print 'After Const', afterConst
print 'Second Column U', secondColumU
print 'Second Row V', secondRowV
print 'Second Product', secondProducBeforeConstant

print 'Final Answer', final_answer
# print 'Multiplication', product
# print 'Numpy Product', numpy_product