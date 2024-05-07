package main

import (
	"github.com/pulumi/pulumi-animals/sdk/go/animals"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		myPlatypus, err := animals.NewPlatypus(ctx, "myPlatypus", &animals.PlatypusArgs{
			Legs: pulumi.Int(4),
		})
		if err != nil {
			return err
		}
		ctx.Export("output", map[string]interface{}{
			"value": myPlatypus.Legs,
		})
		return nil
	})
}
