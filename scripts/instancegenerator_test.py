from instancegenerator import InstanceGenerator


generator = InstanceGenerator(50, 1000, 1, 1000)
generator.generateInstance()
generator.save("regular_instance")

generator.generateOptimumInstance()
generator.save("optimum_instance")
