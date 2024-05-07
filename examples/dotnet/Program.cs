using System.Collections.Generic;
using System.Linq;
using Pulumi;
using Animals = Pulumi.Animals;

return await Deployment.RunAsync(() => 
{
    var myPlatypus = new Animals.Platypus("myPlatypus", new()
    {
        Legs = 4,
    });

    return new Dictionary<string, object?>
    {
        ["output"] = 
        {
            { "value", myPlatypus.Legs },
        },
    };
});

