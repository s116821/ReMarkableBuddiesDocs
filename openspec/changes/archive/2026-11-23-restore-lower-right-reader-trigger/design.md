# Design

Normal startup already resolves the trigger corner after explicit command-line and saved choices. Change the fallback there and reference the same value when a simulation omits its corner. Existing configurations need no migration. Keep the existing hold duration, release handling and corner hit boxes.

Use the existing positive and negative gesture scenarios with coordinates in the lower-right zone. Keep fixtures that explicitly select a different corner available to exercise overrides.
