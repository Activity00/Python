"""
Non-Axiomatic Reasoner

Instances of this represent a reasoner connected to a Memory, and set of Input and Output channels.

 * All state is contained within Memory.  A Nar is responsible for managing I/O channels and executing
 * memory operations.  It executesa series sof cycles in two possible modes:
 *   * step mode - controlled by an outside system, such as during debugging or testing
 *   * thread mode - runs in a pausable closed-loop at a specific maximum framerate.
"""


class Nar:
    def __init__(self):
        pass
   