import os
import pytest
import shutil
import time
import urllib.request

from conf import *
from tempfile import mkdtemp
from utils import shell, screen_exec

@pytest.fixture
def bmt_rc():
    shell('%s rcstart' % BMT_BIN_PATH)
    yield
    shell('%s rcstop' % BMT_BIN_PATH)
    
@pytest.fixture
def iso():
    tdir = mkdtemp()
    iso_path = os.path.join(tdir, 'live.iso')
    urllib.request.urlretrieve(TEST_ISO, iso_path)
    yield iso_path
    shutil.rmtree(tdir)

@pytest.fixture
def vm(iso, bmt_rc):
    shell('%s create %s' % (BMT_BIN_PATH, TEST_VM_NAME))
    shell('%s set %s VM_CDROM=1' % (BMT_BIN_PATH, TEST_VM_NAME))
    shell('%s set %s VM_CDROM_MEDIA=%s' % (BMT_BIN_PATH,
                                            TEST_VM_NAME,
                                            iso))
    shell('%s set %s VM_N1_TAP_NUM=%s' % (BMT_BIN_PATH,
                                            TEST_VM_NAME,
                                            TEST_VM_TAP))
    shell('%s start %s' % (BMT_BIN_PATH, TEST_VM_NAME))
    yield
    shell('%s stop %s' % (BMT_BIN_PATH, TEST_VM_NAME))
    shell('%s destroy %s' % (BMT_BIN_PATH, TEST_VM_NAME))

@pytest.fixture
def vm_net(vm):
    # Wait for iso to boot
    time.sleep(120)

    # Login to the VM
    screen_exec(TEST_VM_NAME, TEST_VM_USER)
    screen_exec(TEST_VM_NAME, TEST_VM_PASS)

    # Set ip in the VM
    screen_exec(TEST_VM_NAME, 'killall dhclient')
    screen_exec(TEST_VM_NAME, 'ifconfig vtnet0 -alias')
    screen_exec(TEST_VM_NAME, 'ifconfig vtnet0 %s up' % TEST_VM_VM_ADDR)

    # Set ip on the Hypervisor
    shell('ifconfig tap%s %s up' % (TEST_VM_TAP, TEST_VM_HY_ADDR))
    yield

def test_vm_start_stop(vm_net):
    time.sleep(180)
