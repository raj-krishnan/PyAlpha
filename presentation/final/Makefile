create:
	pdflatex -shell-escape -interaction=nonstopmode -file-line-error presentation.tex &> /dev/null
	pdflatex -shell-escape -interaction=nonstopmode -file-line-error presentation.tex &> /dev/null
	rm -f *.synctex.gz
	rm -f *.out
	rm -f *.log
	rm -f *.aux
	rm -f *.nav
	rm -f *.snm
	rm -f *.toc

clean:
	rm -f *.pdf

view:
	evince presentation.pdf &> /dev/null &
