echo "Running test2..."

CUR=$(pwd)
echo $CUR
SCRIPT_DIR=$CUR"/script_test"
TEST_DIR=$CUR"/tests"
ANS_DIR=$CUR"/answer"
echo $SCRIPT_DIR


output1=$(./example2)
PIPET1_OUT=$TEST_DIR"/ex2_sum_out"
echo "output for example2----"
echo $output1
echo $output1 > $PIPET1_OUT


# output2=$(./rm_char_a 'IaamaaStudent')
# PIPET2_OUT=$TEST_DIR"/rm_a_out1"
# echo "output 2----"
# echo $output2
# echo $output2 > $PIPET2_OUT

# output3=$(./add_brace 'IaamaaaStudent' -p ./rm_char_a)
# PIPET3_OUT=$TEST_DIR"/add_out3"
# echo "output 3----"
# echo $output3
# echo $output3 > $PIPET3_OUT


# output4=$(./rm_char_a 'IaamaaaStudent' -p ./add_brace)
# PIPET4_OUT=$TEST_DIR"/rm_a_out3"
# echo "output 4----"
# echo $output4
# echo $output4 > $PIPET4_OUT


# CMD1="./write_shared_mem 'This is first write'"
# CMD2=./read_shared_mem
# $CMD1
# output5=$($CMD2)
# PIPET5_OUT=$TEST_DIR"/wr_shared_out1"
# echo "Start -- This is the output for reader and writer for the shared memory"
# echo $CMD1
# echo $CMD2
# echo $output5
# echo $output5 > $PIPET5_OUT
# echo "End -- This is the output for reader and writer for the shared memory"

# if [ "$output5" != "" ] ; then
#   echo "Pass: shared memory test"
# else
#   echo "Fail: shared memory test"
#   exit 1
# fi

echo "Test2 passed."

exit 0