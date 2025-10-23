import pytest
import os
from pathlib import Path
import filecmp


# def test_check_sum():
#   cwd = os.getcwd()
#   stdout_file = cwd + "/tests/thread_child_join_out"
#   f = open(stdout_file)
#   stdout_file_content = f.read()
#   f.close()

#   #ARRRRG sum is 12079685
#   arr = stdout_file_content.split()

#   if int(arr[3]) != 10000000:
#     assert True
#   else:
#     assert False


def test_binary_output1():
  cwd = os.getcwd()
  stdout_file = cwd + "/tests/binary_out"
  f = open(stdout_file)
  stdout_file_content = f.read()
  f.close()

  substring = "20000000"
  count = stdout_file_content.count(substring)

  if count == 2:
    assert True
  else:
    assert False

def test_zemaphore_output1():
  cwd = os.getcwd()
  stdout_file = cwd + "/tests/zemaphore_out"
  f = open(stdout_file)
  stdout_file_content = f.read()
  f.close()

  substring = "parent"
  count = stdout_file_content.count(substring)

  if count == 2:
    assert True
  else:
    assert False


def test_pc_output1():
  cwd = os.getcwd()
  stdout_file = cwd + "/tests/pc_fig_out2"
  f = open(stdout_file)
  stdout_file_content = f.read()
  f.close()

  substring = "-1"
  count = stdout_file_content.count(substring)

  if count == 5:
    assert True
  else:
    assert False


# def test_pipet5_output1():
#   cwd = os.getcwd()
#   stdout_file = cwd + "/tests/pipe_t5_out"
#   f = open(stdout_file)
#   stdout_file_content = f.read()
#   f.close()
#   print("-----")
#   print(stdout_file)
#   substring = "30"
#   count = stdout_file_content.count(substring)

#   if count == 1:
#     assert True
#   else:
#     assert False

# def test_write_read_output1():
#   cwd = os.getcwd()
#   stdout_file = cwd + "/tests/wr_shared_out1"
#   f = open(stdout_file)
#   stdout_file_content = f.read()
#   f.close()
#   print("-----")
#   print(stdout_file)
#   substring = "This is first write"
#   count = stdout_file_content.count(substring)

#   if count == 1:
#     assert True
#   else:
#     assert False

# def test_psh1_output2():
#   cwd = os.getcwd()
#   stdout_file = cwd + "/tests/psh1_out"
#   f = open(stdout_file)
#   stdout_file_content = f.read()
#   f.close()
#   print("-----")
#   print(stdout_file)
#   substring = "TIME "
#   count = stdout_file_content.count(substring)

#   if count > 0:
#     assert True
#   else:
#     assert False
    
# def test_exec_output1():
#   cwd = os.getcwd()
#   stdout_file = cwd + "/tests/exec_out1"
#   f = open(stdout_file)
#   stdout_file_content = f.read()
#   f.close()
#   print("-----")
#   print(stdout_file)
#   substring = "Hello, Alex"
#   count = stdout_file_content.count(substring)

#   if count == 1:
#     assert True
#   else:
#     assert False

# def test_exec_output2():
#   cwd = os.getcwd()
#   stdout_file = cwd + "/tests/exec_out2"
#   f = open(stdout_file)
#   stdout_file_content = f.read()
#   f.close()
#   print("-----")
#   print(stdout_file)
#   substring = "Hello,"
#   count = stdout_file_content.count(substring)

#   if count == 1:
#     assert True
#   else:
#     assert False