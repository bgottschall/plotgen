PLOTGEN := ../plotgen

all: gantt.png gantt_time.png line.png scatter.png bar.png box.png violin.png subplots.png

clean:
	rm -f gantt.png gantt_time.png line.png scatter.png bar.png box.png violin.png subplots.png

gantt.png: gantt.tsv
	$(PLOTGEN) -i $< --plot bar --bar-mode stack --bar-text-position inside --x-type date --orientation h --output $@ --quiet

gantt_time.png: gantt_time.tsv
	$(PLOTGEN) -i $< --plot bar --orientation h --x-type date --bar-text-position outside --bar-mode stack --output $@ --quiet

line.png: lines.tsv
	$(PLOTGEN) -i $< --plot line --output $@ --quiet

scatter.png: scatter.tsv
	$(PLOTGEN) -i $< --plot line --line-mode markers --output $@ --quiet

bar.png: bar.tsv
	$(PLOTGEN) -i $< --plot bar --output $@ --quiet

box.png: distribution.tsv
	$(PLOTGEN) -i $< --plot box --output $@ --quiet

violin.png: distribution.tsv
	$(PLOTGEN) -i distribution.tsv --plot violin --output $@ --quiet

subplots.png: lines.tsv scatter.tsv bar.tsv distribution.tsv
	$(PLOTGEN) -i lines.tsv --colspan 2 -i scatter.tsv --row 2 --colspan 1 --line-mode markers -i bar.tsv --col 2 --plot bar -i distribution.tsv --row 3 --col 1 --plot violin -i distribution.tsv --col 2 --plot box --horizontal-spacing 0.05 --vertical-spacing 0.05 --per-trace-colours --output $@ --quiet
