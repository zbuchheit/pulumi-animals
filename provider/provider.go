// Copyright 2016-2023, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package provider

import (
	p "github.com/pulumi/pulumi-go-provider"
	"github.com/pulumi/pulumi-go-provider/infer"
	"github.com/pulumi/pulumi/sdk/v3/go/common/tokens"
)

// Version is initialized by the Go linker to contain the semver of this build.
var Version string

const Name string = "animals"

func Provider() p.Provider {
	// We tell the provider what resources it needs to support.
	// In this case, a single custom resource.
	return infer.Provider(infer.Options{
		Resources: []infer.InferredResource{
			infer.Resource[Platypus, PlatypusArgs, PlatypusState](),
		},
		ModuleMap: map[tokens.ModuleName]tokens.ModuleName{
			"provider": "index",
		},
	})
}

// Each resource has a controlling struct.
// Resource behavior is determined by implementing methods on the controlling struct.
// The `Create` method is mandatory, but other methods are optional.
// - Check: Remap inputs before they are typed.
// - Diff: Change how instances of a resource are compared.
// - Update: Mutate a resource in place.
// - Read: Get the state of a resource from the backing provider.
// - Delete: Custom logic when the resource is deleted.
// - Annotate: Describe fields and set defaults for a resource.
// - WireDependencies: Control how outputs and secrets flows through values.
type Platypus struct{}

// Each resource has an input struct, defining what arguments it accepts.
type PlatypusArgs struct {
	// Fields projected into Pulumi must be public and hava a `pulumi:"..."` tag.
	// The pulumi tag doesn't need to match the field name, but it's generally a
	// good idea.
	Legs int `pulumi:"legs"`
}

// Each resource has a state, describing the fields that exist on the created resource.
type PlatypusState struct {
	// It is generally a good idea to embed args in outputs, but it isn't strictly necessary.
	PlatypusArgs
	// Here we define a required output called result.
	Legs int `pulumi:"legs"`
}

// All resources must implement Create at a minimum.
func (Platypus) Create(ctx p.Context, name string, input PlatypusArgs, preview bool) (string, PlatypusState, error) {
	state := PlatypusState{PlatypusArgs: input}
	if preview {
		return name, state, nil
	}
	state.Legs = makeLegs(input.Legs)
	return name, state, nil
}

func makeLegs(legs int) int {
	return legs
}
