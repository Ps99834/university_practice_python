import random
import Module
import Base


name = Module.identUser()
attemptPossible = int(Module.enterNumberOfAttempts())

firstBoundary = Module.enterNumberBoundary(Base.firstNumberBoundaryNumber)
secondBounary = Module.enterNumberBoundary(Base.SecondNumberBoundaryNumber)

number = random.randint(Base.firstNumberBoundaryNumber, secondBounary)

Module.description(name,firstBoundary,secondBounary)

#debug purpose only
#print(number)

Module.guessing(attemptPossible, number)
