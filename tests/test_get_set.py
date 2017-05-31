#!/usr/local/bin/python3.5
import pytest
import time

from conf import *
from utils import shell

def test_get_set_memory():
    try:
        memory_key = 12314

        # Get what the memory was before we start
        original_memory = shell('%s get %s VM_MEMORY' % (BMT_BIN_PATH,
                                                            TEST_VM_NAME))
        original_memory = int(original_memory.rstrip())
        # Set the memory to out test known value
        shell('%s set %s VM_MEMORY %i' % (BMT_BIN_PATH,
                                            TEST_VM_NAME, 
                                            memory_key))
        # Get the value that we set above
        test_memory = shell('%s get %s VM_MEMORY' % (BMT_BIN_PATH,
                                                        TEST_VM_NAME))
        
        # Strip the last newline and make sure this is an iteger
        test_memory = int(test_memory.rstrip())

        # Verify what we set and what we got are the same
        assert test_memory == memory_key

        # Set the memory back to the original value
        shell('%s set %s VM_MEMORY %s' % (BMT_BIN_PATH, TEST_VM_NAME, original_memory))

        # Get the memory value we just set, to be sure
        test_memory = shell('%s get %s VM_MEMORY' % (BMT_BIN_PATH,
                                                        TEST_VM_NAME))

        # Strip the last newline and make sure this is an iteger
        test_memory = int(test_memory.rstrip())

        # Verify what we said above
        assert test_memory == memory_key

    except:
        raise
