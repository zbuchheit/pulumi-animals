// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class Platypus extends pulumi.CustomResource {
    /**
     * Get an existing Platypus resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Platypus {
        return new Platypus(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'animals:index:Platypus';

    /**
     * Returns true if the given object is an instance of Platypus.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Platypus {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Platypus.__pulumiType;
    }

    public readonly legs!: pulumi.Output<number>;

    /**
     * Create a Platypus resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: PlatypusArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.legs === undefined) && !opts.urn) {
                throw new Error("Missing required property 'legs'");
            }
            resourceInputs["legs"] = args ? args.legs : undefined;
        } else {
            resourceInputs["legs"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Platypus.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Platypus resource.
 */
export interface PlatypusArgs {
    legs: pulumi.Input<number>;
}
