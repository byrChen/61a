This file holds the tests that you create. Remember to import the python file(s)
you wish to test, along with any other modules you may need.
Run your tests with "python3 ok -t --suite SUITE_NAME --case CASE_NAME -v"
--------------------------------------------------------------------------------

Suite Problem_EC

	>>> from ants import *
  >>> hive, layout = Hive(AssaultPlan()), dry_layout
  >>> dimensions = (1, 9)
  >>> colony = AntColony(None, hive, ant_types(), layout, dimensions)
  
  Case slow
    >>> # Testing Slow
    >>> slow = SlowThrower()
    >>> bee = Bee(3)
    >>> colony.places["tunnel_0_0"].add_insect(slow)
    >>> colony.places["tunnel_0_4"].add_insect(bee)
    >>> slow.action(colony)
    >>> colony.time = 1
    >>> colony.time
    1
    >>> bee.action(colony)
    3
    >>> bee.place.name # SlowThrower should cause slowness on odd turns
    'tunnel_0_4'
    >>> colony.time += 1
    >>> colony.time
    2
    >>> bee.action(colony)
    2
    >>> bee.place.name # SlowThrower should cause slowness on odd turns
    'tunnel_0_3'
    >>> colony.time += 1
    >>> colony.time
    3
    >>> bee.action(colony)
    1
    >>> bee.place.name # SlowThrower should cause slowness on odd turns
    'tunnel_0_3'
    >>> colony.time += 1
    >>> colony.time
    4
    >>> bee.action(colony)
    0
    >>> bee.place.name # SlowThrower should cause slowness on odd turns
    'tunnel_0_2'
    >>> colony.time += 1
    >>> colony.time
    5
    >>> bee.action(colony)
    0
    >>> bee.place.name # SlowThrower should cause slowness on odd turns
    'tunnel_0_1'

  Case scary
    >>> # Testing Scare
    >>> error_msg = "ScaryThrower doesn't scare for exactly two turns."
    >>> scary = ScaryThrower()
    >>> bee = Bee(3)
    >>> colony.places["tunnel_0_0"].add_insect(scary)
    >>> colony.places["tunnel_0_4"].add_insect(bee)
    >>> scary.action(colony)
    >>> bee.action(colony)
    2
    False
    >>> bee.place.name # ScaryThrower should scare for two turns
    'tunnel_0_5'
    >>> bee.action(colony)
    1
    False
    >>> bee.place.name 
    'tunnel_0_6'
    >>> bee.action(colony)
    0
    True
    >>> bee.place.name 
    'tunnel_0_5'
