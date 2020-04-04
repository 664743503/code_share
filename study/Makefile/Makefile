# 1================================================================
# calc: main.c test_print.c
# 	gcc -o calc main.c test_print.c

# 2================================================================
# cc = gcc
# prom = calc
# src = main.c test_print.c

# $(prom):$(src)
# 	$(cc) -o $(prom) $(src)

# 3================================================================
# cc = gcc
# prom = calc
# deps = test_print.h
# obj = main.o test_print.o

# $(prom):$(obj)
# 	$(cc) -o $(prom) $(obj)

# # 将所有的.c文件编译成同名的.o文件
# %.o:%c $(deps)
# 	$(cc) -c $< -o $@

# 4================================================================
cc = gcc
prom = calc
deps = $(shell find ./ -name "*.h")
src = $(shell find ./ -name "*.c")
obj = $(src:%.c=%.o) 

$(prom): $(obj)
	$(cc) -o $(prom) $(obj)

# 将所有的.c文件编译成同名的.o文件
%.o: %.c $(deps)
	$(cc) -c $< -o $@

# 5================================================================

clean:
	rm -rf $(obj) $(prom)
