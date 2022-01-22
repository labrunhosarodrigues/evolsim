# evolsim
Evolution simulator based on self-replicating and mutating genomes codifying behavior and metabolism.

## Sources

 - Inspiration for DNA enconding brain connections: https://www.youtube.com/watch?v=N3tRFayqVtk by @daviddrandallmiller.

## Project descrition

In this envirronment two different objects coexist: plants and animals:
 - plants are autotrofic, and are just randomly spawned across the map. They exist for a limited period of time, and provid a limited energy source to animals that decide to eat them.
 - animals are heterotophic. their DNA codifies their size and their internal behaviour.
  - Animals size dictates life expectancy, maximum energy, energy decay per time, reproductive period, cost of motion, reproduction, and attack damage.
  - Animals brain is a neural network, where the DNA determines which connections are available and their weights

