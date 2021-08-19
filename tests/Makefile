PLOTGEN := ../plotgen

INPUT  := testdata.csv
OUTDIR := tests.out

SKIP_CHECK := false

.PHONY: tests general tests.dev tests.md5s $(OUTDIR)/$(INPUT)

ifeq ($(SKIP_CHECK), false)

define check_exists
	[ -e "$(1)" ] && echo "> PASSED" || { echo "> FAILED"; exit 1; }
endef
define check_output
	[ "$$(grep '$(OUTDIR)/$(1).$(2).out' $(1).checksums)" = "$$(md5sum $(OUTDIR)/$(1).$(2).out)" ] && echo "> PASSED" || { echo "> FAILED"; exit 1; }
endef

else

define check_exists
	[ -e "$(1)" ] && echo "> $(1) exists" || > echo "> $(1) is missing"
endef
define check_output
	[ -e "$(OUTDIR)/$(1).$(2).out" ] && cat "$(OUTDIR)/$(1).$(2).out" || "> $(OUTDIR)/$(1).$(2).out missing"
endef

endif

tests:
	rm -Rf $(OUTDIR)
	$(MAKE) --no-print-directory general
	$(MAKE) --no-print-directory $(OUTDIR)/$(INPUT)

tests.dev:
	$(MAKE) SKIP_CHECK=true tests

tests.md5s: $(INPUT)
	rm -f $<.checksums; \
	for i in tests.out/$<.*.out; do \
		md5sum $$i >> $<.checksums; \
	done


$(OUTDIR):
	mkdir $(OUTDIR)

$(INPUT):
	echo "input;A;B;C;D"      > $@
	echo "0;1;2;3;4"          >> $@
	echo "1;1;2;3;4"          >> $@
	echo "2;1;2;3;4"          >> $@
	echo "3;1;2;3;4"          >> $@
	echo "4;1;2;3;4"          >> $@
	echo ";NaN;nan;nAn;"      >> $@
	echo "i0;1;2;3;4"         >> $@
	echo "i1;1;2;3;4"         >> $@
	echo "i2;1;2;3;4"         >> $@
	echo "i3;1;2;3;4"         >> $@
	echo "i4;1;2;3;4"         >> $@
	echo "f0;1.2;2.2;3.2;4.2" >> $@
	echo "f1;1.4;2.4;3.4;4.4" >> $@
	echo "f2;1.6;2.6;3.6;4.6" >> $@
	echo "f3;1.8;2.8;3.8;4.8" >> $@
	echo "f4;2;3;4;5"         >> $@

general:
	@echo "> Checking plot.py executeable..."
	$(PLOTGEN) --help >/dev/null
	@echo "> PASSED"

$(OUTDIR)/$(INPUT) : $(INPUT) $(OUTDIR)
	@echo "> Reading in $< and writing it as text file"
	$(PLOTGEN) -i $< --file $@.000.out
	@$(call check_output,$<,000)
	@echo "> Reading in $< and writing it as pickle file"
	$(PLOTGEN) -i $< --pickle $@.001.out
	@$(call check_output,$<,001)
	@echo "> Reading in $< and printing it"
	$(PLOTGEN) -i $< --print > $@.002.out
	@$(call check_output,$<,002)
	@echo "> Reading in $@.1.out and printing it"
	$(PLOTGEN) -i $@.001.out --print > $@.003.out
	@$(call check_output,$<,003)

#    --index-icolumn {-inf - +inf}
#    --index-column INPUT  set index column
#    --reset-index         reset index back into data frame as first column
#    --select-mode {all,first,last}
#    --ignore-icolumns INPUT [INPUT ...]
#    --ignore-columns INPUT [INPUT ...]
#    --ignore-irows INPUT [INPUT ...]
#    --ignore-rows INPUT [INPUT ...]
#    --select-irows INPUT [INPUT ...]
#    --select-rows INPUT [INPUT ...]
#    --select-icolumns INPUT [INPUT ...]
#    --select-columns INPUT [INPUT ...]
	@echo "> --filter-irows"
	$(PLOTGEN) -i $< --filter-irows 0:4 1 3 --print > $@.004.out
	@$(call check_output,$<,004)
	@echo "> --filter-row"
	$(PLOTGEN) -i $< --filter-row f0 2.2 4.2 --print > $@.005.out
	@$(call check_output,$<,005)
	@echo "> --filter-icolumns"
	$(PLOTGEN) -i $< --filter-icolumns 0:4 1 2 3 4 --print > $@.006.out
	@$(call check_output,$<,006)
	@echo "> --filter-column"
	$(PLOTGEN) -i $< --filter-column C 3 3.2 3.8 --print > $@.007.out
	@$(call check_output,$<,007)
	@echo "> --filter-mode and --filter-irows"
	$(PLOTGEN) -i $< --filter-mode '!=' --filter-irows 0:4 2 --print > $@.008.out
	@$(call check_output,$<,008)
	$(PLOTGEN) -i $< --filter-mode '>' --filter-irows 0:4 2 --print > $@.009.out
	@$(call check_output,$<,009)
	$(PLOTGEN) -i $< --filter-mode '<' --filter-irows 0:4 2 --print > $@.010.out
	@$(call check_output,$<,010)
	@echo "> --filter-mode and --filter-icolumns"
	$(PLOTGEN) -i $< --filter-mode '!=' --filter-icolumns 1 2 --print > $@.011.out
	@$(call check_output,$<,011)
	$(PLOTGEN) -i $< --filter-mode '>' --filter-icolumns 1 2 --print > $@.012.out
	@$(call check_output,$<,012)
	$(PLOTGEN) -i $< --filter-mode '<' --filter-icolumns 1 2.5 --print > $@.013.out
	@$(call check_output,$<,013)
