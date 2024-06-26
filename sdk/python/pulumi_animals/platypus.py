# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['PlatypusArgs', 'Platypus']

@pulumi.input_type
class PlatypusArgs:
    def __init__(__self__, *,
                 legs: pulumi.Input[int]):
        """
        The set of arguments for constructing a Platypus resource.
        """
        pulumi.set(__self__, "legs", legs)

    @property
    @pulumi.getter
    def legs(self) -> pulumi.Input[int]:
        return pulumi.get(self, "legs")

    @legs.setter
    def legs(self, value: pulumi.Input[int]):
        pulumi.set(self, "legs", value)


class Platypus(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 legs: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Create a Platypus resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PlatypusArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Platypus resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param PlatypusArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PlatypusArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 legs: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PlatypusArgs.__new__(PlatypusArgs)

            if legs is None and not opts.urn:
                raise TypeError("Missing required property 'legs'")
            __props__.__dict__["legs"] = legs
        super(Platypus, __self__).__init__(
            'animals:index:Platypus',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Platypus':
        """
        Get an existing Platypus resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PlatypusArgs.__new__(PlatypusArgs)

        __props__.__dict__["legs"] = None
        return Platypus(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def legs(self) -> pulumi.Output[int]:
        return pulumi.get(self, "legs")

