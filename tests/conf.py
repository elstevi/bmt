import os

### Test configuration ###
TEST_VM_NAME='freebsd-live'
TEST_VM_TAP=999
TEST_VM_USER='root'
TEST_VM_PASS='mfsroot'
TEST_VM_VM_ADDR="172.16.19.2/24"
TEST_VM_HY_ADDR="172.16.19.1/24"
BMT_DIR='/root/src/bmt'
BMT_BIN='bmt'
BMT_BIN_PATH=os.path.join(BMT_DIR, BMT_BIN)
TEST_ISO='http://mfsbsd.vx.sk/files/iso/11/amd64/mfsbsd-mini-11.0-RELEASE-amd64.iso'
