all: paper_summary.pdf

paper_summary.pdf: biblio.bib paper_summary.tex introduction.tex methodology.tex conclusion.tex adversaryModel.tex implementation.tex relatedWork.tex
	pdflatex paper_summary
	bibtex paper_summary
	pdflatex paper_summary
	pdflatex paper_summary

clean: 
	\rm -f *.dvi *.aux *.ps *~ *.log *.blg *.bbl *.pdf