#    --sort-order {asc,desc}
#    --sort-function {mean,median,std,min,max}
#    --sort-columns        sort columns
#    --sort-by-irows INPUT [INPUT ...]
#    --sort-by-rows INPUT [INPUT ...]
#    --sort-rows           sort rows
#    --sort-by-icolumns INPUT [INPUT ...]
#    --sort-by-columns INPUT [INPUT ...]
#    --reverse-columns     reverse columns order
#    --reverse-rows        reverse row order
#    --data-scale {-inf - +inf}
#    --data-offset {-inf - +inf}
#    --normalise-to {-inf - +inf}
#    --normalise-to-icolumn INPUT
#    --normalise-to-column INPUT
#    --normalise-to-irow INPUT
#    --normalise-to-row INPUT
#    --add-at {front,back}
#    --add-function {sum,mean,median,std,var,sum,count,skew,mad,min,max,nan,zero,one}
#    --add-column INPUT    add a new column with name
#    --add-row INPUT       add a new row with name
#    --group-function {sum,mean,median,std,var,sum,count,skew,mad,min,max}
#    --group-by-icolumns INPUT [INPUT ...]
#    --group-by-columns INPUT [INPUT ...]
#    --group-by-irows INPUT [INPUT ...]
#    --group-by-rows INPUT [INPUT ...]
#    --abs                 convert all values to absolute values
#    --apply-parameter INPUT
#    --apply-function {add,radd,sub,rsub,mul,rmul,div,rdiv,mod,rmod,pow,rpow,cumsum,cummax,cummin,cumprod,rank,nan,zero,one,abs,set,polyfit}
#    --apply-icolumns INPUT [INPUT ...]
#    --apply-irows INPUT [INPUT ...]
#    --apply-columns INPUT [INPUT ...]
#    --apply-rows INPUT [INPUT ...]
#    --column-names INPUT [INPUT ...]
#    --row-names INPUT [INPUT ...]
#    --drop-nan            dropping rows/columns that are completely empty
#    --drop-any-nan        dropping rows/columns that contain empty values
#    --transpose           transpose data
#    --print               print out each parsed input file
#    --join {none,index,columns}
#    --split-icolumn {-inf - +inf, or index}
#    --split-column INPUT  split frame along this column
#    --split-irow {-inf - +inf, or columns}
#    --split-row INPUT     split frame along this row
#    --focus-frames INPUT [INPUT ...]
#    --defocus-frames INPUT [INPUT ...]
#    --output-precision {0 - +inf, or default}
#    --file INPUT [INPUT ...]
#    --pickle INPUT        pickle data frames to file (one file containing all
	@echo "> Create basic line plot as py, png, jpg and pdf"
	$(PLOTGEN) -i $< --plot line -o $@.line.py $@.line.png $@.line.jpg $@.line.pdf -q
	@$(call check_exists,$@.line.py)
	@$(call check_exists,$@.line.png)
	@$(call check_exists,$@.line.jpg)
	@$(call check_exists,$@.line.pdf)
	@echo "> Create basic bar plot as py, png, jpg and pdf"
	$(PLOTGEN) -i $< --plot bar -o $@.bar.py $@.bar.png $@.bar.jpg $@.bar.pdf -q
	@$(call check_exists,$@.bar.py)
	@$(call check_exists,$@.bar.png)
	@$(call check_exists,$@.bar.jpg)
	@$(call check_exists,$@.bar.pdf)
	@echo "> Create basic box plot as py, png, jpg and pdf"
	$(PLOTGEN) -i $< --plot box -o $@.box.py $@.box.png $@.box.jpg $@.box.pdf -q
	@$(call check_exists,$@.box.py)
	@$(call check_exists,$@.box.png)
	@$(call check_exists,$@.box.jpg)
	@$(call check_exists,$@.box.pdf)
	@echo "> Create basic violin plot as py, png, jpg and pdf"
	$(PLOTGEN) -i $< --plot violin -o $@.violin.py $@.violin.png $@.violin.jpg $@.violin.pdf -q
	@$(call check_exists,$@.violin.py)
	@$(call check_exists,$@.violin.png)
	@$(call check_exists,$@.violin.jpg)
	@$(call check_exists,$@.violin.pdf)


clean:
	rm -Rf $(INPUT) $(OUTDIR)
