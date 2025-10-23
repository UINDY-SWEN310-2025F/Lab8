compile1:
	echo "compiling binary.c"
	gcc -pthread ./answer/binary.c -o ./binary
compile2:
	echo "compiling zemaphore.c"
	gcc -pthread ./answer/zemaphore.c -o ./zemaphore
compile3:
	echo "compiling pc_works.c and pc_fig.c"
	gcc -pthread ./answer/pc_works.c -o ./pc_works
	gcc -pthread ./answer/pc_fig.c -o ./pc_fig
test:
	bash ./script_test/test1.sh
	bash ./script_test/test0.sh
	#bash ./script_test/test2.sh

done:
	#rm -rf ./tests/pc_pid_out
	#rm -rf ./tests/mmyfork_out
	echo "delete all"

