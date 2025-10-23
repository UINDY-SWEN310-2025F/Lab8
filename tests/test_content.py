import pytest
import os
from pathlib import Path


def test_output_content1():
  cwd = os.getcwd()
  ansfile1 = cwd + "/answer/binary.c"
  f = open(ansfile1)
  ans1_content = f.read()
  f.close()

  substring = "Pthread_create"
  count = ans1_content.count(substring)
  # print count
  if count >= 2:
    assert True
  else:
    assert False

def test_output_content2():
  cwd = os.getcwd()
  ansfile2 = cwd + "/answer/binary.c"
  f = open(ansfile2)
  ans2_content = f.read()
  f.close()

  substring = "Pthread_join"
  count = ans2_content.count(substring)
  # print count
  if count >= 2:
    assert True
  else:
    assert False

def test_output_content3():
  cwd = os.getcwd()
  ansfile3 = cwd + "/answer/binary.c"
  f = open(ansfile3)
  ans3_content = f.read()
  f.close()

  substring = "&mutex"
  count = ans3_content.count(substring)
  # print count
  if count >= 3:
    assert True
  else:
    assert False

def test_output_content4():
  cwd = os.getcwd()
  ansfile4 = cwd + "/answer/binary.c"
  f = open(ansfile4)
  ans4_content = f.read()
  f.close()

  substring = "common_threads.h"
  count = ans4_content.count(substring)
  print(count)
  # print count
  if count >= 1:
    assert True
  else:
    assert False


def test_output_content5():
  cwd = os.getcwd()
  ansfile5 = cwd + "/answer/zemaphore.c"
  f = open(ansfile5)
  ans5_content = f.read()
  f.close()

  substring = "common_threads.h"
  count = ans5_content.count(substring)
  # print count
  if count >= 1:
    assert True
  else:
    assert False


def test_output_content6():
  cwd = os.getcwd()
  ansfile6 = cwd + "/answer/zemaphore.c"
  f = open(ansfile6)
  ans6_content = f.read()
  f.close()

  substring = "Zem_init"
  count = ans6_content.count(substring)
  # print count
  if count >= 1:
    assert True
  else:
    assert False


def test_output_content7():
  cwd = os.getcwd()
  ansfile7 = cwd + "/answer/zemaphore.c"
  f = open(ansfile7)
  ans7_content = f.read()
  f.close()

  substring = "Zem_post"
  count = ans7_content.count(substring)
  # print count
  if count >= 1:
    assert True
  else:
    assert False

def test_output_content8():
  cwd = os.getcwd()
  ansfile8 = cwd + "/answer/zemaphore.c"
  f = open(ansfile8)
  ans8_content = f.read()
  f.close()

  substring = "Zem_t"
  count = ans8_content.count(substring)
  # print count
  if count >= 1:
    assert True
  else:
    assert False


def test_output_content9():
  cwd = os.getcwd()
  ansfile9 = cwd + "/answer/zemaphore.c"
  f = open(ansfile9)
  ans9_content = f.read()
  f.close()

  substring = "Pthread_create"
  count = ans9_content.count(substring)
  # print count
  if count >= 1:
    assert True
  else:
    assert False


def test_output_content10():
  cwd = os.getcwd()
  ansfile9 = cwd + "/answer/zemaphore.c"
  f = open(ansfile9)
  ans9_content = f.read()
  f.close()

  substring = "zemaphore.h"
  count = ans9_content.count(substring)
  # print count
  if count >= 1:
    assert True
  else:
    assert False


def test_output_content10():
  cwd = os.getcwd()
  ansfile9 = cwd + "/answer/pc_works.c"
  f = open(ansfile9)
  ans9_content = f.read()
  f.close()

  substring = "Sem_init"
  count = ans9_content.count(substring)
  # print count
  if count >= 2:
    assert True
  else:
    assert False

def test_output_content11():
  cwd = os.getcwd()
  ansfile9 = cwd + "/answer/pc_works.c"
  f = open(ansfile9)
  ans9_content = f.read()
  f.close()

  substring = "Pthread_create"
  count = ans9_content.count(substring)
  # print count
  if count >= 2:
    assert True
  else:
    assert False

def test_output_content12():
  cwd = os.getcwd()
  ansfile9 = cwd + "/answer/pc_works.c"
  f = open(ansfile9)
  ans9_content = f.read()
  f.close()

  substring = "Pthread_join"
  count = ans9_content.count(substring)
  # print count
  if count >= 2:
    assert True
  else:
    assert False

def test_output_content13():
  cwd = os.getcwd()
  ansfile9 = cwd + "/answer/pc_fig.c"
  f = open(ansfile9)
  ans9_content = f.read()
  f.close()

  substring = "sem_wait"
  count = ans9_content.count(substring)
  # print count
  if count >= 4:
    assert True
  else:
    assert False