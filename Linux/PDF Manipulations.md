# PDF manipulations

## Convert JPG image to PDF
convert <filename>.jpg -auto-orient <filename>.pdf

## Resize PDF to A4-paper
for pdf in *; do
	pdfjam --outfile $pdf --paper a4paper $pdf
done

## Search text within PDF
pdfgrep -r --include *.pdf <search-text>
