echo "Running tests..."

CUR=$(pwd)
echo $CUR
SCRIPT_DIR=$CUR"/script_test"
TEST_DIR=$CUR"/tests"
ANS_DIR=$CUR"/answer"
echo $SCRIPT_DIR


output1=$(./binary)
PIPET5_OUT=$TEST_DIR"/binary_out"
echo "output-binary"
echo $output1
echo $output1 > $PIPET5_OUT

output2=$(./zemaphore)
PIPET6_OUT=$TEST_DIR"/zemaphore_out"
echo "output--zemaphore"
echo $output2
echo $output2 > $PIPET6_OUT

output3=$(./pc_fig 10 10 1)
PIPET7_OUT=$TEST_DIR"/pc_fig_out1"
echo "output--pc_fig"
echo $output3
echo $output3 > $PIPET7_OUT

output4=$(./pc_fig 10 10 5)
PIPET8_OUT=$TEST_DIR"/pc_fig_out2"
echo "output--pc_fig"
echo $output4
echo $output4 > $PIPET8_OUT

output5=$(./pc_works 10 10 5)
PIPET9_OUT=$TEST_DIR"/pc_works_out"
echo "output--pc_works"
echo $output5
echo $output5 > $PIPET9_OUT

# output2=$(./psh2 <<EOF
#   ls
#   -lt
#   ^C
# EOF
# )
# PSH1_OUT=$TEST_DIR"/psh2_out"
# echo $output2 > $PSH1_OUT

echo "Output prepared."

exit 0