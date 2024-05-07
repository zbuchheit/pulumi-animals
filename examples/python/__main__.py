import pulumi
import pulumi_animals as animals

my_platypus = animals.Platypus("myPlatypus", legs=4)
pulumi.export("output", {
    "value": my_platypus.legs,
})
