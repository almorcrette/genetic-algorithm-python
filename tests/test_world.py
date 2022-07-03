import os
import sys
script_dir = os.path.dirname(__file__)
mymodule_dir = os.path.join( script_dir, '..', 'modules')
sys.path.append( mymodule_dir )

from func import func

def test_answer():
    assert func(3) == 5