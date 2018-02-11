from perceptron import Perceptron

test = Perceptron()

test.setThreshold(1)
test.addInput(1, 1)
test.addInput(2, 4.5)
test.addInput(4, 0.2)
test.fire()
test.displayInput()
test.displayOutput()
test.setThreshold(11)
test.fire()
test.displayOutput()