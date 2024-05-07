import * as pulumi from "@pulumi/pulumi";
import * as animals from "@pulumi/animals";

const myPlatypus = new animals.Platypus("myPlatypus", {legs: 4});
export const output = {
    value: myPlatypus.legs,
};
